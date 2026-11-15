---
name: nonprofit-housing-affordable-rental-operations
description: "Runs the operating side of nonprofit-owned affordable rental housing: tenant selection plans, income certification, rent setting across AMI bands, waitlists, asset management and reserves, property-manager selection, NSPIRE readiness, and board reporting. Use when a user says 'draft our tenant selection plan', 'how should we set rents across AMI bands', 'should we self-manage or hire a property manager', or 'build a portfolio dashboard for the board'. Not for Section 42/HUD file compliance (use nonprofit-housing-lihtc-hud-compliance), fair-housing legal review (use nonprofit-housing-fair-housing), or new development (use nonprofit-housing-development-finance)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Tenant selection plans are adopted, consequential policy documents that shape who gets housed."
  last_reviewed: "2026-09-12"
  date_added: "2026-09-12"
  date_added_source: "git:466adeb4b20092f7790a7d1d6b555af30dd69b99"
---

# Nonprofit Housing: Affordable Rental Operations

## Boundaries

This skill covers the operating layer: the recurring decisions and workflows that keep existing
units occupied, compliant, and financially sustainable.

- Section 42 file compliance, LIHTC certifications for tax-credit purposes, HUD/ESG/CoC/HOME
  monitoring → `nonprofit-housing-lihtc-hud-compliance` (this skill runs the income-calculation
  workflow; that skill covers what the file must contain to survive an audit).
- Fair-housing complaints, reasonable-accommodation law, legal review of screening criteria →
  `nonprofit-housing-fair-housing`.
- New projects, site control, capital stacks → `nonprofit-housing-development-finance`.
- PSH service design and Housing First fidelity → `nonprofit-housing-permanent-supportive-housing`.
- ReStore/thrift retail operations → `nonprofit-retail-store-operations`.

## Core Framework: Two Management Lenses, One Asset

Affordable rental operations fail most often when property management and asset management are
conflated. Keep them structurally distinct:

1. **Property management (the physical + tenant lens)** — leasing, tenant relations, rent
   collection, maintenance, unit turns, inspections, delinquency. Time horizon: this week to this
   year. Success metric: occupancy, tenant accounts current, units passing inspection.
2. **Asset management (the financial + regulatory lens)** — whether each property, as a bundle of
   restricted-use contracts, still produces enough cash to sustain itself for the length of its
   compliance period. Time horizon: 5–30 years. Success metric: DSCR and reserve adequacy at the
   property level, compliance in good standing, capital needs funded before they become
   emergencies.

A third-party property manager optimizes the first lens; only the owner's asset manager optimizes
the second, because no one else holds the restricted-use agreements, the note terms, and the
capital-needs picture together. Small nonprofits routinely skip the asset-management function and
discover it ten years later as deferred maintenance their reserves cannot cover.

## Terminology Traps

- **AMI at the applicant's household size**: every income restriction is a percentage of AMI at
  the actual household size (a 1-person household is typically ~70% of the 4-person AMI; an
  8-person household ~150+%). Never apply the 4-person figure to all households.
- **MAX rent vs 30% rent**: most restrictions (notably LIHTC's 60% AMI gross-rent cap including
  utility allowance) set a maximum *rent*, while HOME- and voucher-linked rules often set rent as
  a *percentage of tenant income*. A unit can be legally rented at both only if the limits
  reconcile. Deep-targeting funder rules may cap at 30% of the *actual* AMI level rather than
  tenant income.
- **Compliance period vs extended-use period**: e.g., a 15-year LIHTC compliance period inside a
  30+ year extended-use agreement; the operating budget must survive the *longer* period.
- **Funded reserves**: actually deposited per the loan/LIHTC agreement, not merely budgeted.
- **DSCR**: most deals covenant at 1.10–1.20; asset management watches the *trend*, not just the
  covenant.
- **Physical vs economic occupancy**: economic occupancy nets out vacancy, concessions, and
  collection loss. A building can be 98% physically occupied and 88% economically occupied.

## Deliverable 1: Tenant Selection Plan Draft

