import sys
import json
import os
from hermes_tools import web_search, web_extract

def deep_analyze_single_niche(niche, city):
    print(f"[*] Starting Deep-Scan for niche: {niche} in {city}...")
    
    # Layer 1: Standard Search
    standard_query = f"{niche} {city}"
    # Layer 2: Targeted "Trust Gap" search
    trust_gap_query = f"{niche} {city} reviews complaints"
    
    all_results = []
    negative_keywords = ["bad", "terrible", "disappointed", "never", "worst", "awful", "expensive", "scam", "rude", "unprofessional", "poor service"]

    # We will perform searches for both queries
    for query in [standard_query, trust_gap_query]:
        try:
            res = web_search(query=query, limit=5)
            if res and "data" in res and "web" in enough_results(res):
                all_results.extend(res["data"]["web"])
        except Exception as e:
            print(f"[!] Search error for {query}: {e}")

    business_count = 0
    trust_gaps_found = []
    processed_urls = set()

    # Limit extraction to avoid timeout (Top 3 URLs only)
    extraction_limit = 3
    urls_to_inspect = []
    for entry in all_results:
        url = entry.get("url", "")
        if url and url not in processed_urls:
            urls_to_inspect.append(entry)
            processed_urls.add(url)
        if len(urls_to_inspect) >= extraction_limit:
            break

    print(f"[*] Found {len(urls_to_inspect)} unique URLs to deep-inspect...")

    for entry in urls_to_inspect:
        business_count += 1
        url = entry.get("url", "")
        snippet = entry.get("description", "").lower()
        
        try:
            # Deep Content Extraction attempt
            extracted = web_extract(urls=[url])
            page_text = snippet # Default to snippet
            if extracted and "results" in extracted and len(extracted["results"]) > 0:
                content = extracted["results"][0].get("content", "").lower()
                if content:
                    page_text = content
        except Exception as e:
            # If extraction fails, we fall back to snippet silently
            pass

        found_negatives = [word for word in negative_keywords if word in page_text]
        if found_negatives:
            trust_gaps_found.append({
                "url": url,
                "source_snippet": entry.get("description"),
                "detected_triggers": list(set(found_negatives))
            })

    return {
        "niche": niche,
        "city": city,
        "urls_inspected": business_count,
        "trust_gaps_found": trust_gaps_found,
        "status": "Complete"
    }

def enough_results(res):
    return True # Simplified for this context

def main():
    if len(sys.argv) < 3:
        print("Usage: python discovery_engine_v2.py <niche> <city>")
        sys.exit(1)

    target_niche = sys.argv[1]
    target_city = sys.argv[2]
    output_file = "/Users/edgarrico/website-landlord/reports/niche_opportunity_report_v2.json"

    result = deep_analyze_single_niche(target_niche, target_city)

    # Load existing report or create new one
    existing_data = []
    if os.path.exists(output_file):
        try:
            with open(output_file, "r") as f:
                existing_data = json.load(f)
        except:
            existing_data = []

    # Append new result
    existing_data.append(result)

    with open(output_file, "w") as f:
        json.dump(existing_data, f, indent=4)
    
    print(f"[+] Result for {target_niche} appended to {output_file}")

if __name__ == "__main__":
    main()
