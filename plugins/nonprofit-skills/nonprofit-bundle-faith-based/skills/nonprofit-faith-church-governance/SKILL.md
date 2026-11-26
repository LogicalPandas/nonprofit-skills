---
name: nonprofit-faith-church-governance
description: "Guides governance and polity for US worship communities: diagnosing congregational, presbyterian, episcopal or elder-led polity, bylaws, member vs. non-member form, congregational meetings and quorum, clergy call and separation from the congregation's side, member discipline, disaffiliation and ecclesiastical abstention. Use when asked to 'redo our church bylaws', 'call a pastor', 'we're voting to leave the denomination' or 'quorum failed'. Not for secular boards (use nonprofit-board-governance or nonprofit-bylaws-policy), clergy employment (use nonprofit-faith-employment-ministerial-exception), church tax status (use nonprofit-faith-990-exemption) or clergy's own board reports (use nonprofit-ceo-board-partnership)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Church governance decisions become part of the corporate and ecclesiastical record and can trigger property, employment, and denominational litigation."
  last_reviewed: "2026-09-10"
  date_added: "2026-09-12"
  date_added_source: "git:297d3ef69a314702df1ccc8174826716c88cff40"
---

# Church, Synagogue, Mosque, and Temple Governance (Worship-Community Polity)

## Boundaries

This skill is the congregation's own governance and polity. Route adjacent work:

- Clergy employment terms, ministerial-exception firings, safe-sanctuary policies →
  `nonprofit-faith-employment-ministerial-exception`.
- Clergy compensation, housing allowance, dual tax status → `nonprofit-faith-finance-clergy-comp`.
- Automatic church exemption and the 990-filing exemption → `nonprofit-faith-990-exemption`.
- Worship-space use policies, including the decision to host or refuse a use →
  `nonprofit-faith-facilities-sanctuary`.
- Lay-leader recruitment, formation and terms in practice → `nonprofit-faith-volunteer-lay-leadership`.
- The senior clergy person's own artifacts toward the board (board reports, executive session,
  evaluation from the executive seat) → `nonprofit-ceo-board-partnership`.
- Secular 501(c)(3) board mechanics and generic bylaws, or a faith-based service nonprofit that
  is not a worship community → `nonprofit-board-governance` and `nonprofit-bylaws-policy`.

## Core Frameworks

Name the polity model before drafting anything. "Can we fire the pastor by member vote?" has
opposite answers under congregational and episcopal polity.

- **Congregational polity**: final ecclesiastical and corporate authority rests in the gathered
  membership at a duly called meeting. Baptists (SBC, ABC, CBF, most independent Baptist),
  United Church of Christ, Congregationalists, most non-denominational and community churches,
  and (by practice) the great majority of independent Muslim mosques, Hindu temples, and Buddhist
  sanghas. Officers, elders, deacons, and pastors serve at the pleasure of the members within the
  terms of the bylaws.
- **Presbyterian / synodical polity**: authority is shared between the local session/consistory
  and graded assemblies — presbytery, synod, general assembly — with real jurisdiction over the
  local body. PCUSA (Book of Order), PCA (Book of Church Order), EPC, ECO, RCA, CRC, and (in a
  Lutheran variant) ELCA and LCMS. The local body cannot call or dismiss a pastor without
  presbytery/synod action; property is often held under a denominational trust clause.
- **Episcopal / hierarchical polity**: authority runs from a bishop and higher courts down to the
  parish. The Roman Catholic Church (canon law, diocesan bishop, parish administrator), the
  Episcopal Church (canons, diocesan bishop, vestry, rector), the Anglican Church in North
  America, the United Methodist Church and its Wesleyan cousins (AME, AMEZ, CME — the Book of
  Discipline, bishop, annual conference, district superintendent, charge conference), and the
  Eastern Orthodox jurisdictions. The parish typically does not own its property outright; the
  pastor is appointed, not called.
- **Elder-led / non-denominational hybrid**: an elder or overseer board holds ecclesiastical
  authority; a separate corporate board (sometimes the same people) holds fiduciary authority;
  members may have a narrow vote (bylaws changes, elder confirmation, real estate) or none. Common
  in Acts 29, EFCA, Bible-church, Calvary Chapel, non-denominational charismatic and multi-site
  models. The "elder authority" vs. "member authority" line is where most bylaws disputes live.
