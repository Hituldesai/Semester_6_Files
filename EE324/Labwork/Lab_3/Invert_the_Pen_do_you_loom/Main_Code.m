M_p    = 0.027;
l_p    = 0.153;
L_p    = 0.191;
r      = 0.0826;
J_m    = 3.00e-005;
M_arm  = 0.028;
g      = 9.810;
J_eq   = 1.23e-004;
J_p    = 1.10e-004;
B_eq   = 0;
B_p    = 0;
R_m    = 3.3;
K_t    = 0.02797;
K_m    = 0.02797;

A      = [0, 0, 1, 0; 0, 0, 0, 1; 0, 0, 0, 0; 0, 0, 0, 0];
A(3,2) = r*M_p*M_p*l_p*l_p*g/((J_p*J_eq)+(J_eq*M_p*l_p*l_p)+(J_p*M_p*r*r));
A(3,3) = -K_t*K_m*(J_p+(M_p*l_p*l_p))/(((J_p*J_eq)+(J_eq*M_p*l_p*l_p)+(J_p*M_p*r*r))*R_m);
A(4,2) = M_p*l_p*g*(J_eq+(M_p*r*r))/(((J_p*J_eq)+(J_eq*M_p*l_p*l_p)+(J_p*M_p*r*r)));
A(4,3) = -M_p*l_p*K_t*K_m*r/((((J_p*J_eq)+(J_eq*M_p*l_p*l_p)+(J_p*M_p*r*r)))*R_m);

B      = [0; 0; 0; 0];
B(3,1) = K_t*(J_p+(M_p*l_p*l_p))/(((J_p*J_eq)+(J_eq*M_p*l_p*l_p)+(J_p*M_p*r*r))*R_m);
B(4,1) = M_p*l_p*K_t*r/((((J_p*J_eq)+(J_eq*M_p*l_p*l_p)+(J_p*M_p*r*r)))*R_m);

C      = eye(4);
D      = [0; 0; 0; 0];

q1      = 8;
q2      = 0;
q3      = 0.2;
q4      = 0.2;
0;
Q       = diag([q1 q2 q3 q4]);
R       = 1;
K       = lqr(A, B, Q, R);