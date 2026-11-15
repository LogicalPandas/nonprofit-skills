---
name: nonprofit-donation-intake-grading
description: "Runs donated-goods intake for a thrift or resale operation: accepted-items list, drop-off and pickup logistics, sorting and quality grading, sell/online/salvage/discard triage, and the at-donation receipt. Use for 'set up a donation drop-off process,' 'we have a backlog of unsorted donations,' 'grade incoming donations,' or 'reduce our discard rate.' Not for tax valuation, Form 8283 or high-value gifts (use nonprofit-in-kind-gift-acceptance), shelf pricing (use nonprofit-retail-pricing-merchandising), or online listings (use nonprofit-online-resale)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "At-donation receipts are tax documents for the donor."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Donation Intake & Grading

## Boundaries

- This skill covers the physical intake/sort/grade/triage workflow and the basic at-donation receipt
  (a dated acknowledgment of items received, no value stated).
- Donor-side tax valuation, IRS Form 8283, the $500/$5,000 appraisal thresholds, qualified appraisals,
  and gift acceptance for high-value or unusual in-kind gifts: `nonprofit-in-kind-gift-acceptance`.
- Price and merchandising once an item is released to the floor: `nonprofit-retail-pricing-merchandising`.
- Items routed to online sale: `nonprofit-online-resale`.

## Core Framework: The Intake Funnel

Model intake as a funnel with a named decision at each stage, not an undifferentiated "donations
pile":

1. **Acceptance** — accept or decline at the point of donation (curbside, drop-off door, home
   pickup) against a written accepted/not-accepted items list.
2. **Sort** — split by category (clothing, housewares, furniture, electronics, books/media,
   hazardous/recall) and by initial condition.
3. **Grade** — apply a consistent quality standard within each category.
4. **Triage** — route each graded item to one of four lanes: **Sell-floor**, **Sell-online** (high
   value, handoff to `nonprofit-online-resale`), **Salvage/recycle/textile-recycler or auction-bin
   liquidator**, or **Discard** (landfill, last resort).
5. **Receipt** — issue the donor's at-donation receipt before or at drop-off, regardless of which
   lane the item is later routed to.

Track a **sell-through rate by intake lane** and a **discard rate as % of donation volume by
weight or unit** — these two numbers are the standard health metrics for an intake operation; a
rising discard rate is the earliest signal of an acceptance-policy or donor-communication problem,
not a grading problem.

## Key Terms and Edge Cases

- **Not-accepted items** commonly include mattresses without law tags, cribs pre-2011 standard, CRT
  TVs, upholstered furniture with rips/stains, and recalled items.
- **Default grading tiers**: Premium/Boutique (like-new, name-brand, sets), Standard (sellable, normal
  wear), Value/As-Is (functional but heavily worn, flat low price or by-the-pound), and Reject (routed to
  salvage or discard).
- **Diversion rate**: salvage (textile recyclers, scrap-metal buyers, bulk/auction liquidators) as a %
  of total intake; it demonstrates environmental-mission impact to funders and is often reportable
  separately from retail revenue.
- **Bailment period**: the short window (commonly 24-72 hours) between drop-off and formal
  acceptance during which title has not yet transferred, used in some donation agreements to allow a
  final accept/decline decision after inspection — check state law and the org's own gift acceptance
  policy before relying on a bailment clause.

## Step-by-Step: Building or Fixing an Intake Operation

1. **Publish a written accepted/not-accepted items list** and post it at every drop-off point, on the
   website, and with any pickup-scheduling tool — vague guidance ("bring your gently used items") is
   the single biggest driver of high discard rates and volunteer burnout from unusable donations.
2. **Design the drop-off/pickup logistics.** For staffed drop-off: define hours, a covered
   unloading area, and a "no unattended drop after hours" policy if illegal dumping at the donation
   shed is a problem. For scheduled home pickup: set a routing/scheduling cadence (e.g., weekly by
   zone), a minimum-item threshold to justify a truck stop, and a pre-pickup phone/text screen
   against the accepted-items list to avoid wasted trips.
3. **Set up the sort station** physically separate from the sales floor, with labeled bins per
   category and a clear "reject" bin visible to sorters so declines are consistent, not ad hoc.
4. **Write and train to a grading rubric** with photos of each tier per category (this is worth
   building as a real one-page laminated reference per category — clothing, housewares, electronics —
   since grading disagreement between volunteers/staff is the most common intake quality complaint).
5. **Test electronics and anything with a plug or battery** before grading it sellable; never place
   untested electrical items on the floor — this is both a safety and a return-rate issue.
