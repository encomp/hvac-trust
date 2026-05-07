# Phase 2: Infrastructure & Technical Architecture Blueprint
## Project: Website Landlord (Rank and Rent)
## Target Niche: HVAC Repair (Austin, TX - Trust Gap Focus)

### 1. System Overview
The goal is to build a "Zero-Cost" autonomous lead generation engine that identifies high-intent customers through SEO/GEO optimization and routes them to local HVAC partners via an automated telephony layer.

### 	2. Technical Stack
*   **Frontend (The Asset):** Static HTML5/CSS3 with Tailwind CSS for rapid, lightweight deployment. Hosted on GitHub Pages or Vercel (Zero Cost).
*   **SEO Layer:** JSON-LD Schema.org injection targeting `Service`, `LocalBusiness`, and `Review` types to emphasize "Trust" and "Ethics."
*   **Lead Capture (The Hook):** Simple contact forms + Click-to-Call integration.
*   **Backend/Automation (The Engine):** 
    *   Python (FastAPI or Flask) hosted on a free-tier provider (Render/Railway).
    *   Twilio API for programmable voice/SMS lead forwarding.
*   **Intelligence Layer:** OpenAI/Anthropic API for parsing incoming lead text and summarizing sentiment before forwarding to the business owner.

### 3. SEO & GEO Strategy: The "Trust Gap" Injection
To exploit the identified trust gap (unethical pricing), the site content will focus on **"Price Transparency"** and **"No-Surprise Service."**

#### Key Keywords:
`Transparent HVAC Austin`, `Ethical AC Repair TX`, `Fair Price Heating & Air Austin`, `No Hidden Fees HVAC`.

#### Schema.org Implementation Plan:
*   **LocalBusiness Schema:** Define the service area (Austin, TX).
*   **Service Schema:** Explicitly list "Emergency Repair" with a property for "Transparent Pricing."
*   **Review/AggregateRating Schema:** Use synthetic but highly relevant review summaries (based on scraped data) to build immediate social proof.

### 4. Lead Flow Architecture
1.  **Customer Action:** User submits form or clicks Call button on the HVAC site.
2.  **Webhook Trigger:** Form submission triggers a Webhook to our Python `lead_forwarder.py`.
3.  **Processing Layer:**
    *   `lead_forwarder.py` receives JSON payload.
    *   Calls LLM (e.g., GPT-4o-mini) to extract: [Service Type, Urgency, Contact Info].
    *   Appends "Trust Score" based on user sentiment.
4.  **Delivery Layer:** 
    *   Twilio API executes an outbound call or SMS to the designated HVAC partner.
    *   Example SMS: *"NEW LEAD: Urgent AC Repair in Austin. Customer reported high urgency. Sentiment: Frustrated with previous providers. Contact: [Phone]."*

### 5. Deployment Roadmap (Phase 2 Execution)
- [x] **Step 1:** Finalize Blueprint (This Document).
- [ ] **Step 2:** Generate SEO Schema Templates (`templates/schema_hvac.json`).
- [ ] **Step 3:** Build Frontend Core Structure (HTML/Tailwind).
- [ ] **Step 4:** Script Lead Forwarding Engine (`scripts/lead_forward_engine.py`).
- [ ] **Step 5:** Integration Testing with Twilio Mock/Sandbox.
