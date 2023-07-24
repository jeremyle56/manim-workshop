from manim import *


class Graphing_Challenge(Scene):
    def construct(self):
        xy_plane = NumberPlane(
            x_range=(-np.pi, np.pi), x_length=7, y_range=(-3, 3), y_length=7
        ).to_edge(LEFT)

        # We might like to add coordinates
        xy_plane.add_coordinates()

        # The next thing we would like to do is add a function
        first_order = xy_plane.plot(lambda x: x, color=BLUE)
        first_order_label = MathTex(r"f(x) = x", color=first_order.get_color()).shift(
            3 * RIGHT
        )
        first_order_label.next_to(xy_plane, RIGHT)

        third_order = xy_plane.plot(lambda x: 0 + x - 1 / 6 * x**3, color=GREEN)
        third_order_label = MathTex(
            r"f(x) = x - \frac{x^3}{3!}", color=third_order.get_color()
        )
        third_order_label.next_to(xy_plane, RIGHT)

        fifth_order = xy_plane.plot(
            lambda x: x - 1 / 6 * x**3 + 1 / 120 * x**5, color=YELLOW
        )
        fifth_order_label = MathTex(
            r"f(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!}", color=fifth_order.get_color()
        )
        fifth_order_label.next_to(xy_plane, RIGHT)

        seventh_order = xy_plane.plot(
            lambda x: x
            - 1 / 6 * x**3
            + 1 / (np.math.factorial(5)) * x**5
            - 1 / (np.math.factorial(7)) * x**7,
            color=RED,
        )
        seventh_order_label = MathTex(
            r"f(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} + \frac{x^7}{7!}"
        )
        seventh_order_label.color = seventh_order.get_color()
        seventh_order_label.next_to(xy_plane, RIGHT)

        sine_function = xy_plane.plot(lambda x: np.sin(x), color=WHITE)
        self.play(
            LaggedStart(
                DrawBorderThenFill(xy_plane),
                Write(sine_function),
                lag_ratio=1,
                run_time=4,
            )
        )
        self.play(Write(first_order), Write(first_order_label))
        self.wait()
        self.play(
            Transform(first_order, third_order),
            ReplacementTransform(first_order_label, third_order_label),
        )
        self.wait()
        self.play(
            Transform(third_order, fifth_order),
            ReplacementTransform(third_order_label, fifth_order_label),
        )
        self.wait()
        self.play(
            Transform(fifth_order, seventh_order),
            ReplacementTransform(fifth_order_label, seventh_order_label),
        )

        self.wait(2)
