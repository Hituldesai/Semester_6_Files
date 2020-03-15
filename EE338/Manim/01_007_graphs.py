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
        func_graph1 = self.get_graph(self.notmygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        func_graph2 = self.get_graph(self.mygraph, RED_C)
        self.play(ShowCreation(func_graph1), ShowCreation(func_graph2))
        self.wait(2)
    def mygraph(self,x):
        return np.sin(x)
    def notmygraph(self,x):
        return np.cos(x)

class Scene1(GraphScene):
    CONFIG = {"x_min": -10, "x_max": 10,  "y_min": -10, "y_max": 10, "graph_origin": ORIGIN, }
    
    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, RED_E)
        self.play(ShowCreation(func_graph))
        self.wait(2)
    
    def mygraph(self,x):
        return math.sin(x)
