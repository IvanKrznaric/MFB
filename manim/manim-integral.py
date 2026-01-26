from manim import *

class Integral(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = (Axes(x_range = [-10,10, 1], x_length = 15, y_range = [-7,7,1], y_length = 10, axis_config={"include_numbers":True, "include_tip": False})).set_color(BLACK).scale_to_fit_height(7.5)
        funkcija = axes.plot(lambda x: -0.1*(x+5)*(x+2)*(x-3), x_range = [-6,4], color = BLUE)
        copyright_text = MarkupText("Ivan Krznarić, Faculty of Economics and Business, University of Zagreb \n© Copyright 2025 ", font_size=12, font = "Arial", color = BLACK).to_edge(UR).shift(LEFT * (-0.3) + UP * 0.3)
        self.add(copyright_text)

        # Prikaz koordinatnih osih i funkcije
        self.add(axes)
        self.play(Create(funkcija), run_time = 2)
        self.wait(2)

        # Računanje Riemannove sume
        dx_list = [1, 0.5, 0.3, 0.1, 0.05, 0.025, 0.01]

        rectangles = VGroup(*[axes.get_riemann_rectangles(graph = funkcija, x_range = [-2,3], stroke_width = 0.1, stroke_color = BLACK, color = ORANGE, dx = dx,) for dx in dx_list])

        first_area = rectangles[0]
        for k in range(1, len(dx_list)):
            new_area = rectangles[k]
            self.play(Transform(first_area, new_area), run_time = 2)
            self.wait(0.5)

        self.wait()



        