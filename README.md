# Treasure Point

Treasure Point is a **safe, in-memory Streamlit prototype** for demonstrating a cash-request and cash-provider matching flow. It does not process real money, UPI transactions, OTPs, KYC, Aadhaar, passwords, or identity documents.

## Current prototype features

- Session-only user registration with basic validation.
- Need Cash and Provide Cash request forms.
- Amount, location, and availability validation.
- Case- and whitespace-insensitive location matching.
- Configurable amount tolerance for matching.
- Self-match prevention and match-score ordering.
- Temporary activity table and session reset.
- Prominent prototype-only safety messaging.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The application opens at `http://localhost:8501`.

## Development container

The included development-container configuration installs `requirements.txt` and starts `streamlit run app.py`. Do not expose this prototype as a production financial service. For production, the application would require regulated payment partners, a secure authentication design, a database, authorization, audit logs, privacy controls, fraud monitoring, and legal/compliance review.

## Data and privacy

All data is stored in the current Streamlit session and is lost when the session or process ends. It is not shared between users. Do not enter real financial, identity, or contact information.

The original product requirements are preserved in [`PROJECT_SPEC.md`](PROJECT_SPEC.md) for future implementation planning.
