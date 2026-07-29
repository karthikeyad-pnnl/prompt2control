# Pseudo-Code for Modelica Model: Heat Pump Staging and Mode Control

This pseudo-code provides an overview of the Modelica model's logic and flow. The model controls staging and operation modes for a bank of heat pumps (HPs), supporting 2-pipe and 4-pipe air-source heat pumps (ASHPs) in heating-only, cooling-only, or simultaneous heating-cooling modes. It determines availability, selects staging matrices, computes operation modes, and handles primary pump enables. The logic uses control description language (CDL) blocks for signal processing, with algebraic loops broken via `pre` operators and latches for state management.

Key objectives:
- Detect plant modes (heating/cooling enables) and select appropriate staging matrices.
- Assign integer operation modes (1=heating, 2=cooling, 3=heating-cooling) to each HP, considering 4-pipe specifics.
- Compute availability vectors for 4-pipe HPs in heating/cooling.
- Enable primary pumps for 4-pipe ASHPs when in dual mode.
- Generate staging indices (if no runtime sorting) and output the active staging matrix.

Assumptions in pseudo-code:
- Vectors/matrices are sized by `nHp` (number of HPs), `nSta` (stages), `nEquAlt` (alternate equipment).
- `is_fouPip` is a vector indicating 4-pipe HPs (true/false per HP).
- Modes: Binary `uMod` (true=heating, false=cooling for 2-pipe); extended to integers.
- Parameters like `staEquCooHea` (heating-cooling staging matrix) and `staEquOneMod` (single-mode staging) are pre-defined.

## Parameters (Initialization)
```
parameters:
  have_heaWat: Boolean  // True if plants provide hot water (heating)
  have_chiWat: Boolean  // True if plants provide chilled water (cooling)
  has_sort: Boolean     // True if lead-lag equipment rotates by runtime (affects yIdxSta)
  is_fouPip: Boolean vector[nHp]  // Per-HP: true if 4-pipe ASHP
  nHp: Integer          // Number of heat pumps
  idxEquAlt: Integer vector  // Indices of lead/lag alternate equipment
  staEquCooHea: Real matrix[nSta, nHp]  // Staging matrix for heating-cooling mode
  staEquOneMod: Real matrix[nSta, nHp]  // Staging matrix for heating-only or cooling-only
  nSta: Integer         // Number of stages
  nEquAlt: Integer      // Number of alternate equipment
```

## Inputs
```
inputs:
  u1EnaHea: Boolean      // Heating plant enable
  u1EnaCoo: Boolean      // Cooling plant enable
  uMod: Boolean          // Binary mode for 2-pipe HPs (true=heating, false=cooling)
  u1Hp: Boolean vector[nHp]  // Per-HP enable signals
  u1PumPriHea: Boolean   // Primary pump enable for heating (4-pipe)
  u1PumPriCoo: Boolean   // Primary pump enable for cooling (4-pipe)
```

## Outputs
```
outputs:
  yAvaFouPipHea: Boolean vector[nHp]  // Availability for 4-pipe HPs in heating
  yAvaFouPipCoo: Boolean vector[nHp]  // Availability for 4-pipe HPs in cooling
  y1PumPri: Boolean        // Primary pump enable for 4-pipe ASHP
  yHeaCoo: Boolean         // True if in heating-cooling mode
  yMod: Integer vector[nHp]  // Per-HP operation mode (1=heating, 2=cooling, 3=heating-cooling)
  yIdxSta: Integer vector[nEquAlt]  // Staging indices (direct/reverse if no runtime sort)
  yStaEqu: Real matrix[nSta, nHp]   // Active staging matrix (equipment per stage)
```

## Main Logic Flow

### 1. Detect Heating-Cooling Mode
```
// Compute if both plants are enabled (heating-cooling mode active)
heaCooEnabled = u1EnaHea AND u1EnaCoo  // and2.y
yHeaCoo = heaCooEnabled

// Replicate for vector operations
heaCooVec = replicate(heaCooEnabled, nHp)  // booScaRep.y
heaCooMat = replicateVector(heaCooVec, nSta)  // booVecRep.y (matrix for staging switch)
```

### 2. Select Active Staging Matrix
```
// Switch between matrices based on mode
if heaCooEnabled then
  activeStaging = staEquCooHea  // con.y
else
  activeStaging = staEquOneMod  // con1.y
end if
yStaEqu = switch(activeStaging, heaCooMat, staEquOneMod)  // swi.y (selects con.y if true, else con1.y)
```

