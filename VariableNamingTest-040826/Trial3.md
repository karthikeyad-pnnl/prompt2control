# Variable Name Analysis

| Variable Name              | Issue Identified                                                                 | Suggested Correction                  |
|----------------------------|----------------------------------------------------------------------------------|---------------------------------------|
| has_sort                   | Non-standard prefix 'has_' instead of 'have_' for boolean parameters indicating presence (Rule 5.1). | have_sor                              |
| is_priOnl                  | Non-standard prefix 'is_' not defined in conventions (Rule 5.1); should use 'have_' for presence indicators. | have_priOnl                           |
| is_fouPip                  | Non-standard prefix 'is_' not defined; for vector indicating state, use descriptive name without undefined prefix or standardize to 'have_' if applicable. Does not accurately represent comment as a vector state. | fouPipSta (or have_fouPipVec for vector) |
| THeaWatSupSet_min          | Incorrect suffix '_min' (underscore + abbreviated); value qualifiers like 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | THeaWatSupSetMin                      |
| VHeaWatHp_flow_min         | Incorrect suffix '_min' and wrong position; 'Min' should precede '_flow' in ordering, CamelCase without underscore (Rule 6.1, 6.3). | VHeaWatHpMin_flow                     |
| dpHeaWatRemSet_max         | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | dpHeaWatRemSetMax                     |
| dpHeaWatRemSet_min         | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | dpHeaWatRemSetMin                     |
| yPumHeaWatPriSet           | Inappropriate 'y' prefix for a parameter (not a control output signal); 'y' is for output signals (Rule 4.1, 2.1.1). | pumHeaWatPriSet                       |
| TChiWatSupSet_max          | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | TChiWatSupSetMax                      |
| VChiWatHp_flow_min         | Incorrect suffix '_min' and wrong position; 'Min' should precede '_flow', CamelCase without underscore (Rule 6.1, 6.3). | VChiWatHpMin_flow                     |
| dpChiWatRemSet_max         | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | dpChiWatRemSetMax                     |
| dpChiWatRemSet_min         | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | dpChiWatRemSetMin                     |
| yPumChiWatPriSet           | Inappropriate 'y' prefix for a parameter (not a control output signal); 'y' is for output signals (Rule 4.1, 2.1.1). | pumChiWatPriSet                       |
| resDpHeaWat_max            | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | resDpHeaWatMax                        |
| resTHeaWatSup_min          | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | resTHeaWatSupMin                      |
| resDpChiWat_max            | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | resDpChiWatMax                        |
| resTChiWatSup_min          | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | resTChiWatSupMin                      |
| res_init                   | Non-standard suffix '_init'; if value qualifier, use CamelCase 'Ini' without underscore; full word 'init' may be acceptable per Rule 2.2.3 but inconsistent with conventions (Rule 6.1). | resIni                                |
| res_min                    | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | resMin                                |
| res_max                    | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | resMax                                |
| rspHeaWat_max              | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | rspHeaWatMax                          |
| rspChiWat_max              | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | rspChiWatMax                          |
| yPumHeaWatPri_min          | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). Inappropriate 'y' prefix for parameter. | pumHeaWatPriMin                       |
| yPumChiWatPri_min          | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). Inappropriate 'y' prefix for parameter. | pumChiWatPriMin                       |
| yPumHeaWatSec_min          | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). Inappropriate 'y' prefix for parameter. | pumHeaWatSecMin                       |
| yPumChiWatSec_min          | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). Inappropriate 'y' prefix for parameter. | pumChiWatSecMin                       |
| TChiWatSupHrc_min          | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | TChiWatSupHrcMin                      |
| THeaWatSupHrc_max          | Incorrect suffix '_max'; 'Max' must be CamelCase without underscore (Rule 6.1, 6.2). | THeaWatSupHrcMax                      |
| capCooHrc_min              | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | capCooHrcMin                          |
| capHeaHrc_min              | Incorrect suffix '_min'; 'Min' must be CamelCase without underscore (Rule 6.1, 6.2). | capHeaHrcMin                          |
| u1PumHeaWatPri_actual      | Non-standard 'u1' prefix (should be 'u' for input; numbering not specified in Rule 4); suffix '_actual' should be abbreviated CamelCase 'Act' without underscore (Rule 2.2.1, 6.1). | uPumHeaWatPriAct                      |
| u1PumChiWatPri_actual      | Non-standard 'u1' prefix; suffix '_actual' incorrect (Rule 4, 6.1).              | uPumChiWatPriAct                      |
| u1PumHeaWatSec_actual      | Non-standard 'u1' prefix; suffix '_actual' incorrect (Rule 4, 6.1).              | uPumHeaWatSecAct                      |
| u1PumChiWatSec_actual      | Non-standard 'u1' prefix; suffix '_actual' incorrect (Rule 4, 6.1).              | uPumChiWatSecAct                      |
| u1Hp_actual                | Non-standard 'u1' prefix; suffix '_actual' incorrect (Rule 4, 6.1).              | uHpAct                                |
| u1Hrc_actual               | Non-standard 'u1' prefix; suffix '_actual' incorrect (Rule 4, 6.1).              | uHrcAct                               |
| TChiWatPriSup              | Name uses 'Sup' (supply) but comment describes "return temperature"; does not accurately represent comment information. | TChiWatPriRet (but duplicate; correct comment to "supply") |
| TChiWatSecSup              | Name uses 'Sup' (supply) but comment describes "return temperature"; does not accurately represent comment information. | TChiWatSecRet (but duplicate; correct comment to "supply") |