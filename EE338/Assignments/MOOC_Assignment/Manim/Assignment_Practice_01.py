from manimlib.imports import *
import numpy as np
import math

class Scene2(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    "x_labeled_nums": range(-5, 6),
    "y_labeled_nums": [-1,0,1],
    "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate = True)
        func_graph01 = self.get_graph(self.func01, YELLOW_E)
        func_graph02 = self.get_graph(self.func02, RED_C)
        func_graph03 = self.get_graph(self.func03, RED_C)
        func_graph04 = self.get_graph(self.func04, RED_C)
        self.play(ShowCreation(func_graph01))
        self.wait(1)
        self.play(ShowCreation(func_graph02))
        self.wait(1)
        self.play(ShowCreation(func_graph03))
        self.wait(1)
        self.play(ShowCreation(func_graph04))
        self.wait(3)
    def func01(self,x):
        return np.sin(x)
    def func02(self,x):
        return (np.sin(x) + np.sin(3*x))
    def func03(self,x):
        return (np.sin(x) + np.sin(3*x) + np.sin(5*x))
    def func04(self,x):
        return (np.sin(x) + np.sin(3*x) + np.sin(5*x) + np.sin(7*x))

class Scene1(GraphScene):
    CONFIG = {"x_min": -10, "x_max": 10,  "y_min": -10, "y_max": 10, "graph_origin": ORIGIN, }
    
    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, RED_E)
        self.play(ShowCreation(func_graph))
        self.wait(2)
    
    def mygraph(self,x):
        return math.sin(x)
