within Buildings.Controls.OBC.CDL.Examples;
block Task2
  "Chilled water minimum flow bypass valve controller for primary-only plants"

  parameter Real k(
    final unit="1",
    final min=1e-6) = 1
    "Gain of controller";

  parameter Real Ti(
    final unit="s",
    final min=1e-6) = 120
    "Time constant of integrator block";

  parameter Real Td(
    final unit="s",
    final min=0) = 0.1
    "Time constant of derivative block";

  parameter Real yMax(
    final unit="1",
    final min=0,
    final max=1) = 1
    "Upper limit of PID output";

  parameter Real yMin(
    final unit="1",
    final min=0,
    final max=1) = 0
    "Lower limit of PID output";

  Buildings.Controls.OBC.CDL.Interfaces.RealInput VChiWat_flow(
    final unit="m3/s",
    final quantity="VolumeFlowRate")
    "Measured chilled water flow rate through chillers"
    annotation (Placement(transformation(extent={{-220,40},{-180,80}}),
      iconTransformation(extent={{-140,40},{-100,80}})));

  Buildings.Controls.OBC.CDL.Interfaces.RealInput VChiWatSet_flow(
    final unit="m3/s",
    final quantity="VolumeFlowRate")
    "Minimum chilled water flow setpoint"
    annotation (Placement(transformation(extent={{-220,-20},{-180,20}}),
      iconTransformation(extent={{-140,-20},{-100,20}})));

  Buildings.Controls.OBC.CDL.Interfaces.BooleanInput uChiWatPum
    "Maximum status feedback of all chilled water pumps"
    annotation (Placement(transformation(extent={{-220,-100},{-180,-60}}),
      iconTransformation(extent={{-140,-80},{-100,-40}})));

  Buildings.Controls.OBC.CDL.Interfaces.RealOutput yValPos(
    final min=0,
    final max=1,
    final unit="1")
    "Chilled water minimum flow bypass valve position"
    annotation (Placement(transformation(extent={{180,-20},{220,20}}),
      iconTransformation(extent={{100,-20},{140,20}})));

  Buildings.Controls.OBC.CDL.Reals.PIDWithReset conPID(
    final controllerType=Buildings.Controls.OBC.CDL.Types.SimpleController.PID,
    final k=k,
    final Ti=Ti,
    final Td=Td,
    final yMax=yMax,
    final yMin=yMin,
    final reverseActing=false,
    final y_reset=1)
    "PID controller for bypass valve"
    annotation (Placement(transformation(extent={{20,-10},{40,10}})));

  Buildings.Controls.OBC.CDL.Reals.Switch swiValPos
    "Switch: PID output when pump on, fully open when pump off"
    annotation (Placement(transformation(extent={{120,-10},{140,10}})));

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant fullyOpen(
    final k=1)
    "Fully open valve signal"
    annotation (Placement(transformation(extent={{20,-70},{40,-50}})));

  Buildings.Controls.OBC.CDL.Logical.Edge edgPum
    "Rising edge detector for pump on signal"
    annotation (Placement(transformation(extent={{-80,-130},{-60,-110}})));

equation
  connect(VChiWatSet_flow, conPID.u_s)
    annotation (Line(points={{-200,0},{18,0}},
      color={0,0,127}));

  connect(VChiWat_flow, conPID.u_m)
    annotation (Line(points={{-200,60},{-40,60},{-40,-20},{30,-20},{30,-12}},
      color={0,0,127}));

  connect(uChiWatPum, edgPum.u)
    annotation (Line(points={{-200,-80},{-140,-80},{-140,-120},{-82,-120}},
      color={255,0,255}));

  connect(edgPum.y, conPID.trigger)
    annotation (Line(points={{-58,-120},{24,-120},{24,-12}},
      color={255,0,255}));

  connect(conPID.y, swiValPos.u1)
    annotation (Line(points={{42,0},{80,0},{80,8},{118,8}},
      color={0,0,127}));

  connect(fullyOpen.y, swiValPos.u3)
    annotation (Line(points={{42,-60},{90,-60},{90,-8},{118,-8}},
      color={0,0,127}));

  connect(uChiWatPum, swiValPos.u2)
    annotation (Line(points={{-200,-80},{100,-80},{100,0},{118,0}},
      color={255,0,255}));

  connect(swiValPos.y, yValPos)
    annotation (Line(points={{142,0},{200,0}},
      color={0,0,127}));

  annotation (
    defaultComponentName="chiWatMinFloByp",
    Icon(
      coordinateSystem(preserveAspectRatio=false, extent={{-100,-100},{100,100}}),
      graphics={
        Rectangle(
          extent={{-100,100},{100,-100}},
          lineColor={0,0,0},
          fillColor={255,255,255},
          fillPattern=FillPattern.Solid),
        Text(
          extent={{-96,70},{-36,50}},
          textColor={0,0,0},
          textString="VChiWat_flow"),
        Text(
          extent={{-96,10},{-36,-10}},
          textColor={0,0,0},
          textString="VChiWatSet_flow"),
        Text(
          extent={{-96,-50},{-36,-70}},
          textColor={0,0,0},
          textString="uChiWatPum"),
        Text(
          extent={{36,-10},{96,10}},
          textColor={0,0,0},
          textString="yValPos"),
        Text(
          extent={{-100,140},{100,100}},
          textColor={0,0,255},
          textString="%name")}),
    Diagram(
      coordinateSystem(preserveAspectRatio=false, extent={{-180,-160},{180,120}})),
    Documentation(info="<html>
<p>
This block implements the chilled water minimum flow bypass valve controller
for primary-only plants with a minimum flow bypass valve.
</p>
</html>"));
end Task2;