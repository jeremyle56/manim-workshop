from manim import *


class Graphing_Exercise(Scene):
    def construct(self):
        xy_plane = Axes(x_range=(-3, 3), x_length=9, y_range=(-3, 3))
        xy_plane.add_coordinates()

        first_order = xy_plane.plot(lambda x: x, color=YELLOW)
        first_label = MathTex(r"f(x) = x").next_to(xy_plane, UR)

        second_order = xy_plane.plot(lambda x: x**2, color=YELLOW)
        second_label = MathTex(r"f(x) = x^{2}").next_to(xy_plane, UR)

        third_order = xy_plane.plot(lambda x: x**3, color=YELLOW)
        third_label = MathTex(r"f(x) = x^{3}").next_to(xy_plane, UR)

        fourth_order = xy_plane.plot(lambda x: x**4, color=YELLOW)
        fourth_label = MathTex(r"f(x) = x^{4}").next_to(xy_plane, UR)

        area = xy_plane.get_riemann_rectangles(
            fourth_order,
            x_range=(-2, 2),
            dx=0.2,
            color=[BLUE_D, PINK],
            fill_opacity=1,
            show_signed_area=False,
        )

        self.play(FadeIn(xy_plane), Write(first_order), Write(first_label), run_time=2)

        self.play(
            ReplacementTransform(first_order, second_order),
            ReplacementTransform(first_label, second_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(second_order, third_order),
            ReplacementTransform(second_label, third_label),
        )

        self.wait()

        self.play(
            ReplacementTransform(third_order, fourth_order),
            ReplacementTransform(third_label, fourth_label),
        )

        self.play(Write(area))
        self.wait()
