---
name: nonprofit-faith-programs-social-services
description: "Designs and runs faith-based direct-service programs (food pantry, addiction recovery, refugee resettlement, shelter, prison and re-entry, immigration legal services, disaster response) that keep religious character while meeting voluntary/separate/not-a-condition rules for federal funds. Use when a faith-based ED, program director or clergyperson says 'start a food pantry', 'can our recovery program take SAMHSA money', 'must we offer a secular alternative' or 'FEMA activated our team'. Not for the statutory framework (use nonprofit-faith-religious-liberty-compliance), generic program design (use nonprofit-program-design) or lay-leader development (use nonprofit-faith-volunteer-lay-leadership)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Federal grant compliance and beneficiary-rights language have legal and funder consequences; discipleship-integrated program designs need to be tested against funding source before deployment."
  last_reviewed: "2026-09-10"
  date_added: "2026-09-12"
  date_added_source: "git:297d3ef69a314702df1ccc8174826716c88cff40"
---

# Faith-Based Programs and Social Services (Direct-Service Delivery)

## Boundaries

This skill is program design and operations under the rules; load the rule owner when the question
is about the rule itself.

- The statutory framework (RFRA, RLUIPA §3, Charitable Choice / Equal Treatment regulations at
  45 CFR Part 87 and parallel agency regs, beneficiary-notice requirements, religious hiring) →
  `nonprofit-faith-religious-liberty-compliance`.
- Generic logic models, outcomes measurement and needs assessment → `nonprofit-program-design`,
  `nonprofit-outcomes-measurement`, `nonprofit-needs-assessment` (this skill adds faith overlays).
- Lay leadership of the worship community → `nonprofit-faith-volunteer-lay-leadership` (this skill
  covers volunteers deployed into a service program).
- Worship-space shared-use agreements → `nonprofit-faith-facilities-sanctuary`.
- Pastoral messaging around a launch or beneficiary crisis → `nonprofit-faith-communications-pastoral`.
- Benevolence-fund cash grants (IRC §102 controls) → `nonprofit-faith-finance-clergy-comp`.
- A non-faith 501(c)(3) delivering the same service → the base program skills.

## Core Frameworks

Name the framework the program is operating inside before drafting artifacts — a food pantry
under USDA TEFAP reads a "come to our chapel" flyer as a grant-terminating violation, and a
church-basement pantry running only on private donations does not.

- **Charitable Choice / Equal Treatment Regulations** (HHS 45 CFR Part 87, HUD 24 CFR Part 5,
  DOL 29 CFR Part 2, USDA 7 CFR Part 16, DOJ 28 CFR Part 38). The rule itself is owned by
  `nonprofit-faith-religious-liberty-compliance`. Operationally, a direct-funded provider keeps its
  religious character but must keep inherently religious activities out of the funded service,
  offer them voluntary, separate and not a condition, give written notice with an
  alternative-provider referral, and not discriminate against beneficiaries on religion.
- **Indirect vs. direct federal aid**. Restrictions apply to **direct** funds (grant, contract,
  cooperative agreement). **Indirect** aid — a voucher the beneficiary chooses to redeem — carries
  far fewer content restrictions under *Zelman v. Simmons-Harris*, 536 U.S. 639 (2002). A
  recovery voucher redeemed at Teen Challenge is treated differently from a SAMHSA grant to Teen
  Challenge. Confirm which stream applies before designing the program.
- **The voluntary / separate / not-a-condition test**. Three-prong beneficiary-protection test
  every direct-federally-funded program-design decision gets checked against. Developed below.
- **Warner v. Orange County Dept. of Probation**, 115 F.3d 1068 (2d Cir. 1997), with Kerr v.
  Farrey and Inouye v. Kemna: coercing an offender into a religious-in-effect program without a
  genuine secular alternative violates the Establishment Clause. Applied under "Addiction recovery".
- **USDA TEFAP / Emergency Food Assistance Program** (7 U.S.C. §7501; USDA FNS regs). USDA
  commodities flow state → state agency → eligible recipient agency (often a Feeding America
  affiliate) → local pantry. Recipient agencies sign a 7 CFR Part 15 civil-rights assurance;
  pantries cannot condition distribution on religious activity and must post the USDA "And
  Justice for All" poster.
- **Feeding America network**. ~200 affiliate food banks (verify the current count at feedingamerica.org) (Second Harvest predecessor); most
  church-run pantries source through an affiliate and are governed by its partner-pantry
  agreement, which typically incorporates TEFAP civil-rights terms and adds non-proselytization
  language even for non-federal food.
