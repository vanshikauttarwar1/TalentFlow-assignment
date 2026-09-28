# Process Document

## 1. Prompt Timeline

**[2026-09-28T15:16:38Z | +0m]**
```
I need to complete this TalentFlow PM exercise..... I've shared the assignment files, and the Airtable API key is in the .env file.
First, read the brief and understand the project. Then pull the Airtable data, cache it locally, and set up a clean structure for the analysis.

For now, just help me understand what we have — tables, fields, record counts, relationships, date ranges, aetc etc and any obvious data-quality issues.

Don't make any product or roadmap decisions yet. We'll do that after we understand the data.
@[/Users/vanshika/TalentFlow/CANDIDATE_PACK_PM.md.docx:L17-L18] @[/Users/vanshika/TalentFlow/submission.md.docx] @[/Users/vanshika/TalentFlow/.env]
```

**[2026-09-28T15:23:32Z | +6m]**
```
Before  calculating VP's claims,, 
1. do a proper data-quality check.
2. Go through each tables and relationships and quantify anything that could affect the two claims - especially hire source attribution and offer status. Don't assume that a blank field means a particular status.
3.  check for duplicates, broken links, inconsistent statuses, and date issues.


Give me the important findings with counts or percentages and tell me which ones can actually change our conclusions.....
```

**[2026-09-28T15:49:22Z | +32m]**
```
are u 100% sure abt these findings? show the calculations and flag anything you're not fully confident about.

Once verified, save the validated findings and supporting numbers in an updated-data.md file so we can use it for the remaining deliverables.
```

**[2026-09-28T15:53:17Z | +36m]**
```
These findings look useful.... but lets double-check them before we use them.

Recalculate total vs unique hires, hire source attribution, and offer acceptance rate. Also trace the duplicate application/offer cases and confirm whether each should count as 1 hire or 2.

Show me the numerator + denominator for each % and flag anything that could affect the conclusions.

Don't make roadmap recommendations yet.
```

**[2026-09-28T15:56:36Z | +39m]**
```
good.... but, 
1. Can u verify exactly how the hire source is being determined at the application level? I want the attribution rule to be clear and reproducible, especially for cases where Candidate Source and Referred By are different.
2. Also check if there are any other duplicate/edge cases that could affect the 26 hires or the 6/26 job-board number.

Once this is confirmed, save the final validated numbers + logic in updated-data.md.
```

**[2026-09-28T15:58:30Z | +41m]**
```
great.... lets do D1 now...
Based on the data, give me a clear verdict on both VP claims.
```

**[2026-09-28T16:01:09Z | +44m]**
```
1. Save the final D1 in a separate d1.md file. Each deliverable should be in its own file.
2. For each claim, use this exact structure:
VP's number + how they got it
Validated number + exact numerator/denominator
What the data actually tells us
Verdict: build, don't build, or build something different
1-2 lines of reasoning

Keep it concise and use only numbers we've verified.

3. Also remove subjective wording like "exceptionally healthy" or "recruiting team is doing a great job" — keep the conclusion data-driven.
```

**[2026-09-28T16:04:55Z | +48m]**
```
great.... lets do D2 now.

Based on everything we've validated so far, propose the 6 engineer-week roadmap.
I need exactly:

Three things to build, in priority order
1. what we build
2. rough size in engineer-weeks
3. the specific number/data point that justifies it
4. what problem it solves
Three things NOT to build
1. what we're not building
2. why not
3. the data/number behind the decision

6 engineer-weeks is a timeline we have so make sure build engg effort is 6 weeks
```

**[2026-09-28T16:05:26Z | +48m]**
```
crosscheck again...
Don't invent data or numbers. If something isn't supported by the data, flag it instead of assuming.
Keep it concise and PM-style.....
```

**[2026-09-28T16:09:01Z | +52m]**
```
why did we jump to D3? 
I asked to cross-check D2 itself — specifically:
"....Keep it concise and PM-style." was for d2

So let's validate D2 first. Don't work on D3 yet.
```

