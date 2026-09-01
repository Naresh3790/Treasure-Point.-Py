"""Treasure Point: safe, in-memory Streamlit prototype.

This prototype deliberately does not process real money, OTPs, identity documents,
or payment-provider requests. Data is stored only in the current Streamlit session.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any

import streamlit as st


MIN_AMOUNT = 100
MAX_AMOUNT = 1_000_000
DEFAULT_TOLERANCE = 0.10


@dataclass
class User:
    name: str
    email: str
    city: str
    created_at: str


@dataclass
class CashRequest:
    request_id: int
    request_type: str
    user: str
    amount: int
    location: str
    availability: str
    status: str
    created_at: str


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def normalize_location(value: str) -> str:
    """Normalize user-entered locations for case- and whitespace-insensitive matching."""
    return " ".join(value.strip().casefold().split())


def initialize_state() -> None:
    defaults: dict[str, Any] = {
        "users": [],
        "requests": [],
        "next_request_id": 1,
        "registered": False,
        "current_user": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def validate_text(value: str, label: str) -> str | None:
    cleaned = value.strip()
    if not cleaned:
        st.error(f"{label} is required.")
        return None
    if len(cleaned) > 120:
        st.error(f"{label} must be 120 characters or fewer.")
        return None
    return cleaned


def add_request(request_type: str, user: str, amount: int, location: str, availability: str) -> None:
    request = CashRequest(
        request_id=st.session_state.next_request_id,
        request_type=request_type,
        user=user,
        amount=amount,
        location=location,
        availability=availability,
        status="PENDING",
        created_at=now_iso(),
    )
    st.session_state.requests.append(asdict(request))
    st.session_state.next_request_id += 1


def compatible(request: dict[str, Any], offer: dict[str, Any], tolerance: float) -> bool:
    if normalize_location(request["location"]) != normalize_location(offer["location"]):
        return False
    difference = abs(request["amount"] - offer["amount"])
    allowed_difference = max(request["amount"], offer["amount"]) * tolerance
    availability_matches = (
        request["availability"] == "Any time"
        or offer["availability"] == "Any time"
        or request["availability"] == offer["availability"]
    )
    return difference <= allowed_difference and availability_matches


def get_matches(tolerance: float) -> list[dict[str, Any]]:
    needs = [r for r in st.session_state.requests if r["request_type"] == "NEED_CASH" and r["status"] == "PENDING"]
    offers = [r for r in st.session_state.requests if r["request_type"] == "PROVIDE_CASH" and r["status"] == "PENDING"]
    matches: list[dict[str, Any]] = []
    for need in needs:
        for offer in offers:
            if need["user"] == offer["user"]:
                continue
            if compatible(need, offer, tolerance):
                difference = abs(need["amount"] - offer["amount"])
                score = max(0.0, 1.0 - difference / max(need["amount"], offer["amount"]))
                matches.append(
                    {
                        "need_id": need["request_id"],
                        "offer_id": offer["request_id"],
                        "requester": need["user"],
                        "provider": offer["user"],
                        "requested": need["amount"],
                        "offered": offer["amount"],
                        "location": need["location"],
                        "availability": offer["availability"],
                        "match_score": round(score * 100, 1),
                    }
                )
    return sorted(matches, key=lambda item: item["match_score"], reverse=True)


def register_view() -> None:
    st.subheader("Register a prototype user")
    with st.form("register_form"):
        name = st.text_input("Full name")
        email = st.text_input("Email")
        city = st.text_input("City or area")
        submitted = st.form_submit_button("Register")

    if submitted:
        clean_name = validate_text(name, "Full name")
        clean_email = validate_text(email, "Email")
        clean_city = validate_text(city, "City or area")
        if not all((clean_name, clean_email, clean_city)):
            return
        if "@" not in clean_email or "." not in clean_email.rsplit("@", 1)[-1]:
            st.error("Enter a valid email address.")
            return
        if any(user["email"].casefold() == clean_email.casefold() for user in st.session_state.users):
            st.error("That email is already registered in this session.")
            return
        st.session_state.users.append(asdict(User(clean_name, clean_email, clean_city, now_iso())))
        st.session_state.current_user = clean_name
        st.session_state.registered = True
        st.success(f"Welcome, {clean_name}. Registration completed for this prototype session.")


def request_view(request_type: str) -> None:
    title = "Need Cash" if request_type == "NEED_CASH" else "Provide Cash"
    amount_label = "Amount needed" if request_type == "NEED_CASH" else "Amount available"
    st.subheader(title)
    if not st.session_state.current_user:
        st.info("Register first, then submit a request.")
        return

    with st.form(f"{request_type.lower()}_form"):
        amount = st.number_input(amount_label, min_value=MIN_AMOUNT, max_value=MAX_AMOUNT, value=500, step=100)
        location = st.text_input("City or area")
        availability = st.selectbox("Availability", ["Any time", "Available now", "Later"])
        submitted = st.form_submit_button("Submit request")

    if submitted:
        clean_location = validate_text(location, "City or area")
        if clean_location is None:
            return
        add_request(request_type, st.session_state.current_user, int(amount), clean_location, availability)
        st.success(f"{title} request submitted. It is stored only in this browser session.")


def matches_view() -> None:
    st.subheader("Find prototype matches")
    tolerance_percent = st.slider("Maximum amount difference", 0, 50, 10, 5)
    matches = get_matches(tolerance_percent / 100)
    if not matches:
        st.info("No compatible pending requests found. Add a Need Cash and a Provide Cash request in the same area.")
        return
    st.caption("Matches use normalized location text, amount tolerance, availability, and exclude self-matches.")
    for match in matches:
        with st.container(border=True):
            st.write(f"**{match['requester']}** needs ₹{match['requested']:,}; **{match['provider']}** offers ₹{match['offered']:,}.")
            st.write(f"Location: {match['location']} · Availability: {match['availability']} · Amount fit: {match['match_score']}%")
            st.warning("Prototype only: no real payment, OTP, KYC, or cash exchange is initiated.")


def activity_view() -> None:
    st.subheader("Session activity")
    if not st.session_state.requests:
        st.info("No requests have been submitted yet.")
        return
    st.dataframe(st.session_state.requests, use_container_width=True, hide_index=True)
    if st.button("Clear session requests"):
        st.session_state.requests = []
        st.session_state.next_request_id = 1
        st.rerun()


def main() -> None:
    st.set_page_config(page_title="Treasure Point", page_icon="💰", layout="centered")
    initialize_state()
    st.title("Treasure Point")
    st.caption("Find Cash. Provide Cash. Exchange Securely — safe prototype demonstration.")
    st.warning("Prototype only. No real money, UPI, OTP, KYC, or identity-document processing is enabled.")

    with st.sidebar:
        st.header("Navigation")
        menu = st.radio("Choose a page", ["Register", "Need Cash", "Provide Cash", "Find Matches", "Activity"])
        if st.session_state.current_user:
            st.success(f"Signed in for session: {st.session_state.current_user}")
        st.caption("Session data is temporary and is not shared with other users.")

    if menu == "Register":
        register_view()
    elif menu == "Need Cash":
        request_view("NEED_CASH")
    elif menu == "Provide Cash":
        request_view("PROVIDE_CASH")
    elif menu == "Find Matches":
        matches_view()
    else:
        activity_view()


if __name__ == "__main__":
    main()
