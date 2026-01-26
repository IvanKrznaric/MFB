from manim import *

class Optimizacija_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        k = ValueTracker(-3.5)

        axes = (Axes(x_range = [-10,10, 1], x_length = 15, y_range = [-7,7,1], y_length = 10, axis_config={"include_numbers":True, "include_tip": False})).set_color(BLACK)
        axes2 = (Axes(x_range = [-10,10, 1], x_length = 15, y_range = [-7,7,1], y_length = 10, axis_config={"include_numbers":True, "include_tip": False})).set_color(BLACK)
        axes3 = (Axes(x_range = [-10,10, 1], x_length = 15, y_range = [-7,7,1], y_length = 10, axis_config={"include_numbers":True, "include_tip": False})).set_color(BLACK)
        # stack the axes vertically and fit to screen
        donji_red = VGroup(axes2, axes3).arrange(RIGHT, buff = 1).scale_to_fit_height(7.5)
        VGroup(axes, donji_red).arrange(DOWN,buff=1).scale_to_fit_height(7.5)
        axes_labels = axes.get_axis_labels(x_label = "x", y_label = "y  ")

        derivacija = always_redraw(lambda : axes2.plot(lambda x : 0.5*(3*x**2 + 4*x - 5), x_range = [-3.5,k.get_value()], color = PURE_GREEN))
        funkcija = axes.plot(lambda x: 0.5*(x**3 + 2*x**2 - 5*x -6), x_range = [-3.7,2.5], color = PURE_BLUE)
        druga_derivacija = always_redraw(lambda : axes3.plot(lambda x : 0.5*(6*x + 4), x_range = [-3.5,k.get_value()], color = DARK_BROWN))
        

        moving_slope = always_redraw(lambda: axes.get_secant_slope_group(x=k.get_value(), graph = funkcija, dx = 0.005, secant_line_length = 1, secant_line_color = PURE_RED))
        dot = always_redraw(lambda : Dot().set_color(RED_E).move_to(axes.c2p(k.get_value(), funkcija.underlying_function(k.get_value()))))
        dot2 = always_redraw(lambda : Dot().set_color(GREEN_E).move_to(axes2.c2p(k.get_value(), derivacija.underlying_function(k.get_value()))))
        dot3 = always_redraw(lambda : Dot().set_color(DARK_BROWN).move_to(axes3.c2p(k.get_value(), druga_derivacija.underlying_function(k.get_value()))))

        #Tekst vezan uz nagib
        slope_value_text  = Tex(r"\text{Derivative} = ", color = BLACK).move_to(3*UP + 5.25*LEFT)
        slope_value = always_redraw(
            lambda : DecimalNumber(num_decimal_places = 1)
            .set_value(derivacija.underlying_function(k.get_value()))
            .next_to(slope_value_text)
            .set_color(BLACK)
            )

        naziv_1 = Tex(r"\small f(x)", color = PURE_BLUE).move_to(3*UP + 1.25*LEFT)
        naziv_2 = Tex(r"\small f'(x)", color = PURE_GREEN).move_to(1*DOWN + 4.25*LEFT)
        naziv_3 = Tex(r"\small f''(x)", color = DARK_BROWN).move_to(1*DOWN + 1.25*RIGHT)

        copyright_text = MarkupText("Ivan Krznarić, Faculty of Economics and Business, University of Zagreb \n© Copyright 2025 ", font_size=12, font = "Arial", color = BLACK).to_edge(UR).shift(LEFT * (-0.3) + UP * 0.3)

        
        

        self.add(axes, funkcija, axes2, derivacija, axes3, druga_derivacija, naziv_1, naziv_2, naziv_3, copyright_text)
        self.wait(2)
        self.add(slope_value_text, slope_value, moving_slope, dot, dot2, dot3)
        self.wait(2)
        self.play(k.animate.set_value(-2.1196), run_time = 5)
        self.wait(2)
        self.play(k.animate.set_value(0.78630), run_time = 5)
        self.wait(2)
        self.play(k.animate.set_value(2.5), run_time = 5)
        self.wait(4)