**[2026-09-28T16:11:32Z | +54m]**
```
crosscheck...
1. Verify the 132/350 missing rejection reasons are actually for applications that reached Rejected stage.
2.  application-level source tracking is a real product gap, and flag the 3-week estimate if it's an assumption.
3. Verify the dedup point — don't call them duplicate candidate records unless the data supports that.
```

**[2026-09-28T16:19:04Z | +62m]**
```
no wait...
crosscheck 16/160 ?

confirm they are actually Closed applications
confirm the interview fields are blank
confirm this creates a measurable reporting/capacity issue

Also verify the duplicate application count and the 3-week estimate assumptions.
```

**[2026-09-28T16:21:39Z | +65m]**
```
@[/Users/vanshika/TalentFlow/d2.md] crosscheck each number again
```

**[2026-09-28T16:26:06Z | +69m]**
```
for the 10/24 mismatch count, just check the 4 categories u listed and confirm the math is mathing and its  actually adding up without double-counting.
```

**[2026-09-28T16:27:34Z | +70m]**
```
are u 100% sure abt the metric now? just crosscheck each data again
```

**[2026-09-28T16:32:01Z | +75m]**
```
before we lock D3, crosscheck the metric itself one more time.
check is really math is mathing......
Verify:
1. 26 Accepted + 5 Declined = 31 decided
2. 26/31 = 83.9%
3. whether `Offered On` is actually the right date for the reporting window
4. how the 5 Pending offers, especially the 4 with `Decision On`, should be handled
5. check for any other offer edge cases that could change the metric

Show the actual counts and calculation and flag anything uncertain......
```

**[2026-09-28T16:34:49Z | +78m]**
```
can u directly run a query/script for D2 and D3 and show me the actual output?

I want:

1. total offers by Status
2. Accepted / (Accepted + Declined)
3. all Pending offers with `Offered On` + `Decision On` + Status
4. any other offer records that could affect the metric

Just show the output + calculation. Don't interpret yet.
```

**[2026-09-28T16:37:52Z | +81m]**
```
wait.... don't rewrite d1/d2/d3 yet.

For the 5 Pending offers, directly check:

1.days since Offered On
2. Decision On
3. parent application status/stage
4.  any expiry/decline field

Also check if the data actually supports the 14-day rule or if that's just an assumption.

Just show raw output + math, no recommendations yet.
```

**[2026-09-28T16:38:14Z | +81m]**
```
r u halucinating?
```

**[2026-09-28T16:41:22Z | +84m]**
```
Based on the latest crosscheck, update D3 with these rules:

1. Do NOT use a 14-day rule. The data doesn't support it because 10/31 decided offers took >14 days.
2. Do NOT classify the 5 Pending offers as Declined.
3. Define Acceptance Rate as:
   Accepted / (Accepted + Declined) = 26/31 = 83.9%
4. Show Pending separately: 5/36 = 13.9%.
5. Explicitly flag that 4 of the 5 Pending offers have a Decision On date but still have Status=Pending. Treat this as a data-quality/definition ambiguity, not as an automatic decline.
6. For the reporting window, use Offered On as the cohort date, but clearly define how offers whose decision happens after the reporting period are handled.
7. Update d3.md only. Do not change D1 or D2 yet.

Keep it concise and include the exact numerator, denominator, edge cases, time window, and dashboard behavior.
```

**[2026-09-28T16:42:59Z | +86m]**
```
Verify:



Total offers

Accepted / Declined / Pending counts

Any mismatch between Status and Decision On

Any missing Decline Reason where it should exist

Any other offer-level inconsistency

Exact count and % affected

Whether each issue actually changes our D3 metric or just needs a data-quality flag

Use raw data and show the actual counts/math.



Don't make recommendations yet and don't update D1/D2/D3.
```

