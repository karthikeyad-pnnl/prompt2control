within Buildings.Controls.OBC.CDL.Examples;
block Task1
  "Enable or disable chiller based on chilled water supply temperature"

  parameter Real TDeaBan(
    final unit="K",
    displayUnit="degC",
    final quantity="ThermodynamicTemperature") = 1
    "Dead band to prevent short cycling";

  Buildings.Controls.OBC.CDL.Interfaces.RealInput TChi_CHWST(
    final unit="K",
    displayUnit="degC",
    final quantity="ThermodynamicTemperature")
    "Chilled water supply temperature"
    annotation (Placement(transformation(extent={{-140,40},{-100,80}})));

  Buildings.Controls.OBC.CDL.Interfaces.RealInput TChiSet(
    final unit="K",
    displayUnit="degC",
    final quantity="ThermodynamicTemperature")
    "Set temperature for chilled water leaving chiller"
    annotation (Placement(transformation(extent={{-140,-80},{-100,-40}})));

  Buildings.Controls.OBC.CDL.Interfaces.BooleanOutput y
    "Enable (true) / Disable (false) signal"
    annotation (Placement(transformation(extent={{100,-20},{140,20}})));

  Buildings.Controls.OBC.CDL.Reals.AddParameter addDeaBan(
    final p=TDeaBan)
    "Compute TChiSet + TDeaBan"
    annotation (Placement(transformation(extent={{-60,20},{-40,40}})));

  Buildings.Controls.OBC.CDL.Reals.Greater greEna
    "True when TChi_CHWST > TChiSet + TDeaBan"
    annotation (Placement(transformation(extent={{-10,20},{10,40}})));

  Buildings.Controls.OBC.CDL.Reals.Less lesDis
    "True when TChi_CHWST < TChiSet"
    annotation (Placement(transformation(extent={{-10,-40},{10,-20}})));

  Buildings.Controls.OBC.CDL.Logical.Latch lat
    "Latch: set when enable condition true, reset when disable condition true"
    annotation (Placement(transformation(extent={{60,-10},{80,10}})));

equation
  connect(TChiSet, addDeaBan.u)
    annotation (Line(points={{-120,-60},{-70,-60},{-70,30},{-62,30}},
      color={0,0,127}));
  connect(TChi_CHWST, greEna.u1)
    annotation (Line(points={{-120,60},{-30,60},{-30,36},{-12,36}},
      color={0,0,127}));
  connect(addDeaBan.y, greEna.u2)
    annotation (Line(points={{-38,30},{-20,30},{-20,24},{-12,24}},
      color={0,0,127}));
  connect(TChi_CHWST, lesDis.u1)
    annotation (Line(points={{-120,60},{-30,60},{-30,-24},{-12,-24}},
      color={0,0,127}));
  connect(TChiSet, lesDis.u2)
    annotation (Line(points={{-120,-60},{-30,-60},{-30,-36},{-12,-36}},
      color={0,0,127}));
  connect(greEna.y, lat.u)
    annotation (Line(points={{12,30},{40,30},{40,6},{58,6}},
      color={255,0,255}));
  connect(lesDis.y, lat.clr)
    annotation (Line(points={{12,-30},{40,-30},{40,-6},{58,-6}},
      color={255,0,255}));
  connect(lat.y, y)
    annotation (Line(points={{82,0},{120,0}},
      color={255,0,255}));

  annotation (
    defaultComponentName="chiEna",
    Icon(coordinateSystem(preserveAspectRatio=false, extent={{-100,-100},{100,100}}),
      graphics={
        Rectangle(
          extent={{-100,100},{100,-100}},
          lineColor={0,0,0},
          fillColor={255,255,255},
          fillPattern=FillPattern.Solid),
        Text(
          extent={{-90,90},{90,-90}},
          textColor={0,0,0},
          textString="ChiEnable")}),
    Diagram(coordinateSystem(preserveAspectRatio=false, extent={{-120,-80},{120,80}})),
    Documentation(info="<html>
      <p>
      This block enables or disables a chiller based on the chilled water supply temperature.
      </p>
      <ul>
        <li>Enable when <code>TChi_CHWST &gt; TChiSet + TDeaBan</code></li>
        <li>Disable when <code>TChi_CHWST &lt; TChiSet</code></li>
      </ul>
      </html>"));
end Task1;