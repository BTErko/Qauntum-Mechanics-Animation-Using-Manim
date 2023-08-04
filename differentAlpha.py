
from manim import *
import numpy as np

class coefficientsVsAlpha(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 8],
             y_range=[0, 1],
             #x_length=10,
             #y_length=6,
             axis_config={"include_tip": False, "include_numbers": True}
             )
        xlabel = Text("E", slant=ITALIC)
        labels = axes.get_axis_labels(y_label="", x_label = xlabel.scale(0.5))

        
        self.add(axes, labels)
        alpha = [np.sqrt(2), 0.5, 1.0, 3.0]

        T0 = axes.plot(lambda x: 1.0/(1.0 + 2/(x*alpha[0]**2)), color=RED)
        T1 = axes.plot(lambda x: 1.0/(1.0 + 2/(x*alpha[1]**2)), color=BLUE)
        T2 = axes.plot(lambda x: 1.0/(1.0 + 2/(x*alpha[2]**2)), color=YELLOW)
        T3 = axes.plot(lambda x: 1.0/(1.0 + 2/(x*alpha[3]**2)))

        R0 = axes.plot(lambda x: 1.0/(1.0 + x*2/alpha[0]**2), color=RED)
        R1 = axes.plot(lambda x: 1.0/(1.0 + x*2/alpha[1]**2), color=BLUE)
        R2 = axes.plot(lambda x: 1.0/(1.0 + x*2/alpha[2]**2), color=YELLOW)
        R3 = axes.plot(lambda x: 1.0/(1.0 + x*2/alpha[3]**2))
        
        
        self.play(Create(T0),Create(T1), Create(T2), Create(T3), Create(R0), Create(R1), Create(R2), Create(R3),  x_range=[0,3], run_time=3)

        self.wait(1) 
        