A TSP is an adopted policy document — draft it for board approval, then have counsel check it
against fair-housing law per `nonprofit-housing-fair-housing` before adoption. Required elements:

1. **Program description**: the property, funding sources, unit count and AMI-band mix, and which
   restrictions govern each unit type. State the controlling documents' hierarchy when rules
   conflict (typically: statute/regulation > regulatory agreement > note > TSP).
2. **Eligibility criteria**: income limits by AMI band and household size, occupancy standards
   (persons per bedroom, normally 1.5–2 per bedroom, stated neutrally), and any program
   requirements (e.g., minimum rent ability for non-subsidized units).
3. **Tenant selection preferences** (the highest-scrutiny section): any local preference (residency,
   homelessness, veterans, working families) with the *justification* tied to the funder's or
   community plan's goals. Order preferences cumulatively and state exactly how they rank
   applications within the waitlist. An unjustified or disparate-impact-producing preference is the
   most common fair-housing exposure in a TSP — flag every preference for review under
   `nonprofit-housing-fair-housing`.
4. **Application and waitlist procedures**: where and how to apply, what a complete application
   is, confirmation of receipt, waitlist opening/closing/purging rules, and how position is
   maintained or lost. State the purge protocol (notice + response window + documented removal)
   — undocumented purging is the most common waitlist finding.
5. **Screening criteria** (credit, rental history, criminal history): state each criterion, the
   evidence considered, the standard applied, and the individualized-review/appeal path. Keep
   criminal-history screens narrow and individualized (nature, severity, recency, evidence of
   rehabilitation) — blanket bans are both a fair-housing risk and a barrier to the population the
   org serves. Legal review belongs to `nonprofit-housing-fair-housing`.
6. **Income certification summary**: what income counts, third-party verification hierarchy, and
   the effective dates. Point to the workflow below; the *file* requirements are
   `nonprofit-housing-lihtc-hud-compliance`.
7. **Reasonable accommodation language**: a short section stating the right to request
   accommodations in application, screening, and tenancy, with a contact — even though the
   substantive law is `nonprofit-housing-fair-housing`.
8. **Grievance and appeal**: how an applicant contests a screening denial or waitlist decision,
   with timelines and a reviewer who did not make the original decision.
9. **Amendment and effective-date clause**: adopted-by, version, and how amendments are published
   and applied (existing applicants vs new ones).

Completion condition: a board-ready draft where every preference, screening criterion, and purge
rule has a stated justification and a documented appeal path, and every section cites the funding
source whose rule it implements.

## Deliverable 2: Income Certification and Recertification Workflow

The certification workflow below is the *operating procedure*; the resulting file's compliance
contents are `nonprofit-housing-lihtc-hud-compliance`. Initial certification (move-in):

1. **Take the application and issue a written eligibility determination within your stated TSP
   timeline.** Collect household composition, income sources, and asset statements.
2. **Verify in the required order**: third-party written verification first (employer, benefits
   award letters, bank statements), then documents supplied by the applicant, then — only if both
   fail — a notarized applicant affidavit. Most monitoring findings are verification-hierarchy
   failures.
3. **Annualize and anticipate income**: project income forward 12 months from effective date
   (for hourly workers: rate × hours × pay periods, adjusted for seasonal and variable work; use
   year-to-date figures to test plausibility). Count income of all adult household members;
   exclude the specific categories the program excludes (e.g., minors' earned income, certain
   benefits — check the program rule rather than assuming).
4. **Count assets**: impute income on net assets above the program's threshold, verify household
   assets even when income-tested programs exclude the asset itself.
5. **Set rent per the unit's rules**: max-rent units rent at the published cap (plus or including
   utility allowance); percentage-of-income units compute the tenant rent contribution. Where both
   apply, take the binding one and document the calculation.
6. **Effective-date discipline**: certifications are effective the first day of occupancy; missed
   effective dates are unfixable errors.
7. **Obtain tenant signatures before move-in**, and give the household a copy.

