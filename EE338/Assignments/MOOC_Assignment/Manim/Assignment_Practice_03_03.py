#!/usr/bin/env python
from manimlib.imports import *
from functools import partial

class Shapes(Scene):
	def construct(self):
		circle = Circle()
		square = Square()
		triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

		self.play(ShowCreation(circle))
		self.play(FadeOut(circle))
		self.play(GrowFromCenter(square))
		self.play(Transform(square,triangle))

class PlotFunctions(GraphScene_Dec):
	CONFIG = {
		"x_min" : 0,
		"x_max" : 5,
		"y_min" : -1.5,
		"y_max" : 1.5,
		"graph_origin" : 5*LEFT ,
		"function_color" : RED ,
		"axes_color" : GREEN,
		"x_label_decimals": 2,
		"y_label_decimals": 1,
		"x_labeled_nums" :[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
	}

	def func_to_graph(self,x):
		return np.cos(x)

	def construct(self):
		self.setup_axes(animate=True)
		func_graph	= self.get_graph(self.func_to_graph,self.function_color)
		vert_lines	= self.get_vertical_lines_to_graph(func_graph,0,3,4,color=YELLOW)

		graph_lab	= self.get_graph_label(func_graph, label = "\\cos(x)")
		two_pi		= TexMobject("x = 2 \\pi")
		label_coord	= self.input_to_graph_point(TAU,func_graph)
		two_pi.next_to(label_coord,RIGHT+UP)
		points		= [Dot(self.coords_to_point(0,self.func_to_graph(0))), Dot(self.coords_to_point(1,self.func_to_graph(1))), Dot(self.coords_to_point(2,self.func_to_graph(2))), Dot(self.coords_to_point(3,self.func_to_graph(3)))]
		dots		= VGroup(points[0], points[1], points[2], points[3])
		self.add(dots)
		self.play(ShowCreation(func_graph))
		self.play(ShowCreation(vert_lines), ShowCreation(graph_lab))
		self.wait(2)
		
		func_graph.shift(3*UP)
		func_width	= func_graph.get_width()
		func_graph.scale(0.3)
		func_graph.stretch_to_fit_width(func_width)
		self.play(FadeIn(func_graph))

class PlotSinusoids(GraphScene_Dec):	
	CONFIG = {
		"x_min"				:  0.00,
		"x_max"				:  0.01,
		"y_min"				: -1.50,
		"y_max"				:  1.50,
		"axes_color"		: GREEN,
		"graph_origin"		: 5*LEFT,
		"x_axis_label"		: "$t$",
		"y_axis_label"		: "$x(t)$",
		"x_labeled_nums"	: np.linspace(0, 0.01, 5),
		"y_labeled_nums"	: np.linspace(-1.0, 1.0, 5),
		"x_label_decimals"	: 3,
		"y_label_decimals"	: 1,
	}

	def construct(self):
		line01	= TextMobject("Consider the following sinusoid:")
		line02	= TexMobject("x(t) = \\cos(2 \\pi 100 t - 60^o)")
		line03	= TextMobject("Now ", "sample ", "this signal at $f_s = 1 \\ KHz$")
		line04	= TexMobject("x[n] = \\cos(2 \\pi 100 \\frac{n}{1000} - 60^o)")
		line05	= TextMobject("Given just these samples,")
		line06	= TextMobject("can we recover the original sinusoid?")
		line07	= TextMobject("Pause and Ponder.")
		line08	= TextMobject("Confused?")
		line09	= TextMobject("Watch this closely.")
		line10	= TextMobject("Are you watching closely?")
		line11	= TextMobject("Clearly, many different sinusoids")
		line12	= TextMobject("can give us the same samples")
		line13	= TextMobject("Is there anything special") 
		line14	= TextMobject("about these sinusoids?")
		line15	= TextMobject("Hint: Compute their sum")
		line16	= TextMobject("Watch what happens when we add them")
		line17	= TextMobject("(The summation plots are scaled to fit the screen)")
		line18	= [TexMobject("\\# terms = " + str(n)) for n in range(1,101)]
		line19	= TextMobject("n")
		line20	= TextMobject("In the frequency domain,")
		line21	= TextMobject("a sine wave transforms to an impulse")
		line22	= TextMobject("adding up the sines implies superposing the impulses")
		eqtn01	= TexMobject("x(t) = \\cos(2 \\pi 100 t - 60^o)",  color=RED)
		eqtn02	= TexMobject("x(t) = \\cos(2 \\pi 900 t + 60^o)",  color=BLUE)
		eqtn03	= TexMobject("x(t) = \\cos(2 \\pi 1100 t - 60^o)", color=PURPLE)
		eqtn04	= TexMobject("x(t) = \\cos(2 \\pi 1900 t + 60^o)", color=ORANGE)
		line01.shift(UP)
		line02.next_to(line01, DOWN)
		
		self.play(FadeIn(line01))
		self.wait(0.5)
		self.play(ShowCreation(line02))
		self.wait(0.5)
		self.play(FadeOut(line01))
		self.play(ApplyMethod(line02.shift, 3*UP))
		self.wait(0.5)

		line03.next_to(line02, DOWN)
		line04.next_to(line02, DOWN)
		line05.next_to(line03, UP)
		line06.next_to(line05, DOWN)
		line07.next_to(line03, UP)
		line08.next_to(line03, UP)
		line09.next_to(line03, UP)
		line10.next_to(line03, UP)
		line11.next_to(line03, UP)
		line12.next_to(line11, DOWN)
		line13.next_to(line03, UP)
		line14.next_to(line13, DOWN)
		line15.next_to(line03, UP)
		line16.next_to(line03, UP)
		line20.next_to(line03, UP)
		line21.next_to(line13, DOWN)
		line22.next_to(line13, DOWN)
		eqtn01.next_to(line03, UP)
		eqtn02.next_to(line03, UP)
		eqtn03.next_to(line03, UP)
		eqtn04.next_to(line03, UP)
		line04.shift(0.5*UP)
		line06.shift(0.2*UP)
		line17.shift(3.5*DOWN + 4*LEFT)
		
		line18[0].shift(3*DOWN)
		line18[1].shift(3*DOWN)
		line18[2].shift(3*DOWN)
		line18[3].shift(3*DOWN)
		line18[4].shift(3*DOWN)
		line17.scale(0.5)
		line03[1].set_color(YELLOW)
		
		self.setup_axes(animate=False)
		ind_graph01	= self.get_graph(self.fun1, RED)
		ind_graph02	= self.get_graph(self.fun2, BLUE)
		ind_graph03	= self.get_graph(self.fun3, PURPLE)
		ind_graph04	= self.get_graph(self.fun4, ORANGE)
		sum_graph2	= self.get_graph(self.acc_fun2, BLUE)
		sum_graph3	= self.get_graph(self.acc_fun3, BLUE)
		sum_graph4	= self.get_graph(self.acc_fun4, BLUE)
		sum_graph5	= self.get_graph(self.acc_fun5, BLUE)
		xaxis_dis	= NumberLine(x_min = 0, x_max = 11, include_numbers = True, include_tip = True, label_direction = DOWN, unit_size=10.0/10.0)
		vert_lines	= self.get_vertical_lines_to_graph(ind_graph01,0,0.01,11,color=YELLOW)
		samp_points	= []
		for x in range(11):
			samp_points.append(Dot(self.coords_to_point(0.001*x, self.fun1(0.001*x))))
		dots		= VGroup(*samp_points)
		sum_graph2.set_height(5, stretch = True)
		sum_graph3.set_height(5, stretch = True)
		sum_graph4.set_height(5, stretch = True)
		sum_graph5.set_height(5, stretch = True)
		xaxis_dis.shift(5*LEFT)
		line19.next_to(xaxis_dis, RIGHT)
		
		self.play(ShowCreation(self.axes), ShowCreation(ind_graph01))
		self.wait(1)
		self.play(ShowCreation(line03))
		self.wait(2)
		self.play(ShowCreation(vert_lines), ShowCreation(dots))
		self.wait(0.2)
		self.play(FadeOut(ind_graph01))
		self.play(FadeOut(line03))
		self.play(Transform(line02, line04), FadeOut(self.axes),ShowCreation(xaxis_dis), ShowCreation(line19))
		self.wait(2)
		self.play(FadeOut(line02),FadeOut(xaxis_dis), FadeOut(line19), FadeIn(self.axes),FadeIn(line05), FadeIn(line06))
		self.wait(2)
		self.play(FadeOut(line05), FadeOut(line06), FadeIn(line07))
		self.wait(2)
		self.play(FadeOut(line07), FadeIn(line08))
		self.wait(2)
		self.play(FadeOut(line08), FadeIn(line09))
		self.wait(2)
		self.play(Transform(line09, line10))
		self.wait(2)
		self.play(ShowCreation(ind_graph01), Transform(line09, eqtn01))
		self.wait(2)
		self.play(FadeOut(ind_graph01), ShowCreation(ind_graph02), Transform(line09, eqtn02))
		self.wait(2)
		self.play(FadeOut(ind_graph02), ShowCreation(ind_graph03), Transform(line09, eqtn03))
		self.wait(2)
		self.play(FadeOut(ind_graph03), ShowCreation(ind_graph04), Transform(line09, eqtn04))
		self.wait(2)
		self.play(FadeOut(ind_graph04),FadeOut(line09), FadeIn(line11), FadeIn(line12))
		self.wait(2)
		self.play(FadeOut(line11),FadeOut(line12), FadeIn(line13), FadeIn(line14))
		self.wait(2)
		self.play(FadeOut(line13),FadeOut(line14), FadeIn(line15))
		self.wait(2)
		self.play(Transform(line15, line16), FadeOut(self.axes))
		self.wait(2)
		self.play(FadeIn(line17))
		ind_graph01.set_color(BLUE)
		self.play(ShowCreation(ind_graph01), ShowCreation(line18[0]))
		self.wait(1)
		self.play(Transform(ind_graph01, sum_graph2), Transform(line18[0],line18[1]))
		self.wait(1)
		self.play(Transform(ind_graph01, sum_graph3), Transform(line18[0],line18[2]))
		self.wait(1)
		self.play(Transform(ind_graph01, sum_graph4), Transform(line18[0],line18[3]))
		self.wait(1)
		self.play(Transform(ind_graph01, sum_graph5), Transform(line18[0],line18[4]))
		self.wait(1)
		self.play(FadeOut(ind_graph01), FadeOut(sum_graph5), FadeOut(line18[0]))
		self.wait(0.5)
		self.play(FadeOut(line15), FadeOut(line16), FadeIn(line20))
		self.wait(0.25)
		self.play(FadeOut(vert_lines), FadeOut(dots))
		self.wait(0.5)
		
		self.x_min			=    0
		self.x_max			= 5200
		self.y_min			= -1.5
		self.y_max			=  2.5
		self.y_axis_height	=    3
		self.axes_color		=  RED
		self.graph_origin	= 5*LEFT + 1*DOWN
		self.x_axis_label	= "$\\frac{\\omega}{2\\pi}$"
		self.y_axis_label	= "$F\\left(\\frac{\\omega}{2\\pi}\\right)$"
		self.x_labeled_nums	= np.linspace(0, 5000, 11)
		self.y_labeled_nums	= []
		self.x_label_decimals = 0
		self.y_label_decimals = 0
		self.x_tick_frequency = 10000
		self.y_tick_frequency = 10000
		samp_imp	= [Arrow(self.coords_to_point(100, 0), self.coords_to_point(100, 3))]
		imps		= VGroup(*samp_imp)
		
		self.play(FadeOut(line17), FadeIn(line21))
		self.setup_axes(animate=True)
		self.play(ShowCreation(imps))
		self.wait(2)
		
		
		samp_imp.append(Arrow(self.coords_to_point((0+1)*1000 - 100, 0), self.coords_to_point((0+1)*1000 - 100, 3)))
		samp_imp.append(Arrow(self.coords_to_point((0+1)*1000 + 100, 0), self.coords_to_point((0+1)*1000 + 100, 3)))
		imps		= VGroup(*samp_imp)
		line18[0]	= line18[1]
		self.play(FadeOut(line21), FadeIn(line22), ShowCreation(imps), Transform(line18[0],line18[1]))
		self.wait(1)

		samp_imp.append(Arrow(self.coords_to_point((1+1)*1000 - 100, 0), self.coords_to_point((1+1)*1000 - 100, 3)))
		samp_imp.append(Arrow(self.coords_to_point((1+1)*1000 + 100, 0), self.coords_to_point((1+1)*1000 + 100, 3)))
		imps = VGroup(*samp_imp)
		self.play(ShowCreation(imps), Transform(line18[0],line18[2]))
		self.wait(1)
		
		samp_imp.append(Arrow(self.coords_to_point((2+1)*1000 - 100, 0), self.coords_to_point((2+1)*1000 - 100, 3)))
		samp_imp.append(Arrow(self.coords_to_point((2+1)*1000 + 100, 0), self.coords_to_point((2+1)*1000 + 100, 3)))
		imps = VGroup(*samp_imp)
		self.play(ShowCreation(imps), Transform(line18[0],line18[3]))
		self.wait(1)
		
		samp_imp.append(Arrow(self.coords_to_point((3+1)*1000 - 100, 0), self.coords_to_point((3+1)*1000 - 100, 3)))
		samp_imp.append(Arrow(self.coords_to_point((3+1)*1000 + 100, 0), self.coords_to_point((3+1)*1000 + 100, 3)))
		imps = VGroup(*samp_imp)
		self.play(ShowCreation(imps), Transform(line18[0],line18[4]))
		self.wait(1)
		
	def fun1(self, x):
		phi0 = -60*PI/180;
		return np.cos(2*PI*100*x + phi0)

	def fun2(self, x):
		phi0 = -60*PI/180;
		return np.cos(2*PI*900*x - phi0)

	def fun3(self, x):
		phi0 = -60*PI/180;
		return np.cos(2*PI*1100*x + phi0)

	def fun4(self, x):
		phi0 = -60*PI/180;
		return np.cos(2*PI*1900*x - phi0)

	def fun_gen(self,k,x):
		phi0 = -60*PI/180;
		return [np.cos(2*PI*(100 - 1000*k)*x + phi0), np.cos(2*PI*(100 + 1000*k)*x + phi0)]

	def acc_fun1(self,x):
		k=1
		phi0 = -60*PI/180;
		t0 = np.cos(2*PI*100*x + phi0)
		acc = t0
		m = int((k-1)/2)
		if((k-1)%2==0):
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
		else:
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
			acc = acc + self.fun_gen(m,x)[0]
		return acc

	def acc_fun2(self,x):
		k=2
		phi0 = -60*PI/180;
		t0 = np.cos(2*PI*100*x + phi0)
		acc = t0
		m = int((k-1)/2)
		if((k-1)%2==0):
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
		else:
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
			acc = acc + self.fun_gen(m,x)[0]
		return acc

	def acc_fun3(self,x):
		k=3
		phi0 = -60*PI/180;
		t0 = np.cos(2*PI*100*x + phi0)
		acc = t0
		m = int((k-1)/2)
		if((k-1)%2==0):
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
		else:
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
			acc = acc + self.fun_gen(m,x)[0]
		return acc

	def acc_fun4(self,x):
		k=4
		phi0 = -60*PI/180;
		t0 = np.cos(2*PI*100*x + phi0)
		acc = t0
		m = int((k-1)/2)
		if((k-1)%2==0):
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
		else:
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
			acc = acc + self.fun_gen(m,x)[0]
		return acc

	def acc_fun5(self,x):
		k=5
		phi0 = -60*PI/180;
		t0 = np.cos(2*PI*100*x + phi0)
		acc = t0
		m = int((k-1)/2)
		if((k-1)%2==0):
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
		else:
			for i in range(m):
				acc = acc + self.fun_gen(i,x)[0] + self.fun_gen(i,x)[1]
			acc = acc + self.fun_gen(m,x)[0]
		return acc