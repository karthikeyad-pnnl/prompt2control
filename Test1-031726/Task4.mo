within ;
block Task4
  "Chilled water reset request and chiller plant request based on ASHRAE Guideline 36 Section 5.16.16"

  Buildings.Controls.OBC.CDL.Interfaces.RealInput TAirSup(
    final unit="K",
    displayUnit="degC",
    final quantity="ThermodynamicTemperature")
    "Supply air temperature"
    annotation (Placement(transformation(extent={{-220,100},{-180,140}})));

  Buildings.Controls.OBC.CDL.Interfaces.RealInput TAirSupSet(
    final unit="K",
    displayUnit="degC",
    final quantity="ThermodynamicTemperature")
    "Supply air temperature setpoint"
    annotation (Placement(transformation(extent={{-220,40},{-180,80}})));

  Buildings.Controls.OBC.CDL.Interfaces.RealInput uCooCoi(
    final min=0,
    final max=1,
    final unit="1")
    "Chilled water cooling coil valve position"
    annotation (Placement(transformation(extent={{-220,-100},{-180,-60}})));

  Buildings.Controls.OBC.CDL.Interfaces.IntegerOutput yChiWatResReq
    "Chilled water reset request"
    annotation (Placement(transformation(extent={{180,40},{220,80}})));

  Buildings.Controls.OBC.CDL.Interfaces.IntegerOutput yChiPlaReq
    "Chiller plant request"
    annotation (Placement(transformation(extent={{180,-100},{220,-60}})));

