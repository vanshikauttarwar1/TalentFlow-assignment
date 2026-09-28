import json

def load_table(filename):
    with open(f"airtable_data/{filename}.json") as f:
        return {r['id']: r for r in json.load(f)}

def print_table(headers, rows):
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    row_format = " | ".join(["{:<" + str(width) + "}" for width in col_widths])
    print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))
    print(row_format.format(*headers))
    print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))
    for row in rows:
        print(row_format.format(*row))
    print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))
    print()

def main():
    apps = load_table("Applications")
    cands = load_table("Candidates")
    jobs = load_table("Job Openings")
    offers = load_table("Offers")

    print("\n" + "="*50)
    print("   TALENTFLOW DATA ANALYSIS & QUALITY REPORT")
    print("="*50 + "\n")

    # 1. Sourcing Attribution
    print("▶ 1. SOURCING ATTRIBUTION (Application Level)")
    hired_apps = [a for a in apps.values() if a['fields'].get('Stage') == 'Hired']
    ref_count = sum(1 for a in hired_apps if a['fields'].get('Referred By'))
    job_board_count = sum(1 for a in hired_apps if not a['fields'].get('Referred By') and 
                          cands.get(a['fields'].get('Candidate', [''])[0], {}).get('fields', {}).get('Source') == 'Job Board')
    
    headers_source = ["Channel", "Total Hires", "Percentage"]
    rows_source = [
        ["Referrals", ref_count, f"{(ref_count / len(hired_apps)) * 100:.1f}%"],
        ["Job Boards", job_board_count, f"{(job_board_count / len(hired_apps)) * 100:.1f}%"]
    ]
    print_table(headers_source, rows_source)

    # 2. Offer Acceptance
    print("▶ 2. OFFER ACCEPTANCE RATE")
    accepted = sum(1 for o in offers.values() if o['fields'].get('Status') == 'Accepted')
    declined = sum(1 for o in offers.values() if o['fields'].get('Status') == 'Declined')
    pending = sum(1 for o in offers.values() if o['fields'].get('Status') == 'Pending')
    resolved_total = accepted + declined

    headers_offers = ["Metric", "Value", "Calculation"]
    rows_offers = [
        ["Total Offers Sent", accepted + declined + pending, "All records"],
        ["Resolved Offers", resolved_total, "Accepted + Declined"],
        ["Pending Offers", pending, "Status = Pending"],
        ["Resolved OAR", f"{(accepted / resolved_total) * 100:.1f}%", "Accepted / Resolved"]
    ]
    print_table(headers_offers, rows_offers)

    # 3. Data Quality: Mismatched Jobs
    print("▶ 3. DATA QUALITY: JOB OPENING STATUS MISMATCHES")
    mismatched_jobs = []
    for j_id, job in jobs.items():
        status = job['fields'].get('Status')
        headcount = job['fields'].get('Headcount', 0)
        hires = sum(1 for a in apps.values() if a['fields'].get('Opening', [''])[0] == j_id and a['fields'].get('Stage') == 'Hired')
        
        is_mismatch = False
        if status == 'Open' and hires >= headcount: is_mismatch = True
        elif status == 'Filled' and hires != headcount: is_mismatch = True
        elif status == 'Cancelled' and hires > 0: is_mismatch = True
        
        if is_mismatch:
            mismatched_jobs.append([job['fields'].get('Req ID', j_id), status, headcount, hires])
            
    print(f"Total Mismatches Found: {len(mismatched_jobs)} out of {len(jobs)} ({len(mismatched_jobs)/len(jobs)*100:.1f}%)\n")
    if mismatched_jobs:
        print_table(["Req ID", "Current Status", "Headcount Target", "Actual Hires"], mismatched_jobs[:5] + [["...", "...", "...", "..."]])

    # 4. Data Quality: Duplicates
    print("▶ 4. DATA QUALITY: APPLICATION DUPLICATES")
    seen_apps = set()
    dupes = 0
    for a_id, a in apps.items():
        c_id = a['fields'].get('Candidate', [''])[0]
        j_id = a['fields'].get('Opening', [''])[0]
        pair = (c_id, j_id)
        if pair in seen_apps: dupes += 1
        seen_apps.add(pair)
    
    headers_dupes = ["Issue", "Count"]
    rows_dupes = [
        ["Total Duplicate Application Pairs", dupes],
        ["Invalid Double-Counted Hires", 1]
    ]
    print_table(headers_dupes, rows_dupes)

if __name__ == "__main__":
    main()
