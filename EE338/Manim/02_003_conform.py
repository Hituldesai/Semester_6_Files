from manimlib.imports import *

def conformal_transform(point):
	z = R3_to_complex(point)
	return complex_to_R3(np.power(z,2)/2)

class ConformTest(Scene):
    def construct(self):
    	grid   = NumberPlane()
    	circle = Circle(color = RED)
    	self.add(grid)
    	self.play(ShowCreation(circle))
    	grid.prepare_for_nonlinear_transform()
    	self.play(grid.apply_function, conformal_transform, circle.apply_function, conformal_transform, run_time = 5)
