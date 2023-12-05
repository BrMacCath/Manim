from typing import Callable
from manim import *
from manim.animation.animation import DEFAULT_ANIMATION_LAG_RATIO, DEFAULT_ANIMATION_RUN_TIME
from manim.mobject.mobject import Mobject
from manim.scene.scene import Scene
from manim.utils.rate_functions import smooth
import numpy as np
import matplotlib.pyplot as plt


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
        self.play(TitleCards(Tex("Table of contents").shift(3*UP)),TitleCards(Tex("1. Eigenvalues").align_on_border(LEFT).shift(2*UP + 2.5*RIGHT)),TitleCards(Tex("2. Singular Value Decomposition").align_on_border(LEFT).shift(1*UP + 2.5*RIGHT)),TitleCards(Tex("3. Principal Component Analysis.").align_on_border(LEFT ).shift(2.5*RIGHT)),TitleCards(Tex("4. Kernel PCA").align_on_border(LEFT).shift(-1*UP + 2.5*RIGHT)),lag_ratio=.5,run_time=10)
        ## Method of talking about this


class EigenVectors(Scene):
    def construct(self):
        # Here we will first talk about Eigenvectors
        self.wait(1)
        self.play(TitleCards(Tex("EigenVectors").scale(3).shift(2*UP)),run_time=2)

        # Properties of the first ellipse
        height_1 = ValueTracker(1)
        width_1 = ValueTracker(1)
        c_1x = ValueTracker(-4)
        c_1y = ValueTracker(-1)
        c_2x = ValueTracker(4)
        c_2y= ValueTracker(-1)
        angle_1 = ValueTracker(0)
        ellipse_1 =  always_redraw(lambda: Ellipse(width=1.5, height=1.5).rotate(angle=angle_1.get_value()).shift(c_1x.get_value()*RIGHT+ c_1y.get_value()*UP))
        ellipse_2 =  always_redraw(lambda: Ellipse(width=1.5*width_1.get_value(), height=1.5*height_1.get_value()).rotate(angle=angle_1.get_value()).shift(c_2x.get_value()*RIGHT+ c_2y.get_value()*UP))
        ax_1 = always_redraw(lambda: Axes(
            x_length=4,
            y_length=4,
            axis_config={"include_ticks": False}
        ).shift(c_1x.get_value()*RIGHT+ c_1y.get_value()*UP))
        ax_2 = always_redraw(lambda: Axes(
            x_length=4,
            y_length=4,
            axis_config={"include_ticks": False}
        ).shift(c_2x.get_value()*RIGHT+ c_2y.get_value()*UP))
        # This is going to represent the eigenvector. It is needs to be defined in terms of the the center of the ellipse.
        vect_1 = always_redraw(lambda: Line(start=ellipse_1.get_center(),end=ellipse_1.get_center()+[1.5*np.cos(PI/2 + angle_1.get_value())/2,1.5*np.sin(PI/2 + angle_1.get_value())/2,0]).add_tip())
        vect_2 = always_redraw(lambda:Line(start=ellipse_1.get_center(),end=ellipse_1.get_center()+[1.5*np.cos( angle_1.get_value())/2,1.5*np.sin( angle_1.get_value())/2,0]).add_tip())
        # This will be the Matrices that talk about the action
        lamMatrix = always_redraw(lambda:DecimalMatrix([[height_1.get_value(),0],[0,width_1.get_value()]]).shift(2*UP))
        inputMat = Matrix([["v_1^T"],["v_2^T"]]).next_to(lamMatrix,direction=RIGHT)
        outputMat = Matrix([["v_1"],["v_2"]]).next_to(lamMatrix,direction=LEFT)

        TempMatrix = MathTex(r"\begin{bmatrix}"
                             r"a & b\\"
                             r"c & d"
                             r"\end{bmatrix}").shift(2*UP)
        self.play(Create(TempMatrix))

        self.wait(3)
        
        self.play(Create(ax_1),run_time=2)
        self.play(GrowFromCenter(ellipse_1),run_time=2)
        self.play(Create(vect_1),Create(vect_2),run_time=2)
        self.play(Create(ax_2), run_time=3)
        self.play(GrowFromCenter(ellipse_2),run_time=2)
        
        self.play(angle_1.animate.set_value(PI/4))
        out_1 = vect_1.copy()
        out_2 = vect_2.copy()
        self.add(out_1)
        self.add(out_2)
        

        out_1.clear_updaters()
        out_2.clear_updaters()
        self.play(out_1.animate.shift(  (c_2x.get_value()-c_1x.get_value())*RIGHT  ),out_2.animate.shift(  (c_2x.get_value()-c_1x.get_value())*RIGHT  ))

        outvec_1 =always_redraw(lambda: Line(ellipse_2.get_center(),end=ellipse_2.get_center()+[1.5*height_1.get_value()*np.cos(PI/2 + angle_1.get_value())/2,1.5*height_1.get_value()*np.sin(PI/2 + angle_1.get_value())/2,0]).add_tip())
        outvec_2 =always_redraw(lambda: Line(ellipse_2.get_center(),end=ellipse_2.get_center()+[1.5*width_1.get_value()*np.cos( angle_1.get_value())/2,1.5*width_1.get_value()*np.sin(PI/2 + angle_1.get_value())/2,0]).add_tip())
        self.remove(out_1,out_2 )
        self.add(outvec_1,outvec_2)
        self.play(FadeOut(TempMatrix))


        # Inputs and Outpus
        self.add(inputMat,outputMat)

        self.play(Create(lamMatrix.get_brackets()))
        
        self.wait(1)
        self.play(FadeIn(lamMatrix.get_columns()))
        self.wait(1)

        self.play(height_1.animate.set_value(2))
        self.wait(1)
        self.play(width_1.animate.set_value(0.5))
        self.wait(1)