- **HUD Continuum of Care (CoC) and Emergency Solutions Grant (ESG)**. 24 CFR Parts 578 and 576;
  local CoC governs coordinated entry; Housing First and low-barrier orthodoxy govern most
  CoC-funded projects. Faith-based shelter providers can participate, but funded beds must be
  low-barrier — no sobriety, treatment, or religious-participation preconditions.
- **Reception and Placement (R&P) program** under State Department PRM, delivered through national
  resettlement agencies and local affiliates, plus private sponsorship (Welcome Corps). Structure
  and roster under "Refugee resettlement".
- **SAMHSA grant conditions** for SUD programs (42 U.S.C. §300x-65; 42 CFR Part 54 SAMHSA
  Charitable Choice). A faith-based recovery program on SAMHSA funds must offer a secular
  alternative provider on request and cannot use SAMHSA funds for inherently religious content;
  overall religious character is preserved.
- **RLUIPA §3** (42 U.S.C. §2000cc-1) protects religious exercise of institutionalized persons;
  see `nonprofit-faith-religious-liberty-compliance`. Bureau of Prisons chaplaincy operates under
  Program Statement 5360.09.
- **DOJ Recognition and Accreditation** (8 CFR Part 1292). Non-lawyer immigration representatives
  can serve as "accredited representatives" of a "recognized organization" — the legal backbone
  for CLINIC affiliates, Global Refuge, World Relief, CWS, and diocesan legal-aid offices
  providing immigration services below private-counsel cost.
- **NVOAD (National Voluntary Organizations Active in Disaster)** and the FEMA Voluntary Agency
  Liaison (VAL) structure; faith-based agencies are the operational backbone of US domestic
  disaster response. Agencies by phase under "Disaster response".

## Standard Deliverables

Every request in scope resolves into one of these artifacts:

- **Program design memo** — the model choice (e.g., client-choice pantry vs. commodity box,
  low-barrier shelter vs. sober-living transitional), with the religious-content design decision
  and the motivation-vs-condition statement made explicit.
- **Beneficiary written notice** — the notice required for direct-federally-funded programs:
  right to receive the funded service without participating in any religious activity, right to
  request a referral to an alternative provider, and non-discrimination on religion. Agency-
  specific model language exists (HUD, HHS, USDA); use the funding agency's model.
- **Alternative-provider referral list and MOU** — the identified secular provider that a
  beneficiary who declines the religious component can be referred to, with a memorandum of
  understanding describing referral warm-handoff and reciprocity.
- **Volunteer / spiritual-companion role description** — separating funded case-management staff
  from volunteers or clergy offering optional spiritual support on request.
- **Partner-agreement package** for a worship community hosting a program (food-pantry lease-back
  or use agreement, AA/NA/Celebrate Recovery hosting agreement, sponsor-circle covenant, halfway-
  house lease). Cross-reference `nonprofit-faith-facilities-sanctuary` for the underlying facility
  agreement.
- **Outcomes framework** — the two-report structure (skeleton under "Outcomes and
  Mission-Fulfillment").
- **Cultural / religious accommodation plan** — dietary, gender-of-caseworker, prayer space,
  holiday scheduling and family-structure accommodations (see checklist step 10).

## Designing a Faith-Based Direct-Service Program — Numbered Checklist

Run this checklist for any new program, expansion, or grant application. The failure mode is
designing around the mission first and discovering funding-source incompatibility after launch.

1. **Name the beneficiary and the vulnerability**. The beneficiary's dignity and access to the
   service cannot depend on their response to a religious message from you — the ethical
   foundation, not a legal afterthought.
2. **Separate motivation from condition**. Distinguish "**our motivation** for doing this work is
   religious" (protected First Amendment activity, expected of a faith-based org) from "**we
   require the beneficiary** to receive religious content to get the service" (illegal in direct-
   federally-funded work, ethically fraught even with private funds when the beneficiary is
   vulnerable). Every program-design decision that follows turns on this line.
3. **Identify the funding stack, source by source**. For each revenue line, mark: direct federal
   grant, indirect federal aid (voucher/certificate), state grant with federal pass-through, state
   grant with state-only funds, county/city funds, private foundation, individual donor,
   congregational offering, in-kind. The **direct federal** lines and any **state pass-through of
   federal funds** trigger the voluntary/separate/not-a-condition regime; private-donor funds do
   not. A single program can have mixed funding, in which case the strictest rule governs the
   funded portion.
