node Mod12Counter
  (clock: bool;
  reset: bool)
returns
  (Q_0: bool;
  Q_1: bool;
  Q_2: bool;
  Q_3: bool);

var
  V42_Q_prev: bool;
  V41_Q: bool;
  V52_Q_prev: bool;
  V51_Q: bool;
  V64_Q_prev: bool;
  V56_J: bool;
  V57_K: bool;
  V63_Q: bool;
  V76_Q_prev: bool;
  V68_J: bool;
  V69_K: bool;
  V75_Q: bool;

let
  Q_0 = ((not reset) and V41_Q);
  Q_1 = ((not reset) and V51_Q);
  Q_2 = ((not reset) and V63_Q);
  Q_3 = ((not reset) and V75_Q);
  V42_Q_prev = (false -> (pre V41_Q));
  V41_Q = (if (not clock) then V42_Q_prev else (if ((not true) and (not true)) 
  then V42_Q_prev else (if ((not true) and true) then false else (if (true and 
  (not true)) then true else (not V42_Q_prev)))));
  V52_Q_prev = (false -> (pre V51_Q));
  V51_Q = (if (not clock) then V52_Q_prev else (if ((not Q_0) and (not Q_0)) 
  then V52_Q_prev else (if ((not Q_0) and Q_0) then false else (if (Q_0 and 
  (not Q_0)) then true else (not V52_Q_prev)))));
  V64_Q_prev = (false -> (pre V63_Q));
  V56_J = (Q_0 and Q_1);
  V57_K = (Q_0 and Q_1);
  V63_Q = (if (not clock) then V64_Q_prev else (if ((not V56_J) and (not V57_K)
  ) then V64_Q_prev else (if ((not V56_J) and V57_K) then false else (if (V56_J 
  and (not V57_K)) then true else (not V64_Q_prev)))));
  V76_Q_prev = (false -> (pre V75_Q));
  V68_J = ((Q_0 and Q_1) and Q_2);
  V69_K = ((Q_0 and Q_1) and Q_2);
  V75_Q = (if (not clock) then V76_Q_prev else (if ((not V68_J) and (not V69_K)
  ) then V76_Q_prev else (if ((not V68_J) and V69_K) then false else (if (V68_J 
  and (not V69_K)) then true else (not V76_Q_prev)))));
tel

