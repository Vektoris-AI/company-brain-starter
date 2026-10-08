---
title: "Ingest log"
type: log
status: active
created: 2026-01-07
updated: 2026-10-07
tags: [meta, example]
sources: []
confidence: medium
---

# Ingest log

One line per ingest: date · source · pages created (+) or updated (~). Newest at the bottom.
Written by the `/ingest` skill; agent reports in `00_inbox/` are not logged here until a human
merges them. Fictional example data ([[about-this-example]]).

| Date | Source | Pages |
|---|---|---|
| 2026-01-08 | [[2026-01-07-founders-offsite-notes]] | + [[ADR-001-company-brain-single-source-of-truth]], + [[Dana-Kettlewell]], + [[one-owner-per-client-relationship]], + [[single-source-of-truth-before-ai]], ~ [[ADR-002-niche-b2b-services-and-saas]], ~ [[icp-b2b-services-20-to-200-employees]], ~ [[positioning]] |
| 2026-01-15 | [[2026-01-14-cobaltline-discovery-call]] | + [[Cobaltline-Software]], + [[Rachel-Nguyen]], ~ [[cobaltline-ops-retainer]], ~ [[crm-hygiene-before-automation]], ~ [[discovery-calls-reveal-crm-debt]], ~ [[qualified-opportunity-definition]], ~ [[single-source-of-truth-before-ai]] |
| 2026-01-29 | [[2026-01-28-alderbrook-discovery-call]] | + [[Alderbrook-Freightworks]], ~ [[alderbrook-pipeline-sprint]], ~ [[follow-up-within-48-hours]] |
| 2026-02-06 | [[2026-02-06-pipeline-sprint-pilot-retro]] | + [[Isabel-Cruz]], + [[retros-feed-the-brain]], + [[sales-to-delivery-handoff]], + [[scope-creep-arrives-as-small-asks]], ~ [[ADR-003-productize-the-pipeline-sprint]], ~ [[Kestrelmoor-Cleaning-Co]], ~ [[contract-playbook]], ~ [[kestrelmoor-website-leads-2025]], ~ [[pipeline-sprint-six-week-scope]], ~ [[pipeline-sprints-run-eight-weeks-in-practice]], ~ [[proposals-lead-with-the-problem]] |
| 2026-02-20 | [[2026-02-19-pricing-workshop-notes]] | + [[ADR-003-productize-the-pipeline-sprint]], ~ [[pipeline-sprint-six-week-scope]], ~ [[pricing-model-2025]], ~ [[service-catalog]] |
| 2026-03-04 | [[2026-03-03-retainer-churn-analysis-export]] | + [[ADR-004-six-month-minimum-for-retainers]], + [[Nina-Kowalski]], + [[onboarding-sets-retainer-lifetime]], + [[retainers-churn-in-month-four]], ~ [[weekly-status-beats-monthly-reports]] |
| 2026-03-13 | [[2026-03-12-wrenfield-kickoff-call]] | + [[Chris-Delgado]], + [[Owen-Fletcher]], + [[Wrenfield-Dental-Partners]], + [[wrenfield-content-engine]], ~ [[Aisha-Morgan]], ~ [[regulated-clients-need-review-buffers]] |
| 2026-03-27 | [[2026-03-26-all-hands-notes-q1]] | ~ [[Clara-Benson]] |
| 2026-04-02 | [[2026-04-01-ar-aging-export]] | + [[ADR-006-fifty-percent-upfront-for-sprints]], + [[receivables]], + [[upfront-payment-reduces-receivable-days]], ~ [[Granitefold-Insurance-Brokers]], ~ [[Ironfern-Payroll-Services]], ~ [[Meadowquill-Senior-Living]], ~ [[Priya-Raman]], ~ [[meadowquill-content-program]], ~ [[scope-creep-arrives-as-small-asks]] |
| 2026-04-10 | [[2026-04-09-granitefold-crm-audit-export]] | + [[Andre-Wallace]], + [[Granitefold-Insurance-Brokers]], + [[discovery-calls-reveal-crm-debt]], + [[granitefold-crm-cleanup]], ~ [[ADR-007-client-data-stays-in-client-crm]], ~ [[crm-hygiene-before-automation]] |
| 2026-04-23 | [[2026-04-22-oakvane-compliance-email]] | + [[regulated-clients-need-review-buffers]], ~ [[ADR-009-legal-review-for-regulated-content]], ~ [[Aisha-Morgan]], ~ [[Oakvane-Wealth-Advisors]], ~ [[case-studies-need-written-approval]], ~ [[oakvane-compliant-content]] |
| 2026-05-06 | [[2026-05-05-capacity-planning-meeting]] | + [[ADR-008-cap-concurrent-sprints-at-three]], + [[capacity-board]], + [[capacity-is-planned-in-sprint-slots]], + [[utilization-above-80-percent-burns-out-teams]], ~ [[Eli-Brandt]], ~ [[Marcus-Finch]] |
| 2026-05-15 | [[2026-05-14-copperwick-discovery-call]] | + [[Copperwick-Labs]], + [[buying-committees-have-three-roles]], ~ [[Lena-Vasquez]], ~ [[copperwick-abm-campaign]] |
| 2026-05-29 | [[2026-05-28-employee-survey-summary]] | + [[new-hires-need-a-30-60-90-plan]], + [[people-kpis]], ~ [[Hannah-Brooks]], ~ [[utilization-above-80-percent-burns-out-teams]] |
| 2026-06-11 | [[2026-06-10-brackwater-discovery-call]] | + [[Brackwater-Machine-Works]], ~ [[brackwater-pipeline-sprint]], ~ [[follow-up-within-48-hours]] |
| 2026-06-19 | [[2026-06-18-hiring-plan-meeting]] | + [[Northpine-Talent-Partners]], + [[hiring-plan-q4]], + [[q4-hiring]], + [[role-scorecards-before-job-posts]], ~ [[ADR-011-hire-marketing-ops-before-sales]] |
| 2026-07-03 | [[2026-07-02-tool-audit-export]] | + [[tool-stack]], ~ [[ADR-012-one-project-tool]], ~ [[ADR-013-vendor-dpa-before-any-ai-tool]], ~ [[Sam-Whitaker]] |
| 2026-07-16 | [[2026-07-15-pembury-legal-memo-ai-vendors]] | + [[vendor-dpa-checklist]], ~ [[ADR-013-vendor-dpa-before-any-ai-tool]], ~ [[Pembury-Lane-Legal]], ~ [[ai-use-policy]] |
| 2026-07-30 | [[2026-07-29-quillfield-kickoff-call]] | + [[Quillfield-Health-Analytics]], + [[quillfield-abm-pilot]], ~ [[Kevin-Ashford]], ~ [[buying-committees-have-three-roles]] |
| 2026-08-06 | [[2026-08-05-ai-leadership-pilot-notes]] | ~ [[ADR-010-cfo-agent-reads-bank-only]], ~ [[ADR-014-ai-leadership-team-at-autonomy-level-1]], ~ [[ADR-016-daily-brief-before-standup]], ~ [[Sam-Whitaker]], ~ [[agents-draft-humans-decide]], ~ [[ai-leadership-team]], ~ [[ai-leadership-team-rollout]], ~ [[automate-only-stable-processes]], ~ [[follow-up-rules]], ~ [[single-source-of-truth-before-ai]] |
| 2026-08-20 | [[2026-08-19-northmere-weekly-report-export]] | ~ [[Grace-Holloway]], ~ [[Northmere-Solar]], ~ [[cost-per-lead-is-not-pipeline]], ~ [[northmere-paid-media-pilot]], ~ [[paid-media-needs-tracking-first]] |
| 2026-08-28 | [[2026-08-27-pipeline-sprint-retro-alderbrook]] | + [[pipeline-sprints-run-eight-weeks-in-practice]], ~ [[Alderbrook-Freightworks]], ~ [[Ben-Castillo]], ~ [[Isabel-Cruz]], ~ [[alderbrook-pipeline-sprint]], ~ [[retros-feed-the-brain]] |
| 2026-09-04 | [[2026-09-03-ironfern-qbr-notes]] | + [[qbrs-start-with-client-goals]], ~ [[Ironfern-Payroll-Services]], ~ [[Rachel-Nguyen]], ~ [[client-reporting-dashboard]], ~ [[dashboards-answer-one-question]], ~ [[ironfern-ops-retainer]] |
| 2026-09-11 | [[2026-09-10-cobaltline-renewal-call]] | + [[cobaltline-crm-migration]], ~ [[Cobaltline-Software]], ~ [[Jordan-Pike]], ~ [[cobaltline-ops-retainer]], ~ [[service-catalog]] |
| 2026-09-18 | [[2026-09-17-cash-review-meeting]] | + [[ADR-017-net-15-payment-terms]], + [[cash-runway-in-weeks]], ~ [[Ashgrove-CPA-Group]], ~ [[Priya-Raman]], ~ [[receivables]] |
| 2026-09-23 | [[2026-09-22-pinemarrow-discovery-call]] | + [[Pinemarrow-Staffing-Group]], + [[pinemarrow-pipeline-sprint]] |
| 2026-09-29 | [[2026-09-28-onboarding-feedback-zoe]] | + [[shadowing-shortens-ramp-up]], ~ [[Eli-Brandt]], ~ [[Hannah-Brooks]], ~ [[Zoe-Harper]], ~ [[new-hires-need-a-30-60-90-plan]], ~ [[people-onboarding-routine]], ~ [[service-catalog]] |
| 2026-10-01 | [[2026-09-30-northmere-escalation-call]] | + [[ADR-018-pause-paid-media-as-standalone-service]], + [[paid-media-needs-tracking-first]], ~ [[Grace-Holloway]], ~ [[Marcus-Finch]], ~ [[Northmere-Solar]], ~ [[northmere-paid-media-pilot]] |
| 2026-10-02 | [[2026-10-01-q3-all-hands-notes]] | ~ [[Clara-Benson]], ~ [[Dana-Kettlewell]], ~ [[Lena-Vasquez]], ~ [[ai-leadership-team-rollout]], ~ [[case-studies-need-written-approval]], ~ [[q4-hiring]], ~ [[upfront-payment-reduces-receivable-days]], ~ [[website-relaunch-2026]] |
| 2026-10-07 | [[2026-10-06-stonemeade-rfp-email]] | + [[Stonemeade-Facilities-Group]], ~ [[security-questionnaire-library]] |
| 2026-10-07 | [[2026-10-07-tidelock-intro-email]] | + [[2026-10-07-tidelock-first-impressions]], + [[Tidelock-Freight-Audit]], ~ [[Jordan-Pike]] |
