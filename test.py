from scipy import optimize
from manim import *
from manim_slides import Slide

def get_horizontal_line_to_graph(axes, function, x, width, color):
    result = VGroup()
    line = DashedLine(
        start=axes.c2p(0, function.underlying_function(x)),
        end=axes.c2p(x, function.underlying_function(x)),
        stroke_width=width,
        stroke_color=color,
    )
    dot = Dot().set_color(color).move_to(axes.c2p(x, function.underlying_function(x)))
    result.add(line, dot)
    return result

def get_vertical_line_to_graph(axes, function, x, width, color):
    result = VGroup()
    line = DashedLine(
        start=axes.c2p(x, 0),
        end=axes.c2p(x, function.underlying_function(x)),
        stroke_width=width,
        stroke_color=color,
    )
    dot = Dot().set_color(color).move_to(axes.c2p(x, function.underlying_function(x)))
    result.add(line, dot)
    return result


def demand_func(x, c):
    return (c/100 - x/100)

def supply_func(x, c = 125):
    return ((x/c) + 125/c)

def dot_x(dc): 
    return (125*dc-12500)/225

class AnimateOD(Scene):
    def construct(self):
        
        # Value that will be updated
        dc = ValueTracker(1000)
        
        # Set plane
        plane = (
            NumberPlane(x_range=[-1000, 2000, 1000], x_length = 7, y_range = [-10, 20, 10], y_length = 5)
            .add_coordinates()
        )

        demand = always_redraw( # We tell manim to always check if the value was updated
            lambda: plane.plot(
                lambda x: demand_func(x, dc.get_value()), x_range = [0, dc.get_value()], color = BLUE
            )
        )
        
        static_demand = (
            plane.plot(
                lambda x: demand_func(x, 1000), x_range = [0, 1000], color = BLUE
            )
        )
        
        static_demand.set_opacity(0.5)
        
        demand_lab = (
            Text("D", font_size = 10)
            .set_color(WHITE).move_to(plane.c2p(1000+100, 2))
        )
        text_Group = VGroup(demand_lab)
        text_Group.add_updater(lambda m: demand_lab.move_to(plane.c2p(dc.get_value()+100, 2)) )
        
        mdemand_lab = (
            Text("D'", font_size = 10)
            .set_color(WHITE)
        )

        supply = always_redraw(
            lambda: plane.plot(
                lambda x: supply_func(x, 125), x_range = [0, 1000], color = BLUE
            )
        )
        
        supply_lab = (
            Text("S", font_size = 10)
            .set_color(WHITE)
            .next_to(plane.c2p(1000 + SMALL_BUFF, supply_func(1000) + SMALL_BUFF))
        )
        
        dot = always_redraw(
            lambda: Dot().move_to(
                plane.c2p(dot_x(dc.get_value()), supply_func(dot_x(dc.get_value())))
            )
        )
        
        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane, function=demand, x=dot_x(dc.get_value()), width=2, color=YELLOW
            )
        )
        
        moving_v_line = always_redraw(
            lambda: get_vertical_line_to_graph(
                axes=plane, function=demand, x=dot_x(dc.get_value()), width=2, color=YELLOW
            )
        )
        self.add(dc)
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane),
                Create(demand),
                Create(static_demand),
                Create(supply),
                Write(text_Group),
                Write(supply_lab),
                run_time = 4
            )
        )
        self.wait(1)


        self.add(demand, static_demand,supply, dot, moving_h_line, moving_v_line)
        self.play(dc.animate.set_value(1450),Transform(demand_lab, mdemand_lab) ,rate_func = linear)
        self.wait()


class AnimateOD_2(Scene):
    def construct(self):
        dc= ValueTracker(1000)
        plane = (
            NumberPlane(x_range=[-1000, 2000, 1000], x_length = 7, y_range = [-10, 20, 10], y_length = 5)
            .add_coordinates()
        )
        demand = always_redraw( # We tell manim to always check if the value was updated
            lambda: plane.plot(
                lambda x: self.demand_func(x, dc.get_value()), x_range = [0, dc.get_value()], color = BLUE
            )
        )
        self.add(dc)
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane),
                Create(demand),
                run_time = 4
            )
        )



    def demand_func(self,x, c):
        return (c/100 - x/100)
    

class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.next_slide(loop=True)  # Start loop
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()  # This will start a new non-looping slide

        self.play(dot.animate.move_to(ORIGIN))