### 3. Determine Per-HP Operation Modes (yMod)
```
// Convert binary mode to integer (for 2-pipe: 1=heating, 2=cooling)
modInt = booleanToInteger(uMod)  // booToInt.y (but uMod is binary; heating=true->1, cooling=false->? Logic uses constants)

// Base mode computation
notHeaCoo = NOT(heaCooEnabled)  // not1.y
notHeaCooInt = booleanToInteger(notHeaCoo)  // booToInt2.y
repModInt = replicateVector(modInt, nHp)  // intScaRep.y (vectorized mode)

// For heating-only/cooling-only when not in dual mode
heaOnlyOrCooOnly = multiply(notHeaCooInt, repModInt)  // mulInt1.y (0 if dual mode)

// For dual mode signal
heaCooInt = constantInteger(3)  // conInt.y (heating-cooling=3)
heaCooIntVec = replicate(heaCooInt, nHp)  // intScaRep1.y
dualModeSignal = multiply(booleanToInteger(heaCooEnabled), heaCooIntVec)  // mulInt.y (3 if dual, else 0)

// Combine modes: dual takes precedence, else single mode
combinedMode = add(dualModeSignal, heaOnlyOrCooOnly)  // addInt.y (3 if dual, 1/2 otherwise)

// Switch for 4-pipe HPs (use special logic if 4-pipe)
baseModeVec = replicateScalar(combinedMode, nHp)  // intScaRep.y
if is_fouPip (parameter true for 4-pipe) then
  yMod = baseModeVec  // intSwi.y (u1=base, u2=isFouPip.y, u3= something else? Connections suggest direct for 4-pipe)
else
  // For 2-pipe: use binary converted to 1/2
  yMod = switch(baseModeVec, is_fouPip.y, booleanToIntegerVector(uMod))  // intSwi: selects based on 4-pipe flag
end if
```

### 4. Compute 4-Pipe HP Availability (yAvaFouPipHea, yAvaFouPipCoo)
```
// Delay for algebraic loop breaking (pre operators)
preIsFouPip = pre(is_fouPip.y)  // pre1.y

// Check modes per HP (using yMod)
isHeating = equal(yMod, constantInteger(1))  // intEqu.y (vector: true if mode=1)
isCooling = equal(yMod, constantInteger(2))  // intEqu2.y
isDual = equal(yMod, constantInteger(3))     // intEqu1.y

// OR conditions for availability
heaOrDual = isHeating OR isDual  // or3.y
cooOrDual = isCooling OR isDual  // or4.y

// AND with enables and 4-pipe flag (only for enabled, 4-pipe HPs)
enabledAnd4PipHea = heaOrDual AND u1Hp AND preIsFouPip  // and4.y (pre.y breaks loop)
enabledAnd4PipCoo = cooOrDual AND u1Hp AND preIsFouPip  // and5.y (pre2.y breaks loop)

// Latch logic for 4-pipe state persistence (latches until HP disabled)
fallingEdgeDisable = fallingEdge(u1Hp)  // falEdg.y (true on disable)

// Latch for heating availability (latches if in hea/dual, clears on disable)
latHea = latch(enabledAnd4PipHea, fallingEdgeDisable)  // lat.y
notLatHea = NOT(latHea)  // not2.y
yAvaFouPipCoo = notLatHea AND preIsFouPip  // and7.y (false if latched heating, for cooling avail)

// Similarly for cooling latch
latCoo = latch(enabledAnd4PipCoo, fallingEdgeDisable)  // lat1.y
notLatCoo = NOT(latCoo)  // not3.y
yAvaFouPipHea = notLatCoo AND preIsFouPip  // and6.y (false if latched cooling, for heating avail)

// Heat recovery check (for dual mode, 4-pipe only)
hasHeatRecov = isDual AND is_fouPip  // and8.y
```

### 5. Primary Pump Enable for 4-Pipe ASHP (y1PumPri)
```
// Check if primary pumps are already enabled (OR of inputs)
priPumEnabled = u1PumPriHea OR u1PumPriCoo  // or5.y

// Enable if primary enabled AND heat recovery in dual mode
y1PumPri = priPumEnabled AND hasHeatRecov  // and9.y
```

### 6. Staging Indices (yIdxSta) if No Runtime Sorting
```
// Only if has_sort=false (inferred from components; switches between direct/reverse)
if NOT(has_sort) then
  // Replicate heaCooEnabled for alternate equipment
  heaCooAlt = replicate(heaCooEnabled, nEquAlt)  // booScaRep1.y
  
  // Switch between direct (conInt1.y=1?) and reverse (conInt2.y=2?) orders
  directOrder = constantIntegerVector(1, idxEquAlt)  // conInt1.y replicated?
  reverseOrder = constantIntegerVector(2, idxEquAlt) // conInt2.y
  yIdxSta = switch(reverseOrder, heaCooAlt, directOrder)  // intSwi1.y
else
  // Runtime sorting not implemented here; yIdxSta may be parameter-based
  yIdxSta = idxEquAlt  // Placeholder
end if
```

## Overall Flow Summary
1. **Mode Detection:** AND plant enables to set dual mode (`yHeaCoo`).
2. **Staging Selection:** Switch matrices based on dual mode (`yStaEqu`).
3. **Mode Assignment:** Compute per-HP modes prioritizing dual (3), falling back to single (1/2), with 4-pipe adjustments (`yMod`).
4. **Availability & Latches:** For 4-pipe HPs, latch modes to prevent mode conflicts; output availability vectors (`yAvaFouPipHea/Coo`).
5. **Pump Control:** Enable primary pump if dual mode with heat recovery (`y1PumPri`).
6. **Indices:** Generate staging order if no sorting (`yIdxSta`).

This logic ensures safe operation: 4-pipe HPs avoid simultaneous heating/cooling conflicts via latches, staging adapts to mode, and enables are gated by plant status. Algebraic loops are broken with `pre` for convergence.
```
