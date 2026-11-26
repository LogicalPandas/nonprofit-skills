---
name: nonprofit-faith-employment-ministerial-exception
description: "Handles US employment and safeguarding questions with a religious dimension: ministerial-exception scope, Title VII §702 religious hiring, Groff accommodation, Bostock, clergy misconduct and safe-sanctuary policies, background checks, allegation response, and pastor leave or termination. Use when a church, synagogue, mosque or ministry asks 'we need to let our pastor go', 'can we require staff to share our faith', 'someone made an allegation against a staff member' or 'write our child-protection policy'. Not for clergy pay (use nonprofit-faith-finance-clergy-comp), lay-staff HR (use nonprofit-hr), congregational votes (use nonprofit-faith-church-governance) or RFRA and federal funds (use nonprofit-faith-religious-liberty-compliance)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Ministerial-exception scope calls, misconduct responses, and termination workflows require counsel review and appropriate insurer coordination. Emergency protection and legally required reporting must not wait for counsel, insurer, board, or internal approval; retain professional review for subsequent employment decisions and discretionary disclosures."
  last_reviewed: "2026-09-10"
  date_added: "2026-09-12"
  date_added_source: "git:297d3ef69a314702df1ccc8174826716c88cff40"
---

# Faith-Based Nonprofit Employment & Ministerial Exception (US)

## Boundaries

This skill is the employment-law and safeguarding layer, and the owner of the safe-sanctuary /
child-protection policy for the faith-based family. Route the rest:

- Clergy pay design, §107 housing allowance, SECA, W-2 vs. 1099 clergy classification, love
  offerings, benevolence funds → `nonprofit-faith-finance-clergy-comp` (use it; do not restate it).
- Lay-staff handbook, PTO, benefits, general HR → `nonprofit-hr` and `nonprofit-staff-retention`.
- The congregational or elder-board side of removing a pastor (special meeting, quorum, thresholds,
  denominational concurrence) and denomination-vs-local property disputes →
  `nonprofit-faith-church-governance` (property mechanics: `nonprofit-faith-facilities-sanctuary`).
- Generic D&O / EPLI / general-liability selection → `nonprofit-risk-management`; this skill covers
  the sexual-misconduct rider and the policy content the insurer will require.
- RFRA, RLUIPA, Charitable Choice, ACA contraceptive accommodation → `nonprofit-faith-religious-liberty-compliance`.
- Lay-leader recruitment and terms → `nonprofit-faith-volunteer-lay-leadership`.

## Core Frameworks

Name the framework before drafting. Ministerial exception, Title VII §702, and Bostock look
similar from a distance and produce opposite answers up close.

- **First Amendment ministerial exception (Religion Clauses)**: a constitutional immunity that
  bars most employment-discrimination suits brought by a "minister" against a religious
  employer. Anchored by two unanimous Supreme Court cases:
  - **Hosanna-Tabor Evangelical Lutheran Church & School v. EEOC (2012)**: first recognition;
    barred an ADA retaliation claim by a commissioned, "called" Lutheran teacher.
  - **Our Lady of Guadalupe School v. Morrissey-Berru (2020)**: the inquiry is **functional** —
    what the employee actually did for the religious mission. Title, ordination, commissioning
    and "held out as a minister" are evidence but none is required; lay religion teachers who
    prayed with students and prepared them for Mass qualified.
- **Title VII §702 religious-organization exemption (42 U.S.C. §2000e-1(a))**: permits a
  religious corporation, association, educational institution, or society to prefer members of
  its own religion **for any position, not just clergy**. Upheld unanimously in **Corporation of
  the Presiding Bishop v. Amos (1987)** for a building-engineer job at an LDS gym. Does **not**
  permit discrimination on the other Title VII bases (race, color, sex, national origin). State
  analogs vary; some state fair-employment acts have narrower religious-employer carve-outs than
  federal law.
- **Groff v. DeJoy (2023)**: raised the Title VII "undue hardship" bar for accommodating an
  employee's religious practice from the old **de minimis** reading of *TWA v. Hardison* to a
  **substantial-cost-in-context** standard. Applies to religious employers too — it matters most
  when staff of other faiths request sabbath, prayer-time or dress accommodations.
