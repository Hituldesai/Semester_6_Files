#!/usr/bin/env python

import sys
if '/opt/ros/kinetic/lib/python2.7/dist-packages' in sys.path: sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

from manimlib.imports import *

from functools import partial

# sum_functions = []
# k = 0
class Shapes(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
        square = Square()
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        #Showing shapes
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 5,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : 5*LEFT ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_label_decimals": 2,
        "x_labeled_nums" :[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        # func_graph2=self.get_graph(self.func_to_graph2)
        # vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        vert_lines = self.get_vertical_lines_to_graph(func_graph,0,20,10,color=YELLOW)

        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        # graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)
        points = [Dot(self.coords_to_point(1,self.func_to_graph(1))),Dot(self.coords_to_point(2,self.func_to_graph(2)))]
        dots = VGroup(points[0], points[1])
        self.add(dots)
        self.play(ShowCreation(func_graph))
        # self.play(ShowCreation(vert_line), ShowCreation(graph_lab),ShowCreation(two_pi))
        self.play(ShowCreation(vert_lines), ShowCreation(graph_lab))
        self.wait(2)
        func_graph.shift(3*UP)
        func_width = func_graph.get_width()
        func_graph.scale(0.3)
        func_graph.stretch_to_fit_width(func_width)
        self.play(FadeIn(func_graph))


    def func_to_graph(self,x):
        return np.cos(x)

    # def func_to_graph2(self,x):
    #     return np.sin(x)

class PlotSinusoids(GraphScene):
    
    CONFIG = {
        "x_min" : 0,
        "x_max" : 0.01,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "x_label_decimals": 3,
        "y_label_decimals": 1,
        "graph_origin" : 5*LEFT ,
        "axes_color" : GREEN,
        "x_labeled_nums" : np.linspace(0, 0.01, 5),
        "y_labeled_nums" : np.linspace(-1.0, 1.0, 5),
        "x_axis_label" : "$t$",
        "y_axis_label" : "$x(t)$",

    }

    # TexMobject(r"1", r"\over", r"7").set_color_by_tex("7", BLUE)


    def construct(self):

        line1 = TextMobject("Consider the following sinusoid:")
        line1.shift(UP)
        line2 = TexMobject("x(t) = \\cos(2 \\pi 100 t - 60^o)")
        line2.next_to(line1, DOWN)
        self.play(FadeIn(line1))
        self.wait(0.5)
        self.play(ShowCreation(line2))
        self.wait(0.5)
        self.play(FadeOut(line1))
        self.play(ApplyMethod(line2.shift, 3*UP))
        self.wait(0.5)
        self.setup_axes(animate=False)
        first_graph = self.get_graph(self.fun1, RED)
        self.play(ShowCreation(self.axes), ShowCreation(first_graph))
        self.wait(1)
        line3 = TextMobject("Now ", "sample ", "this signal at $f_s = 1 \\ KHz$")
        line3[1].set_color(YELLOW)
        line3.next_to(line2, DOWN)
        self.play(ShowCreation(line3))
        self.wait(2)
        line4 = TexMobject("x[n] = \\cos(2 \\pi 100 \\frac{n}{1000} - 60^o)")
        line4.next_to(line2, DOWN)
        line4.shift(0.5*UP)
        xaxis_dis = NumberLine(x_min = 0, x_max = 11, include_numbers = True, include_tip = True, label_direction = DOWN, unit_size=10.0/10.0)
        n = TextMobject("n")
        xaxis_dis.shift(5*LEFT)
        n.next_to(xaxis_dis, RIGHT)
        vert_lines = self.get_vertical_lines_to_graph(first_graph,0,0.01,11,color=YELLOW)
        sample_points = []
        for x in range(11):
            sample_points.append(Dot(self.coords_to_point(0.001*x, self.fun1(0.001*x))))
        dots = VGroup(*sample_points)
        self.play(ShowCreation(vert_lines), ShowCreation(dots))
        self.wait(0.2)
        self.play(FadeOut(first_graph))
        self.play(FadeOut(line3))
        self.play(Transform(line2, line4), FadeOut(self.axes),ShowCreation(xaxis_dis), ShowCreation(n))
        self.wait(2)
        line5 = TextMobject("Given just these samples,")
        line6 = TextMobject("can we recover the original sinusoid?")
        line5.next_to(line3, UP)
        line6.next_to(line5, DOWN)
        line6.shift(0.2*UP)
        self.play(FadeOut(line2),FadeOut(xaxis_dis), FadeOut(n), FadeIn(self.axes),FadeIn(line5), FadeIn(line6))
        self.wait(2)
        line7 = TextMobject("Pause and Ponder.")
        line7.next_to(line3, UP)
        self.play(FadeOut(line5), FadeOut(line6), FadeIn(line7))
        self.wait(2)
        line8 = TextMobject("Confused?")
        line9 = TextMobject("Watch this closely.")
        line10 = TextMobject("Are you watching closely?")
        line8.next_to(line3, UP)
        line9.next_to(line3, UP)
        line10.next_to(line3, UP)
        self.play(FadeOut(line7), FadeIn(line8))
        self.wait(2)
        self.play(FadeOut(line8), FadeIn(line9))
        self.wait(2)
        self.play(Transform(line9, line10))
        self.wait(2)
        second_graph = self.get_graph(self.fun2, BLUE)
        third_graph = self.get_graph(self.fun3, PURPLE)
        fourth_graph = self.get_graph(self.fun4, ORANGE)
        first_eqn = TexMobject("x(t) = \\cos(2 \\pi 100 t - 60^o)", color=RED)
        first_eqn.next_to(line3, UP)
        second_eqn = TexMobject("x(t) = \\cos(2 \\pi 900 t + 60^o)", color=BLUE)
        second_eqn.next_to(line3, UP)
        third_eqn = TexMobject("x(t) = \\cos(2 \\pi 1100 t - 60^o)", color=PURPLE)
        third_eqn.next_to(line3, UP)
        fourth_eqn = TexMobject("x(t) = \\cos(2 \\pi 1900 t + 60^o)", color=ORANGE)
        fourth_eqn.next_to(line3, UP)
        self.play(ShowCreation(first_graph), Transform(line9, first_eqn))
        self.wait(2)
        self.play(FadeOut(first_graph), ShowCreation(second_graph), Transform(line9, second_eqn))
        self.wait(2)
        self.play(FadeOut(second_graph), ShowCreation(third_graph), Transform(line9, third_eqn))
        self.wait(2)
        self.play(FadeOut(third_graph), ShowCreation(fourth_graph), Transform(line9, fourth_eqn))
        self.wait(2)
        line11 = TextMobject("Clearly, many different sinusoids")
        line12 = TextMobject("can give us the same samples")
        line11.next_to(line3, UP)
        line12.next_to(line11, DOWN)
        self.play(FadeOut(fourth_graph),FadeOut(line9), FadeIn(line11), FadeIn(line12))
        self.wait(2)
        line13 = TextMobject("Is there anything special") 
        line14 = TextMobject("about these sinusoids?")
        line13.next_to(line3, UP)
        line14.next_to(line13, DOWN)
        self.play(FadeOut(line11),FadeOut(line12), FadeIn(line13), FadeIn(line14))
        self.wait(2)
        line15 = TextMobject("Hint: Compute their sum")
        line16 = TextMobject("Watch what happens when we add them")
        line15.next_to(line3, UP)
        line16.next_to(line3, UP)
        self.play(FadeOut(line13),FadeOut(line14), FadeIn(line15))
        self.wait(2)
        self.play(Transform(line15, line16), FadeOut(self.axes))
        self.wait(2)
        note = TextMobject("(The summation plots are scaled to fit the screen)")
        note.scale(0.5)
        note.shift(3.5*DOWN + 4*LEFT)
        self.play(FadeIn(note))
        term_num = [TexMobject("\\# terms = " + str(n)) for n in range(1,101)]
        term_num[0].shift(3*DOWN)
        first_graph.set_color(BLUE)
        self.play(ShowCreation(first_graph), ShowCreation(term_num[0]))
        self.wait(1)
        
        sum_graph2 = self.get_graph(self.acc_fun2, BLUE)
        sum_graph2.set_height(5, stretch = True)
        term_num[1].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph2), Transform(term_num[0],term_num[1]))
        self.wait(1)

        sum_graph3 = self.get_graph(self.acc_fun3, BLUE)
        sum_graph3.set_height(5, stretch = True)
        term_num[2].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph3), Transform(term_num[0],term_num[2]))
        self.wait(1)

        sum_graph4 = self.get_graph(self.acc_fun4, BLUE)
        sum_graph4.set_height(5, stretch = True)
        term_num[3].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph4), Transform(term_num[0],term_num[3]))
        self.wait(1)

        sum_graph5 = self.get_graph(self.acc_fun5, BLUE)
        sum_graph5.set_height(5, stretch = True)
        term_num[4].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph5), Transform(term_num[0],term_num[4]))
        self.wait(1)

        sum_graph6 = self.get_graph(self.acc_fun6, BLUE)
        sum_graph6.set_height(5, stretch = True)
        term_num[5].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph6), Transform(term_num[0],term_num[5]))
        self.wait(1)

        sum_graph7 = self.get_graph(self.acc_fun7, BLUE)
        sum_graph7.set_height(5, stretch = True)
        term_num[6].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph7), Transform(term_num[0],term_num[6]))
        self.wait(1)

        sum_graph8 = self.get_graph(self.acc_fun8, BLUE)
        sum_graph8.set_height(5, stretch = True)
        term_num[7].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph8), Transform(term_num[0],term_num[7]))
        self.wait(1)

        sum_graph9 = self.get_graph(self.acc_fun9, BLUE)
        sum_graph9.set_height(5, stretch = True)
        term_num[8].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph9), Transform(term_num[0],term_num[8]))
        self.wait(1)

        sum_graph10 = self.get_graph(self.acc_fun10, BLUE)
        sum_graph10.set_height(5, stretch = True)
        term_num[9].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph10), Transform(term_num[0],term_num[9]))
        self.wait(1)

        sum_graph11 = self.get_graph(self.acc_fun11, BLUE)
        sum_graph11.set_height(5, stretch = True)
        term_num[10].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph11), Transform(term_num[0],term_num[10]))
        self.wait(1)

        sum_graph12 = self.get_graph(self.acc_fun12, BLUE)
        sum_graph12.set_height(5, stretch = True)
        term_num[11].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph12), Transform(term_num[0],term_num[11]))
        self.wait(1)

        sum_graph13 = self.get_graph(self.acc_fun13, BLUE)
        sum_graph13.set_height(5, stretch = True)
        term_num[12].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph13), Transform(term_num[0],term_num[12]))
        self.wait(1)

        sum_graph14 = self.get_graph(self.acc_fun14, BLUE)
        sum_graph14.set_height(5, stretch = True)
        term_num[13].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph14), Transform(term_num[0],term_num[13]))
        self.wait(1)

        sum_graph15 = self.get_graph(self.acc_fun15, BLUE)
        sum_graph15.set_height(5, stretch = True)
        term_num[14].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph15), Transform(term_num[0],term_num[14]))
        self.wait(1)

        sum_graph16 = self.get_graph(self.acc_fun16, BLUE)
        sum_graph16.set_height(5, stretch = True)
        term_num[15].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph16), Transform(term_num[0],term_num[15]))
        self.wait(1)

        sum_graph17 = self.get_graph(self.acc_fun17, BLUE)
        sum_graph17.set_height(5, stretch = True)
        term_num[16].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph17), Transform(term_num[0],term_num[16]))
        self.wait(1)

        sum_graph18 = self.get_graph(self.acc_fun18, BLUE)
        sum_graph18.set_height(5, stretch = True)
        term_num[17].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph18), Transform(term_num[0],term_num[17]))
        self.wait(1)

        sum_graph19 = self.get_graph(self.acc_fun19, BLUE)
        sum_graph19.set_height(5, stretch = True)
        term_num[18].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph19), Transform(term_num[0],term_num[18]))
        self.wait(1)

        sum_graph20 = self.get_graph(self.acc_fun20, BLUE)
        sum_graph20.set_height(5, stretch = True)
        term_num[19].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph20), Transform(term_num[0],term_num[19]))
        self.wait(1)

        sum_graph21 = self.get_graph(self.acc_fun21, BLUE)
        sum_graph21.set_height(5, stretch = True)
        term_num[20].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph21), Transform(term_num[0],term_num[20]))
        self.wait(1)

        sum_graph22 = self.get_graph(self.acc_fun22, BLUE)
        sum_graph22.set_height(5, stretch = True)
        term_num[21].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph22), Transform(term_num[0],term_num[21]))
        self.wait(1)

        sum_graph23 = self.get_graph(self.acc_fun23, BLUE)
        sum_graph23.set_height(5, stretch = True)
        term_num[22].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph23), Transform(term_num[0],term_num[22]))
        self.wait(1)

        sum_graph24 = self.get_graph(self.acc_fun24, BLUE)
        sum_graph24.set_height(5, stretch = True)
        term_num[23].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph24), Transform(term_num[0],term_num[23]))
        self.wait(1)

        sum_graph25 = self.get_graph(self.acc_fun25, BLUE)
        sum_graph25.set_height(5, stretch = True)
        term_num[24].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph25), Transform(term_num[0],term_num[24]))
        self.wait(1)

        sum_graph26 = self.get_graph(self.acc_fun26, BLUE)
        sum_graph26.set_height(5, stretch = True)
        term_num[25].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph26), Transform(term_num[0],term_num[25]))
        self.wait(1)

        sum_graph27 = self.get_graph(self.acc_fun27, BLUE)
        sum_graph27.set_height(5, stretch = True)
        term_num[26].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph27), Transform(term_num[0],term_num[26]))
        self.wait(1)

        sum_graph28 = self.get_graph(self.acc_fun28, BLUE)
        sum_graph28.set_height(5, stretch = True)
        term_num[27].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph28), Transform(term_num[0],term_num[27]))
        self.wait(1)

        sum_graph29 = self.get_graph(self.acc_fun29, BLUE)
        sum_graph29.set_height(5, stretch = True)
        term_num[28].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph29), Transform(term_num[0],term_num[28]))
        self.wait(1)

        sum_graph30 = self.get_graph(self.acc_fun30, BLUE)
        sum_graph30.set_height(5, stretch = True)
        term_num[29].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph30), Transform(term_num[0],term_num[29]))
        self.wait(1)

        sum_graph31 = self.get_graph(self.acc_fun31, BLUE)
        sum_graph31.set_height(5, stretch = True)
        term_num[30].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph31), Transform(term_num[0],term_num[30]))
        self.wait(1)

        sum_graph32 = self.get_graph(self.acc_fun32, BLUE)
        sum_graph32.set_height(5, stretch = True)
        term_num[31].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph32), Transform(term_num[0],term_num[31]))
        self.wait(1)

        sum_graph33 = self.get_graph(self.acc_fun33, BLUE)
        sum_graph33.set_height(5, stretch = True)
        term_num[32].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph33), Transform(term_num[0],term_num[32]))
        self.wait(1)

        sum_graph34 = self.get_graph(self.acc_fun34, BLUE)
        sum_graph34.set_height(5, stretch = True)
        term_num[33].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph34), Transform(term_num[0],term_num[33]))
        self.wait(1)

        sum_graph35 = self.get_graph(self.acc_fun35, BLUE)
        sum_graph35.set_height(5, stretch = True)
        term_num[34].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph35), Transform(term_num[0],term_num[34]))
        self.wait(1)

        sum_graph36 = self.get_graph(self.acc_fun36, BLUE)
        sum_graph36.set_height(5, stretch = True)
        term_num[35].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph36), Transform(term_num[0],term_num[35]))
        self.wait(1)

        sum_graph37 = self.get_graph(self.acc_fun37, BLUE)
        sum_graph37.set_height(5, stretch = True)
        term_num[36].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph37), Transform(term_num[0],term_num[36]))
        self.wait(1)

        sum_graph38 = self.get_graph(self.acc_fun38, BLUE)
        sum_graph38.set_height(5, stretch = True)
        term_num[37].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph38), Transform(term_num[0],term_num[37]))
        self.wait(1)

        sum_graph39 = self.get_graph(self.acc_fun39, BLUE)
        sum_graph39.set_height(5, stretch = True)
        term_num[38].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph39), Transform(term_num[0],term_num[38]))
        self.wait(1)

        sum_graph40 = self.get_graph(self.acc_fun40, BLUE)
        sum_graph40.set_height(5, stretch = True)
        term_num[39].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph40), Transform(term_num[0],term_num[39]))
        self.wait(1)

        sum_graph41 = self.get_graph(self.acc_fun41, BLUE)
        sum_graph41.set_height(5, stretch = True)
        term_num[40].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph41), Transform(term_num[0],term_num[40]))
        self.wait(1)

        sum_graph42 = self.get_graph(self.acc_fun42, BLUE)
        sum_graph42.set_height(5, stretch = True)
        term_num[41].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph42), Transform(term_num[0],term_num[41]))
        self.wait(1)

        sum_graph43 = self.get_graph(self.acc_fun43, BLUE)
        sum_graph43.set_height(5, stretch = True)
        term_num[42].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph43), Transform(term_num[0],term_num[42]))
        self.wait(1)

        sum_graph44 = self.get_graph(self.acc_fun44, BLUE)
        sum_graph44.set_height(5, stretch = True)
        term_num[43].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph44), Transform(term_num[0],term_num[43]))
        self.wait(1)

        sum_graph45 = self.get_graph(self.acc_fun45, BLUE)
        sum_graph45.set_height(5, stretch = True)
        term_num[44].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph45), Transform(term_num[0],term_num[44]))
        self.wait(1)

        sum_graph46 = self.get_graph(self.acc_fun46, BLUE)
        sum_graph46.set_height(5, stretch = True)
        term_num[45].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph46), Transform(term_num[0],term_num[45]))
        self.wait(1)

        sum_graph47 = self.get_graph(self.acc_fun47, BLUE)
        sum_graph47.set_height(5, stretch = True)
        term_num[46].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph47), Transform(term_num[0],term_num[46]))
        self.wait(1)

        sum_graph48 = self.get_graph(self.acc_fun48, BLUE)
        sum_graph48.set_height(5, stretch = True)
        term_num[47].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph48), Transform(term_num[0],term_num[47]))
        self.wait(1)

        sum_graph49 = self.get_graph(self.acc_fun49, BLUE)
        sum_graph49.set_height(5, stretch = True)
        term_num[48].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph49), Transform(term_num[0],term_num[48]))
        self.wait(1)

        sum_graph50 = self.get_graph(self.acc_fun50, BLUE)
        sum_graph50.set_height(5, stretch = True)
        term_num[49].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph50), Transform(term_num[0],term_num[49]))
        self.wait(1)

        sum_graph51 = self.get_graph(self.acc_fun51, BLUE)
        sum_graph51.set_height(5, stretch = True)
        term_num[50].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph51), Transform(term_num[0],term_num[50]))
        self.wait(1)

        sum_graph52 = self.get_graph(self.acc_fun52, BLUE)
        sum_graph52.set_height(5, stretch = True)
        term_num[51].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph52), Transform(term_num[0],term_num[51]))
        self.wait(1)

        sum_graph53 = self.get_graph(self.acc_fun53, BLUE)
        sum_graph53.set_height(5, stretch = True)
        term_num[52].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph53), Transform(term_num[0],term_num[52]))
        self.wait(1)

        sum_graph54 = self.get_graph(self.acc_fun54, BLUE)
        sum_graph54.set_height(5, stretch = True)
        term_num[53].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph54), Transform(term_num[0],term_num[53]))
        self.wait(1)

        sum_graph55 = self.get_graph(self.acc_fun55, BLUE)
        sum_graph55.set_height(5, stretch = True)
        term_num[54].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph55), Transform(term_num[0],term_num[54]))
        self.wait(1)

        sum_graph56 = self.get_graph(self.acc_fun56, BLUE)
        sum_graph56.set_height(5, stretch = True)
        term_num[55].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph56), Transform(term_num[0],term_num[55]))
        self.wait(1)

        sum_graph57 = self.get_graph(self.acc_fun57, BLUE)
        sum_graph57.set_height(5, stretch = True)
        term_num[56].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph57), Transform(term_num[0],term_num[56]))
        self.wait(1)

        sum_graph58 = self.get_graph(self.acc_fun58, BLUE)
        sum_graph58.set_height(5, stretch = True)
        term_num[57].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph58), Transform(term_num[0],term_num[57]))
        self.wait(1)

        sum_graph59 = self.get_graph(self.acc_fun59, BLUE)
        sum_graph59.set_height(5, stretch = True)
        term_num[58].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph59), Transform(term_num[0],term_num[58]))
        self.wait(1)

        sum_graph60 = self.get_graph(self.acc_fun60, BLUE)
        sum_graph60.set_height(5, stretch = True)
        term_num[59].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph60), Transform(term_num[0],term_num[59]))
        self.wait(1)

        sum_graph61 = self.get_graph(self.acc_fun61, BLUE)
        sum_graph61.set_height(5, stretch = True)
        term_num[60].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph61), Transform(term_num[0],term_num[60]))
        self.wait(1)

        sum_graph62 = self.get_graph(self.acc_fun62, BLUE)
        sum_graph62.set_height(5, stretch = True)
        term_num[61].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph62), Transform(term_num[0],term_num[61]))
        self.wait(1)

        sum_graph63 = self.get_graph(self.acc_fun63, BLUE)
        sum_graph63.set_height(5, stretch = True)
        term_num[62].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph63), Transform(term_num[0],term_num[62]))
        self.wait(1)

        sum_graph64 = self.get_graph(self.acc_fun64, BLUE)
        sum_graph64.set_height(5, stretch = True)
        term_num[63].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph64), Transform(term_num[0],term_num[63]))
        self.wait(1)

        sum_graph65 = self.get_graph(self.acc_fun65, BLUE)
        sum_graph65.set_height(5, stretch = True)
        term_num[64].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph65), Transform(term_num[0],term_num[64]))
        self.wait(1)

        sum_graph66 = self.get_graph(self.acc_fun66, BLUE)
        sum_graph66.set_height(5, stretch = True)
        term_num[65].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph66), Transform(term_num[0],term_num[65]))
        self.wait(1)

        sum_graph67 = self.get_graph(self.acc_fun67, BLUE)
        sum_graph67.set_height(5, stretch = True)
        term_num[66].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph67), Transform(term_num[0],term_num[66]))
        self.wait(1)

        sum_graph68 = self.get_graph(self.acc_fun68, BLUE)
        sum_graph68.set_height(5, stretch = True)
        term_num[67].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph68), Transform(term_num[0],term_num[67]))
        self.wait(1)

        sum_graph69 = self.get_graph(self.acc_fun69, BLUE)
        sum_graph69.set_height(5, stretch = True)
        term_num[68].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph69), Transform(term_num[0],term_num[68]))
        self.wait(1)

        sum_graph70 = self.get_graph(self.acc_fun70, BLUE)
        sum_graph70.set_height(5, stretch = True)
        term_num[69].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph70), Transform(term_num[0],term_num[69]))
        self.wait(1)

        sum_graph71 = self.get_graph(self.acc_fun71, BLUE)
        sum_graph71.set_height(5, stretch = True)
        term_num[70].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph71), Transform(term_num[0],term_num[70]))
        self.wait(1)

        sum_graph72 = self.get_graph(self.acc_fun72, BLUE)
        sum_graph72.set_height(5, stretch = True)
        term_num[71].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph72), Transform(term_num[0],term_num[71]))
        self.wait(1)

        sum_graph73 = self.get_graph(self.acc_fun73, BLUE)
        sum_graph73.set_height(5, stretch = True)
        term_num[72].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph73), Transform(term_num[0],term_num[72]))
        self.wait(1)

        sum_graph74 = self.get_graph(self.acc_fun74, BLUE)
        sum_graph74.set_height(5, stretch = True)
        term_num[73].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph74), Transform(term_num[0],term_num[73]))
        self.wait(1)

        sum_graph75 = self.get_graph(self.acc_fun75, BLUE)
        sum_graph75.set_height(5, stretch = True)
        term_num[74].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph75), Transform(term_num[0],term_num[74]))
        self.wait(1)

        sum_graph76 = self.get_graph(self.acc_fun76, BLUE)
        sum_graph76.set_height(5, stretch = True)
        term_num[75].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph76), Transform(term_num[0],term_num[75]))
        self.wait(1)

        sum_graph77 = self.get_graph(self.acc_fun77, BLUE)
        sum_graph77.set_height(5, stretch = True)
        term_num[76].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph77), Transform(term_num[0],term_num[76]))
        self.wait(1)

        sum_graph78 = self.get_graph(self.acc_fun78, BLUE)
        sum_graph78.set_height(5, stretch = True)
        term_num[77].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph78), Transform(term_num[0],term_num[77]))
        self.wait(1)

        sum_graph79 = self.get_graph(self.acc_fun79, BLUE)
        sum_graph79.set_height(5, stretch = True)
        term_num[78].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph79), Transform(term_num[0],term_num[78]))
        self.wait(1)

        sum_graph80 = self.get_graph(self.acc_fun80, BLUE)
        sum_graph80.set_height(5, stretch = True)
        term_num[79].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph80), Transform(term_num[0],term_num[79]))
        self.wait(1)

        sum_graph81 = self.get_graph(self.acc_fun81, BLUE)
        sum_graph81.set_height(5, stretch = True)
        term_num[80].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph81), Transform(term_num[0],term_num[80]))
        self.wait(1)

        sum_graph82 = self.get_graph(self.acc_fun82, BLUE)
        sum_graph82.set_height(5, stretch = True)
        term_num[81].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph82), Transform(term_num[0],term_num[81]))
        self.wait(1)

        sum_graph83 = self.get_graph(self.acc_fun83, BLUE)
        sum_graph83.set_height(5, stretch = True)
        term_num[82].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph83), Transform(term_num[0],term_num[82]))
        self.wait(1)

        sum_graph84 = self.get_graph(self.acc_fun84, BLUE)
        sum_graph84.set_height(5, stretch = True)
        term_num[83].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph84), Transform(term_num[0],term_num[83]))
        self.wait(1)

        sum_graph85 = self.get_graph(self.acc_fun85, BLUE)
        sum_graph85.set_height(5, stretch = True)
        term_num[84].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph85), Transform(term_num[0],term_num[84]))
        self.wait(1)

        sum_graph86 = self.get_graph(self.acc_fun86, BLUE)
        sum_graph86.set_height(5, stretch = True)
        term_num[85].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph86), Transform(term_num[0],term_num[85]))
        self.wait(1)

        sum_graph87 = self.get_graph(self.acc_fun87, BLUE)
        sum_graph87.set_height(5, stretch = True)
        term_num[86].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph87), Transform(term_num[0],term_num[86]))
        self.wait(1)

        sum_graph88 = self.get_graph(self.acc_fun88, BLUE)
        sum_graph88.set_height(5, stretch = True)
        term_num[87].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph88), Transform(term_num[0],term_num[87]))
        self.wait(1)

        sum_graph89 = self.get_graph(self.acc_fun89, BLUE)
        sum_graph89.set_height(5, stretch = True)
        term_num[88].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph89), Transform(term_num[0],term_num[88]))
        self.wait(1)

        sum_graph90 = self.get_graph(self.acc_fun90, BLUE)
        sum_graph90.set_height(5, stretch = True)
        term_num[89].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph90), Transform(term_num[0],term_num[89]))
        self.wait(1)

        sum_graph91 = self.get_graph(self.acc_fun91, BLUE)
        sum_graph91.set_height(5, stretch = True)
        term_num[90].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph91), Transform(term_num[0],term_num[90]))
        self.wait(1)

        sum_graph92 = self.get_graph(self.acc_fun92, BLUE)
        sum_graph92.set_height(5, stretch = True)
        term_num[91].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph92), Transform(term_num[0],term_num[91]))
        self.wait(1)

        sum_graph93 = self.get_graph(self.acc_fun93, BLUE)
        sum_graph93.set_height(5, stretch = True)
        term_num[92].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph93), Transform(term_num[0],term_num[92]))
        self.wait(1)

        sum_graph94 = self.get_graph(self.acc_fun94, BLUE)
        sum_graph94.set_height(5, stretch = True)
        term_num[93].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph94), Transform(term_num[0],term_num[93]))
        self.wait(1)

        sum_graph95 = self.get_graph(self.acc_fun95, BLUE)
        sum_graph95.set_height(5, stretch = True)
        term_num[94].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph95), Transform(term_num[0],term_num[94]))
        self.wait(1)

        sum_graph96 = self.get_graph(self.acc_fun96, BLUE)
        sum_graph96.set_height(5, stretch = True)
        term_num[95].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph96), Transform(term_num[0],term_num[95]))
        self.wait(1)

        sum_graph97 = self.get_graph(self.acc_fun97, BLUE)
        sum_graph97.set_height(5, stretch = True)
        term_num[96].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph97), Transform(term_num[0],term_num[96]))
        self.wait(1)

        sum_graph98 = self.get_graph(self.acc_fun98, BLUE)
        sum_graph98.set_height(5, stretch = True)
        term_num[97].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph98), Transform(term_num[0],term_num[97]))
        self.wait(1)

        sum_graph99 = self.get_graph(self.acc_fun99, BLUE)
        sum_graph99.set_height(5, stretch = True)
        term_num[98].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph99), Transform(term_num[0],term_num[98]))
        self.wait(1)

        sum_graph100 = self.get_graph(self.acc_fun100, BLUE)
        sum_graph100.set_height(5, stretch = True)
        term_num[99].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph100), Transform(term_num[0],term_num[99]))
        self.wait(1)




    def fun1(self, x):
        phi0 = -60*PI/180;
        return np.cos(2*PI*100*x + phi0) #f = 100Hz

    def fun2(self, x):
        phi0 = -60*PI/180;
        return np.cos(2*PI*900*x - phi0) #f = 900Hz

    def fun3(self, x):
        phi0 = -60*PI/180;
        return np.cos(2*PI*1100*x + phi0) #f = 1100Hz

    def fun4(self, x):
        phi0 = -60*PI/180;
        return np.cos(2*PI*1900*x - phi0) #f = 1900Hz

    def fun_gen(self,k,x):
        phi0 = -60*PI/180;
        return [np.cos(2*PI*(100- 1000*k)*x + phi0), np.cos(2*PI*(100+1000*k)*x + phi0)]

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

    def acc_fun6(self,x):
        k=6
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

    def acc_fun7(self,x):
        k=7
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

    def acc_fun8(self,x):
        k=8
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

    def acc_fun9(self,x):
        k=9
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

    def acc_fun10(self,x):
        k=10
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

    def acc_fun11(self,x):
        k=11
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

    def acc_fun12(self,x):
        k=12
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

    def acc_fun13(self,x):
        k=13
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

    def acc_fun14(self,x):
        k=14
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

    def acc_fun15(self,x):
        k=15
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

    def acc_fun16(self,x):
        k=16
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

    def acc_fun17(self,x):
        k=17
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

    def acc_fun18(self,x):
        k=18
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

    def acc_fun19(self,x):
        k=19
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

    def acc_fun20(self,x):
        k=20
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

    def acc_fun21(self,x):
        k=21
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

    def acc_fun22(self,x):
        k=22
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

    def acc_fun23(self,x):
        k=23
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

    def acc_fun24(self,x):
        k=24
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

    def acc_fun25(self,x):
        k=25
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

    def acc_fun26(self,x):
        k=26
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

    def acc_fun27(self,x):
        k=27
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

    def acc_fun28(self,x):
        k=28
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

    def acc_fun29(self,x):
        k=29
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

    def acc_fun30(self,x):
        k=30
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

    def acc_fun31(self,x):
        k=31
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

    def acc_fun32(self,x):
        k=32
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

    def acc_fun33(self,x):
        k=33
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

    def acc_fun34(self,x):
        k=34
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

    def acc_fun35(self,x):
        k=35
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

    def acc_fun36(self,x):
        k=36
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

    def acc_fun37(self,x):
        k=37
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

    def acc_fun38(self,x):
        k=38
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

    def acc_fun39(self,x):
        k=39
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

    def acc_fun40(self,x):
        k=40
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

    def acc_fun41(self,x):
        k=41
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

    def acc_fun42(self,x):
        k=42
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

    def acc_fun43(self,x):
        k=43
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

    def acc_fun44(self,x):
        k=44
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

    def acc_fun45(self,x):
        k=45
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

    def acc_fun46(self,x):
        k=46
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

    def acc_fun47(self,x):
        k=47
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

    def acc_fun48(self,x):
        k=48
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

    def acc_fun49(self,x):
        k=49
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

    def acc_fun50(self,x):
        k=50
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

    def acc_fun51(self,x):
        k=51
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

    def acc_fun52(self,x):
        k=52
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

    def acc_fun53(self,x):
        k=53
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

    def acc_fun54(self,x):
        k=54
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

    def acc_fun55(self,x):
        k=55
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

    def acc_fun56(self,x):
        k=56
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

    def acc_fun57(self,x):
        k=57
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

    def acc_fun58(self,x):
        k=58
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

    def acc_fun59(self,x):
        k=59
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

    def acc_fun60(self,x):
        k=60
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

    def acc_fun61(self,x):
        k=61
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

    def acc_fun62(self,x):
        k=62
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

    def acc_fun63(self,x):
        k=63
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

    def acc_fun64(self,x):
        k=64
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

    def acc_fun65(self,x):
        k=65
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

    def acc_fun66(self,x):
        k=66
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

    def acc_fun67(self,x):
        k=67
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

    def acc_fun68(self,x):
        k=68
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

    def acc_fun69(self,x):
        k=69
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

    def acc_fun70(self,x):
        k=70
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

    def acc_fun71(self,x):
        k=71
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

    def acc_fun72(self,x):
        k=72
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

    def acc_fun73(self,x):
        k=73
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

    def acc_fun74(self,x):
        k=74
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

    def acc_fun75(self,x):
        k=75
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

    def acc_fun76(self,x):
        k=76
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

    def acc_fun77(self,x):
        k=77
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

    def acc_fun78(self,x):
        k=78
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

    def acc_fun79(self,x):
        k=79
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

    def acc_fun80(self,x):
        k=80
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

    def acc_fun81(self,x):
        k=81
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

    def acc_fun82(self,x):
        k=82
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

    def acc_fun83(self,x):
        k=83
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

    def acc_fun84(self,x):
        k=84
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

    def acc_fun85(self,x):
        k=85
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

    def acc_fun86(self,x):
        k=86
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

    def acc_fun87(self,x):
        k=87
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

    def acc_fun88(self,x):
        k=88
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

    def acc_fun89(self,x):
        k=89
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

    def acc_fun90(self,x):
        k=90
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

    def acc_fun91(self,x):
        k=91
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

    def acc_fun92(self,x):
        k=92
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

    def acc_fun93(self,x):
        k=93
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

    def acc_fun94(self,x):
        k=94
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

    def acc_fun95(self,x):
        k=95
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

    def acc_fun96(self,x):
        k=96
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

    def acc_fun97(self,x):
        k=97
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

    def acc_fun98(self,x):
        k=98
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

    def acc_fun99(self,x):
        k=99
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

    def acc_fun100(self,x):
        k=100
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

