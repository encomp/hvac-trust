# Phase 3: Asset Generation & Deployment Blueprint
## Project: Website Landlord (Rank and Rent)
## Target Niche: HVAC Repair (Austin, TX - Trust Gap Focus)

### 1. Objective
Generate a high-converting, SEO-optimized static website ("The Asset") that captures leads via webhooks and routes them to local partners.

### 2. Technical Architecture (Phase 3)
*   **Core Technology:** Single-page HTML5 with Tailwind CSS (via CDN for zero-config deployment).
*   **SEO Engine:** Injection of `schema_hvac.json` into the `<head>` section.
*   **Lead Capture:** An integrated `<form>` that sends data to a backend webhook (the Python lead engine).
*   **Deployment Target:** GitHub Pages (Static) + Render/Railway (Backend API for Python).

### 3. Implementation Steps
#### Step 1: The HTML Scaffold
Create `index.html` with the following sections:
- **Hero Section:** High-impact headline ("Austin's Most Transparent HVAC Service").
- **Trust Bar:** Icons representing "No Hidden Fees," "Upfront Pricing," and "Local Technicians."
- **Service List:** Detailed descriptions of AC repair, heating maintenance, etc.
- **Lead Capture Form:** Fields for [Name, Phone, Issue/Description].
- **Footer:** SEO-rich footer with Austin-specific geo-keywords.

#### Step 2: The Schema Injection
Manually (or via script) embed the contents of `~/website-landlord/templates/schema_hvac.json` into a `<script type="application/ld+json">` tag in the `<head>`.

#### Step 3: Lead Capture Integration
Configure the form `action` attribute to point to the deployed Python API endpoint (e.g., `/submit-lead`). For local testing, we will use a mock endpoint.

### 4. Deployment Roadmap
1.  [ ] **Build Asset:** Create `assets/hvac_austin/index.html`.
2.  [ ] **Integrate SEO:** Embed Schema.
3.  [ ] **Test Lead Flow:** Verify form submission triggers the Python script logic.
4.  [ ] **Push to Production:** Deploy HTML to GitHub Pages.
