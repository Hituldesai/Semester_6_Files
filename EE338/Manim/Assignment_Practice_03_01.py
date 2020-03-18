from manimlib.imports import *

class Equations(Scene):
	def construct(self):
		first_eq = TextMobject("$$y_1(\\theta) = sin(\\theta)$$")
		second_eq = ["$y_1(\\theta)$", "=", "$sin(\\theta)$"]

		second_mob = TextMobject(*second_eq)

		for i,item in enumerate(second_mob):
			if(i != 0):
				item.next_to(second_mob[i-1],RIGHT)

		eq2 = VGroup(*second_mob)

		des1 = TextMobject("Let us consider the continuous sine function: ")
		des2 = TextMobject("When sampled at a frequency \(f_S\), we get the function as follows: ")
		des3 = TextMobject("The stem-and-leaf plot of this sampled plot is: ")

		second_mob.set_color_by_gradient("#33ccff","#ff00ff")

		des1.shift(2*UP)
		des2.shift(2*UP)

		self.play(Write(des1))
		self.play(Write(first_eq))
		self.play(Transform(first_eq, eq2))
		self.wait(1)

		for i, item in enumerate(eq2):
			if (i<2):
				eq2[i].set_color(color=PURPLE)
			else:
				eq2[i].set_color(color="#00FFFF")

		self.add(eq2)
		self.wait(1)
		self.play(FadeOutAndShiftDown(eq2), FadeOutAndShiftDown(first_eq), ReplacementTransform(des1, des2))
		self.wait(2)
		self.play(ReplacementTransform(des2, des3))
