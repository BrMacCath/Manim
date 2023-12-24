from scipy import optimize
from manim import *
from manim_slides import Slide
import numpy as np
## Goals of this talk

# Want a set of slides that talk about 

class Deriv(Slide):
    # Slide one: Talks about the fundamental 
    # theorem of calculus.
    def construct(self):
        ## Create an overview of the topic
        ftoc = Tex("Fundamental Theorem of Calculus").shift(2*UP)
        Reason_1 = Tex("1. Geometric understanding").align_on_border(LEFT).shift(1*UP + 2.5*RIGHT)
        Reason_2 = Tex("2. Creating Integration Rules").align_on_border(LEFT).shift( 2.5*RIGHT)

        self.play(FadeIn(ftoc))
        Text = VGroup(Reason_1,Reason_2)
        self.next_slide()

        for reason in Text:
            self.play(FadeIn(reason))
        
        self.next_slide()
        self.wipe(ftoc,Text)

        for reason in Text:
            self.remove(reason)

        ## Geometric Understanding
            
        # Only positive function
        GeoUnder = Tex("Geometric Understanding").shift(3*UP)
        Func = MathTex("\int_1^3 f(x)dx").next_to(GeoUnder,direction=DOWN)
        FA = MathTex("= F(3) -F(1)").next_to(Func,direction=RIGHT)
        self.play(FadeIn(GeoUnder))
        self.next_slide()
        ax = Axes(
            x_range=[-.5,4],
            y_range=[-.5,6],
            axis_config={"include_numbers": True},
        )
        positive_func = ax.plot(lambda x: np.sin(x)+ 2)
        area = ax.get_area(positive_func,[1,3])
        self.play(FadeIn(ax))
        self.next_slide()
        self.play(FadeIn(positive_func))

        self.next_slide()
        self.play(FadeIn(Func))
        self.next_slide()

        self.play(FadeIn(area))

        self.next_slide()
        self.play(FadeIn(FA))
        self.next_slide()
        self.wipe([Func,FA])
        self.wipe([positive_func,area])
        self.next_slide()
        # Both positive and negative function
        ax_2 = Axes(
            x_range=[-.5,4],
            y_range=[-3.5,3.5],
            axis_config={"include_numbers": True},
        )
        self.play(Transform(ax,ax_2))

        func_pm = ax_2.plot(lambda x: -np.sin(PI*x))
        self.play(FadeIn(func_pm))
        self.play(FadeIn(Func))


        self.next_slide()
        neg_area = ax_2.get_area(func_pm,[1,2])
        pos_area = ax_2.get_area(func_pm,[2,3],color="red")
        self.play(FadeIn(neg_area,pos_area))

        self.next_slide()
        equals = MathTex("=").next_to(Func,direction=RIGHT)
        self.play(FadeIn(equals))
        self.next_slide()
        green_square = Square(side_length=1,color="green",fill_color="green",fill_opacity=.25).next_to(equals,direction=RIGHT)
        minus = MathTex("-").next_to(green_square,direction=RIGHT)
        red_square = Square(side_length=1,color="red",fill_color="red",fill_opacity=.25).next_to(minus,direction=RIGHT)
        int_area = VGroup(green_square,minus,red_square)
        for ob in int_area:
            self.play(FadeIn(ob),runtime=1)

        ## Reversing rules
        self.next_slide()
        self.wipe([Func,ax,neg_area,pos_area,func_pm,equals,green_square,minus,red_square,GeoUnder])
        ReverseUnder = Tex("Reverse Understanding").shift(3*UP)
        self.play(FadeIn(ReverseUnder))  
        self.next_slide()
        Rev_Process = Tex("Process").align_on_border(LEFT).shift(2*UP + 1*RIGHT)
        Rev_1 = Tex("1. Put on socks").align_on_border(LEFT).shift(1*UP + 1*RIGHT)
        Rev_2 = Tex("2. Put on shoes").align_on_border(LEFT).shift( 1*RIGHT)
        self.play(FadeIn(Rev_Process))
        self.next_slide()
        self.play(FadeIn(Rev_1))
        self.next_slide()
        self.play(FadeIn(Rev_2))
        self.next_slide()
        Ans_process = Tex("Reverse Process").align_on_border(LEFT).shift(2*UP + 8*RIGHT)
        Ans_1 = Tex("1. Put on socks").align_on_border(LEFT).shift(1*UP + 8*RIGHT)
        Ans_2 = Tex("2. Put on shoes").align_on_border(LEFT).shift( 8*RIGHT)
        self.play(FadeIn(Ans_process))
        self.next_slide()
        self.play(FadeIn(Ans_1))
        self.play(FadeIn(Ans_2))

        











#         codeExample = Code(code="""from Manim import *

# class Deriv(Slide):""",language="python")
#         self.play(FadeIn(codeExample))




