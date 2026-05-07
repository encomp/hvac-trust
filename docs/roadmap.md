# Project Roadmap: Next Steps

## 🔴 High Priority: Backend & Lead Capture
### Task: Implement Lead Forwarding Engine (Backend)
- [ ] **API Development:** Wrap `scripts/lead_forward_engine.py` in a lightweight FastAPI or Flask wrapper.
- [ ] **CORS Configuration:** Ensure the frontend landing page can securely POST data to the new API.
- [ ] **Schema Validation:** Implement Pydantic models to validate incoming lead data (Name, Email, Phone, Service Needed).

### Task: Cloud Deployment
- [ ] **Containerization/Setup:** Prepare environment for deployment on Render or Railway.
- [ ] **Environment Configuration:** Securely configure `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `SMTP` credentials in the production environment.
- [ ] **End-to-end Testing:** Verify a lead submission travels from the HTML form -> Backend API -> Email/SMS notification.

## 🟡 Medium Priority: Scaling Discovery
### Task: Expand Discovery Engine
- [ ] **Multi-City Scans:** Parameterize `discovery_engine_v2.py` to run across multiple US metropolitan areas automatically.
- [ ] **Automated Reporting:** Schedule a cron job to generate weekly "Trust Gap" reports for review.

## 🟢 Low Priority: Optimization
### Task: Advanced SEO & Design
- [ ] **A/B Testing Setup:** Implement basic analytics tracking to measure landing page performance.
- [ ] **Design Iteration:** Experiment with different Tailwind layouts for higher conversion rates.