**[2026-09-28T16:43:57Z | +87m]**
```
check ONLY the Job Openings table.

Verify:
Total job openings
Status vs Headcount vs actual Hires
Every mismatch, with exact record count
Make the mismatch categories mutually exclusive so nothing is double-counted
Show the exact math and percentage of all job openings affected
Check whether these mismatches affect any D1/D2 decision

No recommendations yet. Don't update D1/D2/D3. Just show raw findings and math.
```

**[2026-09-28T16:45:47Z | +89m]**
```
D4:

Verify:
Total offers
Accepted / Declined / Pending counts
Any mismatch between Status and Decision On
Any missing Decline Reason where it should exist
Any other offer-level inconsistency
Exact count and % affected

Whether each issue actually changes our D3 metric or just needs a data-quality flag

Use raw data and show the actual counts/math.



Don't make recommendations yet and don't update D1/D2/D3.
```

**[2026-09-28T16:47:04Z | +90m]**
```
D4 phase 2: check ONLY the Job Openings table.
Verify:
Total Job Openings
Status distribution
Headcount for each opening
Actual number of Hired applications for each opening
Any mismatch between Status, Headcount and actual Hires
Exact count and % of openings affected
Show the records/mismatch categories and math
Explain whether each issue affects D1/D2/D3 or is only a data-quality issue

Don't make recommendations yet. Don't update any other deliverable.
```

**[2026-09-28T16:48:42Z | +92m]**
```
Add the verified Job Openings findings to d4.md as the next working section.

Use neutral wording: "status/headcount/actual hires mismatch" — do NOT call them "ghost jobs" or assume why the mismatch exists.

Include:
* 24 total openings
* Status: 11 Open, 8 Filled, 3 On Hold, 2 Cancelled
* 11/24 (45.8%) have a mismatch
* 4 Open with headcount met
* 1 Open over-hired
* 2 Filled with zero hires
* 2 Filled over-hired
* 2 Cancelled with hires
* State that this does not affect D1 or D3 based on our current calculations, but does affect D2 because the job-status automation sizing was based on this data.

Don't update D1 or D2 yet. Don't add recommendations.
```

**[2026-09-28T16:49:46Z | +93m]**
```
check the Applications table and its relationships.

Verify ONLY:

Total Applications
Applications with missing/invalid Candidate link
Applications with missing/invalid Job Opening link
Applications with missing Stage or Status
Rejected applications: count and whether all have Rejection Reason
Duplicate applications: define duplicate as the same Candidate applying to the same Job Opening more than once. Count the duplicate application pairs/records.
Any impossible or inconsistent application dates
Any other application-level issue that could materially affect D1, D2, or D3.

For every issue, show exact count, percentage, and actual math.

Important:

Do NOT call duplicate applications "duplicate candidates".
Do NOT assume missing fields are errors if they are legitimately not applicable.
Do NOT make recommendations.
Do NOT update D1/D2/D3.
Add only verified findings to the existing d4.md as a new working section.
```

**[2026-09-28T16:51:30Z | +94m]**
```
crosscheck whole findings again if we are 100% correct?
```

**[2026-09-28T16:53:17Z | +96m]**
```
check again

total Candidates
duplicate Candidate records by email
Candidate Source distribution
applications with Referred By
for those applications, compare Referred By vs Candidate Source
calculate the actual hired-channel counts using our rule:
Referral if Referred By exists, otherwise Candidate Source
verify the 26 hired applications and 24 unique hired candidates
etc
etc

Show exact counts + percentages + math.

Add only verified findings to d4.md. No recommendations.
```

**[2026-09-28T16:56:25Z | +99m]**
```
Rewrite D1 and D2 based on our verified analysis.

D1: verdict + deciding number for each claim.
D2: exactly 3 builds totaling 6 engineer-weeks + exactly 3 things not to build, with evidence.

Update only d1.md and d2.md.
```