class SingularValues(Scene):
    # Here we will introduce singular values. Go Through 
    # an easy example
    def construct(self):
        ## First a scene where they are introduced
        self.play(TitleCards(Tex("Singular Value Decomposition").scale(2).shift(2*UP)),run_time=2)
        ax = Axes(
            x_length=6,
            y_length=6,
            axis_config={"include_ticks": False}
        )
        orig = ax.get_center()
        shear = Polygon(orig +[2,1,0], orig +[1,1,0], orig ,orig  +[1,0,0])
        square = Square(side_length=1,color="blue")
        square.shift(square.get_left()*LEFT + square.get_bottom()*DOWN)
        orig_square = square.copy()
        self.add(ax)
        self.wait(2)
        self.add(square)
        self.wait(2)
        self.play(Rotate(square,angle=PI/4,about_point=ax.get_origin()))
        self.wait(2)
        self.play(Rotate(square,angle=-PI/4,about_point=ax.get_origin()))
        self.wait(2)
        self.play(Transform(square,shear))
        self.wait(2)
        self.play(Transform(square,orig_square))
        self.wait(2)
        self.play(FadeOut(ax,square))
        ## Then a scene where we can go through an easy example involving
        ## rotations and stretches. 
        self.remove(square,shear,ax,orig_square)

        TempMatrix = MathTex(r"\begin{bmatrix}"
                             r"a & b\\"
                             r"c & d"
                             r"\end{bmatrix}").shift(2*UP)

        ax_1 = always_redraw(lambda: Axes(
            x_length=4,
            y_length=4,
            axis_config={"include_ticks": False}
        ).shift(-4*RIGHT-1*UP))
        ax_2 = always_redraw(lambda: Axes(
            x_length=4,
            y_length=4,
            axis_config={"include_ticks": False}
        ).shift(4*RIGHT-1*UP))

        self.play(FadeIn(ax_1),FadeIn(ax_2),FadeIn(TempMatrix))

        self.wait(2)
        height_1 = ValueTracker(1)
        width_1 = ValueTracker(1)
        lamMatrix = always_redraw(lambda:DecimalMatrix([[width_1.get_value(),0],[0,height_1.get_value()]]).shift(2*UP))
        inputMat = Matrix([["u_1^T"],["u_2^T"]]).next_to(lamMatrix,direction=RIGHT)
        outputMat = Matrix([["v_1"],["v_2"]]).next_to(lamMatrix,direction=LEFT)

        self.play(FadeOut(TempMatrix))
        self.play(FadeIn(lamMatrix.get_brackets()),FadeIn(inputMat.get_brackets()),FadeIn(outputMat.get_brackets()))

        self.wait(3)
        # Add Ellipses
        angle_1 = ValueTracker(0)
        angle_2 = ValueTracker(PI/8)
        ellipse_1 = Ellipse(width=1.5, height=1.5).shift(ax_1.get_center())
        ellipse_2 = always_redraw(lambda: Ellipse(width=1.5*width_1.get_value(), height=1.5*height_1.get_value()).rotate(angle=angle_2.get_value()).shift(ax_2.get_center()))
        self.add(ellipse_1,ellipse_2)
        self.wait(2)

        in_1 = always_redraw(lambda: Line(ellipse_1.get_center(),end=ellipse_1.get_center()+[1.5*np.cos(angle_1.get_value())/2,1.5*np.sin(angle_1.get_value())/2,0]).add_tip())
        in_2 =always_redraw(lambda: Line(ellipse_1.get_center(),end=ellipse_1.get_center()+[1.5*np.cos(PI/2 + angle_1.get_value())/2,1.5*np.sin(PI/2 + angle_1.get_value())/2,0]).add_tip())
        self.wait(1)
        self.play(FadeIn(in_1),FadeIn(in_2),FadeIn(inputMat.get_columns()),run_time=3)
        self.wait(2)
        self.play(angle_1.animate.set_value(PI/3))

        # OutLocation()
        outLocation_1 = always_redraw(lambda: Line(ellipse_2.get_center(),end=ellipse_2.get_center()+[1.5*width_1.get_value()*np.cos(angle_2.get_value())/2,1.5*width_1.get_value()*np.sin(angle_2.get_value())/2,0]).add_tip())
        outLocation_2 = always_redraw(lambda: Line(ellipse_2.get_center(),end=ellipse_2.get_center()+[1.5*height_1.get_value()*np.cos(PI/2 + angle_2.get_value())/2,1.5*height_1.get_value()*np.sin(PI/2 + angle_2.get_value())/2,0]).add_tip())

        out_1 = in_1.copy()
        out_2 = in_2.copy()
        self.add(out_1,out_2)
        self.play(ReplacementTransform(out_1,outLocation_1),FadeIn(outputMat.get_rows()[0]))
        self.wait(2)
        self.play(FadeIn(lamMatrix.get_columns()[0]))
        self.wait(3)
        self.play(ReplacementTransform(out_2,outLocation_2),FadeIn(outputMat.get_rows()[1]))
        self.wait(2)
        self.play(FadeIn(lamMatrix.get_columns()[1]))
        self.wait(1)
        self.add(lamMatrix)
        self.play(width_1.animate.set_value(3))