- **Non-Christian analogs, US practice**:
  - **Jewish congregations**: almost always a nonprofit corporation with a board of trustees and
    a rabbi under contract; movement affiliation (URJ Reform, USCJ Conservative, OU/Young Israel
    Orthodox, Reconstructionist) supplies standards and dues but rarely legal authority. Chabad
    houses are legally independent but coordinated through the movement.
  - **Muslim mosques (masajid)**: overwhelmingly independent 501(c)(3) corporations with a board
    of directors and a shura (consultative) council; imams are typically employees under the
    board. ISNA, ICNA, and Fiqh Council affiliation is advisory.
  - **Hindu and Buddhist temples**: typically independent corporations; some Buddhist sanghas
    (Soto Zen, certain Tibetan lineages) sit under a lineage authority that functions like an
    episcopal layer for ordination and teaching but not for property.
- **Governing documents stack**: (1) **articles of incorporation** under the state nonprofit
  corporation act (member or non-member; religious-corporation act in some states like New York,
  California, Pennsylvania); (2) **bylaws** or constitution-and-bylaws; (3) **church covenant**
  (Baptist and some evangelical traditions — binds member-to-member); (4) **book of order / book
  of discipline / canons / halakhic standards** (denominational rules adopted by reference);
  (5) **policies** adopted by the board or elders.
- **Ecclesiastical abstention doctrine**: US civil courts will not adjudicate religious doctrine,
  discipline, or internal church government (Watson v. Jones, 80 U.S. 679 (1871); Serbian
  Eastern Orthodox Diocese v. Milivojevich, 426 U.S. 696 (1976); Kedroff v. St. Nicholas
  Cathedral, 344 U.S. 94 (1952)). They decide corporate and property questions on **neutral
  principles of law** where possible (Jones v. Wolf, 443 U.S. 595 (1979)) so long as no doctrinal
  question must be resolved. See the civil-court line section below.
- **First Amendment ministerial exception** (Hosanna-Tabor v. EEOC, 565 U.S. 171 (2012); Our
  Lady of Guadalupe v. Morrissey-Berru, 591 U.S. 732 (2020)): shapes what bylaws can and should say
  about clergy separation; the workflow lives in `nonprofit-faith-employment-ministerial-exception`.

## Standard Deliverables

- **Church/synagogue/mosque bylaws or constitution** — full rewrite or targeted amendment,
  aligned to the polity model and the state nonprofit corporation act.
- **Congregational-meeting packet** — call of meeting, agenda, quorum determination, motions
  language, ballot design, member-roll certification, and minutes (skeleton below).
- **Pastor/rabbi/imam call or separation package** — from the congregation's side: search
  committee charter, call letter (not the compensation exhibit — that is a sibling skill),
  covenant of ministry, separation agreement scaffolding, and required denominational approvals.
- **Member admission / discipline / removal packet** — application, covenant,
  disciplinary-process memo aligned to Matthew 18 (Christian) or the tradition's analog, and the
  ecclesiastical-abstention analysis.
- **Disaffiliation / realignment memo** — the votes, denominational notices, and property analyses
  required to leave a denomination (or to withstand a schism internally).
- **Governance-authority memo** — "who decides?" between clergy, elders, board/vestry/shura, and
  members, cross-walking bylaws, denominational standards, and state law.

Congregational-meeting packet skeleton:

```
[Congregation legal name] — [Annual / Special] Congregational Meeting
1. Call of meeting: called by ___ under Bylaws Art. __ ; state act § ___
2. Notice: date sent ___ ; method(s) ___ ; period required __ days / given __ days
   Business stated verbatim: [each motion to be considered]
3. Record date and certified roll: record date ___ ; members on roll ___ ; certified by ___
4. Quorum: required ___ (Bylaws Art. __) ; present ___ ; proxies/absentee allowed? Y/N
5. Parliamentary authority: ___ ; chair ___ ; secretary ___
6. Motions: exact text ; moved/seconded ; ballot type ; threshold required ___
7. Results: yes ___ / no ___ / abstain ___ ; threshold met? Y/N
8. Minutes: signed by secretary [and chair] ; filed ___ ; copy to [denominational body] if required
9. Ballot retention until ___ (bylaws challenge window + state limitations period)
```

## Diagnosing the Polity Model Before Drafting — Numbered Checklist

