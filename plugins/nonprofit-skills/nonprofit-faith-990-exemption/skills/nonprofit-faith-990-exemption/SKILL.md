---
name: nonprofit-faith-990-exemption
description: "Works out the special US federal tax status of churches and other houses of worship, their integrated auxiliaries and conventions of churches: automatic exemption without Form 1023, the Form 990 filing exemption, the 14-point church test, group rulings, church UBIT and §7611 audit protections. Use when asked 'do we need to file a 1023 for our new congregation', 'do churches file a 990', 'do we owe UBIT on the cell tower lease' or 'the IRS sent our church a letter'. Not for generic 990 filing (use nonprofit-form-990), clergy pay (use nonprofit-faith-finance-clergy-comp), federal-grant compliance (use nonprofit-faith-religious-liberty-compliance) or property-tax exemption (use nonprofit-faith-facilities-sanctuary)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Determinations about church status, integrated-auxiliary classification, UBIT liability, and audit-procedure invocation have direct federal tax consequences and should be reviewed by qualified tax counsel before filing or response."
  last_reviewed: "2026-09-10"
  date_added: "2026-09-12"
  date_added_source: "git:297d3ef69a314702df1ccc8174826716c88cff40"
---

# Church, Integrated-Auxiliary, and Convention/Association Federal Tax Status (IRC §§508, 6033, 7611)

## Boundaries

This skill owns the federal exemption, the information-return exemption, denominational group
rulings, church UBIT (including rental and parking income from church property) and IRC §7611
audit procedure for houses of worship and closely related bodies. Route the rest:

- Generic Form 990 / 990-EZ / 990-N filing for a 501(c)(3) that must file → `nonprofit-form-990`.
- State charitable-solicitation registration → `nonprofit-charitable-registration`.
- Generic enterprise risk and insurance (D&O, cyber, EPLI) → `nonprofit-risk-management`.
- Clergy income tax, §107 housing allowance, SECA, W-2 vs 1099 for clergy, love offerings,
  benevolence funds → `nonprofit-faith-finance-clergy-comp`.
- Charitable Choice / Equal Treatment rules for federal grants → `nonprofit-faith-religious-liberty-compliance`;
  running the funded program → `nonprofit-faith-programs-social-services`.
- State property-tax exemption, facility-use agreements and the operational side of rentals →
  `nonprofit-faith-facilities-sanctuary` (this skill covers only the federal-tax overlay).
- Polity, bylaws, member meetings, denominational relationships → `nonprofit-faith-church-governance`.

## Core Frameworks

Name the statute, reg, or IRS pub before drafting anything; generic 501(c)(3) advice is often
wrong for a church.

- **IRC §501(c)(3)** — churches qualify on the same substantive terms as any other charity
  (organized and operated for exempt purposes, no private inurement, limited lobbying, no
  political-campaign intervention).
  The specialness is procedural, not substantive.
- **IRC §508(a) and §508(c)(1)(A)** — §508(a) requires a 501(c)(3) to notify the IRS (Form 1023
  or 1023-EZ) to be treated as exempt. §508(c)(1)(A) is the "mandatory exception" for
  **churches, their integrated auxiliaries, and conventions or associations of churches** — they
  are exempt without applying ("automatic" church exemption).
- **IRC §6033(a)(3)(A)(i) and (iii)** — the parallel exemption from filing Form 990, 990-EZ, and
  990-N for the same three categories. This is why the church across the street has no Form 990
  on ProPublica Nonprofit Explorer.
- **Treas. Reg. §1.6033-2(h)** — defines "integrated auxiliary of a church": (1) described in both
  §501(c)(3) and §509(a)(1), (2), or (3), (2) affiliated with a church or convention/association
  of churches, and (3) internally supported. Internal support is an **unless-both** test on
  public-facing sales and specified support sources, not a majority-church-funding requirement.
  Paragraph (h)(5) names special groups exempt from internal support; qualifying
  below-college-level schools have a separate annual-return exception under (g)(1)(vii). See the
  classification checklist below.
