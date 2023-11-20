from typing import Callable
from manim import *
from manim.animation.animation import DEFAULT_ANIMATION_LAG_RATIO, DEFAULT_ANIMATION_RUN_TIME
from manim.mobject.mobject import Mobject
from manim.scene.scene import Scene
from manim.utils.rate_functions import smooth
import numpy as np


# This will just introduce our problem. Its purpose is to 
# layout what we will be doing.
class Introduction(Scene):
    def construct(self):
        # Introduction
        self.wait(1)
        self.play(TitleCards(Tex("Introduction").scale(3).shift(2*UP)),run_time=2)
        self.wait(2)

        # Layout
        ## Table of contents
        self.play(TitleCards(Tex("Table of contents").shift(3*UP)),TitleCards(Tex("1. Eigenvalues").align_on_border(LEFT).shift(2*UP + 2.5*RIGHT)),TitleCards(Tex("2. Singular Value Decomposition").align_on_border(LEFT).shift(1*UP + 2.5*RIGHT)),TitleCards(Tex("3. Principal Component Analysis.").align_on_border(LEFT ).shift(2.5*RIGHT)),lag_ratio=.5,run_time=10)
        ## Method of talking about this


class EigenVectors(Scene):
    def construct(self):
        # Here we will first talk about Eigenvectors
        self.wait(1)
        self.play(TitleCards(Tex("Eigen values").scale(3).shift(2*UP)),run_time=2)

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
        # Try to create a visual reason to look at PCA. 
        # Go through an example with 3 points that 
        # highlight the reason for PCA. Show that 
        # singular values are needed here sometimes.
        pass

class TitleCards(Animation):

    def begin(self) -> None:
        start = UL
        self.mobject.set_opacity(0)
        super().begin()
    
    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
        scene.remove(self.mobject)

    def interpolate_mobject(self, alpha: float) -> None:
        if alpha < .33:
            self.mobject.set_opacity(3*alpha)
        elif alpha <.66:
            self.mobject.set_opacity(1)
        else:
            self.mobject.set_opacity(3-3*alpha)
        