Run at the start of every engagement; half of all church-governance disputes are about which
model the community is actually operating under.

1. **Read the articles of incorporation.** Confirm the state of incorporation, general nonprofit
   act or religious-corporation statute, **member** or **non-member** corporation, and any named
   denomination or affiliation. Note the purpose clause verbatim.
2. **Read the current bylaws / constitution in full.** Identify: who the members are (and how
   membership is gained and lost); what members vote on and what they do not; the board and its
   name (trustees, directors, elders, deacons, vestry, council, shura, majlis); officer roles;
   quorum for congregational and board meetings; amendment procedure; dissolution clause; and any
   adoption-by-reference of a denominational book.
3. **Read the denominational book (if any).** UMC, the Book of Discipline; PCUSA, the Book of
   Order; PCA, the Book of Church Order; ELCA, the Model Constitution for Congregations plus the
   ELCA Constitution; Episcopal Church, the Constitution and Canons plus diocesan canons;
   Catholic, the Code of Canon Law plus diocesan statutes; SBC/CBF/ABC, the ministry covenant
   (SBC churches are autonomous — the Convention has no jurisdiction, only fellowship);
   Conservative Jewish, USCJ standards; Reform, URJ standards. Note provisions the local body has
   agreed to that override or supplement its bylaws.
4. **Locate the property title chain.** Pull the deed(s), any declaration of trust, mortgage,
   and any denominational trust clause (e.g., the UMC trust clause in Discipline ¶2501, the PCUSA
   trust clause in Book of Order G-4.0203, the Episcopal Dennis Canon). Property answers drive
   disaffiliation answers.
5. **Reconstruct the actual membership roll.** Compare the paper roll to actual attendance and
   participation; identify inactive members, members who moved, deceased members not removed, and
   admitted-but-never-covenanted attendees. The roll determines quorum and vote outcomes; a stale
   roll is the single most common cause of failed congregational votes.
6. **Map the authority stack.** In one page, name for each major decision — call/dismiss clergy,
   adopt budget, sell real estate, amend bylaws, admit/remove members, discipline members, sue
   or be sued, affiliate/disaffiliate — who has authority: clergy, board/elders/vestry/shura,
   members, or an outside body (presbytery, bishop, diocese, movement). Where the bylaws are
   silent, name the default under state law and the denominational book, and flag the gap.
7. **Flag the ecclesiastical vs. corporate line.** For each disputed question: can a civil court
   decide it on neutral principles (contract, property, corporate procedure), or would it have to
   decide a doctrinal or internal-church-government question? The answer shapes drafting and
   litigation posture.

## Writing or Rewriting the Bylaws — Numbered Checklist

Run this whenever the user says "redo our bylaws" or "we don't know what our bylaws say."

The failure mode is copying a template from another tradition and inheriting a polity the
community does not practice.

1. **Confirm the polity model in writing.** The preamble or governance article states the polity
   and any denominational standards adopted. Silence creates the ambiguity that leads to splits.
2. **Choose member vs. non-member corporate form deliberately.** A **member corporation** gives
   the congregation legal voting rights the state will enforce (annual meeting, director
   elections, bylaw amendments, real-estate votes depending on state law). A **non-member
   corporation** vests all corporate authority in the board and treats "membership" as
   spiritual/covenantal only. Congregational-polity communities almost always want member form;
   elder-led non-denominational churches often want non-member form and a separate
   covenanted-membership roll. A member corporation that functionally operates as elder-led
   produces exactly the lawsuits ecclesiastical abstention will not resolve.
3. **Define membership in one place, with observable criteria.** Age (often 16 or 18 for voting),
   admission process (profession of faith / covenant signing / mikveh or beit din / shahada
   affirmation / bai'at / refuge vows, plus a decision by the elders/board/rabbi/imam), duties
   (attendance, giving, service), and grounds for removal (voluntary withdrawal, transfer,
   inactivity threshold, discipline). Include a **letter of transfer** or equivalent for
   traditions that use one.
4. **Set the meetings architecture.** Annual congregational meeting (required by most state acts
   for member corporations; the state deadline sets the outer bound), special congregational
   meetings (who can call, notice period — usually 10-30 days, notice method aligned to state
   act), regular board/elder/vestry meetings, and executive sessions. State each quorum at a
   **realistically achievable** number — a 50% quorum for a 400-member church that regularly
   draws 120 to worship guarantees failed votes.
5. **Enumerate the members' reserved powers explicitly.** Typical in a congregational church:
   elect board/elders/deacons; call and dismiss the senior pastor; adopt the annual budget;
   approve real-estate purchase, sale, or mortgage above a threshold; amend bylaws and articles;
   approve affiliation or disaffiliation; approve dissolution. Everything else defaults to the
   board.
6. **Enumerate the board's powers and its committees.** Fiduciary duties (care, loyalty,
   obedience under state nonprofit law), standing committees (finance, personnel, nominating,
   audit if applicable), the pastor/rabbi/imam's ex officio status (voting or non-voting — pick
   one), conflict-of-interest policy adoption, and indemnification.
