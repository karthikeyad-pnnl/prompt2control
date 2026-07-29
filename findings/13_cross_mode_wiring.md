## Step 13 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/HybridAirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo
- Key observations:
  - `or1`, `andHeaEna`, and `notCooMod` are all declared as arrays of size `nHpTot` with no conditional guard on the declaration.
  - The controller wiring for the target pins is direct, not loop-based:
    - `connect(avaEquHeaCoo.y1Coo, or1.u1)`
    - `connect(ctlPlaHyb.yAvaHpShcCoo, or1.u2)`
    - `connect(booScaRep.y, or1.u2)`
    - `connect(y1HpPre.y, andHeaEna.u1)`
    - `connect(y1HeaPre.y, andHeaEna.u2)`
    - `connect(y1HeaPre.y, notCooMod.u)`
  - There are no `for` loops or `if` guards around these connect statements.
  - The only obvious duplicate-connection candidate is `or1.u2`, which receives two separate `connect()` statements and therefore deserves review as a potential over-connection source.
  - Under the failing full model configuration, the controller-side pins are present and connected; the heating-only diagnostic is what localizes `or1[1..3].u1`, `andHeaEna[1..3].u2`, and `notCooMod[1..3].u` as unconnected.
- Hypotheses generated/refuted:
  - Refuted: the target pins are controlled by a loop-range mismatch or a guard on the `connect()` itself.
  - Refuted: there is an obvious subset-iteration bug in the target-pin wiring.
  - Generated: the duplicated `or1.u2` connection may be part of the symbolic over-constraint, but it is not the same thing as the localized unconnected-input defect.
  - Generated: the heating-only localization is more consistent with a mode-configuration dependency upstream of the controller pins than with a missing connect inside this slice.
- Artifacts produced: controller wiring table draft; targeted connect/decl extracts from the controller file

| Target pin | Source | Loop / index | Guard | Active when have_chiWat=true | Active when have_chiWat=false | Active when have_heaWat=false |
|---|---|---|---|---|---|---|
| or1[i].u1 | `avaEquHeaCoo.y1Coo` | direct connect, no loop | none | connected | localized as unconnected in the CHW-disabled probe | n/a because the probe is blocked |
| or1[i].u2 | `ctlPlaHyb.yAvaHpShcCoo` and `booScaRep.y` | direct connect, no loop | none | over-connected candidate because two sources target the same pin array | over-connected candidate, if the same structure is preserved | n/a because the probe is blocked |
| andHeaEna[i].u2 | `y1HeaPre.y` | direct connect, no loop | none | connected | localized as unconnected in the CHW-disabled probe | n/a because the probe is blocked |
| notCooMod[i].u | `y1HeaPre.y` | direct connect, no loop | none | connected | localized as unconnected in the CHW-disabled probe | n/a because the probe is blocked |

## Step 13 Addendum
- Each of the 9 localized inputs behaves uniformly across the array dimension; the diagnostics point to a controller-wide mode split rather than one bad index.
- The only over-connection candidate visible in this slice is `or1.u2`.