**[2026-09-28T16:57:50Z | +101m]**
```
crosscheck@[/Users/vanshika/TalentFlow/d1.md]@[/Users/vanshika/TalentFlow/d2.md]@[/Users/vanshika/TalentFlow/d3.md]@[/Users/vanshika/TalentFlow/d4.md]
```

**[2026-09-28T16:59:47Z | +103m]**
```
Referred By:
Why is it now 24/27 mismatched when the previous verified result was 26/27?

Hired applications:
Verify exactly:
total Hired applications
unique Candidate IDs among Hired applications
candidates with multiple Hired applications
their Job Openings/Req IDs

Show raw rows + exact math.

Do not edit any files. No recommendations.
```

**[2026-09-28T17:08:08Z | +111m]**
```
Update `d4.md`.

Re-run the analysis on the source data and verify all key D4 findings independently, especially:

* Referred By vs Candidate Source
* Hired applications vs unique candidates
* Multiple hired applications and whether they are legitimate or duplicates
* Duplicate applications
* Job Opening status vs headcount vs hires
* Offer status vs Decision On consistency

Use raw data as the source of truth, not previous chat summaries. Show exact calculations and explain the impact of each data-quality issue.

Do not modify D1, D2, D3

After editing, show me the complete `d4.md`.
```

**[2026-09-28T17:10:16Z | +113m]**
```
Fix only these in `d4.md`:

* Remove “25 actual humans were hired.” State: **26 Hired applications → 24 unique candidates; one legitimate cross-requisition hire and one duplicate same-requisition application.**
* Replace **“eliminate ghost jobs”** with **“improve job status synchronization and capacity tracking.”**
* Replace **“Permanently validates”** with **“provides strong evidence for.”**

Keep all numbers and other findings unchanged. Show the updated file.
```

**[2026-09-28T17:11:12Z | +114m]**
```
Make only these 2 wording changes in `d4.md`:

* Change **“Unique Hired Candidates (Humans)”** to **“Unique Hired Candidates”**.
* Change **“shifts Referrals to the undisputed #1 channel for hires (38.5%)”** to **“shows Referrals as the largest attributed source for hires (38.5%)”**.

Keep everything else unchanged. Show the updated file.
```

**[2026-09-28T17:12:18Z | +115m]**
```
Just make these 2 wording changes in `d4.md`:

* Change “It directly validates the D2 roadmap, strictly justifying...” to “It supports the D2 roadmap, given the 45.8% mismatch rate...”
* Change “this perfectly supports our D2 decision” to “this supports our D2 decision”

Keep everything else, including all numbers, exactly the same.
```

**[2026-09-28T17:14:22Z | +117m]**
```
Create/update `d1.md` using `d4.md` + source data.
Evaluate the VP’s 2 claims:
1. Job Boards are the biggest channel at 26.9% → should we build the integration?
2. Offer acceptance is ~72% → what should we do?
For each: show the claim, key numbers, verdict (Build / Don’t Build / Build Something Different), and 2–3 line reasoning.
Use verified numbers only. Keep it concise and PM-focused.
Show the final `d1.md`.
```

**[2026-09-28T17:15:18Z | +118m]**
```
Make only these wording changes in `d1.md`:

* Replace “artificially deflates the metric” with “includes pending offers in the denominator.”
* Replace “true, decided close rate is highly healthy at 83.9%” with “the resolved-offer acceptance rate is 83.9%.”
* Keep all numbers, verdicts, and other content unchanged.

Show the final `d1.md`.
```

**[2026-09-28T17:16:26Z | +119m]**
```
Change only:
“candidate-closing tools to fix a crisis that doesn't exist”
to:
“candidate-closing tools based on the current acceptance-rate data.”

Keep everything else unchanged.
```

**[2026-09-28T17:18:13Z | +121m]**
```
@[/Users/vanshika/TalentFlow/d1.md]@[/Users/vanshika/TalentFlow/d2.md] @[/Users/vanshika/TalentFlow/d3.md]@[/Users/vanshika/TalentFlow/d4.md]  analyse throughly
```

