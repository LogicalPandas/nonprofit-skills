---
name: nonprofit-online-resale
description: "Runs online resale of high-value donated items through marketplaces (ShopGoodwill, eBay-style auctions, an own storefront): identifying online-worthy items, sold-comp research, photography, listings with condition disclosure, shipping and online customer service. Use for 'we found a valuable item, should we list it online,' 'list this on ShopGoodwill,' 'set up our eBay auction workflow,' or 'handle online resale shipping.' Not for floor pricing (use nonprofit-retail-pricing-merchandising), intake grading (use nonprofit-donation-intake-grading), or donor tax valuation (use nonprofit-in-kind-gift-acceptance)."
license: MIT
metadata:
  supervision: "unsupervised"
  supervision_note: "Marketplace listings and photos; mistakes are relisted."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Online Resale

## Boundaries

- This skill covers the online marketplace channel only. Items flagged as high-value during triage
  arrive from `nonprofit-donation-intake-grading`.
- Floor-facing pricing and display of everything else: `nonprofit-retail-pricing-merchandising`.
- Register/POS operations and in-store cash handling: `nonprofit-retail-store-operations`.
- Formal donor tax-valuation documentation (Form 8283, qualified appraisal): `nonprofit-in-kind-gift-acceptance`,
  handled in parallel with, not instead of, the listing decision.

## Core Framework: The Online Resale Pipeline

Treat online resale as a distinct operational pipeline parallel to the floor, not an overflow valve:

1. **Identification** — a trained reviewer (not general sort-line staff) flags candidate items during
   or after grading: name-brand/designer goods, vintage or collectible items, complete boxed sets,
   working electronics/tools above a floor-price ceiling, and anything with recognizable resale
   comps online.
2. **Research and comp-pricing** — check completed/sold listings (not just active asking prices) on
   the target marketplace to set a realistic reserve or starting price before listing.
3. **Photography and listing** — produce marketplace-quality photos and a complete, accurate written
   listing (condition disclosure is critical — online buyers can't handle the item before purchase).
4. **Fulfillment** — pick, pack, and ship against the marketplace's required handling-time window.
5. **Customer service and returns** — respond to buyer questions and resolve disputes within the
   marketplace's service-level expectations, since marketplace seller ratings directly affect future
   listing visibility.

## Key Terms

- **Sold comps**: completed/sold listing prices for comparable items on the same platform — the only
  reliable pricing signal for resale goods; active/asking prices overstate achievable value.
- **Condition grade disclosure**: a standardized condition description (New, Like New, Good, Fair, For
  Parts) stated explicitly in every listing — the leading driver of buyer disputes when omitted or
  inflated.
- **Seller rating**: a small number of unresolved disputes can disproportionately suppress visibility,
  so protecting it is an operational priority, not just a customer-service nicety.

## Step-by-Step: Running the Online Resale Channel

1. **Set the identification threshold** with the intake/grading team: a floor-price ceiling above
   which an item is automatically routed to online review (e.g., "anything a grader would price above
   $25 on the floor gets a second look for online potential"), plus named category triggers (designer
   labels, vintage indicators, complete sets, working power tools/electronics).
2. **Build a lightweight research step**: search sold/completed comps on the target platform before
   committing to list; if there's no resale comp history, the item likely belongs on the floor, not
   online.
3. **Standardize photography**: neutral background, multiple angles, close-ups of maker's marks/flaws/
   damage, and a consistent lighting setup — poor photos are the single biggest suppressor of online
   sell-through for otherwise good inventory.
4. **Write listings with full condition disclosure** and accurate measurements/specifications;
   under-disclosure drives returns and dispute rates that hurt the seller rating far more than a
   lower price would have cost in revenue.
5. **Choose listing format deliberately**: fixed-price for items with a well-established comp price,
   auction format (with or without reserve) for genuinely uncertain or collectible-driven value where
   competitive bidding can outperform a guessed fixed price.
6. **Set a shipping and packaging standard** appropriate to category (breakables, electronics, framed
   items) and price it into the listing or shipping charge — absorbing hidden shipping costs
   silently erodes the margin this channel exists to capture.
7. **Fulfill within the platform's handling-time window** every time; build a same-day or next-day
   pack-and-ship routine rather than batching, since missed handling time is a top driver of poor
   seller ratings.
8. **Monitor and respond to buyer messages within the platform's expected response window**, and
   resolve disputes generously enough to protect the seller rating — a disputed sale that damages
   rating typically costs more in future visibility than the item's sale price.
9. **Review a monthly online-channel report**: average sale price vs. floor-price estimate, sell-
   through time, shipping cost as % of sale price, and dispute/return rate — use this to recalibrate
   the identification threshold and photography/listing quality over time.

## Listing Template

```
Title: [Brand/maker] [item type] [model/style] [size/dimensions] [key feature]
Condition grade: [New / Like New / Good / Fair / For Parts]
Flaws: [each flaw, with photo number: e.g., "chip on base rim, photo 6"]
Measurements / specs: [H x W x D, weight; size tag and actual measurements for clothing;
  model number, tested/working status for electronics]
Maker's marks / authenticity: [marks, serials, labels photographed: photo numbers]
Comps used: [3 sold listings: platform, date sold, price]  (internal, not published)
Format: [fixed price $__ / auction start $__, reserve $__]  Reason: [comp strength]
Shipping: [packed weight and box size, carrier/service, handling time __ days, charge $__]
Returns: [policy per platform rules]
Listed by / date: ____
```

## Standard Deliverables

- Online-eligibility identification criteria (threshold + category triggers)
- Listing template with required condition-disclosure fields
- Photography setup guide
- Shipping/packaging standard by category
- Monthly online-channel performance report

## Verify Before Acting

- [ ] Price or reserve is based on at least three sold comps, not asking prices.
- [ ] Every visible flaw in the photos is named in the listing text, and the condition grade matches.
- [ ] Packed weight and box size were measured, not estimated, before setting the shipping charge.
- [ ] The item is not recalled or restricted on the target platform (check the platform's prohibited
      items policy and CPSC recalls).
- [ ] Brand-name or designer items have been checked for authenticity before listing under the brand.

## Common Failure Modes

- **No identification threshold**, so valuable items are missed on the general sort line and sold on
  the floor for a fraction of achievable online value.
- **Pricing from active/asking listings instead of sold comps**, systematically over- or under-pricing
  items.
- **Poor or inconsistent photography**, suppressing buyer interest regardless of item quality.
- **Condition over-stated in listings**, driving returns/disputes that damage the seller rating more
  than accurate disclosure would have cost in sale price.
- **Missed handling-time windows** from batched or irregular fulfillment, degrading marketplace
  visibility over time.
- **Shipping cost absorbed silently**, eroding the margin advantage this channel is supposed to
  capture over floor sale.
- **Listing a suspected counterfeit under the brand name**; marketplaces can remove listings or
  restrict the account. List as "unbranded" or route to the floor when authenticity is unclear.
- **Listing recalled or platform-restricted items** that slipped past intake, which risks takedowns
  and account penalties on top of buyer safety issues.

## For advisors

- Size the channel realistically against available labor: photography, listing-writing, and
  fulfillment are time-intensive per item, so start with a narrow, high-confidence category (e.g., only
  designer clothing or only collectibles) before promising broad online coverage.
