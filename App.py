PROJECT: Treasure Point  "Find Cash. Provide Cash. Exchange Securely."
PRIMARY CONTACT:
  Name: Ganta Naresh
  Mobile: 7702048269
  Email: gantanaresh89@gmail.com
IMPORTANT NOTE (READ FIRST FOR BUILDERS & DEVELOPERS):
  - This project is a college/prototype fintech demonstration only. Do NOT enable real money flows, custody of funds, or UPI transactions without explicit legal, banking, and regulatory approvals.
  - NPCI/UPI cash-withdrawal is available only through authorized Business Correspondents or bank-approved touchpoints. Any real payment integration must be done only after consulting regulated payment partners and compliance/legal teams.
  - For the prototype, all payment flows must be simulated with mock confirmations. Real OTP/UPI endpoints must NOT be invoked in production without authorization.

GOAL:
  Build a mobile-first responsive website prototype for Treasure Point that demonstrates UI flows:
  - Register / Login (OTP simulation)
  - Need Cash / Provide Cash request flows
  - Match discovery & match details
  - Dashboard (user + admin)
  - Map & nearby matches display
  - Notifications, transaction history, profile
  No real financial transactions; all payment exchanges are simulated for prototype.

BRAND:
  Name: Treasure Point
  Tagline: Find Cash. Provide Cash. Exchange Securely.
  Founder/Developer: Ganta Naresh
  Year: 2026

