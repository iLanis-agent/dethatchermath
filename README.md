# Dethatcher Math

Lawn dethatcher honesty. The tines are shorter than the sticker, the
bag is smaller than the print, and the thatch was always thicker than
the Saturday. Dethatcher Math turns the claim, the bite and the bag
into the morning.

Live: https://ilanis-agent.github.io/dethatchermath/

## The three truths

1. **The coverage truth** - the claimed width x the 0.85 overlap norm
   (labeled) is the honest sweep; honest inches against the
   1.5-mile-an-hour walk norm (labeled) is the honest clock: done
   before the grill heats, a working morning, or a second Saturday,
   honestly.
2. **The depth truth** - the claimed bite x 0.7 on the first pass and
   x 0.9 on the second (labeled norms) against the 0.3-inch bite bar:
   one pass through the thatch, two passes through the thatch, or a
   comb-over, honestly.
3. **The bag truth** - square feet x the 0.005-bushels-a-square-foot
   thatch norm (labeled) is the honest pile; the claimed bag x the 0.8
   packing norm (labeled) is the honest hold; pile against hold is the
   fill count: a few trips to the curb, a working rhythm, or a
   wheelbarrow of trips.

Illustrative arithmetic with labeled norms - not a measurement of your
dethatcher, your thatch or your yard. Follow the manual's safety
instructions.

## Files

- `index.html` - landing page
- `app.html` - the three-truth app
- `engine.js` - pure functions (`coveragePlan`, `depthPlan`, `bagPlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
