node TRF_LT
  (S_0: bool;
  S_1: bool;
  S_2: bool;
  S_3: bool)
returns
  (O_0: bool;
  O_1: bool;
  O_2: bool;
  O_3: bool);

var
  V5_SIDE: bool;
  V44_O: int;
  V53_O: int;
  V62_O: int;
  V71_O: int;

let
  O_0 = (if ((S_2 = false) and (S_3 = false)) then true else (not (if (V44_O > 
  0) then true else false)));
  O_1 = (if ((S_2 = false) and (S_3 = false)) then true else (not (if (V53_O > 
  0) then true else false)));
  O_2 = (if (S_2 = false) then false else (if (V62_O > 0) then true else false)
  );
  O_3 = (if (S_3 = true) then false else (if (V71_O > 0) then true else false))
  ;
  V5_SIDE = ((S_2 = true) or (S_3 = true));
  V44_O = (if (V5_SIDE and (not (false -> (pre V5_SIDE)))) then 10 else (if (
  (pre V44_O) > 0) then ((pre V44_O) - 1) else 0));
  V53_O = (if (V5_SIDE and (not (false -> (pre V5_SIDE)))) then 10 else (if (
  (pre V53_O) > 0) then ((pre V53_O) - 1) else 0));
  V62_O = (if (V5_SIDE and (not (false -> (pre V5_SIDE)))) then 10 else (if (
  (pre V62_O) > 0) then ((pre V62_O) - 1) else 0));
  V71_O = (if (V5_SIDE and (not (false -> (pre V5_SIDE)))) then 10 else (if (
  (pre V71_O) > 0) then ((pre V71_O) - 1) else 0));
tel