**[2026-09-28T17:20:53Z | +124m]**
```
Do one final crosscheck of `d1.md`, `d2.md`, `d3.md`, and `d4.md`.

Check:

* All numbers and calculations match the source data
* D1 claims/verdicts are supported by D4
* D2 priorities and 3 not-to-build decisions are supported by the data
* D3 metric definition matches D1
* No contradictions across the 4 files
* Remove subjective/strong wording like “panic”, “undeniable”, “flawless”, “ghost jobs”, “forcefully”, etc.

Do NOT change the files yet.

Give me only:

1. Issues found
2. Exact correction needed
3. Whether D1-D4 are ready for D5
```

**[2026-09-28T17:21:41Z | +125m]**
```
Apply only the wording corrections you identified in `d2.md`, `d3.md`, and `d4.md`.

Do not change any numbers, calculations, priorities, verdicts, or structure.

After editing, confirm:

* D1–D4 are internally consistent
* All calculations match the source data
* No strong/subjective wording remains

Do not create or modify `d5.md` yet.
```

**[2026-09-28T17:22:39Z | +126m]**
```
Create `d5.md` as a concise 1-page executive memo based only on the final `d1.md`–`d4.md`.

Structure it as:

1. **What we found** — key findings and numbers
2. **What we’re doing** — exactly 3 builds within 6 engineer-weeks
3. **What we’re not doing** — exactly 3 items
4. **What happens next** — immediate next steps

Keep it human, concise, PM-focused, and data-driven.

Use only verified numbers from D1–D4. Do not introduce new analysis or recommendations.

Show me the complete `d5.md`.
```

**[2026-09-28T17:23:20Z | +126m]**
```
Clean up `d5.md` with only these wording changes:

* “Offer acceptance is highly healthy” → “Offer acceptance is higher than the reported figure.”
* “includes pending offers as failures” → “includes 5 pending offers in the denominator.”
* “eliminate manual tracking errors” → “reduce manual tracking errors.”
* “giving Finance accurate capacity data” → “improving capacity visibility.”
* Remove “already highly healthy” from the Offer Acceptance Optimization section.
* “Candidate data is consistent” → “Candidate emails are 100% unique.”
* “upcoming 6-week engineering sprint” → “within the 6 engineer-week budget.”

Keep all numbers, decisions, roadmap items, and structure unchanged. Show the final `d5.md`.
```

**[2026-09-28T17:24:10Z | +127m]**
```
Make only these 3 changes in `d5.md`:

* “6-week product roadmap” → “6 engineer-week roadmap”
* “The reported 72.2% acceptance rate incorrectly includes 5 pending offers in the denominator.” → “The reported 72.2% figure includes 5 pending offers in the denominator.”
* “We will not allocate resources to our second-best channel (23.1%) based on the assumption that it is our primary driver.” → “We will not allocate resources to Job-Board integration while application-level attribution shows Job Boards at 23.1% of hires.”

Keep everything else unchanged.
```

**[2026-09-28T17:25:41Z | +129m]**
```
1. “stem from reporting inaccuracies, rather than performance failures.”
Use:
“highlight reporting and data-quality gaps affecting the two areas raised by leadership.”
2. “We are prioritizing high-ROI infrastructure fixes…”
to:
“We are prioritizing targeted fixes…”
```

