from manimlib.imports import *
import numpy as np
import math

class SquareWave(GraphScene):
	CONFIG = {
	"x_min": -10,
	"x_max": 10,
	"y_min": -1,
	"y_max": 1,
	"x_labeled_nums": range(-10, 10),
	"y_labeled_nums": [-1,0,1],
	"graph_origin": ORIGIN,
	}
	def construct(self):
		self.setup_axes(animate = True)
		func_graph_e = self.get_graph(lambda x: self.sum_gen(x,0), YELLOW_E)
		func_graph_o = self.get_graph(lambda x: self.sum_gen(x,1), YELLOW_E)
		self.play(ShowCreation(func_graph_e))
		self.wait(1)
		for j in range(1, 20):
			if (j % 2 == 0):
				func_graph_e = self.get_graph(lambda x: self.sum_gen(x,j), YELLOW_E)
				self.play(ReplacementTransform(func_graph_o, func_graph_e))
			else:
				func_graph_o = self.get_graph(lambda x: self.sum_gen(x,j), YELLOW_E)
				self.play(ReplacementTransform(func_graph_e, func_graph_o))
			self.wait(1)
	def sum_gen(self, x, i):
		if (i == 0): return np.sin(float(x))
		else: return np.sin(np.sin(float(x)*(2*i + 1))/(2*i + 1) + self.sum_gen(x, i-1))