- **Bostock v. Clayton County (2020)**: Title VII "because of sex" now includes sexual
  orientation and gender identity. For religious employers this interacts with §702 and the
  ministerial exception in unsettled ways: the ministerial exception still bars any Title VII
  claim by a minister; §702 still permits co-religionist preference; a same-sex-marriage or
  gender-transition decision framed and documented as a **religious** decision under the org's
  doctrinal standards is different from a decision framed as a sex/orientation decision.
  Litigation (Bear Creek Bible Church v. EEOC, Braidwood Management v. EEOC) was producing a
  circuit split as of this skill's last review; verify the current status of these cases and any
  later appellate or Supreme Court ruling, and do not promise the user a settled answer.
- **Denominational polity and church-court process**: clergy discipline is defined by the
  denomination's own governing document (see "Denominational Discipline and Its Employment
  Consequences"); civil courts generally will not review those determinations (church-autonomy
  doctrine, **Serbian Orthodox Diocese v. Milivojevich, 1976**).
- **Safe-sanctuary / safe-church programs**: named systems the org will be measured against by
  insurers, denominations, and state licensors: **USCCB Charter for the Protection of Children
  and Young People** (Catholic "Dallas Charter," 2002: safe-environment offices, review boards,
  checks, training, zero tolerance for substantiated abuse of a minor) and **VIRTUS** training;
  **MinistrySafe** (evangelical and nondenominational churches, camps); **GRACE** (independent
  investigation, culture assessment); **Reducing the Risk**, **Praesidium**, and denominational
  curricula (Episcopal Safeguarding God's Children/People, UMC Safe Sanctuaries, PCUSA/ELCA,
  Jewish federation and USCJ, ISNA/MCC). Confirm which program the insurer and denomination
  currently require.
- **Mandatory-reporter statutes**: every US state has a child-abuse reporting law. Clergy are
  named mandatory reporters in most states; a minority still exempt "penitential communications"
  but that carve-out has been narrowed or abolished for child-abuse reports in several states.
  Always confirm the specific state before advising a "you don't have to report" conclusion.
- **Fair Credit Reporting Act (FCRA) and EEOC criminal-history guidance**: background-check
  vendors are consumer-reporting agencies, so the FCRA disclosure, authorization and
  adverse-action sequence applies (see "Background-Check Program"); EEOC guidance disfavors
  blanket exclusions and expects individualized assessment (offense, time elapsed, role).

## Standard Deliverables

- **Ministerial-exception scope memo** — functional test applied to real duties (skeleton below).
- **Religious-hiring policy language** — religious qualification, statement-of-faith subscription,
  conduct expectations, and the documentation trail that keeps a §702 decision defensible.
- **Safe-sanctuary / child-protection policy** and **clergy misconduct policy and response plan**.
- **Allegation-response runbook** — the first-72-hours workflow.
- **Administrative-leave / termination letter for clergy** — drafted with counsel.
- **Background-check program design** — screening matrix, vendor, FCRA workflow, renewal cadence,
  disqualifying-offense schedule.
- **Coordination memo with the judicatory** — who acts, in what sequence, under concurrent jurisdiction.

Ministerial-exception scope memo skeleton (write it before any personnel action):

```
Privileged & confidential [if prepared at counsel's request] — Role: ___  Entity: ___  Date: ___
1. Employer: religious institution? basis (governing documents, mission, operations)
2. Sources reviewed: job description, posting, offer letter, actual-duties account
   (who provided it, date), training/commissioning records
3. Religious-mission functions (checklist step 3): (a)-(e), each with evidence
4. Corroborating factors (step 4): title, ordination/commissioning, training, holding out
5. Claim(s) at issue and whether the exception reaches them (step 6)
6. Conclusion: inside / outside / fact-dependent, with residual risks
7. Other frameworks still in play: §702, state law, contract, tort, FLSA
8. Counsel review: name / date
```

## Scoping the Ministerial Exception — Numbered Checklist

Run whenever the question is "does the ministerial exception apply to this role or claim." Never
answer from the job title: an org that fires an unordained "director of communications" and then
argues the exception must reconstruct what the person actually did, which is hard after the fact.

1. **Identify the employer**: is the entity a "religious institution" for constitutional
   purposes — a house of worship, religious school, seminary, denominational agency, or a
   parachurch nonprofit organized and operating for religious purposes? Secular nonprofits with
   a faith heritage but no current religious mission (some legacy hospitals, universities,
   social-service agencies) are a harder call and belong to counsel.
