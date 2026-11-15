---
name: nonprofit-retail-store-operations
description: "Runs resale-store floor procedures: POS and inventory setup, cash handling and daily over/short reconciliation, deposits, loss prevention and shrinkage tracking, and opening/closing checklists. Use for 'our till never balances,' 'set up our POS,' 'design a daily cash reconciliation process,' or 'reduce shrinkage.' Implements org-wide control policy on the floor; not for designing that policy (use nonprofit-financial-controls), pricing (use nonprofit-retail-pricing-merchandising), online sales (use nonprofit-online-resale), or scheduling (use nonprofit-retail-staffing)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Cash handling, reconciliation and loss prevention are financial controls."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Retail Store Operations

## Boundaries

- This skill is the retail-floor procedure layer. Org-wide control policy design (approval thresholds,
  segregation of duties, board-adopted financial policy, audit prep) is `nonprofit-financial-controls`;
  reference, don't redesign, the org's approval-threshold table.
- Pricing strategy and merchandising: `nonprofit-retail-pricing-merchandising`.
- Online marketplace operations: `nonprofit-online-resale`.
- Staffing and scheduling of the people running these procedures: `nonprofit-retail-staffing`.

## Core Framework: The Store Operations Triangle

Every resale store's floor operation rests on three interlocking systems, each with its own named
failure mode if under-built:

1. **POS/inventory system** — the transaction and stock-tracking backbone; weak systems produce
   unreliable sales and shrinkage data that makes every other control (cash reconciliation, loss
   prevention) impossible to verify.
2. **Cash handling and reconciliation** — the daily till-count, deposit, and reconciliation cycle
   that turns register activity into verifiable, bank-matched revenue.
3. **Loss prevention** — the combination of physical, procedural, and data controls that keep
   shrinkage (inventory or cash loss from theft, error, or breakage) within an acceptable, tracked
   range.

A resale store is unusually exposed on all three relative to ordinary retail: donated inventory has
no invoice trail to check receipts against, item-level pricing is often set at the register rather
than pre-ticketed with barcodes, and high volunteer-to-staff ratios raise both training and
accountability challenges. Build procedures assuming these conditions, not a standard retail template.

## Store-Specific Control Defaults

- Track shrink rate monthly as a % of retail sales and investigate any month-over-month jump
  immediately rather than averaging it away.
- Dual-count verification (two people independently count and initial the drawer at open, close, and
  deposit) is the single highest-leverage cash control for a thrift store's small-team reality.
- Set a cap on cash in the working till and sweep the excess to a locked drop safe during the day.

## Step-by-Step: Building Store Operations Procedures

1. **Select or configure a POS/inventory system** that supports category-level (not necessarily full
   SKU-level, given donated-goods volume) sales tracking, discount/markdown-tag entry, and a daily
   close-of-day sales report by category and payment type.
2. **Write opening procedures**: unlock/alarm sequence, till float count-in with dual verification,
   register/terminal power-on and system check, floor walk-through for safety, and a designated
   opener sign-off.
3. **Write closing procedures**: final sale cutoff, till count-out with dual verification against the
   POS close-of-day report, discrepancy documentation on any over/short, deposit prep, alarm/lock
   sequence, and a designated closer sign-off.
4. **Set the daily over/short threshold and escalation path**: define what dollar variance is normal
   register error (e.g., under $5) versus what triggers a manager review and, above a second
   threshold, a report up to whoever owns org-wide financial controls per
   `nonprofit-financial-controls`'s approval structure — this skill executes that org policy at store level rather than
   setting the threshold itself.
5. **Build the deposit and reconciliation cycle**: bank the counted deposit promptly (same or next
   business day), reconcile the bank-deposit slip against the POS close-of-day total, and route any
   variance to a second person for review, never the same person who counted the till.
6. **Design physical and procedural loss-prevention controls**: fitting-room item-count tags, staffed
   or camera-monitored blind spots, a no-cash-in-pockets policy for register staff, mandatory receipt
   for every transaction (also a fraud control — no receipt enables a "no-sale" cash skim), and a
   locked backroom/donation-holding area so unsorted or unpriced inventory isn't accessible to
   shoppers or unsupervised staff.