7. **Handle clergy call, review, and separation from the polity's perspective.** Congregational:
   pulpit/search committee composition and charge, call vote threshold (typically 75-90%
   supermajority), annual review, and grounds and procedure for congregational dismissal.
   Presbyterian: the presbytery's role in call, review, and dissolution. Episcopal: the bishop's
   appointment authority and the parish's role in petitioning. Bylaws only need to name **who
   decides, by what vote, after what process**; employment terms live in
   `nonprofit-faith-employment-ministerial-exception`.
8. **Include a member-discipline article.** Grounds (violation of the covenant, persistent
   unrepentant sin, teaching contrary to the doctrinal standards, harm to others), process
   (private conversation → witnesses → elders/board → congregation, tracking Matthew 18 in
   Christian traditions or the tradition's analog), remedies (admonition, suspension of
   privileges, removal from the roll, excommunication in Catholic and Orthodox traditions,
   herem in Jewish tradition — rare), and the appeal path. This makes the process defensible
   under ecclesiastical abstention.
9. **Include a dispute-resolution and abstention article.** Members agree to resolve internal
   disputes through the community's own process (elders/beit din/shura/parish arbitration),
   waive civil recourse for ecclesiastical matters to the extent permitted by law, and submit to
   courts only for corporate and property questions resolvable on neutral principles. Civil
   courts will still hear tort, contract, and statutory claims regardless.
10. **Set the amendment clause carefully.** Notice period, quorum, and vote threshold for bylaws
    amendments; higher threshold for articles, doctrinal statement, and any
    denominational-affiliation clause. Distinguish amendments the board can make (policies) from
    those only members can make (bylaws, articles, covenant, doctrinal statement). Never let the
    members lose the power to amend the doctrinal statement without their own supermajority vote
    — this clause, more than any other, prevents hostile takeovers by a captured board.
11. **Set the dissolution clause consistent with 501(c)(3) and any denominational trust
    clause.** Residual assets go to another 501(c)(3), identified by category (typically the
    denomination, a named seminary, or a sister congregation). Under a trust clause, residual
    real estate reverts to the denomination by operation of the trust clause, not the
    dissolution clause — do not draft around this without counsel.

## Running the Annual (or Special) Congregational Meeting — Numbered Checklist

The failure mode is a vote the losing side can challenge on procedure.

1. **Certify the members' roll as of the record date.** The state act typically requires a
   record date (often 10-60 days before the meeting); only members on the roll then may vote.
   Publish the roll, invite corrections, and close it; members added afterward do not vote.
2. **Issue notice as the bylaws and state act require.** Notice period, permissible method
   (pulpit announcement, mailed notice, email if the bylaws authorize it), and content (date,
   time, place, purpose — with special business stated verbatim so no motion outside the notice
   can be taken up). Notice is a jurisdictional prerequisite: no notice, no meeting, no matter
   how many people showed up.
3. **Confirm quorum before the first motion.** Count members present (and, if the bylaws allow,
   proxies or absentee ballots — many denominations do not); record the count in the minutes.
   If quorum fails, adjourn to a date certain per the bylaws; do not proceed under any
   circumstances.
4. **Follow the parliamentary authority the bylaws name.** Robert's Rules is the default; some
   traditions use their own (Presbyterian churches often use the denominational rules of order;
   the UMC has its own Rules of Order). The chair rules on procedure; a member may appeal a
   ruling to the body.
5. **Structure the ballot to survive later challenge.** Written ballots for elections and any
   vote with a bylaws threshold; oral or standing votes for routine business. Preserve ballots
   for the bylaws challenge window (often 30-60 days) plus the statute of limitations for
   corporate challenges under the state act.
