// Dethatcher Math engine - lawn dethatcher honesty, labeled norms, honest arithmetic.
(function(root){
"use strict";
var OVERLAP = 0.85; // labeled norm: honest working width after lane overlap
var WALKFT = 132;   // labeled norm: honest walking pace in feet a minute (about 1.5 mph)
var FIRST = 0.7;    // labeled norm: honest first-pass bite share of the claim
var SECOND = 0.9;   // labeled norm: honest second-pass bite share of the claim
var BITEBAR = 0.3;  // labeled norm: inches of bite that count as a real thatch pull
var THATCH = 0.005; // labeled norm: bushels of thatch a square foot
var PACKING = 0.8;  // labeled norm: honest bag fill share of the claim
function r1(x){ return Math.round(x*10)/10; }
function f1(x){ return r1(x).toFixed(1); }

function coveragePlan(claimIn, sqft){
  if (!(claimIn > 0)) return { error: "the claimed inches must be above zero" };
  if (!(sqft > 0)) return { error: "the square feet must be above zero" };
  var honestRaw = claimIn * OVERLAP;
  var rateRaw = honestRaw / 12 * WALKFT;
  var minRaw = sqft / rateRaw;
  var verdict = minRaw <= 25 ? "done before the grill heats" : (minRaw <= 70 ? "a working morning" : "a second Saturday, honestly");
  return { honestIn: r1(honestRaw), minutes: r1(minRaw), verdict: verdict };
}
function renderCoverage(r, claimIn, sqft){
  var minWord = r.minutes === 1 ? "1 minute" : f1(r.minutes) + " minutes";
  return "The " + claimIn + "-inch claim honestly sweeps " + f1(r.honestIn) + " inches after the 0.85 overlap norm; " + sqft + " square feet at the 1.5-mile-an-hour walk norm takes " + minWord + " - " + r.verdict + ".";
}

function depthPlan(claimIn){
  if (!(claimIn > 0)) return { error: "the claimed inches must be above zero" };
  var firstRaw = claimIn * FIRST;
  var secondRaw = claimIn * SECOND;
  var verdict = firstRaw >= BITEBAR ? "one pass through the thatch"
    : (secondRaw >= BITEBAR ? "two passes through the thatch" : "a comb-over, honestly");
  return { firstIn: r1(firstRaw), secondIn: r1(secondRaw), verdict: verdict };
}
function renderDepth(r, claimIn){
  return "The " + claimIn + "-inch claim honestly bites " + f1(r.firstIn) + " inches on the first pass and " + f1(r.secondIn) + " on the second (labeled norms); against the 0.3-inch bite bar, " + r.verdict + ".";
}

function bagPlan(sqft, bagBu){
  if (!(sqft > 0)) return { error: "the square feet must be above zero" };
  if (!(bagBu > 0)) return { error: "the claimed bushels must be above zero" };
  var thatchRaw = sqft * THATCH;
  var holdRaw = bagBu * PACKING;
  var fills = Math.ceil(thatchRaw / holdRaw);
  var verdict = fills <= 4 ? "a few trips to the curb" : (fills <= 10 ? "a working rhythm" : "a wheelbarrow of trips");
  return { bushels: r1(thatchRaw), holds: r1(holdRaw), fills: fills, verdict: verdict };
}
function renderBag(r, sqft, bagBu){
  var fillWord = r.fills === 1 ? "1 fill" : r.fills + " fills";
  return sqft + " square feet at the 0.005-bushels-a-square-foot thatch norm is " + f1(r.bushels) + " bushels; the claimed " + bagBu + "-bushel bag honestly holds " + f1(r.holds) + " after the 0.8 packing norm; " + fillWord + " - " + r.verdict + ".";
}

root.DethatcherMath = { coveragePlan: coveragePlan, renderCoverage: renderCoverage, depthPlan: depthPlan, renderDepth: renderDepth, bagPlan: bagPlan, renderBag: renderBag };
})(typeof window !== "undefined" ? window : globalThis);