- **IRS 14-point church test** — the IRS working definition absent a statutory one, restated in
  **IRS Publication 1828 (Tax Guide for Churches and Religious Organizations)** and applied in
  cases including American Guidance Foundation v. United States and Foundation of Human
  Understanding v. Commissioner. Walked in the church-status checklist below.
- **Rev. Proc. 80-27 (as modernized by Rev. Proc. 2023-5 and its successors)** — mechanics of
  **group exemption rulings**; see the group-ruling section below.
- **IRC §7611** — special church-audit procedures: IRS church tax inquiries and examinations need
  approval by a "high-level Treasury official" on "reasonable belief" of noncompliance, with
  written notice, staged procedure, limited scope, and a shorter statute of limitations. See the
  §7611 deep dive.
- **IRC §§511-514 (UBIT)** — see the Church UBIT deep dive for rental, §514 debt-financing and
  the Form 990-T threshold.

## Standard Deliverables

- **Church-status memo** — the 14-point test applied to a specific congregation, with written
  conclusion and residual risks.
- **"Should we file Form 1023 anyway?" decision memo** — grantor, state, and reputational
  trade-offs, with a recommendation.
- **Integrated-auxiliary classification memo** — for a seminary, mission board, publishing arm,
  denominational agency, retreat center, or affiliated ministry, walking the three-part test.
- **Group-exemption package or update** — initial group-ruling readiness review (subject to current
  IRS moratorium), annual subordinate-list update, or onboarding checklist for a new subordinate.
- **Federal-filing map for the church** — what the church does NOT file (990/990-EZ/990-N) and
  what it DOES still file (941, W-2/1099, 1098-C, 8282, 5578, 990-T if UBI).
- **UBIT analysis** — for a specific revenue stream (parking-lot rental, cell tower lease,
  bookstore, coffee shop, retreat rentals, thrift store, bulletin advertising, sponsorships), with
  Form 990-T threshold and estimated-tax implications.
- **§7611 response plan** — when an IRS letter arrives: church tax inquiry or examination; were
  procedural prerequisites met; what is the scope; what is the church's response window.

Skeleton for the church-status and integrated-auxiliary memos (adapt headings to the entity):

```
[Entity legal name] — Federal Church / Integrated-Auxiliary Status Memo
Prepared by / date / reviewed by (tax counsel): ___
1. Question presented (church? integrated auxiliary? which filing exception?)
2. Entity facts: state-law form, EIN, determination or group-listing letter (if any),
   governing documents reviewed, affiliated entities mapped
3. Analysis
   - Church: 14-point factors satisfied / weak / absent, with evidence
   - Integrated auxiliary: tax status; affiliation route under Reg. §1.6033-2(h)(2);
     internal-support A and B findings, or (h)(5) special group; any (g)(1)(vii) school exception
4. Conclusion (use the checklist's conclusion sentence)
5. Residual risks and facts that would change the answer
6. Filing consequences: what is not filed; what still is (see federal-filing map)
7. Recheck date and owner
```

## Determining Whether an Organization Is a "Church" for IRC Purposes — Numbered Checklist

Run this whenever church status is asked about or claimed on a filing, state exemption
application, or IRS response. The failure mode is concluding "yes" from religious identity alone.
Synagogues, mosques, temples, gurdwaras, Buddhist sanghas, and indigenous religious communities
satisfy the test on their own equivalents.

1. **Purpose confirmation**: confirm the org substantively meets §501(c)(3) for religious
   purposes; otherwise the procedural specialness is moot.
2. **Distinct legal existence**: identify the state-law entity (nonprofit corporation,
   unincorporated association, trust) — not merely a program of another org.
3. **Regular worship + regular congregation**: the practical center of gravity. Regularly
   scheduled worship (weekly or more is the archetype) for an identifiable, returning community,
   not primarily the founder's household or a broadcast audience.
4. **Established place of worship**: a fixed, regularly used location — owned, leased, or shared.
   A church in a school gym or a mosque in a leased storefront qualifies; a purely virtual or
   broadcast-only ministry with no gathering place trends against.
5. **Ecclesiastical government + code of doctrine + creed and form of worship**: a recognizable
   polity (elder-led, congregational, denominational, imam-led, rabbinic-led), an articulated body
   of teaching, and a recognizable worship form, written down in a doctrinal statement,
   siddur/liturgy/prayer-book use, or a governing document.
