from scipy import optimize
from manim import *
from manim_slides import Slide
import numpy as np
## Goals of this talk

# Talk about uSub

# The goal of this is to convert things into 

## Finish the example question.


class uSub(Slide):
    # We need to create slides where the color 
    # shows the substitution.
    def construct(self):
        # First part is talking about the 
        # dvariable part.
        BeginingTex = Tex("Important notational aspects").shift(3*UP)
        eq1 = MathTex("\int","d","variable")
        eq1T=MathTex("\int","f(variable)","d","variable")
        eqx = MathTex("\int","d","x")
        eqxT = MathTex("\int","f(x)","d","x")
        eqr = MathTex("\int","f(r)")
        eqrT= MathTex("\int","f(r)","d","r")
        equT = MathTex("\int","f(u)","d","x")
        self.play(FadeIn(BeginingTex))
        self.next_slide()
        self.play(FadeIn(eq1))
        self.next_slide()
        self.play(TransformMatchingTex(eq1,eq1T))
        self.next_slide()
        self.play(TransformMatchingTex(eq1T,eqx))
        self.next_slide()
        self.play(TransformMatchingTex(eqx,eqxT))
        self.next_slide()
        self.play(TransformMatchingTex(eqxT,eqr))
        self.next_slide()
        self.play(TransformMatchingTex(eqr,eqrT))
        self.next_slide()
        self.play(TransformMatchingTex(eqrT,equT))
        self.next_slide()
        self.wipe([BeginingTex,equT])

        # Second part is to talk about that
        # usub reverses Chain Rule.
        TitleTex = Tex("u Substitution").shift(3*UP)
        self.play(FadeIn(TitleTex))
        self.next_slide()
        RevQuestion = Tex("What differentiation Rule does this reverse?").shift(2*UP)
        chainRule = Tex("Chain Rule").shift(1*UP)
        howToThink = Tex("How to figure out u?")
        inside_func = Tex("The u would be the inside function").shift(1*DOWN)
        self.play(FadeIn(RevQuestion))
        self.next_slide()
        self.play(FadeIn(chainRule))
        self.next_slide()
        self.play(FadeIn(howToThink))
        self.next_slide()
        self.play(FadeIn(inside_func))
        self.next_slide()
        self.wipe([TitleTex,chainRule,RevQuestion,howToThink,inside_func])

        ## Third part: Do an example.
        Variables = VGroup(MathTex("\sin(x)")).shift(UP)
        eqExample = MathTex("\int","e^{","\sin(x)","}","\cos(x)","dx")
        eqExampleu = MathTex("\int","e^{","u","}","\cos(x)","dx")
        self.play(FadeIn(eqExample))
        uChoice = MathTex("u","=","\sin(x)").shift(3*UP)
        uChoiceBlue = MathTex("u","=","\sin(x)",tex_to_color_map={"u":BLUE,"\sin(x)":BLUE}).shift(3*UP)
        self.next_slide()
        self.play(FadeIn(uChoice))
        self.next_slide()
        self.play(TransformMatchingTex(uChoice,uChoiceBlue))
        self.next_slide()
        self.play(TransformMatchingTex(Group(eqExample,Variables),eqExampleu  ))
        self.play(TransformMatchingTex(uChoiceBlue,uChoice))
        self.next_slide()
        dxTodu = MathTex("dx","\\to","du").next_to(uChoice,direction=DOWN)
        self.play(FadeIn(dxTodu))
        self.next_slide()
        self.play(FadeOut(dxTodu))
        Question = Tex("What operation can form a dx and a du from a u?").shift(2*UP)
        self.play(FadeIn(Question))