2. **Get the actual job description and daily duties, not the title**: the current written job
   description, the job posting, the offer letter, and — critically — a truthful description of
   what the person actually does hour to hour.
3. **Score the religious-mission function**: does the role (a) teach or transmit the faith,
   (b) lead or plan worship, prayer, sacraments, or ritual, (c) form or catechize children or
   converts, (d) provide pastoral care, spiritual direction, or counseling with religious
   content, or (e) hold the org out publicly as a religious voice? A clear "yes" on any of
   (a)–(d) usually puts the role inside.
4. **Score the corroborating factors** (evidence, not requirements): formal ordination,
   commissioning, licensing, or set-apart status; religious title (pastor, minister, imam,
   rabbi, cantor, chaplain, director of religious education, youth pastor, worship leader,
   religion teacher); religious training/education requirement; how the org holds the person
   out to the public; whether the person holds themselves out as a minister.
5. **Apply the typical-role map**: senior/associate pastors, rabbis, imams, cantors, worship
   leaders, youth pastors, chaplains, directors of religious education, seminary and
   divinity-school faculty, and religion teachers in religious schools who pray with and
   catechize students are almost always inside. Custodians, maintenance staff, bookkeepers,
   secretaries handling non-religious functions, and lay teachers of purely secular subjects who
   do not pray with or catechize students are almost always outside. Music director,
   communications director, executive pastor, school principal, and administrator roles are
   fact-dependent — score by duties.
6. **Identify the claim**: the exception categorically bars Title VII (race, color, sex,
   religion, national origin), ADEA (age), ADA (disability), state anti-discrimination claims,
   and retaliation claims by a ministerial employee — and, per most circuits,
   hostile-work-environment claims by a minister about the employer's religious practice. It
   does **not** categorically bar tort claims for sexual assault or child sexual abuse,
   breach-of-contract claims resolvable on neutral principles, wage-and-hour claims under the
   FLSA (which has separate church exemptions and a ministerial carve-out of its own), or
   workers' compensation claims. Some circuits have applied it to hostile-environment claims
   against co-workers; some have not.
7. **Document the analysis before the personnel action, not after**: a contemporaneous memo
   written before termination — not a post-hoc defense — is what makes the exception hold up on a
   motion to dismiss. For any role the org may later treat as ministerial (including lay
   religious-school teachers), draft religious-formation duties into the job description at hire
   and keep records (lesson plans, prayer logs, chapel schedules) that show the function in
   operation.

## Religious Hiring Under Title VII §702 — Numbered Checklist

Run when the org wants religion or religious conduct as a hiring/retention criterion for a role
that is **not** clearly ministerial (custodian, admin, program staff, lay teacher). Do not confuse
the frameworks: telling a maintenance worker membership is required "because of the ministerial
exception" is wrong (that is §702) — and §702 does not permit firing "for any reason," only
religion-based selection.

1. **Confirm the employer qualifies as a religious organization** under §702. Factors: religious
   purpose in governing documents, religious ownership/affiliation, religious practices in
   operations, financial support from religious sources, whether the org holds itself out as
   religious. Broader than "church" — includes religious schools, seminaries, denominational
   agencies, and many parachurch nonprofits.
2. **Define the religious qualification in writing before recruiting**: a statement of faith or
   doctrinal standard the employee must affirm, and — separately, if used — a lifestyle/conduct
   expectation ("sexual conduct within the historic teaching of our tradition," specific
   substance-use standards, sabbath practice, dietary rules). Put it in the job posting,
   application, offer letter, and employee handbook. Every employee subscribes on hire and
   (ideally) re-affirms annually.
3. **Stay inside religion, not the other protected classes**: "We hire only Christians" is
   protected; "we hire only Christian men" is not, unless the role itself is ministerial and the
   exception applies.
4. **Apply the rule consistently**: selective enforcement (enforcing a chastity or marriage-fidelity
   standard against women who become pregnant outside marriage but not men whose partners do,
   such as firing the pregnant unmarried woman but not the unmarried father) is the fastest way
   to convert a §702 religious decision into a Title VII sex-discrimination case. Keep written enforcement records
   and apply the standard evenly, or narrow it.
