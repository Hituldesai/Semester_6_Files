from manimlib.imports import *

class TestManimInstallation(Scene):
    def construct(self):
        circle = Circle()
        texts = TexMobject(r"e^{i\pi} = -1")
        self.play(ShowCreation(circle))
        self.play(Transform(circle, texts))
        self.wait(2)
