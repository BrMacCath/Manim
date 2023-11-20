from manim import *
import numpy as np


# This will just introduce our problem. Its purpose is to 
# layout what we will be doing.
class Introduction(Scene):
    def construct(self):
        # Introduction
        IntroText = Tex("Introduction")
        self.add(IntroText)
        self.wait(1)

        # Layout
        ## Table of contents


        ## Method of talking about this


class EigenVectors(Scene):
    def construct(self):
        # Here we will first talk about Eigenvectors


        # Properties of the first ellipse
        height_1 = ValueTracker(1)
        width_1 = ValueTracker(1)
        c_1x =ValueTracker(-4)
        c_1y =ValueTracker(-1)
        angle_1 = ValueTracker(0)
        ellipse_1 =  always_redraw(lambda: Ellipse(width=1.5*width_1.get_value(), height=1.5*height_1.get_value()).rotate(angle=angle_1.get_value()).shift(c_1x.get_value()*RIGHT+ c_1y.get_value()*UP))
        ax_1 = always_redraw(lambda: Axes(
            x_length=4,
            y_length=4,
            axis_config={"include_ticks": False}
        ).shift(c_1x.get_value()*RIGHT+ c_1y.get_value()*UP))
        # This is going to represent the eigenvector. It is needs to be defined in terms of the the center of the ellipse.
        vect_1 = always_redraw(lambda: Line(start=ellipse_1.get_center(),end=ellipse_1.get_center()+[1.5*height_1.get_value()*np.cos(PI/2 + angle_1.get_value())/2,1.5*height_1.get_value()*np.sin(PI/2 + angle_1.get_value())/2,0]).add_tip())

        # This will be the Matrices that talk about the action
        lamMatrix = always_redraw(lambda:DecimalMatrix([[height_1.get_value(),0],[0,width_1.get_value()]]).shift(2*UP))
        inputMat = DecimalMatrix([[1],[2]]).next_to(lamMatrix,direction=RIGHT)
        outputMat = DecimalMatrix([[1],[2]]).next_to(lamMatrix,direction=LEFT)
        columns = lamMatrix.get_columns()
        self.add(ellipse_1,vect_1,lamMatrix.get_brackets(),inputMat,outputMat,ax_1)
        self.play(angle_1.animate.set_value(PI/2))
        self.wait(1)
        self.play(FadeIn(columns[0]))
        self.wait(1)


class SingularValues(Scene):
    # Here we will introduce singular values. Go Through 
    # an easy example
    def construct(self):
        ## First a scene where they are introduced


        ## Then a scene where we can go through an easy example involving
        ## rotations and stretches. 
        pass


class PCA(Scene):
    def construct(self):
        pass
