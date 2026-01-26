from manim import *

class Limes_e(Scene):
    def construct(self):

        self.camera.background_color = WHITE
       
        axes = Axes(x_range = [0, 500, 50], y_range = [0,10, 1]).add_coordinates().set_color(BLACK)
        copyright_text = MarkupText("Ivan Krznarić, Faculty of Economics and Business, University of Zagreb \n© Copyright 2025 ", font_size=12, font = "Arial", color = BLACK).to_edge(UR).shift(LEFT * (-0.3) + UP * 0.3)
        self.add(copyright_text)

        self.play(Create(axes), run_time = 3)

        graf = axes.plot(lambda x : (1+1/x)**x, color = PURE_BLUE, x_range = [0.2, 500, 0.01])

        self.play(Write(graf))
        self.wait()

        x = ValueTracker(0.21)

        dot = always_redraw(lambda : Dot(axes.c2p(x.get_value(), graf.underlying_function(x.get_value())), color = PURE_RED))

        table = MathTable([["x", "f(x) = (1+\\frac{1}{x})^{x}"], ["a", "b"]], include_outer_lines=True).set_color(BLACK)
        table.get_rows()[1].set_opacity(0)
        table.move_to(2.5*UP + 2*LEFT).scale(0.6)

        vrijednost_x = always_redraw(lambda : DecimalNumber().set_value(x.get_value()).move_to(3.4*LEFT + 2*UP).set_color(BLACK).scale(0.6))
        vrijednost_fx = always_redraw(lambda : DecimalNumber((1+1/x.get_value())**x.get_value(), num_decimal_places = 5).move_to(1.5*LEFT + 2*UP).set_color(BLACK).scale(0.7))
        



    
        self.play(Create(dot))
        self.play(Write(table))
        self.play(FadeIn(vrijednost_x, vrijednost_fx))
        self.wait()
        self.play(x.animate.set_value(100), run_time = 7)
        self.wait()
        self.play(x.animate.set_value(300), run_time = 7)
        self.wait()
        self.play(x.animate.set_value(499), run_time = 7)
        self.wait(2)