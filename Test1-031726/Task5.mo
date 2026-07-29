within Buildings.Controls.OBC.CDL.Examples;
block Task5
  "Relief damper control for AHUs with actuated dampers without fan"

  parameter Real pBuiSet(
    final unit="Pa",
    final quantity="PressureDifference") = 12
    "Building static pressure difference setpoint";

  parameter Real k(final unit="1") = 1
    "Gain of P-only controller";

  Buildings.Controls.OBC.CDL.Interfaces.RealInput dpBui(
    final unit="Pa",
    final quantity="PressureDifference")
    "Building static pressure difference"
    annotation (Placement(transformation(extent={{-200,40},{-160,80}}),
      iconTransformation(extent={{-140,40},{-100,80}})));

  Buildings.Controls.OBC.CDL.Interfaces.BooleanInput u1SupFan
    "Supply fan proven on signal"
    annotation (Placement(transformation(extent={{-200,-80},{-160,-40}}),
      iconTransformation(extent={{-140,-80},{-100,-40}})));

  Buildings.Controls.OBC.CDL.Interfaces.RealOutput yRelDam(
    final min=0,
    final max=1,
    final unit="1")
    "Relief damper commanded position"
    annotation (Placement(transformation(extent={{160,-20},{200,20}}),
      iconTransformation(extent={{100,-20},{140,20}})));

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant buiPreSet(
    final k=pBuiSet)
    "Building static pressure setpoint"
    annotation (Placement(transformation(extent={{-120,60},{-100,80}})));

  Buildings.Controls.OBC.CDL.Reals.PID relDamCtl(
    controllerType=Buildings.Controls.OBC.CDL.Types.SimpleController.P,
    k=k,
    final yMax=1,
    final yMin=0)
    "P-only controller for relief damper"
    annotation (Placement(transformation(extent={{-40,40},{-20,60}})));

  Buildings.Controls.OBC.CDL.Reals.Switch relDamSwi
    "Switch relief damper position based on fan status"
    annotation (Placement(transformation(extent={{80,-10},{100,10}})));

  Buildings.Controls.OBC.CDL.Reals.Sources.Constant zerDam(
    final k=0)
    "Zero damper position when disabled"
    annotation (Placement(transformation(extent={{-40,-60},{-20,-40}})));

equation
  connect(buiPreSet.y, relDamCtl.u_s)
    annotation (Line(points={{-98,70},{-60,70},{-60,50},{-42,50}},
      color={0,0,127}));

  connect(dpBui, relDamCtl.u_m)
    annotation (Line(points={{-180,60},{-140,60},{-140,20},{-30,20},{-30,38}},
      color={0,0,127}));

  connect(relDamCtl.y, relDamSwi.u1)
    annotation (Line(points={{-18,50},{40,50},{40,8},{78,8}},
      color={0,0,127}));

  connect(u1SupFan, relDamSwi.u2)
    annotation (Line(points={{-180,-60},{40,-60},{40,0},{78,0}},
      color={255,0,255}));

  connect(zerDam.y, relDamSwi.u3)
    annotation (Line(points={{-18,-50},{40,-50},{40,-8},{78,-8}},
      color={0,0,127}));

  connect(relDamSwi.y, yRelDam)
    annotation (Line(points={{102,0},{180,0}},
      color={0,0,127}));

  annotation (
    defaultComponentName="task5",
    Icon(coordinateSystem(preserveAspectRatio=false, extent={{-100,-100},{100,100}}),
      graphics={
        Rectangle(
          extent={{-100,100},{100,-100}},
          lineColor={0,0,0},
          fillColor={255,255,255},
          fillPattern=FillPattern.Solid),
        Text(
          extent={{-96,60},{96,-60}},
          textString="Relief Damper Control",
          textColor={0,0,0}),
        Text(
          extent={{-150,150},{150,110}},
          textString="%name",
          textColor={0,0,255})}),
    Diagram(coordinateSystem(preserveAspectRatio=false, extent={{-160,-100},{160,100}})),
    Documentation(info="<html>
<p>
Relief damper control block for AHUs with actuated dampers without fan.
</p>
<ul>
<li>
Relief dampers are enabled when the associated supply fan is proven on
(u1SupFan = true), and disabled (closed) otherwise.
</li>
<li>
When enabled, a P-only control loop modulates the relief damper to maintain
building static pressure dpBui at its setpoint (default 12 Pa).
</li>
<li>
When disabled, the damper is commanded to fully closed position (0).
</li>
</ul>
</html>"));
end Task5;