file1 = open("func_defs.txt","w")
def_string = "def acc_fun{0}(self,x):\n\tk={0}\n\tphi0 = -60*PI/180;\n\tt0 = np.cos(2*PI*100*x + phi0)\n\tacc = t0\n\tm = int((k-1)/2)\n\tif((k-1)%2==0):\n\t\tfor i in range(m):\n\t\t\tacc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]\n\telse:\n\t\tfor i in range(m):\n\t\t\tacc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]\n\t\tacc = acc + self.fun_gen(m,x)[0]\n\treturn acc\n\n"
file2 = open("func_calls.txt","w")
call_string = "sum_graph{0} = self.get_graph(self.acc_fun{0}, BLUE)\nsum_graph{0}.set_height(5, stretch = True)\nterm_num[{1}].shift(3*DOWN)\nself.play(Transform(first_graph, sum_graph{0}), Transform(term_num[0],term_num[{1}]))\nself.wait({2})\n\n"
def_full = ""
call_full = ""
for i in range(1,101):
	def_full = def_full + def_string.format(str(i))
	call_full = call_full + call_string.format(str(i),str(i-1), "1")
# print(full)
file1.write(def_full)
file1.close()

file2.write(call_full)
file2.close()