4. **Pick the program mode against the funding stack**. Three archetypes:
   (a) **Fully secular delivery, religious character preserved at the org level** — the funded
   service contains no religious content; religious character shows in name, art, mission, board,
   and staff hiring. Use for direct-federally-funded services.
   (b) **Optional / separate religious component** — the funded service is secular; a religious
   component (evening chapel, Bible study, prayer circle, community iftar) is offered alongside
   on a voluntary basis, separated in time or location, never a condition. Compatible with direct
   federal funding.
   (c) **Discipleship-integrated program** — the religious content is the treatment (Bible-based
   recovery curriculum, faith-based re-entry cohort, sponsor-circle relationship). Compatible
   only with private funds or with indirect-aid vouchers the beneficiary chose.
5. **Apply the voluntary / separate / not-a-condition test** to any religious content included in
   or adjacent to a direct-federally-funded service (walk-through under "The Voluntary / Separate /
   Not-a-Condition Test — Applied"). Not-a-condition is the prong most often failed by orgs that
   pass the first two.
6. **Draft the written beneficiary notice** using the funding agency's model language (HUD's
   model at 24 CFR 578.87 for CoC; HHS model at 45 CFR 87.3(c) for HHS grants; parallel language
   at other agencies). Post it at intake; give a copy; document the giving. The notice covers:
   the funded service will be provided regardless of the beneficiary's religion or willingness to
   participate in religious activity; the beneficiary has the right to a referral to an
   alternative provider; the beneficiary has the right to report a violation.
7. **Build the alternative-provider infrastructure before you need it** — a named secular
   provider, referral MOU and six-month verification (see "Alternative-Provider Infrastructure").
   Include the list in the beneficiary notice packet.
8. **Design the staffing model to keep the two lanes clean** (see "Staffing the Two Lanes"). A
   single person doing both the funded service and religious support, even sincerely, is the most
   common source of compliance findings and beneficiary complaints.
9. **Define outcomes in two reports** (see "Outcomes and Mission-Fulfillment"): funded-service
   outcomes to the grantor; mission-fulfillment metrics to board and donors only, never a
   service-access gate. Do not mix the two reports.
10. **Cultural and religious accommodation as a design input**. Assume the beneficiary population
    is more religiously diverse than the staff. Design for: dietary accommodation (halal, kosher,
    vegetarian, no-pork defaults where relevant), gender-of-caseworker preference, prayer space
    and time, holiday scheduling that does not force a beneficiary to choose between observance
    and service, family-structure sensitivity. A Muslim beneficiary receiving food at a Christian
    pantry, or a Christian beneficiary receiving resettlement services through HIAS, should
    experience the service with full dignity — the practical expression of the theology, not a
    compliance exercise.

## Program Family Playbooks

Seven operational contexts; load the relevant subsection. Partner and agency rosters change —
confirm current names, status and services before recommending.

### Food security / food pantry

Standard architecture: **congregational volunteers → local pantry → Feeding America affiliate
food bank → USDA / private donors** (TEFAP and partner-agreement terms under Core Frameworks).
Partner-agreement violations put the sourcing relationship at risk long before a federal grant.

- **Client-choice vs. pre-packed**: client-choice (beneficiaries select from shelves) is the
  current best practice — dignity, waste reduction, cultural fit.
- **Wraparound services** (benevolence cash, case management, coaching, ESL, immigration
  referrals): each needs its own funding-source analysis; benevolence controls live in
  `nonprofit-faith-finance-clergy-comp`.
- **Gleaning ministry**: private-funded farm-recovery partnerships (Society of St. Andrew model).
- **Religious content**: distribution is done without religious message at the point of service;
  a chaplain, prayer table, or invitation card is available on the side for beneficiaries who
  request it. Requiring a devotional before food violates the Feeding America partner agreement
  and, if TEFAP-sourced, the USDA civil-rights assurance.

### Addiction recovery

Faith-based recovery has a well-developed ecosystem of programs with different theological
depths and different compliance profiles:

- **AA and NA** — religious-in-effect but formally non-sectarian; courts have repeatedly held
  (Warner, Kerr, Inouye) that mandating AA/NA attendance without a genuine secular alternative
  violates the Establishment Clause. A congregation hosting an AA meeting is providing space, not
  running the program.