6. **Announce the result against the bylaws threshold, not the raw count.** A pastor call at
   "72% in favor" fails a 75% threshold and is not a call. State threshold and count in the
   announcement and minutes.
7. **File the minutes as a corporate record.** Signed by the secretary and (where required) the
   chair; retained permanently; provided to the denominational body if the polity requires
   (charge-conference minutes to the district superintendent; session minutes to presbytery for
   annual review). Minutes are the primary evidence in every later dispute.

## The Pastor / Rabbi / Imam Call from the Congregation's Side

Recruiting, interviewing, and negotiating are not in this skill. The polity work around the call:

- **Congregational polity**: the members (through an elected pulpit committee) present a single
  candidate and the congregation votes. Bylaws almost always require a supermajority (75-90%) and
  a separate call letter stating term (usually indefinite in Baptist practice), compensation by
  reference to the exhibit, and grounds for review and separation. A low-supermajority call ("we
  barely got 76%") is a warning sign to hear, not overrule.
- **Presbyterian polity**: the congregation votes to call; the presbytery examines and installs;
  the relationship is dissolved by presbytery action (usually on joint request), not by
  congregational vote alone.
- **Episcopal polity**: in the Episcopal Church, the vestry issues the letter of agreement
  subject to the bishop's approval. In the UMC, the bishop appoints in consultation with the
  SPRC and cabinet; there is no parish vote on the appointment. In the Catholic Church, the
  bishop assigns the pastor.
- **Elder-led non-denominational**: typically the elders (sometimes with a member confirmation
  vote at a specified threshold) call the senior pastor. Bylaws should say whether members have a
  confirmation vote and, if so, on the elders' single nominee or on a slate.
- **Jewish congregations**: the board (often through a search committee, sometimes with movement
  placement services — CCAR, RA, RCA) presents the candidate; members typically vote to approve
  the contract. The rabbi is an employee, not a corporate officer, unless the bylaws provide
  otherwise.
- **Muslim mosques**: the board (with shura input) hires the imam as an employee. A
  congregation-wide vote is rare and, where held, is on the board's nominee.

Regardless of polity, the **call letter is a contract**. Keep the ecclesiastical call
(covenant/appointment) in a separate document from the **employment agreement and compensation
exhibit** (`nonprofit-faith-finance-clergy-comp`), cross-referenced cleanly; one mixed document
lets ministerial-exception litigation
(`nonprofit-faith-employment-ministerial-exception`) fight over which clauses are which.
The employment agreement and compensation exhibit drive the ministerial-exception analysis.

## Pastoral Separation, Removal, and Congregational-Side Discipline

Termination mechanics (cause, process, ministerial exception) belong to
`nonprofit-faith-employment-ministerial-exception`. The **polity-side** sequencing:

- **Congregational churches**: bylaws specify whether members dismiss the pastor by direct vote or
  only through the elders/board under member-delegated authority, the vote threshold (often the
  call supermajority), notice period, and procedure (typically an elder or board resolution, a
  special congregational meeting, and a written vote). Skipping the special-meeting step is the
  single most common procedural defect in a challenged dismissal.
- **Presbyterian churches**: the congregation and/or session petition; the presbytery holds a
  hearing and dissolves the call. A local body cannot "fire" its pastor unilaterally.
- **Episcopal / UMC**: the bishop moves the appointment. In the UMC, the SPRC works with the
  district superintendent and cabinet. In the Episcopal Church, the vestry may terminate the
  letter of agreement subject to canonical process and, in many dioceses, bishop involvement.
- **Elder-led non-denominational**: the elders act, often with member ratification at a
  specified threshold. If the elders are also the corporate directors, one meeting can suffice;
  if separate, both bodies must act.
- **All traditions**: give the departing clergy a meaningful and confidential process; keep
  substantive discussion of allegations and reasons out of open congregational meetings unless
  required; document each step; treat the separation letter as **restricted** because it will surface in later
  litigation or reference calls.

Member discipline is a distinct process. In congregational and covenantal traditions, the
bylaws or covenant should provide a graduated process: private conversation, witnesses, elder
or board involvement, congregational involvement, removal from the roll, tracking the
tradition's own theological grammar (Matthew 18 for Christian traditions; teshuvah and beit din
for Jewish; shura mediation for Muslim). Follow it exactly. **Civil courts will not review the
merits of the discipline decision**, but they will review whether the community followed its own written
process and whether the discipline gave rise to independent tort claims (defamation, invasion of
privacy, IIED). The most common lawsuit is not against the excommunication; it is against
announcing it beyond the membership (from the pulpit, online). Keep discipline communications in
the members' channel with non-descriptive language ("no longer a member"), not reasons.

