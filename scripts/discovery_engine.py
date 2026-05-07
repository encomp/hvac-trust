from hermes_tools import web_search
import json
import re

def analyze_niche(niche, city):
    query = f"{niche} {city}"
    print(f"[*] Researching niche: {niche} in {city}...")
    
    results = web_search(query=query, limit=10)
    
    business_count = 0
    trust_gaps_found = []
    negative_keywords = ["bad", "terrible", "disappointed", "never", "worst", "awful", "expensive", "scam", "rude", "unprofessional"]

    if not results or "data" not in results or "web" not in results["data"]:
        return {"niche": niche, "error": "No results found"}

    for entry in results["data"]["web"]:
        business_count += 1
        snippet = entry.get("description", "").lower()
        url = entry.get("url", "")
        
        # Check for negative sentiment indicators in the snippet
        found_negatives = [word for word in negative_keywords if word in snippet]
        if found_negatives:
            trust_gaps_found.append({
                "url": url,
                "snippet": entry.get("description"),
                "triggers": found_negatives
            })

    return {
        "niche": niche,
        "city": city,
        "businesses_scanned": business_count,
        "trust_gaps_found": trust_gaps_found,
        "status": "Complete"
    }

def main():
    target_city = "Austin, TX"
    niches = [
        "Junk Removal", 
        "Tree Service", 
        "HVAC Repair", 
        "Pest Control", 
        "Foundation Repair", 
        "Roofing Contractor",
        "Drain Cleaning",
        "Handyman Services"
    ]
    
    final_report = []

    for niche in niches:
        try:
            analysis = analyze_niche(niche, target_city)
            final_report.append(analysis)
        except Exception as e:
            print(f"[!] Error researching {niche}: {e}")

    output_path = "../reports/niche_opportunity_report.json"
    with open(output_path, "w") as f:
        json.dump(final_report, f, indent=4)
    
    print(f"[+] Discovery complete. Report saved to {output_path}")

if __name__ == "__main__":
    main()