5. **Frame conduct-based decisions on the religious standard, not the protected characteristic**:
   the decision record references the doctrinal or conduct standard the employee agreed to and
   how it was violated. Post-Bostock, decisions about employees in same-sex marriages or
   undergoing gender transition are drafted and documented as violations of the org's religious
   standard on marriage/sexuality; whether that framing survives litigation is the live question
   in Bear Creek Bible Church, Braidwood Management, and their successors. Route to counsel.
6. **Know what §702 does not do**: it does not protect against ADA, ADEA, FLSA, NLRA, OSHA, or
   most state-law claims not about religion, nor Title VII race or national-origin claims, nor
   tort liability. For ministerial roles the exception is broader; for others, §702 is the only
   Title VII shield.

## Religious Accommodation of Employees Under Groff — Numbered Checklist

Accommodate an employee's religious practice unless doing so imposes a substantial cost in the
context of the business; do not rely on the old de minimis reading.

1. **Log the request** — the religious belief and the specific accommodation (schedule change for
   sabbath or holy day, prayer time and space, dress or grooming, dietary, exemption from a
   specific task).
2. **Presume the belief is sincere** unless there is objective evidence otherwise — sincerity,
   not orthodoxy, is the test. Do not litigate the employee's theology.
3. **Explore accommodations** — schedule swaps, shift trades, voluntary substitutes, remote
   work, use of PTO, reassignment. Document the interactive process.
4. **If denying**, articulate the substantial cost specifically — direct expense, safety,
   operational disruption, impact on other employees' rights — in writing. Vague "hardship"
   language is what Groff rejected.
5. **Watch the internal-consistency trap**: denying a Muslim employee's Friday prayer
   accommodation while granting Sunday off to Christian staff creates both a Title VII case and a
   public-witness problem.

## Clergy Sexual-Misconduct Policy — Required Elements

Every faith-based nonprofit with clergy or ministry staff needs a written misconduct policy
adopted by the governing board, reviewed by counsel and the insurer, and known to every
employee, volunteer, and (in age-appropriate form) participant.

- **Definitions covering all three primary categories**:
  - **Abuse of a minor** — any sexual contact with, or sexual exploitation of, a person under
    the age of majority or under the age of consent in the relevant state. Zero-tolerance
    standard.
  - **Sexual misconduct with an adult in a pastoral, counseling, or supervisory relationship** —
    treated as non-consensual per se because of the power differential, regardless of the
    adult's stated consent. The category boards most often mishandle as a "consenting adults"
    private matter; most denominations and misconduct policies treat it as sexual misconduct per
    se, and civil tort claims under theories like breach of fiduciary duty can survive the
    ministerial exception. Name it explicitly.
  - **Sexual harassment and sexual misconduct in ministry to family, colleagues, or
    subordinates** — Title VII-style harassment plus ministry-specific relational-boundary
    violations.
- **Reporting channels that do not route through the alleged perpetrator's supervisor** — a
  named intake person or committee, a denominational hotline, and (always) the option to
  report directly to civil authorities.
- **Mandatory-reporter alignment** — a plain-English statement of the org's obligation under
  the applicable state child-abuse reporting statute, an explicit instruction that any staff
  member or volunteer with reasonable suspicion of abuse of a minor must report directly to
  authorities (not "up the chain" first), and a policy statement on the clergy-penitent
  privilege in states where it has been narrowed or abolished for child-abuse reports. Even where
  the privilege stands, it typically attaches only to confession-like communications, not to a
  third party (e.g., a parent in pastoral counseling) describing a victim; train clergy on the
  state's current statute and require reporting in any doubt. Emergency protection and legally
  required reporting must not await counsel, insurer, board, or internal approval. Internal
  notification does not replace a required report to the designated civil authority.
- **Investigation ownership** — for allegations against clergy or senior staff, use an
  independent investigator (GRACE, an outside law firm, or a denomination-level review board),
  not the alleged perpetrator's peers or direct reports, whose findings get dismissed as
  self-serving and draw insurer pushback on coverage.
- **Interim measures** — administrative leave (paid, unless the denomination or contract
  requires otherwise), restrictions on access to facilities and to minors, communications
  restrictions with the reporter and witnesses.
- **Denominational notification** — who tells the bishop, presbytery, district
  superintendent, association, beit din, or governing body, and when.