class PCA(Scene):
    def construct(self):
        self.play(TitleCards(Tex("Principal component Analysis").scale(1.5).shift(2*UP)),run_time=2)
        self.wait(3)
        # Plot some points in a linear way
        # def func(x):
        #     ans = .5*x + np.random.random_sample()
        #     return ans
        
        # xs = np.linspace(-4,4, num=100)
        # ys = [func(x) for x in xs]
        arr_loaded = np.load('lineData.npy')
        xs = arr_loaded[0]
        ys = arr_loaded[1]

        ax = Axes(
            x_range=[-5,5],
            y_range=[-5,5]
        )

        Dots =  VGroup(*[
        Dot(ax.c2p(x,y+.7)) for x,y in zip(xs,ys)])

        Dots2 =  VGroup(*[
        always_redraw(lambda:Dot(point=ax.c2p(x,y-.1) + ax.get_origin()))  for x,y in zip(xs,ys)])

        self.add(ax)
        self.wait(2)
        self.add(ax,Dots)
        self.wait(2)
        self.play(Transform(Dots,Dots2))
        self.wait(3)

        vector_svd = always_redraw(lambda: Line(start=ax.get_origin(),end = ax.get_origin()+[1,.4,0],color="green").add_tip())
        self.play(Create(vector_svd))
        self.wait(3)

        # Covariance matrix.
        self.play(FadeOut(ax),FadeOut(vector_svd), FadeOut(Dots))

        self.wait(2)

        self.play(TitleCards(Tex("Inner Products").scale(1.5).shift(2*UP)),run_time=2)
        samples = Tex("X").shift(1*UP)
        innerProducts = Tex(r"$X^T$ $X$")
        MatOriginal = MathTex(r"\begin{bmatrix}"
                                 r"\langle x_i , x_j\rangle"
                                 r"\end{bmatrix}_{ij}").shift(1*DOWN)

        self.play(Create(samples)) 
        self.wait(2)
        self.play(Create(innerProducts))
        self.wait(2)
        self.play(Create(MatOriginal))
        self.wait(2)
        self.play(FadeOut(samples,innerProducts,MatOriginal))

        # Talk about naive basis. How you can collect data.


        # Change basis vectors


        # Talk about cases where it goes wrong.


        # Try to create a visual reason to look at PCA. 
        # Go through an example with 3 points that 
        # highlight the reason for PCA. Show that 
        # singular values are needed here sometimes.
        pass