6. **Ordained ministers, selected after prescribed studies + minister-preparation pathway**:
   "ordained ministers" reads as the tradition's recognized clergy. Name the ordination or
   recognition process (seminary, yeshiva, madrasa, monastic training, denominational
   credentialing, apprenticeship under a recognized teacher). A sole self-appointed founder with
   no external recognition trends against.
7. **Religious instruction of the young ("Sunday schools")**: the tradition's equivalent —
   Sunday school, Hebrew school, weekend Islamic school, dharma school, catechism, first-communion
   prep, bar/bat mitzvah prep, youth halaqa. Absence is not fatal; presence weighs heavily.
8. **Membership discipline**: an identifiable membership or equivalent — regular congregants,
   registered families, mosque or temple members. Being part of a denomination is fine.
9. **Distinct religious history + literature of its own**: recognizable tradition (denominational,
   ancient, or newly emerging); literature is satisfied by sermons, a newsletter, prayer book,
   study guide, Sunday-school curriculum, or tradition-specific liturgical texts.
10. **Weigh, do not tally**: no single factor is dispositive and no fixed number is required.
    Regular worship, regular congregation, established place, community-recognized clergy, and
    instruction of the next generation carry the most weight; a distinct religious ministry is
    also part of the center of gravity. Traditions that express these differently (a Quaker
    meeting with no ordained minister, a Buddhist sangha with a teacher
    rather than seminary-trained clergy) are not disqualified when the associational substance is
    there.
11. **Write the conclusion**: "The organization is / is not a church for IRC §§508(c)(1)(A) and
    6033(a)(3)(A)(i) purposes because [factors satisfied], notwithstanding [factors weak or
    absent], based on the 14-point test and IRS Publication 1828." Note residual risk if any weak
    factor could become material on audit.

## Integrated-Auxiliary Classification — Numbered Checklist

Use for an affiliated seminary, mission board, publishing house, denominational agency, retreat
center, counseling center, or campus ministry to determine its annual-return obligation.
Distinguish integrated-auxiliary status from other filing exceptions, including the separate
qualifying-school exception. Neither affiliation alone nor a majority-fee calculation settles
the result.

1. **Tax-status requirement:** document that the entity is described in §501(c)(3) and in
   §509(a)(1), (2), or (3), as required by (h)(1)(i), and the basis for that status, including
   applicable group-ruling coverage; a pending application alone is not a completed analysis.
2. **Affiliation with a church or convention/association of churches**: Reg. §1.6033-2(h)(2)
   provides three routes: coverage by an applicable church group exemption letter;
   operation, supervision, or control by or in connection with a church as defined in
   §1.509(a)-4; or relevant facts and circumstances. For the last route, document the (h)(3)
   factors, including governing documents, appointment powers, reporting relationships,
   institutional affirmation, and dissolution provisions. Branding alone is not the analysis.
3. **Internal-support test under (h)(4):** the organization is internally supported
   **unless both A and B are true**:
   - **A, public-facing sales:** it offers admissions, goods, services, or facilities for sale
     to the general public other than incidentally. Exclude goods, services, or facilities
     sold at a nominal charge or for an insubstantial portion of cost.
   - **B, support mix:** it normally receives **more than 50%** of its support from the
     combination of governmental sources, public solicitation of contributions, and receipts
     from selling admissions or goods, performing services, or furnishing facilities in
     activities that are **not unrelated trades or businesses**.
   Record A and B separately with evidence. Only A true and B true fails the test. Exactly 50%
   does not satisfy B. Do not substitute "majority grants or fees" or "majority church funding".
4. **Special groups and separate school exception:** men's and women's organizations,
   seminaries, mission societies, and youth groups satisfying steps 1 and 2 are integrated
   auxiliaries under (h)(5) regardless of internal support. Colleges and universities do not
   qualify for this special rule merely because they are religiously affiliated.
   Separately, (g)(1)(vii) excepts a below-college-level educational organization described in
   §170(b)(1)(A)(ii), with a general academic program, that is affiliated with a church under
   (h)(2) or operated by a religious order. Record that as its own annual-return exception,
   not an automatic integrated-auxiliary classification or a blanket Form 1023 exemption.