**[2026-09-28T17:29:30Z | +132m]**
```
Make only these final wording/logic fixes across d1.md, d2.md, d3.md, d4.md, and d5.md. Keep all numbers, structure, and other content unchanged.

1. D1: “When we correctly attribute sourcing” → “Using application-level attribution”.

2. D2 Build #2: Replace the rigid “automatically sets to Filled and blocks Hired if Headcount is exceeded” logic with: “reconciles Job Opening status with Headcount and Hired Applications, automatically flagging or updating status when thresholds are reached or exceeded.”

3. D2 Not-build #1: Replace with: “We will not allocate resources to Job-Board integration while application-level attribution shows Job Boards at 23.1% of hires.”

4. D2 Not-build #2: Remove “72% crisis” and replace with: “The 72% figure includes pending offers in the denominator, so it does not represent the acceptance rate among decided offers.”

5. D3: “accepted/declined offers” → “decided offers”.

6. D4: “systematically masks referral volume” → “does not consistently capture application-level referral information.”

7. D4: “Proves that the deduplication bug slightly inflated the hiring numbers…” → “Shows that one duplicate application resulted in an additional Hired application for the same requisition.”

8. D5: “Referrals are our primary channel” → “Referrals are the largest attributed source for hires.”

9. D5: “duplicate profiles are a non-issue” → “Candidate emails are 100% unique.”

Do not make any other changes.
```

**[2026-09-28T17:34:59Z | +138m]**
```
Create a polished, professional **single-file `talentflow_submission.html`** for my TalentFlow PM assignment.

First, read the existing `d1.md`, `d2.md`, `d3.md`, `d4.md`, `d5.md`, and `findings.csv` files in the project. Use them as the **only source of truth**. Do not create new analysis or change any numbers.

The HTML should be a clean PM-style submission page with these sections:

1. **Executive Memo — D5**
2. **Decision Summary — D1**

   * VP Claim 1
   * VP Claim 2
   * Verdict + deciding number
3. **6-Week Engineering Roadmap — D2**

   * Exactly 3 things to build
   * Exactly 3 things not to build
   * Include effort and supporting numbers
4. **Offer Acceptance Rate Metric Spec — D3**

   * Numerator
   * Denominator
   * Edge cases
   * Time window
   * Dashboard behavior
5. **Data Quality & Trust — D4**

   * What is trustworthy
   * What is ambiguous/inconsistent
   * Magnitude
   * Impact on decisions
6. **Findings Table**

   * Render `findings.csv` as a proper readable table with:
     Claim | Metric | Value | Method | Confidence
7. **Code & Reproducibility**

   * Link/section for the analysis code and queries
   * Link/section for the Antigravity session transcript
   * If actual paths/URLs are unavailable, add clearly marked placeholders instead of inventing links.

Requirements:

* Keep all numbers exactly consistent with the source files.
* Do not introduce unsupported claims.
* Use clear headings, cards, tables, and subtle visual hierarchy.
* Make it responsive for desktop and mobile.
* Make it look like a strong **Product Manager case-study submission**, not a generic dashboard.
* Use plain HTML/CSS/JS in one file.
* Avoid external dependencies unless absolutely necessary.
* Add a small footer: `TalentFlow | Product Management Case Study`.
* Make the final page polished enough to submit directly.
```

**[2026-09-28T17:39:25Z | +142m]**
```
sanitise folder if require
```

**[2026-09-28T17:42:08Z | +145m]**
```
can u add this info 

Data Analysis Scripts: analyze_data.py | data_quality_check.py
Execution Transcript: Antigravity Session Transcript
Raw Data Cache: /airtable_data/ (Internal Access Only)
```

**[2026-09-28T17:44:45Z | +148m]**
```
when click on transcript jsonl should get downloaded
```

**[2026-09-28T17:45:58Z | +149m]**
```
its opening in tab insted directly should yet downloaded once click
```

**[2026-09-28T17:48:11Z | +151m]**
```
why cant we directly download if user just click on it
```

**[2026-09-28T17:50:48Z | +154m]**
```
data quality check why we are not giving in structure format?
```

**[2026-09-28T17:53:34Z | +156m]**
```
why we are not giving this in butiful way by seing user will feel happy and clutter free? if user want to see table there should be proper table , if user want to see metric it should be present in beautiful way 

5. What to send back
The memo, the roadmap and the metrics spec — one document is fine.
A findings table — claim, metric, value, method, confidence. Markdown or CSV. (The Findings table in the base is read-only for you, so send this as a file rather than writing rows.)
Your code or queries, in a repo or a zip. We will re-run them and expect your numbers back.
Your Claude Code session transcript.
```