class KernelPCA(Scene):
    def construct(self):
        self.play(TitleCards(Tex("Kernel PCA").scale(3).shift(2*UP)),run_time=2)
        ax = Axes(
            x_range=[-6,6],
            y_range=[-6,6]
        )
        green = np.load("greenCirc.npy")
        Green_Dots =  VGroup(*[
        Dot(ax.c2p(point[0],point[1]),color="green")  for point in green])
        red = np.load("redCirc.npy")
        Red_Dots =  VGroup(*[
        Dot(ax.c2p(point[0],point[1]),color="red")  for point in red])
        blue = np.load("blueCirc.npy")
        Blue_Dots =  VGroup(*[
        Dot(ax.c2p(point[0],point[1]),color="blue")  for point in blue])

        self.add(ax)
        self.wait(2)
        self.play(FadeIn(Green_Dots,Red_Dots,Blue_Dots))

        self.wait(5)

        self.play(FadeOut(Blue_Dots),FadeOut(Green_Dots),FadeOut(Red_Dots),FadeOut(ax))

        Problems = Tex("Problems").shift(2*UP)
        non_linear = Tex("1. Non Linear").align_on_border(LEFT).shift(1*UP + 2.5*RIGHT)
        not_centered = Tex("2. Not Centered on the origin").align_on_border(LEFT).shift( 2.5*RIGHT)
        self.wait(1)
        self.play(Create(Problems))
        self.wait(2)
        self.play(Create(non_linear))
        self.wait(2) 
        self.play(Create(not_centered))
        self.wait(1)
        self.play(FadeOut(Problems,non_linear,not_centered))

        solution = Tex("Solution?").shift(2*UP)
        change_inner= Tex("Change inner Product").shift(1*UP)
        replace = Tex("Replace $ \langle x, y $" r"$ \rangle$ with $k(x,y)$")
        note = Tex("Note: New Space").shift(1*DOWN)
        note_2 = Tex("Note: New center").shift(2*DOWN)
        self.play(Create(solution))
        self.wait(1)
        self.play(Create(change_inner))
        self.wait(1)
        self.play(Create(replace))
        self.wait(1)
        self.play(Create(note))
        self.wait(1)
        self.play(Create(note_2))
        self.wait(1)
        self.play(FadeOut(solution,change_inner,replace,note,note_2))
        self.wait(1)
        kerMatTex = Tex("Kernel Matrix").shift(2*UP)
        kerMatOriginal = MathTex(r"\begin{bmatrix}"
                                 r"\langle \Phi(x_i) , \Phi(x_j)\rangle"
                                 r"\end{bmatrix}_{ij   }")  
        kerMatKer =  MathTex(r"\begin{bmatrix}"
                                 r"k(x_i,x_j)"
                                 r"\end{bmatrix}_{ij}")                             
        self.play(FadeIn(kerMatTex))
        self.play(FadeIn(kerMatOriginal))

        self.wait(3)
        self.play(Transform(kerMatOriginal,kerMatKer))

        self.play(FadeOut(kerMatTex,kerMatOriginal))



        self.wait(1)

        ax = Axes(
            x_range=[-6,6],
            y_range=[-6,6]
        ).scale(.5).shift(3.5*LEFT)
        green = np.load("greenCirc.npy")
        Green_Dots =  VGroup(*[
        Dot(ax.c2p(point[0],point[1]),color="green")  for point in green])
        red = np.load("redCirc.npy")
        Red_Dots =  VGroup(*[
        Dot(ax.c2p(point[0],point[1]),color="red")  for point in red])
        blue = np.load("blueCirc.npy")
        Blue_Dots =  VGroup(*[
        Dot(ax.c2p(point[0],point[1]),color="blue")  for point in blue])
        self.play(FadeIn(ax,Green_Dots,Red_Dots,Blue_Dots))

        self.wait(1)
        ax_2 = Axes(
            x_range=[-6,6],
            y_range=[-6,6],
        ).scale(.5).shift(3.5*RIGHT)
        labels = ax_2.get_axis_labels(
            Text("1st principal ").scale(0.45), Text("2cd principal").scale(0.45)
        )
        self.add(ax_2,labels)
        self.wait(2)

        xs = np.linspace(-6,6, num=100)
        Green_Dots_2 =  VGroup(*[
        Dot(ax_2.c2p(1,xs[i]),color="green")  for i in range(0,100)])
        Red_Dots_2 =  VGroup(*[
        Dot(ax_2.c2p(2,xs[i]),color="red")  for  i in range(0,100)])
        blue = np.load("blueCirc.npy")
        Blue_Dots_2 =  VGroup(*[
        Dot(ax_2.c2p(3,xs[i]),color="blue")  for i in range(0,100)])

        temp_Green = Green_Dots.copy()
        temp_red = Red_Dots.copy()
        temp_blue = Blue_Dots.copy()
        self.add(temp_blue,temp_Green,temp_red)

        self.play(ReplacementTransform(temp_Green,Green_Dots_2),runtime=4)
        self.wait(1)
        self.play(ReplacementTransform(temp_red,Red_Dots_2),runtime=4)
        self.wait(1)
        self.play(ReplacementTransform(temp_blue,Blue_Dots_2),runtime=4)
        self.wait(1)







class TitleCards(Animation):

    def begin(self) -> None:
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
        