5. **Recheck annually:** apply the regulation's "normally" standard to the support evidence
   and reassess public-facing activities and special-group status. An 80%-fee figure alone
   does not settle classification.
6. **Document and review the conclusion:** the memo names the legal entity, tax-status and
   affiliation evidence, A/B findings or (h)(5) exception, any separate school filing exception,
   conclusion, and review date. Obtain qualified tax-counsel review before relying on a
   no-filing conclusion; if no exception applies, determine the appropriate annual return.

Classification references: [Treas. Reg. §1.6033-2(g)(1)(vii), (h)(1)–(5)](https://www.irs.gov/pub/irs-regs/td8640.txt)
and [IRS Publication 557, annual-return exceptions](https://www.irs.gov/pub/irs-pdf/p557.pdf).
Last checked September 16, 2026; these references are not tax-counsel sign-off.

## Group Exemption Rulings for Denominations

A **central organization** (denomination, association, convention of churches, or parent religious
body) obtains a single IRS determination covering itself plus its listed subordinates
(congregations, agencies, missions, camps, schools), so subordinates do not each file a 1023.

- **Governing authority**: Rev. Proc. 80-27, modernized by Rev. Proc. 2023-5 and successors.
  Read the current-year Rev. Proc. before filing anything.
- **Current IRS posture**: the IRS has not accepted new group exemption applications since a
  moratorium beginning in 2020, pending revised procedures (Notice 2020-36 and successors).
  Verify current status before advising that a new group ruling is available. Existing group
  rulings continue to function.
- **Central-org obligations**: general supervision or control of subordinates as defined in the
  Rev. Proc.; an accurate subordinate list; annual group-ruling update filed at least 90 days
  before the close of the central org's accounting period, listing subordinates added, deleted,
  or changed; ensuring subordinates are of substantially the same character as those originally
  covered.
- **Subordinate obligations**: authorize inclusion; agree to the central org's supervision terms;
  notify the central org of material changes (dissolution, name change, address, activities).
  Subordinate churches remain independently eligible for automatic §508(c)(1)(A) exemption whether
  or not they appear on a group roster.
- **Independent (non-denominational) congregations**: cannot be added to another denomination's
  group ruling merely for convenience. Their automatic §508(c)(1)(A) exemption is sufficient in
  law but does not produce a stampable determination letter — see the 1023 decision section below.
- **Practical value of the listing**: the central org can furnish a copy of the group
  determination letter and a listing letter confirming the subordinate is on the current roster —
  the artifact grantors, banks, and states want.

## The Federal-Filing Map for a Church

The 990 exemption is an exemption from the annual information return, **not** from being an
employer or a tax collector; every church with paid staff, vehicle donations, or UBI has federal
filings. Build this map for every church. Dollar thresholds and deadlines change; verify current
figures in the form instructions on irs.gov and in IRS Publication 1828 before advising.

- **Form 1023 or 1023-EZ**: NOT required (§508(c)(1)(A)). Optional — see decision section below.
- **Form 990, 990-EZ, 990-N**: NOT required (§6033(a)(3)(A)(i) and (iii)).
- **Form 941 (Employer's Quarterly Federal Tax Return)**: REQUIRED for withholding on non-clergy
  employees. Clergy withholding is not required (though voluntary withholding under a §3402(p)
  agreement is common), but any non-clergy staff (secretaries, custodians, musicians treated as
  employees, childcare workers, school teachers) create Form 941 liability. See
  `nonprofit-faith-finance-clergy-comp` for clergy-side detail.
- **Forms W-2 and 1099-NEC / 1099-MISC**: REQUIRED for wages and contractor payments, including
  W-2s for clergy (even though they pay their own SECA and can exclude a housing allowance).
- **Form 1098-C**: REQUIRED when the church receives a donated motor vehicle, boat, or airplane
  valued over $500 and disposes of it. Written acknowledgment to the donor within 30 days of sale
  or use.
- **Form 8282**: REQUIRED when the church disposes of donated non-cash property (other than cash
  or publicly traded securities) within 3 years of receipt if the donor's claimed value exceeded
  $500. Filed with IRS and copy to donor within 125 days of disposition.
- **Form 8283 acknowledgment**: for non-cash donations over $5,000 (over $500 for vehicles), the
  church signs Section B of the donor's Form 8283.
- **Form 5578**: annual certification of racial nondiscrimination policy — REQUIRED for any church
  that operates a school (K-12 or preschool) that would otherwise file a 990.
- **Form 990-T**: REQUIRED when the church has $1,000 or more of gross unrelated business income
  in the tax year. See UBIT section below.
- **Backup withholding and Form 945**: if applicable.
- **Federal unemployment tax (FUTA)**: churches are generally exempt under §3306(c)(8). State
  unemployment varies — many states also exempt but some require coverage or offer
  reimbursable-employer status.

## Church UBIT — Deep Dive

Churches owe UBIT on the same terms as other §501(c)(3)s. Run the three-part test on every
non-donation revenue stream: (1) a trade or business,
(2) regularly carried on, (3) not substantially related to the church's exempt (religious)
purposes.

- **Parking-lot rentals to non-members**: renting the lot on weekdays to commuters or event-goers
  is generally UBI. If the church merely owns the lot and rents it without services (no attendant,
  no ticketing services), income may be excluded under §512(b)(3) as passive rental of real property — unless the lot is
  debt-financed under §514.
- **Coffee shops and bookstores open to the public**: primarily for the convenience of members and
  attendees (§513(a)(2)) — not UBI; a commercial coffee shop open to the neighborhood generally is.
  Look at signage, hours, marketing, and customer mix.
- **Cell tower leases on the church roof or steeple**: passive rental under §512(b)(3) is
  generally excluded. **But** if any portion of the property is debt-financed (mortgage on the
  sanctuary), §514 pulls the debt-financed fraction back into UBI. A deal that includes services
  (power, maintenance, security monitoring) beyond bare space can lose the §512(b)(3) exclusion.
- **Advertising vs. sponsorship in bulletins, programs, and websites**: **advertising income is
  UBI**; **qualified sponsorship payments** under §513(i) are not, as long as the payment does not
  include qualitative or comparative language, price information, or an endorsement — a plain
  "This service sponsored by [Business Name]" is generally a sponsorship; "Best plumber in town —
  call 555-1212 for 20% off" is advertising.
- **Thrift stores operated by the church**: the substantially-all-volunteer-labor exception under
  §513(a)(1) removes the activity from UBI even if commercial; lost if paid staff exceed the
  volunteer base.
- **Retreat center rentals to outside groups**: renting to outside religious retreats is often
  substantially related; secular corporate off-sites are generally UBI unless another exception
  applies. Split-use facilities need percentage-of-use tracking.
- **Wedding and funeral fees for non-members**: usually not UBI when integrated with religious
  services provided by clergy; facility-only fees from non-members trend toward UBI (facility side:
  `nonprofit-faith-facilities-sanctuary`).
- **Investment income, dividends, interest, royalties**: generally excluded under §512(b)(1),
  (b)(2), and (b)(5) unless debt-financed.

**Form 990-T mechanics** (verify current thresholds in the Form 990-T and 990-W instructions): file
990-T if gross UBI is $1,000 or more; tax is computed at the corporate rate. Estimated taxes on
Form 990-W quarterly if tax owed will exceed $500. UBI losses can offset gains only within each
unrelated trade or business ("silo" rule under §512(a)(6)); losses may not offset the church's
exempt-purpose activities.

## IRC §7611 Church Audit Procedures — Deep Dive

§7611 applies to any IRS **inquiry into or examination of a church** to determine tax liability or
exempt status. It does NOT protect an integrated auxiliary audit as such, a payroll (Form 941)
audit, or audits of non-church affiliated organizations. Confirm the target and scope first.

- **Reasonable-belief threshold**: an inquiry may begin only if an "appropriate high-level Treasury
  official reasonably believes on the basis of the facts and circumstances recorded in writing"
  that the church may not qualify for exemption or may be engaged in taxable activities.
- **High-level Treasury official**: originally the Regional Commissioner. After IRS reorganization,
  the IRS designated the **Director of Exempt Organizations**, later shifted to the **Commissioner
  of TE/GE**. This assignment was ruled inadequate in *United States v. Living Word Christian
  Center* (D. Minn. 2009), and the IRS has since revised its position more than once. Verify the
  current delegation order against the signature on the notice.
- **Two-stage procedure**: (1) **Church Tax Inquiry**: written notice sent to the church explaining
  the concerns, the general subject matter of the inquiry, and the church's right to a conference before
  examination. (2) **Church Tax Examination** — a separate written notice, sent at least 15 days
  after the inquiry notice, specifying the records and religious activities to be examined and
  offering a pre-examination conference.
- **Scope**: limited to what is necessary to determine liability; religious activities may be
  examined only to the extent necessary to decide whether the org qualifies as a church or is
  engaged in an unrelated trade or business.
- **Two-year completion rule**: an examination must generally be completed within two years of the
  examination notice.
- **Statute of limitations**: shorter than the general SOL for exemption revocation and UBIT — 3
  years back for UBIT; only the tax year at issue plus (in cases of fraud) prior years, per the
  §7611 limits.
- **Outside §7611**: it does NOT apply to (a) inquiries into whether an organization is actually a
  church, if the IRS is treating it as not-a-church; (b) criminal matters; (c) third-party
  recordkeeping; (d) certain routine payroll and information-return audits (Form 941, W-2
  matching). A payroll audit that opens substantive-status questions can create dispute about
  whether §7611 was triggered — get counsel.
- **Rarity is not optionality**: church audits are rare, but always check the notice against the
  statute.

## Should the Church File Form 1023 Anyway? — Decision Framework

Independent (non-denominational, non-group-covered) congregations often ask this. There is no
right answer for every church; frame the tradeoffs and recommend.

- **In favor**: (1) grantor foundations routinely require the determination letter regardless of
  automatic status; (2) many state agencies (income-tax exemption, charitable-solicitation
  registration, sales-tax exemption, some property-tax offices) want a copy; (3) banks, merchant
  processors, and payment platforms often ask for it to open accounts or grant nonprofit rates;
  (4) it produces a searchable IRS record (Publication 78 / Tax Exempt Organization Search) donors
  and auditors can verify; (5) if the church later reorganizes or spins off a school or affiliate,
  a determination letter simplifies everything downstream.
- **Against**: (1) filing fees ($275 for 1023-EZ, $600 for full 1023; verify the current user fee
  on irs.gov or Pay.gov); (2) full 1023 is a substantial narrative + financials package requiring
  outside help for most churches; (3) the church affirmatively invites IRS review of its
  organization and operations; (4) no substantive protection is lost by not filing; (5) for a
  small, all-donor-funded, single-site congregation with no grant plans and no state registration
  requirement, the practical benefit is marginal.
- **Recommendation shape**: if the church (a) wants grant funding, (b) is in a state that requires
  charitable-solicitation registration for churches, or (c) plans to grow beyond a small
  member-funded model — file the 1023 (or 1023-EZ if eligible) proactively. For a small member-funded
  congregation with none of those pressures, the automatic exemption is enough; document it
  with a church-status memo and be ready to explain it to bankers.

## State-Level Implications

State law rides on top of federal exemption and diverges materially; always cover the state
overlay.

- **State income-tax exemption** usually piggybacks on §501(c)(3) status. Some states
  auto-recognize federal exemption on receipt of the determination letter; others require a
  separate state application. Proving federal exemption without a determination letter is harder.
- **Sales-tax exemption for church purchases**: highly state-specific — automatic in some states;
  a state-issued exemption certificate in others; some exempt only certain categories (Bibles,
  prayer books, worship supplies).
- **Property-tax exemption** for the sanctuary and parsonage is entirely state property law —
  covered by `nonprofit-faith-facilities-sanctuary`. Federal §501(c)(3) status is neither
  necessary nor sufficient for it.
- **State charitable-solicitation registration**: most states that require registration exempt
  churches by statute, but not all, and exemptions vary in scope. Illinois generally exempts
  religious corporations from AG registration; Virginia exempts churches from Solicitation of
  Contributions Law registration; New York exempts most religious corporations from Article 7-A
  but not automatically (see N.Y. Exec. Law §172-a); California requires most religious
  corporations to register with the AG Registry of Charitable Trusts unless a specific exemption
  applies; Florida exempts "bona fide" religious institutions from Ch. 496; some states exempt
  churches themselves but not their affiliated fundraising subsidiaries. Confirm state-by-state —
  a home-state exemption does not follow the church to states where it fundraises. Route
  multi-state mechanics to `nonprofit-charitable-registration`.

## Verify Before Acting

- [ ] Every legal entity is mapped and classified separately (church, integrated auxiliary,
      qualifying school, convention/association, ordinary 501(c)(3), taxable affiliate).
- [ ] The memo conclusion cites the factors and evidence actually reviewed, not religious identity.
- [ ] Integrated-auxiliary memos record affiliation route and internal-support A and B separately.
- [ ] Group-ruling status, the group-ruling moratorium and any §7611 delegation were checked
      against current IRS guidance before advising.
- [ ] Every non-donation revenue stream was run through the UBI test, §512(b)(3) and §514.
- [ ] Fees, dollar thresholds and filing deadlines were confirmed on irs.gov for the current year.
- [ ] Qualified tax counsel has reviewed the conclusion before any filing or IRS response.

## Common Failure Modes

- **Automatic exemption confused with automatic recognition**: the church assumes a grantor
  foundation must accept its §508(c)(1)(A) status. Foundations don't. Explain substantive
  exemption (automatic) vs. a determination letter (only issued on filing) and, where grants
  matter, recommend the 1023.
- **Integrated-auxiliary status claimed on affiliation alone**: a denominational counseling center
  or camp never files a 990. Document tax status, affiliation, both internal-support conditions,
  and any (h)(5) special rule; check other filing exceptions before concluding a return is
  required.
- **Church-affiliated 501(c)(3) treated as a church**: a related legal-aid ministry, food pantry
  corp, or K-12 school is treated as "the church" for 990 purposes when it is a separate
  §501(c)(3). Map each legal entity and test its own filing exception (church, integrated
  auxiliary, qualifying below-college-level school, or other). Separate incorporation does not
  itself prove that a Form 990 is required.
- **Ignoring UBIT because "we're a church"**: cell tower on the roof + mortgage on the sanctuary
  produces UBI via §514; nobody files 990-T; audit produces back tax, interest, penalties.
  Inventory every non-donation revenue stream annually.
- **Missing payroll filings on the theory that "clergy don't pay tax"**: clergy have dual tax
  status (income tax + SECA) and still get a W-2; non-clergy staff generate Form 941 obligations.
  Map every worker (clergy vs. non-clergy, employee vs. contractor) and build a filings calendar;
  route clergy-comp mechanics to `nonprofit-faith-finance-clergy-comp`.
- **Group-ruling roster drift**: closed congregations still listed, new ones missing. Make the
  annual update a calendared responsibility with a named owner, cross-checked against the
  denomination's congregation database.
- **Invoking §7611 for the wrong audit**: demanding §7611 procedures in an ordinary payroll audit
  or an audit of a non-church affiliate costs credibility and counsel-of-record standing. First
  classify the notice (what entity, tax year, tax, stage).
- **"Church" claimed by an online-only ministry with no gathering community**: the 14-point test
  centers associational features a broadcast or podcast ministry lacks. Advise a more defensible
  classification (ordinary §501(c)(3) religious org that files a 990) rather than claim-and-hope.

## For advisors

- Before opining, collect the certificate of incorporation, EIN letter, any determination letter,
  any group-ruling listing letter, the last three years of financials and the payroll register;
  for group-covered clients, confirm current listing with the central org's group-ruling administrator.
- Build the church's federal-filings calendar explicitly (941 quarterly, W-2/1099 in January, 990-T
  May 15 if applicable, 5578 if the church runs a school, 8282 and 1098-C
  event-driven) plus the state overlay; most failures here are calendar failures.
- Record the "file a 1023 anyway?" decision in writing and revisit it when the church seeks
  foundation grants, plants congregations, opens a school or fundraises in new states.
