from tkinter.font import ITALIC
from manim import *
import numpy as np

class TransmVsEnergy(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 5],
             y_range=[0, 1],
             #x_length=10,
             #y_length=6,
             axis_config={"include_tip": False, "include_numbers": True}
             )
        xlabel = Text("E", slant=ITALIC)
        labels = axes.get_axis_labels(y_label="", x_label = xlabel.scale(0.5))

         
        self.add(axes, labels)
        hbar = 1
        mass = 1
        alpha = np.sqrt(2)

        cons = (2*hbar**2)/(mass*alpha**2)

        Reflection = axes.plot(lambda x: 1.0/(1.0 + cons*x), color=RED)
        Transmission = axes.plot(lambda x: 1./(1. + 1./(cons*x)), color=BLUE)

        Rlabel = Text("R", color=RED)
        Tlabel = Text("T", color=BLUE)

        Rlabel.next_to(Reflection, DR, buff=0.1)
        Tlabel.next_to(Transmission, UR, buff=0.1)

        self.play(Create(Reflection), Create(Transmission), Write(Rlabel.scale(0.5)), Write(Tlabel.scale(0.5)), run_time=4)
        self.wait(1)

