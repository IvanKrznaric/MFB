from manim import *

class Derivative(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        #tekst = Tex(r"\textbf{Story behind the derivative}", color = PURE_BLUE)
        #tekst.move_to(3.5*UP + 3*LEFT)
        copyright_text = MarkupText("Ivan Krznarić, Faculty of Economics and Business, University of Zagreb \n© Copyright 2025 ", font_size=12, font = "Arial", color = BLACK).to_edge(UR).shift(LEFT * (-0.3) + UP * 0.3)
        self.add(copyright_text)
        self.add( copyright_text)

        definicija = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}").set_color(BLACK).scale(0.75)
        okvir = SurroundingRectangle(definicija, color = GREEN, fill_opacity = 0.4)
        sve = VGroup(definicija, okvir)
        sve.move_to(3*UP +3*LEFT)
        self.add(sve)
        self.wait(3)

        axes = (Axes(x_range = [0,10, 1], x_length = 10, y_range = [0, 20, 5], y_length = 5, axis_config={"include_numbers":True, "include_tip": False})).set_color(BLACK).scale(0.75)
        axes_labels = axes.get_axis_labels(x_label = "x", y_label = "y  ")

        funkcija = axes.plot(lambda x : 0.1*(x-2)*(x-5)*(x-7)+7, x_range = [0,10], color = PURE_BLUE)


        #SADA ANIMIRAMO
        x = ValueTracker(7)
        dx = ValueTracker(2)


        tocka_A = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(), funkcija.underlying_function(x.get_value())))
            .set_color(BLACK)
        )
        

        tocka_B = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                axes.c2p(x.get_value()+dx.get_value(), funkcija.underlying_function(x.get_value()+dx.get_value())),
            )
            .set_color(BLACK)
        )

        tocka_C = always_redraw(
            lambda: Dot()
            .scale(0.8)
            .move_to(
                axes.c2p(x.get_value()+dx.get_value(),0)
            )
            .set_color(PURE_RED)
        )
        tocka_D = always_redraw(
            lambda : Dot()
            .scale(0.8)
            .move_to(
                axes.c2p(7,0)
            )
            .set_color(PURE_RED)
        )

        crta_1 = always_redraw(
            lambda : DashedLine(tocka_A.get_center(), tocka_D.get_center(), dash_length = 0.1).set_color(PURE_RED)
        )

        crta_2 = always_redraw(
            lambda : DashedLine(tocka_B.get_center(), tocka_C.get_center(), dash_length = 0.1).set_color(PURE_RED)
        )

        #sekanta = always_redraw(
            #lambda : Line(tocka_A, tocka_B, color = PURE_GREEN).scale(100)
        #)

        sekanta = always_redraw(
            lambda : axes.get_secant_slope_group(
                x = x.get_value(), 
                graph = funkcija, 
                dx = dx.get_value(),
                dx_line_color = WHITE,
                dy_line_color = PURE_RED,
                secant_line_color = GREEN,
            )
        )

        
        crta_zagrade_1 = Line(axes.c2p(7,0), axes.c2p(9,12.6)).set_opacity(0)
        brace_1 = Brace(crta_zagrade_1, direction = 4*DOWN).set_color(BLACK).shift(0.25*DOWN)
        h = MathTex(r"h").set_color(BLACK).scale(0.5)
        h.next_to(brace_1, DOWN)

        crta_zagrade_2 = Line(axes.c2p(7,7), axes.c2p(9,12.6)).set_opacity(0)
        brace_2 = Brace(crta_zagrade_2, direction = RIGHT).set_color(BLACK).shift(0.25*RIGHT)
        pomak = MathTex(r"f(x+h)-f(x)").set_color(BLACK).scale(0.5)
        pomak.next_to(brace_2, RIGHT)

        self.add(axes, axes_labels, funkcija)
        self.wait(2)
        self.play(Create(VGroup(tocka_A, tocka_B, tocka_C, tocka_D, crta_1, crta_2)), run_time = 2)
        self.add(brace_1, h, brace_2, pomak)
        self.play(Create(sekanta))
        self.wait(4)
        self.play(FadeOut(brace_1, h, brace_2, pomak))
        self.play(dx.animate.set_value(0.001), run_time = 8)