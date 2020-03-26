#!/usr/bin/env python
from manimlib.imports import *
from functools import partial

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

    def func01(self,x):
        return np.cos(x)

    def func02(self,x):
        return np.sin(x)

    def func03(self,x):
        return (1 +  np.sin(x))

    def func04(self,x):
        return (2 + np.cos(x))

    def construct(self):
        self.setup_axes(animate=True)
        graph01  = self.get_graph(self.func01, self.function_color)
        graph02  = self.get_graph(self.func02, self.function_color)
        graph03  = self.get_graph(self.func03, self.function_color)
        graph04  = self.get_graph(self.func04, self.function_color)
        
        self.play(ShowCreation(graph01))
        self.wait(2)
        self.play(FadeOut(graph01), FadeIn(graph02))
        self.wait(2)
        self.play(Transform(graph02, graph03))
        self.wait(2)
        self.play(ReplacementTransform(graph02, graph04))
        self.wait(2)