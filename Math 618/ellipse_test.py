from manim import *
import numpy as np
class EllipseExample(Scene):
    def construct(self):
        # Properties of the first ellipse
        height_1 = ValueTracker(1)
        width_1 = ValueTracker(1)
        c_1x =ValueTracker(0)
        c_1y =ValueTracker(0)
        angle_1 = ValueTracker(0)
        ellipse_1 =  always_redraw(lambda: Ellipse(width=width_1.get_value(), height=height_1.get_value()).rotate(angle=angle_1.get_value()).shift(c_1x.get_value()*RIGHT+ c_1y.get_value()*UP))

        # This is going to represent the eigenvector. It is needs to be defined in terms of the the center of the ellipse.
        vect_1 = always_redraw(lambda: Line(start=ellipse_1.get_center(),end=ellipse_1.get_center()+[height_1.get_value()*np.cos(PI/2 + angle_1.get_value())/2,height_1.get_value()*np.sin(PI/2 + angle_1.get_value())/2,0]).add_tip())

        # This will be the Matrices that talk about the action
        lamMatrix = always_redraw(lambda:DecimalMatrix([[height_1.get_value(),0],[0,width_1.get_value()]]).shift(2*UP))
        testMat = DecimalMatrix([[1],[2]]).next_to(lamMatrix,direction=RIGHT)
        testMat2 = DecimalMatrix([[1],[2]]).next_to(lamMatrix,direction=LEFT)
        self.add(ellipse_1,vect_1,lamMatrix,testMat,testMat2)
        self.play(height_1.animate.set_value(6), width_1.animate.set_value(4),run_time=4)
        self.wait(1)
        self.play(angle_1.animate.set_value(PI/2))
        self.wait(1)
        # self.add(Ellipse(width=width_1.get_value(), height=height_1.get_value()).rotate(angle=angle.get_value()))
        self.play(width_1.animate.set_value(7),rate_func=linear)
        self.wait(1)
        self.add(ellipse_1)
        self.wait(1)
        self.play(width_1.animate.set_value(1), height_1.animate.set_value(1),c_1x.animate.set_value(-2),c_1y.animate.set_value(2))
        self.wait(1)
