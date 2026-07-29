| name           | className                                                  | comment                                                                                   | type      |
|:---------------|:-----------------------------------------------------------|:------------------------------------------------------------------------------------------|:----------|
| conStaDouMod   | Buildings.Controls.OBC.CDL.Reals.Sources.Constant          | Staging matrix for heating-cooling mode                                                   | internal  |
| conStaSinMod   | Buildings.Controls.OBC.CDL.Reals.Sources.Constant          | Staging matrix for heating-only and cooling-only mode                                     | internal  |
| swi            | Buildings.Controls.OBC.CDL.Reals.Switch                    | Switch between staging matrices for heating-cooling mode, and the staging                 | internal  |
|                |                                                            |     matrix for other modes                                                                |           |
| and2           | Buildings.Controls.OBC.CDL.Logical.And                     | Check if both heating plant and cooling plant are enabled                                 | internal  |
| booScaRep      | Buildings.Controls.OBC.CDL.Routing.BooleanScalarReplicator | Generate vector with size equal to number of heat pumps                                   | internal  |
| booVecRep      | Buildings.Controls.OBC.CDL.Routing.BooleanVectorReplicator | Change into matrix with same dimensions as staging matrix                                 | internal  |
| booToInt       | Buildings.Controls.OBC.CDL.Conversions.BooleanToInteger    | Convert binary mode signal to Integer mode signals                                        | internal  |
| intSwi         | Buildings.Controls.OBC.CDL.Integers.Switch                 | Output mode for 2-pipe and SHC HPs                                                        | internal  |
| isHpShc        | Buildings.Controls.OBC.CDL.Logical.Sources.Constant        | Is the heat pump an SHC HP?                                                               | internal  |
| booToInt1      | Buildings.Controls.OBC.CDL.Conversions.BooleanToInteger    | Output Integer signal 1 when both heating plant and cooling plant are enabled             | internal  |
| mulInt         | Buildings.Controls.OBC.CDL.Integers.Multiply               | Output mode signal only when heating-cooling mode is enabled                              | internal  |
| conInt         | Buildings.Controls.OBC.CDL.Integers.Sources.Constant       | Constant Integer signal representing heating-cooling mode                                 | internal  |
| not1           | Buildings.Controls.OBC.CDL.Logical.Not                     | Check if not in heating-cooling mode                                                      | internal  |
| booToInt2      | Buildings.Controls.OBC.CDL.Conversions.BooleanToInteger    | Output Integer 1 when not in heating-cooling mode                                         | internal  |
| mulInt1        | Buildings.Controls.OBC.CDL.Integers.Multiply               | Output heating-only mode signal or cooling-only mode signal when not                      | internal  |
|                |                                                            |     in heating-cooling mode                                                               |           |
| addInt         | Buildings.Controls.OBC.CDL.Integers.Add                    | Output non-zero mode signal                                                               | internal  |
| intScaRep      | Buildings.Controls.OBC.CDL.Routing.IntegerScalarReplicator | Vectorize mode signal with dimension equal to number of heat pumps                        | internal  |
| intSwi1        | Buildings.Controls.OBC.CDL.Integers.Switch                 | Switch between two staging orders when runtime sorting is not used                        | internal  |
| conIntDir      | Buildings.Controls.OBC.CDL.Integers.Sources.Constant       | Sort components in direct order when runtime sorting is not used                          | internal  |
| conIntRev      | Buildings.Controls.OBC.CDL.Integers.Sources.Constant       | Sort components in reverse order when runtime sorting is not used                         | internal  |
| booScaRep1     | Buildings.Controls.OBC.CDL.Routing.BooleanScalarReplicator | Generate vector with size equal to list of lead-lag equipment                             | internal  |
| heaModSig      | Buildings.Controls.OBC.CDL.Logical.Sources.Constant        | Constant heating mode signal                                                              | internal  |
| cooModSig      | Buildings.Controls.OBC.CDL.Logical.Sources.Constant        | Constant cooling mode signal                                                              | internal  |
| intEqu1        | Buildings.Controls.OBC.CDL.Integers.Equal                  | Check for HPs in heating-cooling mode                                                     | internal  |
| and8           | Buildings.Controls.OBC.CDL.Logical.And                     | Identify heat recovery heat pumps in heating-cooling mode                                 | internal  |
| or5            | Buildings.Controls.OBC.CDL.Logical.Or                      | Check for primary heat pumps already enabled                                              | internal  |
| and9           | Buildings.Controls.OBC.CDL.Logical.And                     | Check if primary pump for 4 pipe ASHP is enabled                                          | internal  |
| intScaRep1     | Buildings.Controls.OBC.CDL.Routing.IntegerScalarReplicator | Vectorize mode signal with dimension equal to number of heat pumps                        | internal  |
| and10          | Buildings.Controls.OBC.CDL.Logical.And                     | Extract availability signal for SHC HP                                                    | internal  |
| have_heaWat    | Boolean                                                    | Set to true for plants that provide HW                                                    | parameter |
| have_chiWat    | Boolean                                                    | Set to true for plants that provide CHW                                                   | parameter |
| have_sorRunTim | Boolean                                                    | Are the lead-lag equipment rotated based on runtime?                                      | parameter |
| is_HpShc       | Boolean                                                    | Vector indicating if each HP is an SHC HP; True=Is SHC HP;False=Not SHC HP                | parameter |
| nHp            | Integer                                                    | Number of heat pumps                                                                      | parameter |
| idxEquAlt      | Integer                                                    | Indices of lead-lag alternate equipment                                                   | parameter |
| staEquDouMod   | Real                                                       | Staging matrix for heating-cooling mode – Equipment required for each stage               | parameter |
| staEquSinMod   | Real                                                       | Staging matrix for heating-only and cooling-only mode – Equipment required for each stage | parameter |
| nSta           | Integer                                                    | Number of stages                                                                          | parameter |
| nEquAlt        | Integer                                                    | Number of lead-lag alternate equipment                                                    | parameter |
| u1EnaHea       | Buildings.Controls.OBC.CDL.Interfaces.BooleanInput         | Heating plant enable                                                                      | interface |
| u1EnaCoo       | Buildings.Controls.OBC.CDL.Interfaces.BooleanInput         | Cooling plant enable                                                                      | interface |
| uMod           | Buildings.Controls.OBC.CDL.Interfaces.BooleanInput         | Binary mode signal indicating if 2-pipe HP is in heating mode or cooling mode             | interface |
| u1HpAva        | Buildings.Controls.OBC.CDL.Interfaces.BooleanInput         | HP availability signal vector                                                             | interface |
| u1PumPriHea    | Buildings.Controls.OBC.CDL.Interfaces.BooleanInput         | Primary pump enable for SHC HP heating loop                                               | interface |
| u1PumPriCoo    | Buildings.Controls.OBC.CDL.Interfaces.BooleanInput         | Primary pump enable for SHC HP cooling loop                                               | interface |
| yAvaHpShcHea   | Buildings.Controls.OBC.CDL.Interfaces.BooleanOutput        | Availability vector of SHC HPs for heating operation                                      | interface |
| yAvaHpShcCoo   | Buildings.Controls.OBC.CDL.Interfaces.BooleanOutput        | Availability vector of SHC HPs for cooling operation                                      | interface |
| y1PumPri       | Buildings.Controls.OBC.CDL.Interfaces.BooleanOutput        | Primary pump enable for SHC HP                                                            | interface |
| yHeaCoo        | Buildings.Controls.OBC.CDL.Interfaces.BooleanOutput        | Signal indicating heat pump plant is in heating-cooling mode                              | interface |
| yMod           | Buildings.Controls.OBC.CDL.Interfaces.IntegerOutput        | Operation mode integer signal for each HP                                                 | interface |
| yIdxSta        | Buildings.Controls.OBC.CDL.Interfaces.IntegerOutput        | Staging index if runtime sorting is absent                                                | interface |
| yStaEqu        | Buildings.Controls.OBC.CDL.Interfaces.RealOutput           | Staging matrix – Equipment required for each stage                                        | interface |