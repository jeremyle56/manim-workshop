from manim import *


class Quadratic(Scene):
    def construct(self):
        eq1 = MathTex("ax^2 + bx + c = 0")
        eq2 = MathTex("4a^2x^2 + 4abx + 4ac = 0")
        eq3 = MathTex("4a^2x^2 + 4abx - 4ac")
        eq4 = MathTex("4a^2x^2 + 4abx + b^2 = b^2 - 4ac")
        eq5 = MathTex("(2ax + b)^2 = b^2 - 4ac")
        eq6 = MathTex("2ax + b = \pm\sqrt(b^2 - 4ac)")
        eq7 = MathTex("2ax = -b \pm\sqrt(b^2 - 4ac)")
        eq8 = MathTex("x = \frac{-b \pm\sqrt(b^2 - 4ac)}{2a}")
        self.add(eq1)
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait()
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait()
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait()
        self.play(TransformMatchingTex(eq6, eq7))
        self.wait()
        self.play(TransformMatchingTex(eq7, eq8))
        self.wait()