7. **Track and review shrinkage monthly** by comparing POS-recorded inventory movement against
   physical spot counts in high-value categories (electronics, boutique section); investigate any
   month with a shrink-rate jump before the next inventory cycle, not after.
8. **Run periodic unannounced till audits** and rotate which staff/volunteers are paired for
   dual-count duties, so no single pairing becomes a long-term blind spot.
9. **Document every procedure in a store operations manual** accessible to all shift staff and
   volunteers, and retrain to it whenever a POS system changes or a new loss-prevention control is
   added.

## Opening/Closing Checklist and Over/Short Template

```
OPENING  Date ____  Opener ____  Second counter ____
[ ] Alarm off / unlock sequence        [ ] Floor and exits walked for safety
[ ] Till float counted: $____ (opener) $____ (second)   Both initials ____
[ ] POS/terminals on, prior-day close posted   [ ] Backroom/donation area locked

CLOSING  Date ____  Closer ____  Second counter ____
[ ] Final sale cutoff at ____          [ ] POS close-of-day report printed
[ ] Till counted out with second person; float set aside   [ ] Over/short recorded below
[ ] Deposit bagged, logged, locked in safe   [ ] Backroom locked   [ ] Alarm set / locked
```

| Register | Cashier(s) | Float | POS cash sales | Expected cash | Counted cash | Over/(short) | Above threshold? | Explanation / reviewer |
|----------|------------|-------|----------------|---------------|--------------|--------------|------------------|------------------------|
| 1        |            |       |                |               |              |              |                  |                        |
| 2        |            |       |                |               |              |              |                  |                        |
| Total    |            |       |                |               |              |              |                  |                        |

Expected cash = float + POS cash sales (less any paid-outs with receipts). Thresholds come from the
org's `nonprofit-financial-controls` policy.

## Standard Deliverables

- POS/inventory system configuration checklist
- Opening/closing procedure checklists with sign-off lines
- Daily over/short report template and escalation thresholds
- Deposit reconciliation procedure
- Loss-prevention control checklist (physical + procedural)
- Monthly shrinkage report

## Verify Before Acting

- [ ] Over/short thresholds and escalation path match the board-adopted policy in
      `nonprofit-financial-controls`; none were invented at store level.
- [ ] The person who reconciles the deposit slip to the POS total is not the person who counted the till.
- [ ] Each day's POS close, counted deposit, and bank deposit agree, or the variance is documented.
- [ ] Opening and closing checklists carry two sets of initials for every cash count.
- [ ] Shrink reports compare POS movement to physical spot counts in high-value categories.

## Common Failure Modes

- **Single-person till counts** with no dual verification, removing the only real-time check against
  cash skimming or simple counting error.
- **No receipt required for every sale**, which both frustrates customers on returns and opens a
  "no-sale" register fraud vector.
- **POS system used only for ringing sales, not tracked for shrinkage**, so inventory loss goes
  undetected until a full physical count reveals a large unexplained gap.
- **Deposits delayed or batched irregularly**, making bank reconciliation difficult and creating a
  window where cash sits unsecured on-site.
- **Store-level procedures invented ad hoc instead of tied to the org's approval-threshold policy**,
  creating a gap between what `nonprofit-financial-controls` says should happen and what actually
  happens at the register.
- **Unsorted/unpriced backstock accessible to the sales floor**, enabling both shrinkage and
  inconsistent off-book pricing by whoever reaches it first.
- **Prices set at the register without a published band or price code**, which makes "sweethearting"
  (cashiers undercharging friends or regulars) invisible; require category price codes or pre-tagged
  prices and review POS manual-price and discount overrides.

## For advisors

- Treat the over/short report as a daily habit; same-day review of a variance is far more likely to
  identify a training gap or an actual loss than a variance found weeks later.
- Don't propose new thresholds from scratch; a floor-level fix that contradicts board-adopted policy
  creates an audit finding even if it solves the immediate complaint.
