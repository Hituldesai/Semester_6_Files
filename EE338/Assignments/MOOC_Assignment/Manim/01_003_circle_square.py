from manimlib.imports import *

class CreateBox(Scene):
    def construct(self):
        sq = Square()
        cc = Circle()
        cc.shift(3*RIGHT + 3*UP)
        sq.shift(2*LEFT  + 2*DOWN)
        self.play(ShowCreation(sq), ShowCreation(cc))
        self.wait(2)
