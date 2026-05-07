# 🚀 Hosting Research Report: Unified Frontend & Backend Deployment (2025)

## 🎯 Objective
To identify the most cost-effective and low-maintenance hosting strategy for the "Agentic Website Landlord" project, specifically focusing on a **unified deployment** where both the static HTML/Tailwind frontend and the Python (FastAPI/Flask) backend can be managed under one platform.

---

## 📊 Platform Comparison Matrix

| Feature | **Render** (Recommended) | **Railway** | **Fly.io** | **Vercel / Netlify** | **DigitalOcean / Vultr** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Strategy** | Unified Web Services | Container-First | Edge/Container | Serverless Functions | Managed VPS (Droplet) |
| **Setup Effort** | ⭐⭐⭐⭐⭐ (Lowest) | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ (Highest) |
| **Free Tier** | Generous Static + Free Backend (with sleep) | Usage-based trial | Very generous for small apps | Industry standard/Best | No true free tier (low $5/mo) |
| **Frontend + Backend Unified?** | **Yes** (via Web Services) | **Yes** (via Services) | **Yes** (via Apps) | **Partial** (Functions only) | **Yes** (Full Server) |
| **Scaling Cost** | Predictable Monthly | Usage-based (can spike) | Highly Scalable | Pay-per-request | Fixed/Predictable |

---

## 🔍 Deep Dive: The Top Candidates

### 1. 🏆 The Winner: **Render**
*Why it wins:* It is the closest successor to the "Heroku Experience." You can host your static site (frontend) and your Python API (backend) as two separate services within the same project dashboard, both deploying automatically from your GitHub repo.

*   **Pros:** 
    *   Extremely simple "Git-to-Deploy" workflow.
    *   Zero configuration required for SSL/HTTPS.
    *   Supports static sites (Free) and Python web services in one place.
*   **Cons:** The free tier for the Python backend goes into "sleep mode" after 15 minutes of inactivity, causing a ~30-second "cold start" delay on the first visitor.
*   **Cost Estimate:** **$0/mo** (for testing) $\rightarrow$ **~$7/mo** (to keep backend always-on for production).

### 2. The Challenger: **Railway**
*Why it's great:* It is incredibly fast and developer-friendly. If you want to deploy a Docker container with your entire project in one click, Railway is unmatched.

*   **Pros:** 
    *   Unrivaled Developer Experience (DX).
    *   Handles databases (Postgres/Redis) with zero effort.
    *   Supports monorepos perfectly.
*   **Cons:** The pricing model is strictly usage-based; if your discovery engine runs a massive scrape, you could see unexpected costs.
*   **Cost Estimate:** **$0 - $5/mo** (depending on usage).

### 3. The "Serverless" Approach: **Vercel / Netlify**
*Why it's great:* If we rewrite the `lead_forward_engine.py` to run as a "Serverless Function" (one function per route), we can host everything for $0 indefinitely.

*   **Pros:** 
    *   Infinite scalability.
    *   The fastest global delivery of frontend assets.
*   **Cons:** Requires a fundamental change in how our Python backend is structured (moving from a long-running process to event-driven functions).
*   **Cost Estimate:** **$0/mo** (until you hit massive traffic).

---

## 💡 Final Recommendation & Implementation Strategy

### **Phase 1: The "Zero-Dollar" Prototype (Current Target)**
We should proceed with **Render**. It allows us to maintain our current Python structure without rewriting code for serverless functions, and it provides the easiest path to a live, production-ready URL.

**Implementation Plan:**
1.  **Frontend:** Continue using GitHub Pages/Render Static for the `index.html`.
2.  **Backend:** Wrap `lead_forward_engine.py` in a simple **FastAPI** wrapper and deploy it as a **Render Web Service**.
3.  **Unified Management:** Use a single GitHub repository where a change to a `.py` file triggers a backend redeploy, and a change to `.html` triggers a frontend redeploy.

### 🚀 Next Steps for Approval
1.  **Approve the Render strategy.**
2.  If approved, I will begin the "Backend Wrapper" development (FastAPI) and prepare the `Dockerfile` for deployment.
