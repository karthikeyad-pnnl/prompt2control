within Buildings.Controls.OBC.CDL.Examples;
block Task3
  "Cooling tower fan speed control for different cooling modes"

  parameter Real k(final unit="1") = 1
    "Gain of PID controller";
  parameter Real Ti(final unit="s") = 60
    "Time constant of integrator block";
  parameter Real Td(final unit="s") = 0
    "Time constant of derivative block";

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant TCWSupSet(
    k=273.15 + 29)
    "Condenser water supply temperature setpoint"
    annotation (Placement(transformation(extent={{-180,100},{-160,120}})));

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant TCWSup(
    k=273.15 + 31)
    "Condenser water supply temperature measurement"
    annotation (Placement(transformation(extent={{-180,60},{-160,80}})));

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant TCHWSupSet(
    k=273.15 + 7)
    "Chilled water supply temperature setpoint"
    annotation (Placement(transformation(extent={{-180,-60},{-160,-40}})));

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant TCHWSup(
    k=273.15 + 9)
    "Chilled water supply temperature measurement"
    annotation (Placement(transformation(extent={{-180,-100},{-160,-80}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant cooMod(
    k=2)
    "Cooling mode: 0=Free Cooling, 1=PMC, 2=FMC"
    annotation (Placement(transformation(extent={{-180,-160},{-160,-140}})));

  Buildings.Controls.OBC.CDL.Reals.PID pidFMC(
    controllerType=Buildings.Controls.OBC.CDL.Types.SimpleController.PI,
    k=k,
    Ti=Ti,
    Td=Td,
    reverseActing=false)
    "PID controller for FMC mode: control CWST"
    annotation (Placement(transformation(extent={{-60,100},{-40,120}})));

  Buildings.Controls.OBC.CDL.Reals.PID pidFC(
    controllerType=Buildings.Controls.OBC.CDL.Types.SimpleController.PI,
    k=k,
    Ti=Ti,
    Td=Td,
    reverseActing=false)
    "PID controller for FC mode: control CHWST"
    annotation (Placement(transformation(extent={{-60,-60},{-40,-40}})));

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant one(
    k=1.0)
    "Constant 1.0 for PMC mode"
    annotation (Placement(transformation(extent={{-60,20},{-40,40}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant modFMC(
    k=2)
    "Fully Mechanical Cooling mode index"
    annotation (Placement(transformation(extent={{-140,-130},{-120,-110}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant modPMC(
    k=1)
    "Partially Mechanical Cooling mode index"
    annotation (Placement(transformation(extent={{-140,-170},{-120,-150}})));

  Buildings.Controls.OBC.CDL.Integers.Equal isFMC
    "Check if cooling mode is FMC"
    annotation (Placement(transformation(extent={{-80,-130},{-60,-110}})));

  Buildings.Controls.OBC.CDL.Integers.Equal isPMC
    "Check if cooling mode is PMC"
    annotation (Placement(transformation(extent={{-80,-170},{-60,-150}})));

  Buildings.Controls.OBC.CDL.Reals.Switch swiPMC
    "Switch for PMC mode"
    annotation (Placement(transformation(extent={{40,0},{60,20}})));

  Buildings.Controls.OBC.CDL.Reals.Switch swiFMC
    "Switch for FMC mode"
    annotation (Placement(transformation(extent={{100,-20},{120,0}})));

  Buildings.Controls.OBC.CDL.Interfaces.RealOutput y(
    final min=0,
    final max=1,
    final unit="1")
    "Cooling tower fan speed signal"
    annotation (Placement(transformation(extent={{160,-20},{200,20}})));

equation
  connect(TCWSupSet.y, pidFMC.u_s)
    annotation (Line(points={{-158,110},{-62,110}},
      color={0,0,127}));
  connect(TCWSup.y, pidFMC.u_m)
    annotation (Line(points={{-158,70},{-50,70},{-50,98}},
      color={0,0,127}));
  connect(TCHWSupSet.y, pidFC.u_s)
    annotation (Line(points={{-158,-50},{-62,-50}},
      color={0,0,127}));
  connect(TCHWSup.y, pidFC.u_m)
    annotation (Line(points={{-158,-90},{-50,-90},{-50,-62}},
      color={0,0,127}));
  connect(cooMod.y, isFMC.u1)
    annotation (Line(points={{-158,-150},{-110,-150},{-110,-120},{-82,-120}},
      color={255,127,0}));
  connect(modFMC.y, isFMC.u2)
    annotation (Line(points={{-118,-120},{-100,-120},{-100,-128},{-82,-128}},
      color={255,127,0}));
  connect(cooMod.y, isPMC.u1)
    annotation (Line(points={{-158,-150},{-110,-150},{-110,-160},{-82,-160}},
      color={255,127,0}));
  connect(modPMC.y, isPMC.u2)
    annotation (Line(points={{-118,-160},{-100,-160},{-100,-168},{-82,-168}},
      color={255,127,0}));
  connect(one.y, swiPMC.u1)
    annotation (Line(points={{-38,30},{20,30},{20,18},{38,18}},
      color={0,0,127}));
  connect(pidFC.y, swiPMC.u3)
    annotation (Line(points={{-38,-50},{20,-50},{20,2},{38,2}},
      color={0,0,127}));
  connect(isPMC.y, swiPMC.u2)
    annotation (Line(points={{-58,-160},{10,-160},{10,10},{38,10}},
      color={255,0,255}));
  connect(pidFMC.y, swiFMC.u1)
    annotation (Line(points={{-38,110},{80,110},{80,-2},{98,-2}},
      color={0,0,127}));
  connect(swiPMC.y, swiFMC.u3)
    annotation (Line(points={{62,10},{80,10},{80,-18},{98,-18}},
      color={0,0,127}));
  connect(isFMC.y, swiFMC.u2)
    annotation (Line(points={{-58,-120},{90,-120},{90,-10},{98,-10}},
      color={255,0,255}));
  connect(swiFMC.y, y)
    annotation (Line(points={{122,-10},{140,-10},{140,0},{180,0}},
      color={0,0,127}));

  annotation (
    defaultComponentName="cooTowSpe",
    experiment(StopTime=3600),
    Icon(coordinateSystem(preserveAspectRatio=false,
      extent={{-160,-200},{160,200}}),
      graphics={
        Rectangle(
          extent={{-160,200},{160,-200}},
          lineColor={0,0,0},
          fillColor={255,255,255},
          fillPattern=FillPattern.Solid),
        Text(
          extent={{-150,250},{150,210}},
          textString="%name",
          textColor={0,0,255}),
        Text(
          extent={{-100,140},{100,100}},
          textString="CT Speed",
          textColor={0,0,0})}),
    Diagram(coordinateSystem(preserveAspectRatio=false,
      extent={{-200,-200},{200,200}})),
    Documentation(info="<html>
<p>
This block implements cooling tower fan speed control for three cooling modes:
</p>
<ul>
<li>Free Cooling (FC, cooMod=0): PID control to maintain CHWST at setpoint.</li>
<li>Partially Mechanical Cooling (PMC, cooMod=1): Fan speed set to 100%.</li>
<li>Fully Mechanical Cooling (FMC, cooMod=2): PID control to maintain CWST at setpoint.</li>
</ul>
</html>"));
end Task3;