Annual recertification: begin 120 days before the anniversary date, complete with new
verifications before the effective date, apply rent changes with proper notice (check lease/state
notice periods, commonly 30 days), and process interim recertifications when household income or
composition changes beyond the program's reporting threshold. Completion condition: every unit has
a current certification, verifications inside their validity window, and effective dates unbroken
since move-in.

## Deliverable 3: Rent Setting and AMI-Band Targeting

1. **Build the unit-restriction matrix**: for every unit, list each funding source's income band,
   max rent, and utility allowance treatment. One unit with three sources has three tests; the
   rent must pass all of them.
2. **Set rents at the binding constraint**: usually the LIHTC 60% AMI gross rent (including
   utility allowance) for tax-credit units, but check whether the deepest source (HOME, NHTF,
   state programs) imposes a lower band on a share of units.
3. **Apply the correct utility allowance**: the source-mandated method (e.g., PHA schedule, local
   utility company schedule, or engineering model for LIHTC buildings) and re-check annually —
   using a stale allowance is a rent overage that must be refunded.
4. **Target bands deliberately**: deeper bands (30% AMI) need rental subsidy or operating support
   because max rent at 30% AMI rarely covers operating costs; pairing a 30%-band unit with a
   voucher or project-based subsidy is the standard structure. Balance the band mix so blended
   rental income supports the budget — this is an asset-management decision, not a leasing one.

   Unit-restriction matrix skeleton (one row per unit per source; fill from the regulatory
   agreements and the current published limits):

   | Unit | Source | Income band | Max gross rent | Utility allowance (method, date) | Rent passes? |
   |---|---|---|---|---|---|
   | [unit #, BR] | LIHTC | [__% AMI] | [$ from HFA table] | [method, effective date] | [Y/N] |
   | [unit #, BR] | HOME | [__% AMI] | [$ from HUD HOME rents] | [method, effective date] | [Y/N] |
   | [unit #, BR] | [state/local source] | [__% AMI] | [$ per agreement] | [method, effective date] | [Y/N] |
   | **Binding rent** | | | [lowest passing rent] | | |
5. **Publish a rent schedule by unit type and band** effective each new income-limit release
   (HUD limits publish each spring; apply per each program's effective-date rule, which differ —
   Section 42 uses the earlier of the release or 45-day deadline while other programs differ;
   verify current release dates and effective-date rules with HUD's income-limits page and the
   state HFA each year).
   Completion condition: a rent-addenda-ready schedule where every unit's rent passes every
   source's test and the utility allowance is current.

## Deliverable 4: Waitlist Management

1. **Keep the waitlist in the TSP's exact order** (preferences applied at offer time or at ranking
   — state which, and do it the same way every time).
2. **Confirm currency annually**: purge protocol with a mailed notice, stated response window
   (commonly 14–30 days), returned-mail handling, and documented removals. Never purge by
   assumption.
3. **Offer units per TSP rule** (top-of-list, with stated number of refusals before passing over,
   with the refusal documented) and log every offer, refusal, and removal with dates.
4. **Track meaningful metrics**: length, average days from application to offer, offer refusal
   rate, ineligibility rate at certification (a high rate means screening questions at application
   are weak), and demographic composition reviewed against the service area for fair-housing
   purposes per `nonprofit-housing-fair-housing`.
5. **Close and reopen cleanly**: closing requires public notice per the TSP; reopening requires a
   stated order for merging old and new lists. Completion condition: any auditor can reconstruct
   why applicant #1 was housed before applicant #2 from the log alone.

## Deliverable 5: Annual Asset-Management Plan

One document per property (or one plan with a section per property), reviewed by the board or
asset-management committee annually:

1. **Property snapshot**: units by AMI band, compliance period remaining, key covenant dates
   (extended-use end, note maturity, any covenant flexibility date).
2. **Financial performance**: actual vs budget NOI, DSCR, economic occupancy, collection loss,
   expense trends against inflation (insurance and taxes are the usual 2020s offenders — model
   them explicitly).
3. **Reserve adequacy**: current replacement-reserve balance vs the reserve study's projected
   needs over the next 5 and 15 years; flag any component whose projected replacement year arrives
   before the reserve can fund it.
4. **Physical condition**: last inspection scores (HQS/NSPIRE or CRIA/state), open work orders
   aging, deferred-maintenance list with costs.
5. **Regulatory standing**: filings current, monitoring findings open/closed, certifications
   current (detail per `nonprofit-housing-lihtc-hud-compliance`).
6. **Risk register and decisions**: the 3–5 things most likely to impair the asset (expiring
   subsidy, a manager relationship failing, a capital system) with the decision each requires this
   year. Completion condition: a board member can read it in 20 minutes and know what decision is
   being asked of them.

## Capital-Needs Planning and Reserve Studies

1. **Commission a reserve study** (or an updated one) every 3–5 years per property, from a firm
   with multifamily affordable experience; ask whether the engineer inspected a sample of units
   and the major systems, and get component-level data you can maintain in-house.
2. **Reconcile the reserve study to the regulatory deposit**: many loan/LIHTC agreements require a
   fixed annual deposit that is *lower* than the study says is needed — the gap is the owner's
   problem and belongs in the asset-management plan's risk register.
3. **Maintain a rolling 20-year capital schedule**: component, install year, useful life,
   replacement year, current cost estimate, escalation assumption. Update annually with actual
   work performed.
4. **Never let the replacement reserve fund operations**: it is the most common slow-motion
   failure in nonprofit portfolios — legal only where the agreement permits, and even then it
   converts a 15-year-away roof problem into a current covenant violation.
5. **Plan recapitalization early**: if the reserve math does not close, the answer is a
   refinancing/rehab (per `nonprofit-housing-development-finance`), decided ~3–5 years out, not
   at year 14. Completion condition: every major component has a funded replacement year on a
   schedule the board has seen.

## Property-Management Vendor Selection and Oversight

### In-house vs third-party decision

Choose third-party when: portfolio is small or scattered, the org lacks maintenance and
collections capacity, or scale (rule of thumb: several hundred units) hasn't been reached. Choose
in-house when: portfolio is large and geographically concentrated, tenant-services integration
(PSH, services-rich buildings) is central, or third-party fees exceed the cost of a qualified
staffing plan. Test the decision annually with a full-cost comparison including supervision
overhead on both sides — in-house is usually cheaper only above scale, and usually better at
mission alignment at any size.

### PM vendor RFP and scorecard

1. **Scope the RFP** to the property types (conventional affordable vs PSH requires different
   competencies; for PSH coordinate with `nonprofit-housing-permanent-supportive-housing`).
2. **Score proposals on a weighted scorecard**, e.g.: affordable compliance track record (20%),
   financial reporting capability and software (15%), maintenance operations and turn speed (15%),
   staffing plan and PM credentials (10%), fee schedule (15%), references from comparable
   nonprofits (15%), tenant-communication approach and language access (10%). Weight *before*
   opening proposals.
3. **Read the management agreement** for: term and termination-for-cause and
   termination-for-convenience (get 60–90 days convenience), fee structure (base % of collections
   typically ~3–6% plus leasing, setup, and construction-management fees — cap the extras), the
   reporting package and deadlines, budget approval rights, audit/access rights, and a cap on
   aggregate expenses approvable without owner sign-off.
4. **Oversight rhythm**: monthly — review the financial package (budget variance, delinquency
   aging, work-order aging, occupancy) before accepting it; quarterly — site visit, unit
   file sampling, inspection-spotlight walk; annually — full performance review against the
   scorecard criteria, insurance and license verification, and a re-bid trigger if two consecutive
   annual reviews miss targets. Failure mode: owners who only see the manager's own reports —
   verify occupancy and delinquency against the general ledger at least quarterly.

## HQS/NSPIRE Inspection Readiness

1. **Know which regime applies to each funding source** — NSPIRE replaced HQS for most HUD
   programs (verify the current implementation date for each program, including vouchers, on
   HUD's NSPIRE page); state CRIA and LIHTC physical inspections are separate regimes with their own
   standards. A building can face more than one.
2. **Run the NSPIRE inspection areas proactively**: unit, inside, outside, and systems —
   prioritize the health-and-safety (H&S) defects that fail or abate scoring: smoke/CO alarms,
   GFCI near water, egress blockage, infestation, mold/moisture, electrical hazards, secure
   entry.
3. **Build a 90-day pre-inspection cycle**: full self-inspection of a unit sample plus 100% of
   common areas and systems, work-order blitz on H&S items, resident notice and education
   (resident-caused defects still fail the unit — schedule a pre-inspection entry with notice).
4. **Track defects to closure with dates** so the pattern (which building, which system) informs
   the capital plan. Completion condition: a self-inspection log with zero open H&S items at
   inspection date and a closed-loop work-order trail.

## Occupancy and Financial Reporting to Owners/Boards

The board-level portfolio dashboard is one page per portfolio (one section per property):

- **Occupancy**: physical and economic occupancy by property, units vacant >30 days, lease-up
  progress on any new building.
- **Collections**: delinquency aging (30/60/90+), eviction filings by reason (nonpayment vs
  lease violation — a spike in nonpayment filings is an affordability or screening signal).
- **Financials**: NOI vs budget, DSCR vs covenant, replacement-reserve balance vs deposit
  schedule, and the largest budget-variance drivers in plain language.
- **Physical**: last inspection score and open findings, work orders open >30 days, top three
  upcoming capital items from the rolling schedule.
- **Compliance/mission**: certifications current, monitoring findings open, waitlist depth, and
   households served by AMI band (the mission metric most affordable boards actually want).
- **Decisions requested**: never report without them — the dashboard ends with what the board is
   being asked to approve or note.

Report monthly to staff/committee, quarterly to the board, with the annual asset-management plan
as the yearly deep-dive. Consultants: build the dashboard *with* staff so it survives your
departure; every metric should name its source system.

## Verify Before Acting

- [ ] Every income limit and rent is pulled from the current HUD/HFA table at the household's
      actual size, and its effective date matches the program's rule.
- [ ] Each unit's rent passes every funding source's test in the unit-restriction matrix, with a
      current utility allowance.
- [ ] Every TSP preference, screening criterion, and purge rule has a justification and an appeal
      path, and the draft is flagged for fair-housing review before board adoption.
- [ ] Manager-reported occupancy and delinquency tie to the general ledger for the period.
- [ ] Reserve balances and deposits in the asset-management plan reconcile to the regulatory
      agreement and the latest reserve study.

## Common Failure Modes

- **Asset management skipped**: property-level reports flow to the board but no one asks whether
  the property survives to the end of its extended-use period. Remedy: the annual asset-management
  plan with reserve adequacy is non-optional, even at 40 units.
- **AMI applied at the wrong household size**: rejecting an eligible 2-person household against
  the 4-person limit, or vice versa. Remedy: income-limit tables pulled by household size, every
  time.
- **Utility allowance drift**: rents set with a two-year-old allowance create silent overages.
  Remedy: calendar the annual allowance update with the income-limit release.
- **Waitlist purged without documentation**: legal exposure and lost applicants. Remedy: notice,
  response window, and a removal log — per the TSP, every time.
- **Manager reports accepted unaudited**: occupancy and delinquency restated later. Remedy:
  quarterly tie-out of manager reports to the general ledger.
- **Reserve raided for operations** "just this year." Remedy: treat as a board-level decision
  with a written replenishment plan; check the regulatory agreement first.
- **Certification verifications out of hierarchy or expired** at monitoring. Remedy: audit a
  sample of files quarterly using `nonprofit-housing-lihtc-hud-compliance`'s file standards.
- **Deferred maintenance invisible to the board** because work-order aging never appears in the
  dashboard. Remedy: open >30 days is a standing dashboard line.
- **In-house management adopted for mission reasons without the compliance capacity** to run
  certifications. Remedy: decide the management model on a full-cost, full-capability comparison,
  and re-test annually.