protected
  Buildings.Controls.OBC.CDL.Reals.Subtract dTSup
    "Difference: TAirSup - TAirSupSet"
    annotation (Placement(transformation(extent={{-160,100},{-140,120}})));

  Buildings.Controls.OBC.CDL.Reals.GreaterThreshold greThr3(
    t=3,
    h=0.2)
    "Check if supply air temperature exceeds setpoint by 3 degC"
    annotation (Placement(transformation(extent={{-120,130},{-100,150}})));

  Buildings.Controls.OBC.CDL.Reals.GreaterThreshold greThr2(
    t=2,
    h=0.2)
    "Check if supply air temperature exceeds setpoint by 2 degC"
    annotation (Placement(transformation(extent={{-120,70},{-100,90}})));

  Buildings.Controls.OBC.CDL.Logical.TrueDelay truDel3(
    delayTime=120,
    delayOnInit=false)
    "True delay 2 minutes for 3 degC condition"
    annotation (Placement(transformation(extent={{-70,130},{-50,150}})));

  Buildings.Controls.OBC.CDL.Logical.TrueDelay truDel2(
    delayTime=120,
    delayOnInit=false)
    "True delay 2 minutes for 2 degC condition"
    annotation (Placement(transformation(extent={{-70,70},{-50,90}})));

  Buildings.Controls.OBC.CDL.Reals.GreaterThreshold greThrVal95(
    t=0.95,
    h=0.005)
    "Check if cooling coil valve position is greater than 95%"
    annotation (Placement(transformation(extent={{-160,-60},{-140,-40}})));

  Buildings.Controls.OBC.CDL.Reals.LessThreshold lesThrVal85(
    t=0.85,
    h=0.005)
    "Check if cooling coil valve position is less than 85%"
    annotation (Placement(transformation(extent={{-160,-100},{-140,-80}})));

  Buildings.Controls.OBC.CDL.Reals.LessThreshold lesThrVal10(
    t=0.10,
    h=0.005)
    "Check if cooling coil valve position is less than 10%"
    annotation (Placement(transformation(extent={{-160,-150},{-140,-130}})));

  Buildings.Controls.OBC.CDL.Logical.Latch latVal85
    "Latch: set when valve > 95%, reset when valve < 85%"
    annotation (Placement(transformation(extent={{-100,-80},{-80,-60}})));

  Buildings.Controls.OBC.CDL.Logical.Latch latVal10
    "Latch: set when valve > 95%, reset when valve < 10%"
    annotation (Placement(transformation(extent={{-100,-140},{-80,-120}})));

  Buildings.Controls.OBC.CDL.Logical.Not not3
    "Negate 3 degC condition"
    annotation (Placement(transformation(extent={{-30,130},{-10,150}})));

  Buildings.Controls.OBC.CDL.Logical.Not not2
    "Negate 2 degC condition"
    annotation (Placement(transformation(extent={{-30,70},{-10,90}})));

  Buildings.Controls.OBC.CDL.Logical.And and2req
    "2 requests: 2 degC exceeded AND NOT 3 degC exceeded"
    annotation (Placement(transformation(extent={{20,90},{40,110}})));

  Buildings.Controls.OBC.CDL.Logical.And and1reqA
    "Intermediate: latched AND NOT 3 degC"
    annotation (Placement(transformation(extent={{20,20},{40,40}})));

  Buildings.Controls.OBC.CDL.Logical.And and1req
    "1 request: latched AND NOT 3 degC AND NOT 2 degC"
    annotation (Placement(transformation(extent={{60,10},{80,30}})));

  Buildings.Controls.OBC.CDL.Integers.Switch swi3
    "Priority 1: output 3 if truDel3"
    annotation (Placement(transformation(extent={{120,100},{140,120}})));

  Buildings.Controls.OBC.CDL.Integers.Switch swi2
    "Priority 2: output 2 if and2req, else check next"
    annotation (Placement(transformation(extent={{120,60},{140,80}})));

  Buildings.Controls.OBC.CDL.Integers.Switch swi1
    "Priority 3: output 1 if and1req, else 0"
    annotation (Placement(transformation(extent={{90,-40},{110,-20}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant intConst3(
    k=3)
    "Constant integer 3"
    annotation (Placement(transformation(extent={{60,130},{80,150}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant intConst2(
    k=2)
    "Constant integer 2"
    annotation (Placement(transformation(extent={{60,80},{80,100}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant intConst1(
    k=1)
    "Constant integer 1"
    annotation (Placement(transformation(extent={{20,-30},{40,-10}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant intConst0(
    k=0)
    "Constant integer 0"
    annotation (Placement(transformation(extent={{20,-60},{40,-40}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant intConst1Pla(
    k=1)
    "Constant integer 1 for chiller plant request"
    annotation (Placement(transformation(extent={{-40,-110},{-20,-90}})));

  Buildings.Controls.OBC.CDL.Integers.Sources.Constant intConst0Pla(
    k=0)
    "Constant integer 0 for chiller plant request"
    annotation (Placement(transformation(extent={{-40,-150},{-20,-130}})));

  Buildings.Controls.OBC.CDL.Integers.Switch swiPla
    "Chiller plant request switch"
    annotation (Placement(transformation(extent={{60,-130},{80,-110}})));

equation
  connect(TAirSup, dTSup.u1)
    annotation (Line(points={{-200,120},{-170,120},{-170,116},{-162,116}},
      color={0,0,127}));
  connect(TAirSupSet, dTSup.u2)
    annotation (Line(points={{-200,60},{-170,60},{-170,104},{-162,104}},
      color={0,0,127}));
  connect(dTSup.y, greThr3.u)
    annotation (Line(points={{-138,110},{-130,110},{-130,140},{-122,140}},
      color={0,0,127}));
  connect(dTSup.y, greThr2.u)
    annotation (Line(points={{-138,110},{-130,110},{-130,80},{-122,80}},
      color={0,0,127}));
  connect(greThr3.y, truDel3.u)
    annotation (Line(points={{-98,140},{-72,140}},
      color={255,0,255}));
  connect(greThr2.y, truDel2.u)
    annotation (Line(points={{-98,80},{-72,80}},
      color={255,0,255}));
  connect(uCooCoi, greThrVal95.u)
    annotation (Line(points={{-200,-80},{-170,-80},{-170,-50},{-162,-50}},
      color={0,0,127}));
  connect(uCooCoi, lesThrVal85.u)
    annotation (Line(points={{-200,-80},{-170,-80},{-170,-90},{-162,-90}},
      color={0,0,127}));
  connect(uCooCoi, lesThrVal10.u)
    annotation (Line(points={{-200,-80},{-170,-80},{-170,-140},{-162,-140}},
      color={0,0,127}));
  connect(greThrVal95.y, latVal85.u)
    annotation (Line(points={{-138,-50},{-120,-50},{-120,-70},{-102,-70}},
      color={255,0,255}));
  connect(lesThrVal85.y, latVal85.clr)
    annotation (Line(points={{-138,-90},{-116,-90},{-116,-76},{-102,-76}},
      color={255,0,255}));
  connect(greThrVal95.y, latVal10.u)
    annotation (Line(points={{-138,-50},{-120,-50},{-120,-130},{-102,-130}},
      color={255,0,255}));
  connect(lesThrVal10.y, latVal10.clr)
    annotation (Line(points={{-138,-140},{-116,-140},{-116,-136},{-102,-136}},
      color={255,0,255}));
  connect(truDel3.y, not3.u)
    annotation (Line(points={{-48,140},{-32,140}},
      color={255,0,255}));
  connect(truDel2.y, not2.u)
    annotation (Line(points={{-48,80},{-32,80}},
      color={255,0,255}));
  connect(truDel2.y, and2req.u1)
    annotation (Line(points={{-48,80},{-44,80},{-44,100},{18,100}},
      color={255,0,255}));
  connect(not3.y, and2req.u2)
    annotation (Line(points={{-8,140},{0,140},{0,92},{18,92}},
      color={255,0,255}));
  connect(latVal85.y, and1reqA.u1)
    annotation (Line(points={{-78,-70},{-60,-70},{-60,30},{18,30}},
      color={255,0,255}));
  connect(not3.y, and1reqA.u2)
    annotation (Line(points={{-8,140},{0,140},{0,22},{18,22}},
      color={255,0,255}));
  connect(and1reqA.y, and1req.u1)
    annotation (Line(points={{42,30},{50,30},{50,20},{58,20}},
      color={255,0,255}));
  connect(not2.y, and1req.u2)
    annotation (Line(points={{-8,80},{4,80},{4,12},{58,12}},
      color={255,0,255}));
  connect(intConst3.y, swi3.u1)
    annotation (Line(points={{82,140},{100,140},{100,118},{118,118}},
      color={255,127,0}));
  connect(truDel3.y, swi3.u2)
    annotation (Line(points={{-48,140},{-44,140},{-44,160},{110,160},{110,110},{118,110}},
      color={255,0,255}));
  connect(intConst2.y, swi2.u1)
    annotation (Line(points={{82,90},{100,90},{100,78},{118,78}},
      color={255,127,0}));
  connect(and2req.y, swi2.u2)
    annotation (Line(points={{42,100},{108,100},{108,70},{118,70}},
      color={255,0,255}));
  connect(intConst1.y, swi1.u1)
    annotation (Line(points={{42,-20},{80,-20},{80,-22},{88,-22}},
      color={255,127,0}));
  connect(and1req.y, swi1.u2)
    annotation (Line(points={{82,20},{90,20},{90,-14},{76,-14},{76,-30},{88,-30}},
      color={255,0,255}));
  connect(intConst0.y, swi1.u3)
    annotation (Line(points={{42,-50},{80,-50},{80,-38},{88,-38}},
      color={255,127,0}));
  connect(swi1.y, swi2.u3)
    annotation (Line(points={{112,-30},{120,-30},{120,54},{118,54},{118,62}},
      color={255,127,0}));
  connect(swi2.y, swi3.u3)
    annotation (Line(points={{142,70},{150,70},{150,90},{108,90},{108,102},{118,102}},
      color={255,127,0}));
  connect(swi3.y, yChiWatResReq)
    annotation (Line(points={{142,110},{160,110},{160,60},{200,60}},
      color={255,127,0}));
  connect(intConst1Pla.y, swiPla.u1)
    annotation (Line(points={{-18,-100},{40,-100},{40,-112},{58,-112}},
      color={255,127,0}));
  connect(latVal10.y, swiPla.u2)
    annotation (Line(points={{-78,-130},{-60,-130},{-60,-120},{58,-120}},
      color={255,0,255}));
  connect(intConst0Pla.y, swiPla.u3)
    annotation (Line(points={{-18,-140},{40,-140},{40,-128},{58,-128}},
      color={255,127,0}));
  connect(swiPla.y, yChiPlaReq)
    annotation (Line(points={{82,-120},{160,-120},{160,-80},{200,-80}},
      color={255,127,0}));

  annotation (
    defaultComponentName="chiWatReq",
    Icon(coordinateSystem(preserveAspectRatio=false, extent={{-180,-180},{180,180}}),
      graphics={
        Rectangle(
          extent={{-180,180},{180,-180}},
          lineColor={0,0,127},
          fillColor={255,255,255},
          fillPattern=FillPattern.Solid),
        Text(
          extent={{-160,160},{160,120}},
          textColor={0,0,255},
          textString="%name"),
        Text(
          extent={{-160,100},{-60,80}},
          textColor={0,0,127},
          textString="TAirSup"),
        Text(
          extent={{-160,40},{-60,20}},
          textColor={0,0,127},
          textString="TAirSupSet"),
        Text(
          extent={{-160,-60},{-60,-80}},
          textColor={0,0,127},
          textString="uCooCoi"),
        Text(
          extent={{40,80},{160,60}},
          textColor={255,127,0},
          textString="yChiWatResReq"),
        Text(
          extent={{40,-60},{160,-80}},
          textColor={255,127,0},
          textString="yChiPlaReq")}),
    Diagram(coordinateSystem(preserveAspectRatio=false, extent={{-220,-180},{220,180}})),
    Documentation(info="<html>
<p>
This block outputs the chilled water reset request and chiller plant request
based on ASHRAE Guideline 36, Section 5.16.16.
</p>
<h4>Chilled Water Reset Request (yChiWatResReq)</h4>
<ul>
<li>Send 3 requests if TAirSup exceeds TAirSupSet by 3 K for 2 minutes.</li>
<li>Send 2 requests if TAirSup exceeds TAirSupSet by 2 K for 2 minutes (but not 3 K).</li>
<li>Send 1 request if cooling coil valve position is greater than 95%, until it drops below 85%.</li>
<li>Send 0 requests otherwise.</li>
</ul>
<h4>Chiller Plant Request (yChiPlaReq)</h4>
<ul>
<li>Send 1 request if cooling coil valve position is greater than 95%, until it drops below 10%.</li>
<li>Send 0 requests otherwise.</li>
</ul>
</html>"));
end Task4;