- **Celebrate Recovery** — Christ-centered 12-step curriculum originating at Saddleback;
  weekly church-basement small-group model, volunteer-led, private-funded.
- **Reformers Unanimous** and **Alcoholics for Christ** — similar church-based Christ-centered
  fellowship models.
- **Adult and Teen Challenge (Global Teen Challenge internationally)** — long-term (12–15 month)
  faith-based residential program with explicit Christian discipleship curriculum. Historically
  private-funded; where SAMHSA or state funds are accepted, the discipleship curriculum must be
  unbundled or funded from private sources.
- **Licensed clinical treatment** with chaplaincy — secular funded treatment (detox, MAT, IOP)
  plus on-request chaplain access.

Design considerations:
- **Court-ordered attendance**: document that a genuine secular alternative was offered (see
  Common Failure Modes).
- **SAMHSA / state-block-grant funding** triggers 42 CFR Part 54 (see Core Frameworks).
- **Vouchers** (indirect aid) can send a beneficiary to a discipleship-integrated program under
  *Zelman* logic; the compliance surface is different from a direct grant.

### Refugee resettlement

Standard architecture: **State Dept PRM cooperative agreement → national agency → local
affiliate**. Six of the nine nationals have been faith-based — USCCB, Church World Service, HIAS
(Jewish), Global Refuge (formerly LIRS), World Relief (evangelical), Episcopal Migration
Ministries — with three secular (IRC, USCRI, Ethiopian Community Development Council). Federal
admissions, funding and the agency roster have shifted sharply in recent years; verify the
current status of R&P, Matching Grant and Welcome Corps with PRM and ORR before planning. R&P per-capita covers ~90 days; the ORR **Matching Grant** program extends
employment services to 240 days for eligible clients.

- **Sponsor circle / Welcome Corps** (launched 2023): private groups of five or more sponsor a
  refugee household directly. Congregations are the natural sponsor unit. The Welcome Corps
  handbook governs the sponsor covenant, fundraising minimum, and case-plan handoff.