- **Care for the reporter and the affected community** — independent pastoral care for the
  reporter (not from the accused's supervisor or colleagues), transparent age-appropriate
  communication with the community, and a plan for healing regardless of the investigation's
  outcome.

## Safe-Sanctuary / Child-Protection Policy — Required Elements

- **Two-adult / two-deep rule**: no unrelated adult alone with a minor in a ministry setting;
  minimum two screened adults present for children's and youth ministry activities, classroom
  windows or open doors, no closed-door meetings.
- **Line-of-sight and access rules**: bathroom escort protocols, transportation rules (no
  1:1 driving of an unrelated minor), overnight/lock-in protocols with sleeping-area rules.
- **Age gap between youth workers and youth**: typically a minimum 5-year gap between the
  youngest adult worker and the oldest minor being supervised.
- **Digital communication rules**: no private DMs from adults to minors; group texts and
  parent-copy expectations; social-media friending policy; the same rules for volunteer
  coaches, camp staff, and worship-arts leaders as for paid staff.
- **Screening threshold**: define who requires background checks and training: typically all
  staff, all volunteers with recurring access to minors, and any volunteer serving overnight
  or off-site. Six
  months of active engagement in the community is a common waiting period before serving with
  minors (the "six-month rule").
- **Training cadence**: initial safe-sanctuary training before serving, refresher on a defined
  cycle (annually or every 2–3 years), documentation retained centrally.
- **Allegation-response team**: a pre-named team (senior clergy or ED, board chair,
  safe-sanctuary coordinator, insurer contact, counsel) that convenes on a defined timeline.
- **Insurance alignment**: adopt the policy the carrier requires. Insurers often condition
  sexual-misconduct-liability coverage on documented adoption of a compliant safe-church
  program and annual attestation of compliance. Non-compliance can void coverage.

## Background-Check Program — Design Points

- **Tiered screening matrix by role**: **clergy, ministry staff, school employees, camp
  directors, anyone with unsupervised access to minors or vulnerable adults** — national
  criminal database + multi-state sex-offender registry (Dru Sjodin NSOPW) + county-level
  searches for every county of residence over 7–10 years + Social Security trace + reference
  calls + (for clergy) prior-judicatory disclosure requests. **Volunteers with recurring minor
  access** — national + sex-offender registry + county where applicable (add MVR for driving
  roles). **General volunteers without minor access** — often sex-offender registry only or
  none; document the risk-based rationale.
- **Vendor**: use an FCRA-compliant consumer reporting agency (not a free aggregator) and verify
  that it runs county-level checks; national databases have significant gaps.
- **FCRA workflow**: standalone written disclosure, written authorization, pre-adverse-action
  notice with copy of the report and the FTC "Summary of Your Rights," a wait period
  (typically 5–10 business days), and a final adverse-action notice. Train the intake person on
  this sequence; skipping it gets the org sued on FCRA rather than the underlying decision.
- **Renewal cadence**: commonly every 3–5 years for staff and volunteers, more often for clergy
  in some denominations. Set a calendar; do not rely on one-time screening.
- **Disqualifying-offense schedule**: a written list that categorically disqualifies (any
  offense against a minor, sexual offenses, violent felonies) plus a category requiring
  individualized assessment (older convictions, financial crimes for non-financial roles, DUI
  for non-driving roles), aligned with EEOC guidance disfavoring blanket exclusions.
- **Clergy-transfer disclosure**: insist on a written disclosure from every prior
  denomination/judicatory of any allegations, investigations, or discipline. Denominational
  agreements (UMC "clergy file follows the pastor," Episcopal Title IV disclosure) create
  affirmative obligations; nondenominational orgs must build the equivalent contractually.

## Allegation Response — First 72 Hours

Run this sequence when an allegation lands. Do not improvise; do not "look into it" first.

**Safety and reporting take precedence:** the responsible human must initiate urgent protection
and make legally required reports to the designated authorities without waiting for a complete
intake record, the response-team meeting, counsel, or insurance clearance. Identify the applicable
jurisdiction, reporting trigger, authority, and deadline; do not turn the "72 hours" heading or
the 24-hour team-convening target into a reporting grace period. The agent supports preparation
and documentation; it does not substitute for the responsible person's reporting duty.

1. **Take the report seriously and in writing**: the intake person documents the allegation
   verbatim, date/time, source, and immediate details. Do not interrogate the reporter or
   press for corroboration.
2. **If the allegation involves a minor, report to civil authorities per state law immediately**
   — before internal deliberation. Mandatory-reporter obligations run to the individual, not
   the organization. Record who reported, to which authority, when, and any confirmation
   available, without delaying the report to complete that record.
3. **Convene the pre-named allegation-response team within 24 hours** — clergy or ED, board
   chair (or designated director if allegation involves the ED/senior clergy), safe-sanctuary
   coordinator, insurer, counsel. If the allegation is against the ED or senior clergy, they
   are not on the team.
4. **Notify the insurer** at this 24-hour mark — most policies require prompt notice; notifying
   only after weeks of internal investigation, once a claim looks likely, can void coverage.
5. **Notify the denomination or judicatory** if the accused is credentialed clergy or the
   denomination's polity requires reporting.
6. **Place the accused on administrative leave** — paid unless the contract or polity requires
   otherwise — with a written letter restricting access to facilities, minors, and the
   reporter/witnesses. Frame as neutral pending investigation, not a finding of guilt.
7. **Retain an independent investigator** (GRACE, outside firm, or judicatory review body). Do
   not investigate internally, especially with peers of the accused.
8. **Communicate to the community on a defined schedule**, coordinated with counsel, in
   age-appropriate form. Silence and rumor are worse than a careful, honest statement that
   acknowledges an allegation, describes the process, and commits to a follow-up.
9. **Arrange independent pastoral care for the reporter**, from someone with no supervisory or
   collegial relationship to the accused.
10. **Preserve documents** — email, texts, personnel file, prior complaints, training records,
    background-check file. Issue a written litigation hold.
11. **Close the loop**: at investigation completion, communicate the outcome (to the extent
    permitted), take employment action based on the finding, complete required reporting to
    civil authorities and denomination, and conduct an after-action review to fix the system
    conditions that allowed the incident.

Last checked September 16, 2026. This is not a determination of any particular state's reporting law.

## Terminating or Placing a Pastor on Leave — Workflow

Firing clergy is legally distinct from firing a lay employee and politically distinct from any
other board decision. Get all three pieces right: employment, ecclesiastical, communal.

1. **Confirm authority**: who can hire and fire this role — the congregation by vote, the elder
   board, the vestry, the session, the bishop, the denominational agency? Check the bylaws and
   polity before deciding (a UMC administrative board that "fires" the appointed pastor by vote
   lacks that authority — the bishop appoints). Governance mechanics of a congregational vote or
   judicatory concurrence are `nonprofit-faith-church-governance`; this skill covers what happens
   **inside the employment relationship** once authority is clear.
2. **Confirm the classification and contract**: W-2 employee, at-will, a written call agreement,
   or a denominational appointment (UMC itinerancy, Catholic assignment)? The instrument controls
   notice, severance, housing, and property (parsonage) obligations.
3. **Ministerial-exception scope check**: is this a straightforward inside-the-exception
   ministerial role (almost always yes for a pastor)? That makes discrimination-based suits
   difficult but does not eliminate contract, tort, or wage-hour exposure.
4. **Decide between administrative leave and termination** — leave fits pending investigation, a
   discipline process, or a discernment period; termination requires the substantive ground and
   the authority in place.
5. **Draft the letter with counsel**: neutral factual language, effective date, compensation
   and benefits treatment (including housing allowance and parsonage), access to facilities
   and files, communication obligations to the congregation, non-disparagement or
   reference-protocol terms if any, denominational-notification acknowledgment, and — if the
   departure is by mutual agreement — a release with the appropriate age-based waiver periods
   (ADEA OWBPA if the pastor is 40+).
6. **Coordinate with the denomination**: a credentialed pastor faces the denomination's own
   process (credentials review, defrocking/laicization/removal from the roll). Local employment
   action and ecclesiastical process are separate but must be sequenced, in parallel — local
   termination without denominational notification burns the relationship and, in connectional
   polities, may exceed local authority.
7. **Housing and parsonage**: if the pastor lives in a parsonage, the letter addresses move-out
   date and terms; if the pastor receives a housing allowance, address final allocation and
   W-2 treatment (see `nonprofit-faith-finance-clergy-comp`).
8. **Constructive-discharge risk**: reducing compensation, stripping duties, publicly
   disciplining, or forcing a "resign or be fired" choice without process can be framed as
   constructive discharge and, for a non-ministerial claim (breach of contract, defamation,
   sometimes tort), can survive the exception.
9. **Communicate to the community**: pre-drafted with counsel and, where relevant, the
   denomination. Address what happened, who is providing pastoral coverage, and how questions
   are handled — without violating confidentiality obligations or defaming the departing clergy.

## Denominational Discipline and Its Employment Consequences

- **Connectional/appointive (UMC and similar)**: the bishop appoints; the local church cannot
  unilaterally fire; discipline runs through the Book of Discipline (complaint, supervisory
  response, just resolution, or church trial).
- **Presbyterian (PCUSA, PCA, EPC)**: presbytery holds ordination and dissolves the call
  relationship; the local session works with presbytery under the Book of Order (PCUSA) or
  Book of Church Order (PCA).
- **Episcopal/Anglican**: bishop holds authority over clergy; Title IV canons govern clergy
  misconduct through intake, reference panel, hearing panel, and possible deposition.
- **Roman Catholic**: 1983 Code of Canon Law governs; diocesan bishop plus the Dicastery for
  the Doctrine of the Faith handles serious cases; laicization is the extreme outcome. USCCB
  Charter overlays for abuse of minors.
- **Congregational/independent (SBC congregations, nondenominational, most Jewish
  congregations, most mosques)**: the local body is the hiring and firing authority; no
  external ecclesiastical court to defer to. Discipline lives entirely in local bylaws and (for
  some Jewish congregations) a beit din process the congregation opts into.
- **Baptist associations / conventions**: the local church is autonomous; associations and
  conventions can withdraw fellowship or remove credentials but do not employ the pastor
  (SBC credentials-committee abuse-response activity has been one example; check its current
  status before citing it).
- **Civil-court restraint**: courts will not review the ecclesiastical determination but will
  hear neutral-principles property, contract and tort disputes — a defrocked pastor's Title VII
  claim is usually barred; the same pastor's contract or tort claim may not be.

## Volunteer vs. Employee Lines for Ministry Roles

Classification tests for clergy sit in `nonprofit-faith-finance-clergy-comp`; the volunteer
side sits in `nonprofit-faith-volunteer-lay-leadership`. What this skill adds: an uncompensated
volunteer worship leader is still subject to safe-sanctuary policy, background checks, and
misconduct policy; a stipended small-group leader may be a volunteer for classification but is
not immune from misconduct standards; ministry "interns" and "residents" who receive housing,
food, and a stipend in exchange for full-time work are usually FLSA employees regardless of what
the org calls them.

## Common Failure Modes

Each is detailed in the section named; use this as a final scan.

- **Treating the ministerial exception as a title test** (Scoping checklist, intro and step 7).
- **Confusing §702 with the ministerial exception** (§702 checklist intro).
- **Investigating internally when the allegation is serious** (misconduct policy; allegation step 7).
- **"Consenting adults" framing for pastor-congregant misconduct** (misconduct policy definitions).
- **Mandatory-reporter confusion via clergy-penitent privilege**: in most states the privilege
  has been narrowed or abolished for child-abuse reports (mandatory-reporter alignment).
- **Selective enforcement of a religious lifestyle standard** (§702 step 4).
- **Late notice to the insurer** (allegation step 4).
- **No pre-set ministerial-exception documentation for lay religious-school teachers** (Scoping step 7).
- **Background-check compliance failure under FCRA** (Background-Check Program).
- **Confusing local employment authority with denominational authority in connectional
  polities** (termination step 1).

## For advisors

- Get the system in place before an incident: board-adopted safe-sanctuary and misconduct
  policies, the tiered background-check matrix with a renewal calendar, religious-formation
  duties written into job descriptions for any role the org may later treat as ministerial,
  documented training, and a pre-named, rehearsed allegation-response team.
- Name the framework each question lives under before answering, and push back on two instincts:
  treating misconduct as only an HR question (it is also mandatory-reporter, insurance-coverage
  and pastoral-care work) and answering ministerial-exception questions from titles.
- Before any employment action against clergy, require the current written job description, a
  contemporaneous ministerial-exception memo, a counsel-drafted letter, denominational
  coordination, insurer notice and a community communication plan. This review sequence must
  not delay emergency protection or legally required reporting.
