from manim import *

class SolutionAnimation(Scene):
    def construct(self):

        # create mobjects
        title = Text("Particle Subjected To Delta Potential", color=BLUE)
        potential = MathTex(r'v(x) &= - \alpha \delta(x)', color=RED)
        schrodingerTitle = Text("Schrodinger's Equation:", color=YELLOW)
        schrodinger = MathTex(r'-\frac{\hbar^2}{2m}\frac{d^2 \psi}{dx^2} - \alpha \delta(x) = E\psi')
        rearrangedschrodinger = MathTex("\\frac{d^2\psi}{dx^2}=","-\\frac{2mE}{\hbar^2}", "\psi")
        rearrangedschrodinger2 = MathTex("= \kappa^2\psi")
        kappa =  MathTex("=\kappa^2", color=RED)
        schrodingerFinal = MathTex("\\frac{d^2\psi}{dx^2}", "= \kappa^2\psi", color=BLUE)


            # locate mobjects
        title.to_edge(UP, buff=0.3)
        potential.next_to(title, DOWN, buff=0.5)
        schrodingerFinal.to_edge(UL, buff=0.6)
        schrodingerTitle.next_to(potential, DOWN, buff=0.5)
        schrodinger.next_to(schrodingerTitle, DOWN, buff=0.5)
        rearrangedschrodinger.next_to(schrodinger, DOWN, buff=0.5)
        rearrangedschrodinger2.next_to(rearrangedschrodinger, RIGHT, buff=0.3)
        kappa.next_to(rearrangedschrodinger[1], DOWN, buff=0.3)

        


        self.play(Write(title), run_time=2)
        self.play(Write(potential), run_time=2)
        self.play(FadeIn(schrodingerTitle))
        self.play(Write(schrodinger), run_time=2)
        self.play(Write(rearrangedschrodinger), run_time=2)
        kappa_frame = SurroundingRectangle(rearrangedschrodinger[1], color=BLUE, buff = .1)
        self.play(Create(kappa_frame))
        self.play(Write(kappa), run_time = 2)       
        self.play(Write(rearrangedschrodinger2), run_time=2)

        

        self.play(FadeOut(title,potential, schrodingerTitle, schrodinger, kappa, rearrangedschrodinger[1],rearrangedschrodinger[2], kappa_frame),
                  Transform(rearrangedschrodinger[0], schrodingerFinal[0]),
                  Transform(rearrangedschrodinger2[0], schrodingerFinal[1]), run_time=2.5
        )

        

        solutionTitle = Text("Solutions", color=YELLOW, font_size=60)
        solutionTitle.next_to(schrodingerFinal[1], RIGHT, buff=3)
        
        #Bound State Solutions
        negEnergynegx = MathTex("E < 0, x < 0", color=RED)
        bssolutionnegx = MathTex("\psi_{-}(x)=","Ae^{\kappa x}", font_size = 50)

        negEnergyposx = MathTex("E < 0, x > 0", color=RED)
        bssolutionposx = MathTex("\psi_{+}(x)=","Be^{-\kappa x}", font_size = 50)
        continuitycond = MathTex("A = B")
        continuitytext = Text("Continuity", color=BLUE, font_size=30)
        continuityEqn = MathTex("\psi_{-}(0) = \psi_{+}(0)")
        normalizationeqn = MathTex("B^{2}\int^{\infty}_{-\infty}e^{-2\kappa x}dx = 1", font_size=40)
        normcondition = MathTex("B = \sqrt{\kappa} = \\frac{\sqrt{m\\alpha}}{\hbar}")
        finalsolution = MathTex("\psi(x) = \\frac{\sqrt{m}\\alpha}{\hbar}e^{\\frac{-m\\alpha|x|}{\hbar^{2}}}", color=BLUE)
        finalsolutiontext = Tex("Bound State Solution", color=RED, font_size=40)

        negEnergynegx.next_to(schrodingerFinal[1],DOWN, buff=0.5)
        bssolutionnegx.next_to(negEnergynegx, DOWN, buff=0.3)

        negEnergyposx.next_to(solutionTitle,DR, buff=0.5)
        bssolutionposx.next_to(negEnergyposx, DOWN, buff=0.3)

        
        continuityEqn.next_to(bssolutionnegx, RIGHT, buff=0.8)
        continuitytext.next_to(continuityEqn, UP, buff=0.3)
        continuitycond.next_to(continuityEqn, DOWN, buff=0.3)
        normalizationeqn.next_to(bssolutionnegx, DOWN, buff=0.3)
        normcondition.next_to(normalizationeqn, DOWN, buff=0.5)
        finalsolution.next_to(continuitycond, DOWN, buff=2)
        finalsolutiontext.next_to(finalsolution, RIGHT, buff=0.3)



        posEnergy = MathTex("E > 0", color=GREEN)

        posEnergy.next_to(solutionTitle, DR,buff=0.5)
        
        self.play(Write(solutionTitle), run_time=3)
        self.play(Write(negEnergynegx), run_time=3)
        self.play(Write(bssolutionnegx), run_time=3)
        
        self.play(Write(negEnergyposx), run_time=3)
        self.play(Write(bssolutionposx), run_time=3)

        self.play(Write(continuityEqn), run_time=3)
        self.play(Write(continuitytext), run_time=1.2)
        self.play(Write(continuitycond), run_time=3)
        self.play(Write(normalizationeqn), run_time=3)
        self.play(Write(normcondition), run_time=3)
        self.play(Write(finalsolution), run_time=4)
        self.play(Write(finalsolutiontext), run_time=3)

