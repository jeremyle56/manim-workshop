from manim import *


class Triangle_Star(Scene):
    def construct(self):
        star = Star(color=TEAL).shift(5 * LEFT + 2 * UP)

        self.add(star)
        self.play(star.animate.set_fill(BLUE_D, opacity=0.5))
        self.wait()

        triangle = Triangle(color=PURPLE, fill_opacity=0.8)
        self.play(Create(triangle))
        self.play(triangle.animate.shift(3 * RIGHT + 2 * DOWN))
        self.play(triangle.animate.rotate(PI).shift(7 * LEFT))
        self.play(Rotate(triangle, angle=PI))
        self.play(
            triangle.animate.shift(7 * RIGHT + 4 * UP),
            run_time=2,
        )

        text = Text("Completed Exercise 1")
        self.play(Write(text))
