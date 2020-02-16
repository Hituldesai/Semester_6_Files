node JK_FlipFlop
  (J: bool;
  K: bool)
returns
  (Q: bool;
  nQ: bool);

var
  V6_nS: bool;
  V7_nR: bool;
  V8_CLK: bool;

let
  Q = (false -> (not (V6_nS and (pre nQ))));
  nQ = (true -> (not (V7_nR and Q)));
  V6_nS = (not ((J and (not (pre Q))) and V8_CLK));
  V7_nR = (not ((K and (pre Q)) and V8_CLK));
  V8_CLK = (false -> (not (pre V8_CLK)));
tel

