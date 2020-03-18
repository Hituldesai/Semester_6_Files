#!/usr/bin/env python

import sys
if '/opt/ros/kinetic/lib/python2.7/dist-packages' in sys.path: sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

from manimlib.imports import *

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
        term_num = [TexMobject("\\# terms = " + str(n)) for n in range(1,12)]
        sum_graph1 = self.get_graph(self.acc_fun1, BLUE)
        sum_graph1.set_height(5, stretch = True)
        term_num[0].shift(3*DOWN)
        self.play(ShowCreation(first_graph), ShowCreation(term_num[0]))
        self.wait(2)
        sum_graph2 = self.get_graph(self.acc_fun2, BLUE)
        sum_graph2.set_height(5, stretch = True)
        term_num[1].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph2), Transform(term_num[0],term_num[1]))
        self.wait(2)
        sum_graph3 = self.get_graph(self.acc_fun3, BLUE)
        sum_graph3.set_height(5, stretch = True)
        term_num[2].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph3), Transform(term_num[0],term_num[2]))
        self.wait(2)
        sum_graph4 = self.get_graph(self.acc_fun4, BLUE)
        sum_graph4.set_height(5, stretch = True)
        term_num[3].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph4), Transform(term_num[0],term_num[3]))
        self.wait(2)
        sum_graph5 = self.get_graph(self.acc_fun5, BLUE)
        sum_graph5.set_height(5, stretch = True)
        term_num[4].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph5), Transform(term_num[0],term_num[4]))
        self.wait(2)
        sum_graph6 = self.get_graph(self.acc_fun6, BLUE)
        sum_graph6.set_height(5, stretch = True)
        term_num[5].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph6), Transform(term_num[0],term_num[5]))
        self.wait(2)
        sum_graph7 = self.get_graph(self.acc_fun7, BLUE)
        sum_graph7.set_height(5, stretch = True)
        term_num[6].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph7), Transform(term_num[0],term_num[6]))
        self.wait(2)
        sum_graph8 = self.get_graph(self.acc_fun8, BLUE)
        sum_graph8.set_height(5, stretch = True)
        term_num[7].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph8), Transform(term_num[0],term_num[7]))
        self.wait(2)
        sum_graph9 = self.get_graph(self.acc_fun9, BLUE)
        sum_graph9.set_height(5, stretch = True)
        term_num[8].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph9), Transform(term_num[0],term_num[8]))
        self.wait(2)
        sum_graph10 = self.get_graph(self.acc_fun10, BLUE)
        sum_graph10.set_height(5, stretch = True)
        term_num[9].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph10), Transform(term_num[0],term_num[9]))
        self.wait(2)
        sum_graph11 = self.get_graph(self.acc_fun11, BLUE)
        sum_graph11.set_height(5, stretch = True)
        term_num[10].shift(3*DOWN)
        self.play(Transform(first_graph, sum_graph11), Transform(term_num[0],term_num[10]))
        self.wait(2)


        # main_graph1=self.get_graph(self.fun1,RED)
        # vert_lines = self.get_vertical_lines_to_graph(main_graph1,0,0.01,11,color=YELLOW)
        # sample_points = []
        # for x in range(11):
        #     sample_points.append(Dot(self.coords_to_point(0.001*x, self.fun1(0.001*x))))
        # dots = VGroup(*sample_points)
        # graph_lab1 = self.get_graph_label(main_graph1, label = "\\cos(2 \\pi 100 x -60^o)")
        # graph_lab1.shift(LEFT + UP)
        # full_diagram = VGroup(self.axes, main_graph1, vert_lines, dots, graph_lab1)
        # full_diagram.stretch_to_fit_width(FRAME_WIDTH - 2)
        # self.play(ShowCreation(full_diagram))
        # self.wait(1)
        # self.play(ShowCreation(vert_lines))
        # self.wait(1)
        # self.play(ShowCreation(dots))
        # self.wait(1)

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
        return [np.cos(2*PI*(1000*k - 100)*x - phi0), np.cos(2*PI*(1000*k + 100)*x + phi0)]

    def acc_fun1(self,x):
        k=1
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun2(self,x):
        k=2
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun3(self,x):
        k=3
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun4(self,x):
        k=4
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun5(self,x):
        k=5
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun6(self,x):
        k=6
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun7(self,x):
        k=7
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun8(self,x):
        k=8
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun9(self,x):
        k=9
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun10(self,x):
        k=10
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc

    def acc_fun11(self,x):
        k=11
        phi0 = -60*PI/180;
        t0 = np.cos(2*PI*100*x + phi0)
        acc = t0
        m = int((k-1)/2)
        if((k-1)%2==0):
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
        else:
            for i in range(m):
                acc = acc + self.fun_gen(m,x)[0] + self.fun_gen(m,x)[1]
            acc = acc + self.fun_gen(m+1,x)[0]
        return acc