6. **Route high-value or collectible-looking items to a designated reviewer** (not the general sort
   line) for a decision between sell-floor, online listing (`nonprofit-online-resale`), or referral
   to `nonprofit-in-kind-gift-acceptance` if the item may need formal tax documentation.
7. **Issue the at-donation receipt at the point of drop-off**: dated, lists the organization's name
   and EIN, a general description of item categories (not a per-item value — the donor is
   responsible for valuing their own non-cash gift for tax purposes), and a standard statement that
   no goods or services were provided in exchange. Do not let receipt issuance become a bottleneck
   that discourages donors from completing drop-off.
8. **Track discard rate and diversion rate monthly** and review with the intake team; if discard rate
   rises, the fix is almost always to the accepted-items list or donor communication, not to
   re-training graders.
9. **Reconcile intake volume against any hauling/disposal cost** — discard and salvage streams often
   carry a real cost (tip fees, recycler pickup fees); an intake operation that doesn't track this
   cost will understate the true cost of donation processing in the business model.

## At-Donation Receipt Template

```
[Organization legal name]   EIN: [XX-XXXXXXX]
[Store / drop-off location]   Date received: [MM/DD/YYYY]

Items received (general description, no values):
[ ] Clothing/shoes  [ ] Housewares  [ ] Furniture  [ ] Electronics
[ ] Books/media     [ ] Other: ____________   Approx. bags/boxes/items: ____

No goods or services were provided in exchange for this donation.
[Organization] does not assign a value to donated items; the donor is responsible
for determining fair market value for tax purposes. Items over $500 or $5,000 in
claimed value may require additional IRS forms (ask staff for gift acceptance contact).

Received by (staff/volunteer initials): ____
```

## Worked Example: Clothing Grading Rubric (one category)

| Tier | Criteria | Lane |
|------|----------|------|
| Premium/Boutique | Like-new or with tags; name brand or designer; no stains, holes, pilling | Boutique rack or online review |
| Standard | Clean, all buttons/zippers work, light normal wear | Sell-floor, standard price band |
| Value/As-Is | Wearable but faded, minor pilling, out-of-season overflow | Value rack or by-the-pound |
| Reject | Stains, odors, tears, mildew, missing parts | Textile recycler (salvage); discard only if wet or contaminated |

Pair each tier with 2-3 photos on the laminated station card.

## Standard Deliverables

- Written accepted/not-accepted items list (public-facing)
- Drop-off and pickup logistics plan (hours, routing cadence, minimum thresholds)
- Category grading rubric with tier photos
- Intake triage flowchart (sell-floor / sell-online / salvage / discard)
- At-donation receipt template
- Monthly intake dashboard: volume, discard rate, diversion rate, sell-through by lane

## Verify Before Acting

- [ ] The receipt template shows the organization's name, EIN and date, describes items by category
      only, states no value, and includes the no-goods-or-services statement.
- [ ] Receipt wording on appraisal thresholds and Form 8283 matches `nonprofit-in-kind-gift-acceptance`;
      verify current IRS thresholds in IRS Publication 526 and Publication 561 before printing.
- [ ] The accepted/not-accepted list matches current recall and product-safety rules (check CPSC
      recalls) and any state mattress or electronics rules.
- [ ] Discard and diversion rates are computed on the same basis (weight or unit) month to month, and
      tip/recycler fees are included in donation-processing cost.
- [ ] Any bailment clause has been checked against state law and the gift acceptance policy.

## Common Failure Modes

- **Vague accepted-items list** leading to high discard rates and volunteer time spent triaging junk.
- **No separation between sort station and sales floor**, so ungraded, untested, or unsafe items
  reach customers.
- **Untested electronics placed on the floor**, creating safety complaints and refund/return churn.
- **High-value items sorted into the general line** instead of routed to a designated reviewer, losing
  revenue that online resale or a proper in-kind gift process would have captured.
- **Receipt issuance skipped or delayed**, generating donor complaints at tax time and eroding repeat
  donation behavior.
- **Discard cost untracked**, making the true cost of running the donation program invisible to
  leadership and the board.
- **Relying on a bailment clause the donor never saw** (not posted at drop-off or not in the donation
  agreement) to refuse items after the donor has left, which leaves the org holding unwanted goods
  with no clear right to decline.
- **Writing a value on the receipt** at the donor's request, turning a donor's own valuation into an
  apparent organizational appraisal.

## For advisors

- Diagnose intake problems by looking at the discard-rate trend line first, before touching staffing
  or pricing; fixing pricing or staffing without fixing an upstream acceptance-policy gap won't move
  the number.