- **Faith character**: faith-based nationals serve refugees of every religion — HIAS's motto
  ("we used to welcome refugees because they were Jewish; today we welcome refugees because we
  are Jewish") is the cleanest articulation of the motivation-religious, service-universal
  posture.
- **Religious content**: not part of the funded service; a beneficiary wanting worship connection
  is helped to find their own tradition's community. A Christian sponsor circle resettling a
  Muslim family helps the family find a mosque.

### Homeless shelter and transitional housing

Standard architecture: **local Continuum of Care → HUD CoC / ESG funding → provider agencies**,
with a locally coordinated entry system. Housing First orthodoxy governs most HUD-funded projects:
low-barrier admission, no sobriety or treatment or religious-participation preconditions, rapid
move to permanent housing with wraparound support.

Design choices:
- **Low-barrier HUD-funded shelter**: the bed is the funded service; sobriety, treatment,
  employment, or religious participation cannot condition admission or continued stay. Evening
  chapel is voluntary/separate/not-a-condition with written notice.
- **Traditional / private-funded shelter**: Salvation Army corps community centers and the
  Rescue Mission network / Citygate (City Union of Rescue Missions) historically run private-
  funded programs that require sobriety and program participation. Compatible with private
  funding; not compatible with HUD CoC direct grant funds without redesign.
- **Transitional housing / halfway house** with required Bible study is discipleship-integrated:
  private funds or vouchers only. A common pattern is to fund the housing entirely with private
  donations and decline federal grant for the beds.
- **Coordinated entry**: some CoCs require even non-federally-funded providers to accept CE
  referrals as a condition of network participation — read the CoC charter first.

### Prison and re-entry ministry

Standard architecture: **BOP or state DOC chaplaincy office → contract or MOU with the outside
provider → in-facility programming**. RLUIPA §3 protects the incarcerated person's religious
exercise; the provider's job is to serve into that protected space, not to substitute for it.

- **Prison Fellowship**: in-prison discipleship classes, Angel Tree (Christmas gifts for children
  of incarcerated parents), re-entry mentoring. The InnerChange Iowa case (*Americans United v.
  Prison Fellowship Ministries*, 509 F.3d 406, 8th Cir. 2007) is the cautionary tale — state funds cannot pay for pervasively sectarian
  in-custody programming that confers tangible benefits.
- **Kairos Prison Ministry**: short-course weekend model, volunteer-led, private-funded.
- **BOP chaplaincy** under Program Statement 5360.09: volunteer religious service providers apply
  through the institution chaplain, visiting inmates of their tradition who request it.
- **Re-entry housing** (halfway houses, sober-living): private-funded houses with required
  devotional are common and lawful; a federally contracted Residential Reentry Center cannot
  condition RRC placement on religious participation.

### Immigration legal services

Standard architecture: **DOJ Recognized Organization → DOJ Accredited Representatives + staff
attorneys → beneficiaries paying nominal or no fees**. Recognition is granted under 8 CFR Part
1292 to nonprofits that meet the "nominal fees" test and demonstrate legal-services capacity;
accreditation qualifies specific staff (partial or full) to represent clients before DHS and
EOIR.

- **Catholic Legal Immigration Network (CLINIC)**: federation of ~400 affiliate legal-services
  offices, mostly diocesan (verify the current count at cliniclegal.org). Confirm any provider's
  current recognition on the EOIR roster of recognized organizations.
- **Global Refuge (formerly LIRS)**, **World Relief**, **Church World Service**, **Episcopal
  Migration Ministries**, **HIAS**: all operate DOJ-recognized legal-services networks.
- **Services**: affirmative and defensive asylum, DACA renewal, adjustment of status, family
  petitions, naturalization, U/T-visa, VAWA self-petition, TPS, humanitarian parole.
- **Sanctuary hosting** of immigrants facing removal is public witness, not legal-services
  strategy: harboring exposure (8 U.S.C. §1324) depends on charging theory and hosting confers no
  status. Undertake only with counsel and congregational discernment; operations →
  `nonprofit-faith-facilities-sanctuary`, statement → `nonprofit-faith-communications-pastoral`.

### Disaster response

Standard architecture: **NVOAD member agencies → local Voluntary Organizations Active in Disaster
(VOAD) chapter → coordinated response with FEMA Voluntary Agency Liaison → Long-Term Recovery
Group in the affected community**. FEMA does not usually fund the faith-based response directly;
the faith-based agencies are the response backbone, and FEMA public assistance and individual
assistance flow to affected jurisdictions and households separately.

- **Response phase** (first 30 days): Southern Baptist Disaster Relief (mass feeding, chainsaw and
  mud-out crews), Salvation Army (mobile
  canteens), Convoy of Hope (bulk supplies), Team Rubicon (veteran-led, ecumenical), Adventist
  Community Services (donations warehousing).
- **Case management / unmet needs** (30 days to 24 months): UMCOR, Catholic Charities USA,
  Lutheran Disaster Response, Presbyterian Disaster Assistance, Episcopal Relief and Development,
  Islamic Relief USA, LDS Charities.
- **Long-term rebuild** (6 months to 5 years): Mennonite Disaster Service (largest faith-based
  volunteer construction operation in North America), Samaritan's Purse, Fuller Center for
  Housing, Habitat for Humanity affiliates, denominational teams.
- **Long-Term Recovery Groups** coordinate case management, unmet needs and volunteer housing
  after federal responders leave.
- **Compliance surface**: activation-mode response is largely private-funded on jurisdictional
  invitation; voluntary/separate/not-a-condition rules attach if the org accepts a FEMA or state
  disaster grant. Non-proselytization at the point of aid delivery is universal NVOAD member
  practice regardless of funding source (per the NVOAD "points of consensus" on disaster
  spiritual and emotional care).

## The Voluntary / Separate / Not-a-Condition Test — Applied

When the user asks "can we include [religious activity] in this program," walk the prongs in
order:

1. **Is the program direct-federally-funded** (including state pass-through)? If not, the federal
   regime does not apply — but the ethical framing does, and partner agreements (food bank,
   judicatory, insurer, funder MOU) may restrict separately. Confirm against the chart of accounts.
2. **Is the activity "inherently religious"?** Worship, religious instruction, proselytization,
   religious counseling, sacramental practice, evangelistic invitation. A grace before a shared
   meal, art on the wall, a cross on the building, staff wearing religious dress, an optional
   chaplain prayer on request — these have been read consistently as protected religious
   character, not inherently religious activity requiring separation. The test is whether a
   reasonable beneficiary would experience the activity as religious formation of them.
3. **If direct-federally-funded and inherently religious**: apply all three prongs. **Voluntary**
   — no attendance-taking, no follow-up on absence, no adverse consequence. **Separate** —
   different time slot or room; beneficiary can be in the funded-service space without being in
   the religious space; federally-funded staff do not lead the religious activity on federal
   time. **Not a condition** — no benefit, preference, better bed, faster appointment, favorable
   case note, or informal favor available to attendees but not to non-attendees.
4. **Written beneficiary notice** and **alternative-provider referral** are required for
   direct-funded services whether or not a religious activity is offered.

Failing any prong is a compliance finding; the fix is either to unbundle and fund the religious
component privately, or to remove it from the program.

## Staffing the Two Lanes — Paid Staff vs. Spiritual Companions

The most common source of both compliance findings and beneficiary complaints is a sincere staff
member doing the funded service and the religious support simultaneously. Design around this from
the start.

- **Paid program staff on a direct federal grant** perform the funded service. During federally-
  funded work time, they do not initiate religious conversation, distribute religious literature,
  offer prayer over a beneficiary, or condition any service element on a religious response. They
  may answer a direct question factually and refer to a spiritual companion or chaplain.
- **Lay volunteers and clergy visitors** — separately deployed, distinct role, written role
  description, badge identifying them as clergy/volunteer, background check appropriate to the
  setting (children, incarcerated persons, medical beneficiaries), training on the beneficiary-
  notice regime. They offer prayer, spiritual counsel, worship invitation, and religious
  literature only on beneficiary request.
- **Chaplain / clergy visitation line**: a way for the beneficiary to request a chaplain of a
  specified tradition, or none. Legally required in most institutional settings
  (prison, hospital, shelter) under RLUIPA or state parallels; a design best practice in others.
- **Multi-faith staff competence**: hire, train and retain staff and volunteer networks whose
  lived religious competence covers the beneficiary population (see checklist step 10).

## Alternative-Provider Infrastructure

The alternative-provider requirement is real, and a paper answer fails it.

- **Identify a genuine secular provider** of the same service in the same catchment — a named
  organization, not "any other pantry" — and sign a referral MOU (who refers, consented
  information transfer, warm-handoff protocol, response time, reciprocity).
- **Verify availability every six months**; a provider that has closed, moved or hit capacity is
  not an alternative. Update the notice packet on verification.
- **Warm handoff**: staff call with the beneficiary present, confirm the intake appointment, help
  with transportation where feasible, follow up within one week. A brochure is not a referral.
- **Document referrals** and report the count to the grantor. Zero referrals over years signals
  the offer is not being made or is socially discouraged.

## Outcomes and Mission-Fulfillment — The Two Reports

Faith-based programs that fold "professions of faith" into the outcome report to the government
funder will lose the grant and deserve to. Faith-based programs that refuse to count faith-
formation activity at all lose the ability to steward the mission with board and donors. Keep
two reports.

- **Funded-service outcomes** go to the grantor, board program committee and auditor: outputs,
  short-term outcomes (housed at exit, employed at 240 days, abstinence at six months), long-term
  outcomes (housed at 12 months, recidivism at 36 months), disaggregated as required. No
  religious content.
- **Mission-fulfillment metrics** go to board, donors and judicatory: faith-formation
  opportunities **offered** (the design metric, not accepted), spiritual-support requests,
  referrals, volunteer hours, accommodations, and (where counted) professions of faith.
- **Two-report skeleton** (fill from the program's own data; never invent figures):

  ```
  REPORT A — FUNDED-SERVICE OUTCOMES (grantor, compliance auditor)
  Program / grant / period:
  Outputs: [meals | bed-nights | cases opened | hearings]
  Short-term outcomes: [measure, target, actual, data source]
  Long-term outcomes: [measure, target, actual, data source]
  Disaggregation required by grantor:
  Alternative-provider referrals made: [count]
  (No religious content in this report.)

  REPORT B — MISSION FULFILLMENT (board, donors, judicatory only)
  Faith-formation opportunities offered: [type, count]
  Spiritual-support requests received:
  Accommodations fulfilled: [dietary | prayer space | caseworker gender]
  Partner-congregation volunteer hours:
  Other mission measures the board has chosen:
  (Never a service gate; never sent to the government funder.)
  ```
- **Do not moralize the two reports at each other**. Strong outcomes with low mission engagement
  means the funded service is working and the religious component may not be reaching people;
  strong mission engagement with weak outcomes means service drift. Both are diagnostics; neither
  invalidates the other.

## Partnering with Worship Communities as a Volunteer Pipeline

Most faith-based service programs are volunteer-heavy, and the pipeline runs through worship
communities — the church hosts the food pantry, the synagogue hosts the sponsor circle, the
mosque hosts the community iftar and clothing distribution, congregations rotate overnight-
shelter beds.

Governance essentials for a congregation hosting a program:
- **Written hosting agreement**: spaces used, insurance coverage, liability for beneficiary and
  volunteer injury, protocol when the program's religious character diverges from the host's
  (mainline church hosting a conservative recovery program; interfaith coalition hosting a
  Christian pantry). See `nonprofit-faith-facilities-sanctuary` for the underlying facility deal.
- **Insurance rider**: host GL may not cover the hosted program; a rider or separate program
  policy is usually required.
- **Background-check standard**: unified at the higher of host and program standards; see
  safe-sanctuary standards in `nonprofit-faith-employment-ministerial-exception`.
- **Mission-alignment agreement**: shared understanding of how each party's religious character
  is honored in the shared space — not a doctrinal test on the beneficiary.
- **Termination protocol**: 90–180 days' notice so no beneficiary is stranded mid-service.

## Verify Before Acting

Before launch, a new funding stream, or a grant application:

- [ ] Every revenue line is marked direct federal, pass-through, indirect voucher or private, from
      the chart of accounts rather than memory.
- [ ] The program mode (secular, optional/separate, discipleship-integrated) matches the strictest
      funding source on the funded portion.
- [ ] Each religious element adjacent to a funded service passes voluntary, separate and
      not-a-condition, with no attendance-taking.
- [ ] The beneficiary notice uses the funding agency's current model language and is given at intake.
- [ ] A named secular alternative provider is under MOU and was verified in the last six months.
- [ ] Partner agreements (food bank, CoC charter, host congregation) were read for restrictions
      beyond federal rules.
- [ ] Rule questions went to `nonprofit-faith-religious-liberty-compliance` and counsel where the
      supervision note requires review.

## Common Failure Modes

- **Confusing "our motivation is religious" with "we condition service on religion"**. Fix by
  putting the motivation-vs-condition statement in the program design memo and referring back to
  it in every content review.
- **No genuine secular alternative provider identified**. "We'd refer them somewhere" is not
  identification. Fix by building a named, MOU'd alternative-provider list before the first
  federally funded beneficiary walks in, and verifying every six months.
- **Volunteer-staff role collapse**. A case manager prays with a beneficiary and offers a Bible
  during a funded intake; the beneficiary experiences that as a condition of service. Fix by
  keeping paid federally-funded staff and lay spiritual-companion volunteers in distinct roles,
  badges, role descriptions, and training.
- **Attendance-taking at the "voluntary" religious component**. Sign-ins at chapel or absence
  follow-up collapses "voluntary" into "monitored." Fix by removing attendance-taking from any
  religious component adjacent to a funded service.
- **Court-mandated participants without a documented secular alternative**. A probation officer
  routing offenders to Celebrate Recovery or Teen Challenge without offering a secular alternative
  creates Establishment Clause exposure. Fix by documenting on intake that the beneficiary was
  offered and declined a secular option, or by refusing court-mandated intake without it.
- **Reporting professions of faith to the government grantor as a program outcome**. Legal and
  evaluation-integrity error. Fix by isolating mission-fulfillment metrics in a board/donor
  report and stripping them from the grantor report.
- **Assuming beneficiary religious homogeneity with staff**. Dietary defaults, holiday
  scheduling, caseworker-gender assumptions, prayer-in-intake defaults — all feel wrong to
  differently-situated beneficiaries. Fix by designing accommodations from the start, hiring
  multi-tradition staff, and building clergy visitation covering the beneficiary population.
- **Compliance treated as "legal will handle it" not as a program-design input**. Drift found at
  year-end audit is far more expensive to fix than compliance built into intake, notice, and
  staffing from day one.

## For advisors

- Identify the funding stack, source by source, before critiquing religious-content design — a
  Christ-centered halfway house on private donations is doing nothing wrong, and the same house
  taking a BOP RRC contract next month is a redesign project.
- Push for the alternative-provider MOU and beneficiary notice as concrete artifacts, and audit
  staff-vs-volunteer role separation on the ground, not on the org chart.
- When the org resists ("our mission requires we tell them about Jesus"), name the
  motivation-vs-condition distinction and offer the choice between funding stream and program
  design; do not let it take federal money while running a program designed for private funding.