STYLE & DESIGN:
  - Design style: Modern fintech, mobile-first, clean, light background, rounded cards.
  - Primary brand colors:
      Primary: #0B6E4F (deep teal)
      Accent / Gold: #D4AF37 (treasure gold)
      Dark text: #0F1724
      Surface / Light: #F8FAFB
      Muted gray: #6B7280
  - Fonts:
      Headings: Poppins (600/700)
      Body: Inter (400/500)
  - Buttons:
      Primary: filled, primary color background (#0B6E4F) with white text, border-radius 12px, 12px vertical padding. Shadow: small elevation.
      Secondary: white background, primary colored text, border.
  - Icons: use simple line icons (Heroicons or Material Icons).
  - Card style: white cards, px inner padding, border-radius, subtle drop shadow.
  - Animations: micro-interactions only (hover lift on cards, subtle pulse for "Match Found" badge, slide-in toast notifications).
  - Accessibility: color contrast >= 4.5:1 for text, focus outlines, label all form controls, ARIA attributes for dynamic content.

RESPONSIVE LAYOUT:
  - Breakpoints: mobile-first (min widths): px (mobile), px (tablet), px (desktop).
  - Mobile-first: ensure the primary flows (Need Cash / Provide Cash) are fully usable on px screens.

PRIMARY PAGES & CONTENT (exact items to build)
  PUBLIC PAGES:
    - Home
      Hero: Heading "Need Cash? Find Someone Nearby." Subheading: "Treasure Point connects people who need physical cash with verified cash providers through a location-based matching platform."
      CTA buttons: [Need Cash] [Provide Cash]
      Visual: smartphone mockup showing the app screen
      Sections: How It Works (5-step), Features icons, Why Treasure Point, Safety, Contact
      Footer: links + brand + Â© 2026 Treasure Point. Founder/Developer: Ganta Naresh

    - About Treasure Point
      Short description, advantages, applications (students, rural, merchants, travelers)

    - How It Works
      5 steps:
       1. Register
       2. Select Requirement (Need/Provide)
       3. Enter Amount & Location
       4. Find a Match
       5. Complete Exchange (simulated for prototype)

    - Features
      Cards: Location-based matching, Quick discovery, Secure Authentication (OTP), Transaction history, Rating system (future)

    - Safety & Security
      List: verification guidance, location privacy (show approximate distance), fraud detection overview

    - Contact
      Contact details exactly:
        Name: Ganta Naresh
        Mobile Number: 7702048269
        Email: gantanaresh89@gmail.com
      Contact form: Name, Email, Mobile, Message, Send Message button

    - Login
    - Register

  AUTHENTICATED PAGES (User)
    - Dashboard (mobile-first)
      Top greeting: "Welcome, {FirstName} ðŸ‘‹"
      Cards: Need Cash (current request amount), Provide Cash (current available), Active Requests count, Completed Transactions count, Wallet/Transaction Status (prototype label only)
      Quick actions: [Need Cash] [Provide Cash] [Find Match]

    - Need Cash (form UI)
      Heading: Need Cash
      Fields:
        Amount Needed (numeric currency input, prefix â‚¹)
        Location (auto-detect or manual entry: City/Area/PIN)
        Availability: Immediately / Time-window (optional)
      Buttons: Submit Request
      Quick Options below: Post Your Request, Get Nearby Match, View Request Status

    - Provide Cash (form UI)
      Heading: Provide Cash
      Fields:
        Amount Available (â‚¹)
        Location (auto-detect or manual)
        Availability: Available Now / Available Later (time / date)
      Button: Provide Cash

    - Find Match / Matching Page (list + map)
      Heading: Match Found (when match exists)
      Display each match as a card:
        Example:
          â‚¹500
          Anil K.
          ðŸ“ 0.5 km away
          Available Now
          Verification Badge (âœ“ Verified)
          Rating: â­ 4.6
        Buttons: [View Match] [Message] (message = prototype chat)
      Map: shows approximate location markers, user location as "You".

    - Match Details (modal or page)
      Show match attributes: shared amount, approximate distance, availability, verification status, created_at, request status.
      Action buttons: Accept Match, Decline, Cancel Request.
      After Accept: show simulated "UPI Transfer" step with mock confirmation.

    - Transaction History
      Table/list:
        Date | Type (Need/Provide) | Amount | Status
      Statuses: Pending, Matching, Match Found, Accepted, Completed, Cancelled, Disputed

    - Profile
      Fields shown:
        Name
        Mobile (verified badge)
        Email
        City
        Verification Status (Prototype: "Unverified" / "Verified (manual)")
        Rating
        Completed Transactions
      Edit profile modal: change display name, city, email.

    - Notifications
      In-app toasts and notifications list:
        - Match Found!
        - Cash Request Accepted
        - Transaction Completed
      Notification item: title, short body, timestamp, read/unread.

    - Help & Support (FAQ + contact form)

  ADMIN PAGES:
    - Admin Login (separate)
    - Admin Dashboard: KPIs (Total Users, Active Requests, Active Providers, Completed Matches, Cancelled Requests, Flagged Transactions)
    - User Management: list, search, verify, suspend, block
    - Requests: view filter by type/status
    - Matches: view active/past matches
    - Transactions: audit trail
    - Reports: export user/request/transaction CSV
    - Fraud Monitoring: flagged transactions list, ability to mark safe/flag/block
    - Admin Tools: seed test data, run simulations, configure matching weights

UI BEHAVIOR & MICRO-FLOWS:
  - Registration: collect Full Name, Mobile, Email, Password, City.
    Flow: Enter mobile -> request OTP -> verify OTP (prototype: simulated OTP or a test mode where OTP = 123456).
    After OTP verified create profile and redirect to Dashboard.
    Do NOT accept Aadhaar in prototype; show KYC placeholder text "For production, KYC will follow regulated partner flow."

  - Login: mobile/email + password or OTP (choose OTP to prototype).
  - Location permissions: when user clicks "Allow location" request browser geolocation; fall back to manual location entry if denied.
  - Map integration: use Google Maps or Mapbox (configurable). Show approximate distance only (do not disclose exact addresses).
  - Matching notification: when a match is found, show an in-app toast + push notification simulation and a red/ gold animated badge on the Matches tab.
  - Match acceptance: once both users accept, show "Complete Exchange" flow with steps:
      1) Meet at neutral spot (UI guidance)
      2) Provider receives mock UPI transfer confirmation (prototype)
      3) Receiver confirms cash received -> mark transaction Completed
      For prototype, use simulated confirmations and allow manual marking for testing.

MATCHING ALGORITHM (PROTOTYPE)
  - Purpose: find compatible pairs (Need_Cash <> Provide_Cash)
  - Inputs:
      amount_requested, amount_offered, user_location, provider_location, availability_status, verification_status, rating
  - Scoring (example weights, configurable by admin):
      amount_score = 0.4 * (1 - abs(amount_requested - amount_offered) / max(amount_requested, amount_offered))
      distance_score = 0.3 * normalize_distance_score(distance_km)    # normalize 0..1 where closer = 1
      availability_score = 0.15 * (1 if availability matches else 0)
      verification_score = 0.1 * (1 if both verified else 0)
      rating_score = 0.05 * (provider_rating / 5)
      match_score = amount_score + distance_score + availability_score + verification_score + rating_score
  - Filters:
      - Only consider matches where abs(amount_requested - amount_offered) <= configurable threshold (e.g., 10-20% or fixed tolerance).
      - Only consider providers within a configurable distance radius (e.g., 2 km default).
  - Output: top N matches sorted by match_score. Show approximate distance and time to meet estimation.

MAP & LOCATION:
  - Map pins: show user and nearby providers; pin tooltip shows amount, distance, verification badge.
  - Clicking a pin opens Match Details.
  - Always show "approximate distance" and never exact address publicly.

