# Variables

| name   | className                                           | comment                             | type      |
|:-------|:----------------------------------------------------|:------------------------------------|:----------|
| nout   | Integer                                             | Number of outputs                   | parameter |
| u      | Buildings.Controls.OBC.CDL.Interfaces.BooleanInput  | Input signal to be replicated       | interface |
| y      | Buildings.Controls.OBC.CDL.Interfaces.BooleanOutput | Output with replicated input signal | interface |

# Connections

equation
  y=fill(u, nout);
  


# Internal Context

| className   | connectorsDf   | classComment   |
|-------------|----------------|----------------|
