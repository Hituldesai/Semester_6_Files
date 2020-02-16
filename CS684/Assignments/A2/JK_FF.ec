node JK_FF
  (J: bool;
  K: bool;
  CLK: bool)
returns
  (Q: bool;
  nQ: bool);

var
  V15_Q_prev: bool;

let
  Q = (if (not (CLK and (not (false -> (pre CLK))))) then V15_Q_prev else (if (
  (not J) and (not K)) then V15_Q_prev else (if ((not J) and K) then false else 
  (if (J and (not K)) then true else (not V15_Q_prev)))));
  nQ = (not Q);
  V15_Q_prev = (false -> (pre Q));
tel