DATABASE DESIGN (Prototype - PostgreSQL)
  - users
    id (uuid PK)
    name (text)
    mobile (text, indexed)
    email (text, indexed)
    password_hash (text)
    city (text)
    location_lat (decimal, nullable)
    location_lng (decimal, nullable)
    verification_status (enum: none, pending, verified)
    rating (numeric default 0)
    completed_transactions (int default 0)
    created_at (timestamp)
    updated_at (timestamp)

  - cash_requests
    id (uuid PK)
    user_id (fk users)
    type (enum: NEED_CASH, PROVIDE_CASH)
    amount (numeric)
    location_lat (decimal)
    location_lng (decimal)
    city (text)
    status (enum: PENDING, MATCHING, MATCH_FOUND, ACCEPTED, COMPLETED, CANCELLED, DISPUTED)
    availability (json or structured: {available_now: bool, start: timestamp, end: timestamp})
    expires_at (timestamp)
    created_at (timestamp)
    updated_at (timestamp)

  - matches
    id (uuid PK)
    need_request_id (fk cash_requests)
    provide_request_id (fk cash_requests)
    provider_id (fk users)
    receiver_id (fk users)
    distance_km (numeric)
    match_score (numeric)
    status (enum: PENDING, ACCEPTED, REJECTED, COMPLETED, CANCELLED)
    created_at (timestamp)
    updated_at (timestamp)

  - transactions
    id (uuid PK)
    match_id (fk matches)
    amount (numeric)
    simulated_payment (json)    # prototype confirmation data
    payment_status (enum: NONE, INITIATED, CONFIRMED)
    cash_status (enum: NONE, RECEIVED, NOT_RECEIVED)
    status (enum: PENDING, COMPLETED, CANCELLED, DISPUTED)
    created_at (timestamp)
    updated_at (timestamp)

  - ratings
    id (uuid PK)
    transaction_id (fk transactions)
    from_user (fk users)
    to_user (fk users)
    rating (int 1..5)
    review (text)
    created_at (timestamp)

  - notifications
    id (uuid PK)
    user_id (fk users)
    title (text)
    message (text)
    read (bool default false)
    metadata (json)
    created_at (timestamp)

  INDEXES & PERFORMANCE:
    - Index cash_requests on (type, status, location_lat, location_lng, amount)
    - Index users on (location_lat, location_lng)
    - Use PostGIS for efficient geospatial distance queries if using production DB; prototype can use Haversine function.

API ENDPOINTS (PROTOTYPE - example)
  Auth:
    POST /api/auth/register {name,mobile,email,password,city}
    POST /api/auth/request-otp {mobile}  -> (prototype OTP)
    POST /api/auth/verify-otp {mobile,otp}
    POST /api/auth/login {mobile,password}
  Users:
    GET /api/users/me
    PUT /api/users/me
  Requests:
    POST /api/requests {type,amount,location_lat,location_lng,city,availability}
    GET /api/requests/:id
    GET /api/requests?type=NEED_CASH&nearby=true&lat=X&lng=Y
    DELETE /api/requests/:id
  Matching:
    GET /api/matches?request_id=:id -> returns sorted matches
    POST /api/matches/:id/accept
    POST /api/matches/:id/reject
  Transactions:
    POST /api/transactions/simulate-payment {match_id,provider_confirmation:true}
    POST /api/transactions/:id/confirm-cash {received:true}
  Notifications:
    GET /api/notifications
    POST /api/notifications/mark-read
  Admin:
    GET /api/admin/users
    POST /api/admin/users/:id/verify
    GET /api/admin/flags
    POST /api/admin/seed-test-data

SEED / TEST DATA (for demo)
  - Create 6 test users across a sample city (Naresh â€” Nizamabad) with mix of verified/unverified.
  - Create sample NEED_CASH and PROVIDE_CASH requests of varied amounts (â‚¹200, â‚¹500, â‚¹1000).
  - Create simulated matches and transactions to demonstrate flows.

SIMULATED PAYMENT FLOW (PROTOTYPE)
  - Provider clicks "Accept" -> system shows simulated UPI transfer instructions screen (mock QR or "Simulate UPI transfer" button).
  - Provider clicks "Simulate Transfer" -> system marks payment_status: CONFIRMED (simulation).
  - Receiver clicks "Confirm Cash Received" -> transaction status = COMPLETED, rating prompt appears.

ADMIN FEATURES (minimum prototype)
  - View and search users and requests.
  - Verify / suspend / block user accounts (manual).
  - Flag suspicious requests; admin can mark as fraudulent.
  - Export CSV reports for auditing.

