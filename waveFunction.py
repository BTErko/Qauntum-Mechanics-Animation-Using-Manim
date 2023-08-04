from manim import *
import numpy as np

class PlotBoundState(Scene):
    def construct(self):
        axes = Axes(x_range=[-2.0, 2.0, 0.5],
             y_range=[-1, 3, 0.5],
             x_length=10,
             y_length=6,
             axis_config={"include_tip": False}
             )
        
        labels = axes.get_axis_labels(y_label="\psi(x)")

         
        self.add(axes, labels)
        hbar = 1
        mass = 1
        alpha = 3.5

        cons = mass*alpha/(hbar**2)

        func = axes.plot(lambda x: np.sqrt(cons) * np.exp(-1*cons * abs(x)), color=BLUE)

        self.play(Create(func), run_time=4)
        self.wait(2)