## Denominational Reporting and the Local-Denominational Relationship

| Polity / body | What the local body owes |
|---|---|
| Congregational (SBC, ABC, CBF, UCC, most independents) | Minimal: annual statistical/church-profile report, voluntary contributions (Cooperative Program, Our Church's Wider Mission), messenger credentials in some. No jurisdiction over local governance. |
| Presbyterian (PCUSA, PCA, EPC, ECO) | Annual statistical report to the General Assembly; presbytery review of session minutes; per-capita apportionment; presbytery approval for major real-estate transactions and for calling or dismissing clergy. |
| Episcopal / Anglican | Annual parochial report to diocese and national church; diocesan assessment; diocesan approval for property alienation; canonical residence of clergy. |
| UMC / AME / AMEZ / CME | Annual charge conference presided over by the district superintendent (adopts pastor's compensation, elects lay leaders, reviews ministry); connectional apportionments; trustees hold property under the trust clause; itinerant pastors appointed annually. |
| Catholic | Parish usually not a separate civil entity (the diocese is a corporation sole or religious corporation owning parish property); parish and finance councils are consultative to the pastor, who answers to the bishop. |
| ELCA / LCMS | Constitutional relationship with the synod; synod bishop or president has defined roles in call and discipline; assessments to synod and churchwide. |
| Reform (URJ) / Conservative (USCJ) / Orthodox (OU/Young Israel) | Movement dues and standards (e.g., USCJ Standards for Congregational Practice); placement services for rabbi search; congregation legally independent and can disaffiliate at will. |
| Islamic (ISNA, ICNA, MAS, tariqas) | Affiliation is honorary; no jurisdictional authority in most cases. |

Cite the specific provision of the current denominational book, not a paraphrase.

## Disaffiliation, Realignment, and Splits — Numbered Checklist

The highest-stakes governance workflow in the family; handle it with a written plan.

1. **Determine whether disaffiliation is legally available.** The UMC ¶2553 disaffiliation window
   closed December 31, 2023; ongoing disaffiliation now requires either ¶2548.2 (transfer to
   another Methodist denomination with annual conference approval), ¶2549 (church closure), or
   civil-court action (verify against the current Book of Discipline and annual-conference
   rules, which General Conference can change). PCUSA congregations use the presbytery-negotiated
   dismissal process; PCA has its own transfer procedure. Episcopal parishes cannot unilaterally
   leave with property under the Dennis Canon. Independent and most Baptist churches can leave
   any affiliation at will. Verify the current provision before advising and frame the memo
   around what is actually available, not what the congregation wishes were available.
2. **Read the property trust clause before scheduling any vote.** UMC Discipline ¶2501, PCUSA
   G-4.0203, Episcopal Dennis Canon, and various diocesan and synodical trust clauses commonly
   hold parish property in trust for the denomination. State courts split: Jones v. Wolf permits
   "neutral principles" analysis, but a trust clause meeting the state's requirements for an
   express trust is often enforceable regardless of the congregation's wishes — a 90% vote to
   leave with the building can collide with a clause the state courts have enforced for 40 years.
   Get a title opinion and build the property settlement into the plan.
3. **Sequence the votes required by the bylaws and the denominational book.** Typical:
   (a) elder/board resolution recommending disaffiliation; (b) special congregational meeting
   with the disaffiliation motion, at the bylaws supermajority (often 66-75%); (c) denominational
   filings and any required denominational-body vote; (d) property settlement, if any;
   (e) revised articles of incorporation removing denominational references and adopting a new
   purpose clause and dissolution clause; (f) new employer-of-record arrangements for clergy
   pension and health benefits (Wespath for UMC, Board of Pensions for PCUSA, Church Pension
   Group for Episcopal).
4. **Address minority-faction protections in the vote design.** Leaving 78-22 with no path for
   the 22% likely produces a second lawsuit. Consider dividing assets, letters of transfer to a
   sister congregation of the losing side, or delaying the vote pending a mediated process.
5. **Manage employee transitions.** Clergy pension, health benefits, and denominational status
   change on disaffiliation; lay employees may or may not (depends on the plan). Coordinate with
   `nonprofit-faith-finance-clergy-comp` and the denominational benefits body directly.
6. **Communicate through a written pastoral letter, not a Facebook post.** Communications
   discipline lives in `nonprofit-faith-communications-pastoral`; here, ensure the letter
   accurately states the vote count, process followed, and next steps, and does not defame the
   leaving or staying faction.

## The Civil-Court / Ecclesiastical-Court Line

Give this memo whenever a governance dispute is on the edge of litigation.

- **Courts will decide**: corporate procedure (quorum, notice, vote counted against the
  bylaws-defined threshold), contract (call letter or lease breached, compensation-exhibit terms
  enforceable), property (title, trust-clause enforceability under state law), and independent
  torts (defamation, IIED, negligence — including negligent hiring/supervision claims from clergy
  misconduct, which reach the corporation regardless of the ministerial exception).
- **Courts will not decide**: who is qualified to hold clergy office, whether a member is in
  good standing, whether a discipline decision was doctrinally correct, whether a doctrinal
  interpretation is right, whether an ecclesiastical assembly acted within its own religious
  jurisdiction (Milivojevich).
  Ecclesiastical questions framed as contract or tort claims are routinely dismissed on First
  Amendment grounds.
- **Neutral principles vs. deference**: most states now use the Jones v. Wolf neutral-principles
  approach in property and corporate disputes — reading deeds, articles, bylaws, and trust
  clauses as legal documents. A minority of states (and federal courts in some
  hierarchical-church cases) still defer to the highest church court's determination on
  questions characterized as ecclesiastical. Know the state's regime before advising.
- **What to draft into governing documents**: a clear polity statement; an unambiguous property
  clause (either "held in trust for [denomination]" or "held solely by the corporation for its
  own purposes and not in trust for any external body"); a dispute-resolution article channeling
  disputes through the community's own process; and separation of the ecclesiastical call from
  the employment contract.

## Verify Before Acting

- [ ] The polity model is named in writing and matches the bylaws, denominational book,
      property title and actual practice (or each gap is flagged).
- [ ] Draft bylaws were checked against the state nonprofit or religious-corporation act and any
      denominational book adopted by reference; denominational paragraph numbers were confirmed
      in the current edition.
- [ ] The authority map assigns every major decision (clergy, budget, real estate, amendments,
      members, affiliation) to one body; members' reserved powers are explicit.
- [ ] Quorum, notice, record date and vote thresholds in any meeting packet trace to a bylaws
      article or statute.
- [ ] Discipline and separation communications stay inside the membership and state no reasons.
- [ ] Disaffiliation advice rests on a title opinion and counsel review, not the congregation's wishes.

## Common Failure Modes

- **Polity drift** — bylaws describe congregational polity but the community operates as
  elder-led (or vice versa), so every disputed decision fails one authority test or the other.
  Align bylaws to actual practice in the next amendment cycle; do not let the community keep
  operating in the gap.
- **Stale membership roll** — quorum or a threshold vote fails because of people who moved away
  years ago. Clean the roll under the bylaws process before any threshold vote.
- **Notice defects** — a special meeting called by phone or Facebook, without the required
  method, and the vote is later voided.
- **Silent bylaws on member-vs.-board authority** — on a real-estate sale, pastor call, or bylaws
  amendment, both sides claim authority. Enumerate members' reserved powers in the next amendment.
- **Ignored trust clause** — see disaffiliation step 2.
- **Ecclesiastical discipline announced beyond the membership** — produces a defamation suit that
  survives ecclesiastical abstention.
- **Collapsed clergy call and employment contract** — see the call section; draft two documents.
- **Board that is not the corporate board** — the elders think they govern, but the articles
  name a different body as directors, so "elder decisions" are legally ultra vires. Align the
  articles, bylaws, and actual governance to name the same body as corporate directors.

## For advisors

- Most "our governance is broken" complaints are roll-hygiene and notice problems, not
  authority-design problems; check those first.
- Cross-walk the stated polity, the bylaws, the denominational book, the property title and actual
  practice in your first memo; the divergences are where the litigation lives.
- Push bylaws fixes in peacetime; amendments adopted during a fight are usually the next lawsuit.