SECURITY & PRIVACY (REQUIREMENTS)
  - All API communications must be over HTTPS.
  - Passwords hashed with bcrypt/argon2.
  - Implement rate limiting on OTP requests and critical endpoints.
  - Store minimal location granularity in public responses (return only distance and approximate location).
  - Implement audit logs for admin actions and transactions.
  - Privacy policy page and Terms & Conditions page placeholders.

PRODUCTION CAUTION & COMPLIANCE (TO SHOW ON SITE)
  - Add a prominent banner or modal in Admin & public pages: "Prototype demo only â€” no real UPI/monetary transactions are enabled. For production, obtain legal and banking approvals and integrate with authorized BC/Bank partners per NPCI/RBI guidelines."

TECH STACK & DEPLOYMENT SUGGESTION
  - Frontend: React + Next.js (Vercel deploy) OR simple HTML/CSS/JS prototype for quick demo
  - Backend: Python FastAPI (uvicorn) OR Node.js + Express
  - Database: PostgreSQL (PostGIS recommended for spatial)
  - Maps: Google Maps or Mapbox (configurable)
  - Auth: OTP simulation on dev; for production integrate with a secure OTP provider or bank partner
  - Hosting: Vercel (frontend), Render/Railway/AWS (backend), Managed Postgres (Heroku, Railway, Supabase)
  - CI/CD: GitHub Actions to run lint/test and deploy

DELIVERABLES (Acceptance criteria)
  - Fully responsive UI matching mobile screenshots and flows (Need Cash, Provide Cash, Match).
  - Working registration/login using simulated OTP.
  - Create/Cancel cash requests and search for matches based on location+amount.
  - Map view showing approximate matches and distance.
  - Match details modal and simulated transaction flow to mark Completed.
  - Admin dashboard and basic user management controls.
  - Seed data for demo and instructions to toggle simulated payment flows.
  - README with run/deploy instructions, environment variables, and where to change the OTP simulation and maps API keys.
  - Privacy, Terms and Prototype disclaimer pages.

ASSETS & GRAPHICS
  - Placeholder logo: "TREASURE POINT" wordmark + simple treasure/chest icon (use gold accent).
  - Use a smartphone mockup for hero section â€” supply a simple PNG or allow builder to use a supplied screenshot.
  - Use minimal images; prefer SVG icons for crispness.

DELIVERABLE UX COPY (EXACT TEXT)
  - Home Hero:
      Heading: Need Cash? Find Someone Nearby.
      Subheading: Treasure Point connects people who need physical cash with verified cash providers through a location-based matching platform.
      CTA Buttons: [Need Cash] [Provide Cash]
  - Safety Banner:
      Prototype Notice: This is a prototype. No real UPI or money transfers occur. For production, integrate only via authorized partners.
  - Contact Section (exact):
      Contact Us
      Name: Ganta Naresh
      Mobile Number: 7702048269
      Email: gantanaresh89@gmail.com
  - Footer:
      Â© 2026 Treasure Point. All Rights Reserved.
      Founder/Developer: Ganta Naresh

IMPLEMENTATION NOTES FOR BUILDERS
  - Keep all monetary actions simulated and clearly labeled in the UI as simulated for demo.
  - Store configuration options (matching weights, tolerance thresholds, max radius) in admin-config table or environment variables so testers can tweak behavior.
  - Provide a developer/test mode toggle that:
      - Shows OTP codes for testing (e.g., OTP = 123456)
      - Allows simulated payment confirmations
      - Seeds test data
  - Add a "How to Demo" section in README that lists step-by-step demo scenarios (create need request, create provide request, show match found, accept, simulate payment, complete).

TASK BREAKDOWN FOR DEVELOPER (recommended sprints)
  Sprint 1 (UI Prototype): Home, Hero, Register/Login (simulated), Need Cash, Provide Cash, Dashboard, Contact, Profile, static Map.
  Sprint 2 (Backend & DB): Auth, requests CRUD, basic matching endpoint, transactions simulation, notifications.
  Sprint 3 (Map & Matching): integrate maps, geolocation, match scoring improvements, admin panel basics.
  Sprint 4 (Security & polish): Rate limiting, password hashing, audit logs, accessibility fixes.
  Sprint 5 (Deploy & Demo): host frontend/backend, seed demo data, prepare demo script.

FINAL REMARKS
  - This prompt is intended to create a full prototype that replicates the flows and UI from your specification. It intentionally avoids enabling real UPI/cash transfers.
  - After prototype UI and backend are validated, schedule legal and banking conversations before enabling any real payment features. NPCI and RBI guidelines must be followed for any cash/UPI integration.

END OF PROMPT
