from manim import *
import random

class CoinConvergence(Scene):
    """Optional Manim insert; 1080p clip for replacing the fifth Remotion scene."""
    def construct(self):
        rng = random.Random(2026)
        bits = [rng.choice([0,1]) for _ in range(1000)]
        running = []
        total = 0
        for i, bit in enumerate(bits, 1):
            total += bit
            running.append(total / i)
        axes = Axes(x_range=[0,1000,200], y_range=[0,1,.25], x_length=11, y_length=5, axis_config={"color":GREY_B})
        line = axes.plot_line_graph(list(range(1,1001)),running,line_color=YELLOW,add_vertex_dots=False)
        target = DashedLine(axes.c2p(0,.5),axes.c2p(1000,.5),color=GREY_A)
        self.add(axes,target)
        self.play(Create(line),run_time=7,rate_func=linear)
        self.wait(1)
