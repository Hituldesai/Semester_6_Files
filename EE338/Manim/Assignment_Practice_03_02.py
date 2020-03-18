from manimlib.imports import *
pi = 3.14159265

class Main(GraphScene, Scene):
	CONFIG = {
		"x_min": -50,
		"x_max":  50,
		"y_min": -3,
		"y_max":  3,
		"graph_origin": ORIGIN,
		"function_color": WHITE,
		"axes_color": BLUE
	}
	
	def f1(self, x):
		return (np.sin(2*pi*0.1*x))
	
	def f2(self, x):
		if (((x * 4) % 1) == 0):
			print(x)
			print(self.f1(x))
			return self.f1(x)
		else:
			return 0	

	def construct(self):
		nullObj  = TextMobject("")
		ttObj_01 = TextMobject("Consider the continuous function: ")
		ttObj_01.shift(3.7*UP)
		ttObj_02 = TextMobject("Sampling at a frequency \(f_S = 4 Hz\) gives: ")
		ttObj_02.shift(3.7*UP)
		ttObj_03 = TextMobject("The stem-and-leaf plot of this sampled plot is: ")
		ttObj_03.shift(3.7*UP)
		
		eqObj_01	= TextMobject("$$ y_1(t) = sin\\left(2\\pi\\cdot 0.1\\cdot t\\right)\ rad\ s^{-1} $$")
		
		eqOrg_02	= ["Time", "Value", "0.0", "0.000", "0.25", "0.156", "0.50", "0.309", "0.75", "0.454", "...", "...", "2.50", "1.000", "2.75", "0.988", "...", "...", "6.00", "-0.588", "6.25", "-0.707", "...", "..."]
		eqMob_02	= TextMobject(*eqOrg_02)
		for i, item in enumerate(eqMob_02):
			if   (i % 2 == 0 and i != 0):
				item.next_to(eqMob_02[i-2], DOWN)
			elif (i % 2 == 1):
				item.next_to(eqMob_02[i-1], RIGHT)
		eqMob_02.shift(3*UP)
		eqMob_02.shift(3*RIGHT)
		eqMob_02.set_color_by_gradient("#33ccff","#ff00ff")
		eqMob_02.scale(0.65)
		eqObj_02 = VGroup(*eqMob_02)
		
		self.play(Write(ttObj_01))
		self.play(Write(eqObj_01))
		self.wait(1.5)
		
		self.play(FadeOut(eqObj_01))
		self.setup_axes(animate = False)
		fnObj_01	= self.get_graph(self.f1, self.function_color)
		self.play(ShowCreation(fnObj_01))
		self.wait(2)
		
		self.play(ReplacementTransform(ttObj_01, ttObj_02))
		self.remove(fnObj_01)
		self.play(FadeOut(self.x_axis))
		self.remove(self.x_axis)
		self.x_min	= -5
		self.x_leftmost_tick = -5
		self.setup_axes(animate = False)
		point_01	= [Dot(self.coords_to_point(0.25*j, self.f2(0.25*j))) for j in range(210)]
		for j in range(210):
			self.add(point_01[j])
		self.wait(2)
		
		self.play(ReplacementTransform(ttObj_02, ttObj_03))
		self.play(ShowCreation(eqObj_02))
		self.wait(2)
		for j in range(210):
			self.remove(point_01[j])
		self.play(FadeOut(self.x_axis), FadeOut(self.y_axis))
		self.wait(1)
