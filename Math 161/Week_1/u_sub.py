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
        
        eqExampleYell = MathTex("\int","e^{","u","}","\cos(x)","dx",tex_to_color_map={"dx":YELLOW})
        self.play(Transform(eqExampleu,eqExampleYell))
        self.next_slide()
        self.play(FadeOut(dxTodu))
        Question = Tex("What operation can form a dx and a du from a u?").shift(2*UP)
        self.play(FadeIn(Question))
        self.next_slide()
        self.play(FadeOut(Question))
        self.next_slide()
        eqDiff = MathTex("{","{","du","}","\over","{","dx","}","}","=","\cos(x)").next_to(uChoice,direction=DOWN)
        self.play(FadeIn(eqDiff))
        self.next_slide()
        eqDiff2 = MathTex("du","=","\cos(x)","dx").next_to(eqDiff,direction=DOWN)
        eqDiffCopy = eqDiff.copy()
        self.play(TransformMatchingTex(eqDiffCopy,eqDiff2))
        eqDiff3 = MathTex("du","=","\cos(x)","dx",tex_to_color_map={"dx":YELLOW}).next_to(eqDiff,direction=DOWN)
        self.next_slide()
        self.play(TransformMatchingTex(eqDiff2,eqDiff3))
        eqExampleYell2 = MathTex("\int","e^{","u","}","\cos(x)","dx",tex_to_color_map={"dx":YELLOW,"\cos(x)":YELLOW})
        self.next_slide()
        self.play(Transform(eqExampleYell,eqExampleYell2))
        eq_2 = MathTex("=").next_to(eqExampleYell2,direction=RIGHT)
        self.next_slide()
        self.play(FadeIn(eq_2))
        self.next_slide()
        u_int = MathTex("\int","e^{","u","}","du").next_to(eq_2,direction=RIGHT)
        tempCopy=eqExampleYell2.copy()
        self.play(TransformMatchingTex(tempCopy,u_int))
        self.next_slide()
        e2copy = eq_2.copy()
        eq3=  MathTex("=").next_to(eq_2,direction=DOWN,buff=1)
        tempu_intcopy = u_int.copy()
        u_ans = MathTex("e^{","u","}","+","C").next_to(eq3,direction=RIGHT)
        self.play(TransformMatchingTex(e2copy,eq3),TransformMatchingTex(tempu_intcopy,u_ans))
        self.next_slide()
        eq4=  MathTex("=").next_to(eq3,direction=DOWN,buff=1)
        x_ans = MathTex("e^{","\sin(x)","}","+","C").next_to(eq4,direction=RIGHT)
        eq3copy = eq3.copy()
        u_anscopy = u_ans.copy()
        self.play(TransformMatchingTex(eq3copy,eq4),TransformMatchingTex(u_anscopy,x_ans))