**[2026-09-28T17:55:59Z | +159m]**
```
u can use html css js py if required but make it beautiful
```

**[2026-09-28T17:59:33Z | +162m]**
```
transcript is not downloadable
```

**[2026-09-28T18:03:38Z | +167m]**
```
make UI light i dont want dark UI
```

**[2026-09-28T18:06:45Z | +170m]**
```
@[/Users/vanshika/TalentFlow/CANDIDATE_PACK_PM.md.docx] check again if we did everything
```


## 2. Session Analysis

**Direction Changes:**
The AI initially moved too fast into formatting deliverables (D3), so I forced a hard pivot back to validating D2, telling it to cross-check the numbers first. Later, I requested a massive pivot in the final output format, abandoning the AI's static markdown files to request a "beautiful" and "clutter-free" interactive HTML dashboard, and subsequently instructed it to change it from a dark theme to a light theme.

**Verifications & Pushback:**
I aggressively pushed back against the AI's early conclusions and assumptions. I demanded exact mathematical proofs (numerator/denominator) for the VP's claims and heavily scrutinized its `Referred By` vs `Candidate Source` attribution logic. I frequently commanded the AI to "check again," "verify exactly," and "confirm the math is mathing," particularly concerning the 10/24 job opening mismatches and the 16/160 closed applications.

**Abandoned Approaches:**
We abandoned the AI's initial "14-day rule" for assuming offers were declined, because I pointed out that the data didn't support it (10/31 decided offers took >14 days). We also abandoned the AI's initial approach of generating separate markdown documents (`d1.md`, `d2.md`, etc.), replacing them entirely with a single, consolidated `talentflow_submission.html` dashboard. We also abandoned linking raw JSONL files directly in the browser after encountering tab-opening issues, switching to `.zip` archives instead.

**Decisions:**
I rigidly controlled the analytical methodology, metrics definitions, and roadmap priorities (e.g., explicitly commanding the AI: "Define Acceptance Rate as: Accepted / (Accepted + Declined) = 26/31 = 83.9%"). I left the technical implementation—the Python scripting, data extraction strategies, and the design/aesthetics of the final HTML UI—entirely to the AI.

**Data Insights from Me:**
I explicitly flagged to the AI that 4 of the 5 Pending offers had a `Decision On` date but remained in a `Pending` status, instructing it to treat this as a data ambiguity rather than an automatic decline. I also instructed the AI not to call duplicate applications "duplicate candidates," ensuring our definitions remained strictly precise.

## 3. Questions to Answer

* **What did I get wrong first, and what made me notice?**
I initially let the AI move too fast into formatting the final deliverables before fully scrutinizing the underlying data quality. I noticed this when the AI started generating polished recommendations that relied on unchecked assumptions—like treating pending offers as declined after 14 days. It made me realize I needed to immediately halt the formatting process and force a rigorous, manual cross-check of the underlying raw data first.

* **Which of my numbers would I least like to defend, and why?**
The 38.5% Referral attribution rate (10 hires). While it is mathematically supported by the `Referred By` column, relying entirely on one field to override the static `Candidate Source` is risky without knowing how that field is populated. If `Referred By` is manually typed by recruiters instead of system-generated, it is prone to inflation or attribution bias. I wouldn't want to stake a massive engineering investment on it without auditing the actual data entry process first.

* **What would I have asked the hiring manager if I could?**
I would have asked how the "Offer Pending" status is operationally managed by the team. Seeing offers stuck in "Pending" despite having a past `Decision On` date suggests a process failure, not just a software bug. I would want to know if recruiters are simply forgetting to close out offers, or if candidates are actually ghosting us, as this drastically changes whether we need an engineering fix (status automations) or an operational fix (recruiter training).
