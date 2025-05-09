from manim import *
from manim_slides import Slide
from MF_Tools import *

template = TexTemplateLibrary.default
template.add_to_preamble(r"\usepackage[T1]{fontenc}")
template.add_to_preamble(r"\usepackage[utf8]{inputenc}")
template.add_to_preamble(r"\PassOptionsToPackage{polish}{babel}")
Tex.set_default(tex_template = template)

from manim import config as global_config
config = global_config.copy()



class Intro(Slide):
    def construct(self):
        title = Tex(
            r"""$\mathbb{S}$ymetryczne $\mathbb{U}$ogólnienie $\mathbb{R}$óżniczkowalności $\mathbb{F}$unkcji"""
        )

        oblicze = MathTex(r"\mathbb{K}\text{onferencja } \theta \beta \ell \imath c \mathbb{Z}\varepsilon")

        logo = ImageMobject("assets/uam_logo.png")
        logo.scale(0.2)
        logo.next_to(title, DOWN)
        oblicze.next_to(logo, DOWN)

        author = Tex("$\mathbb{A}$drian $\mathbb{M}$adajewski")
        author.next_to(oblicze, DOWN)

        group = Group(title, logo, author, oblicze).move_to(ORIGIN)

        self.next_slide()
        self.play(FadeIn(logo), Write(oblicze))
        self.next_slide()

        self.play(Write(author))
        self.next_slide()

        self.play(Write(title))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

""" class Scene_0(Slide):
    def construct(self):
        eq = MathTex(r"f : X \to Y").scale(2)
       
        self.play(Write(eq))
        self.next_slide()

        self.play(eq.animate.move_to(UP))

        eq2 = MathTex(r"X,Y \subset \mathbb{R}").next_to(eq, DOWN).move_to(DOWN).scale(2)

        self.play(Write(eq2))
        self.next_slide()

        self.play(FadeOut(*self.mobjects)) """

class Scene_1(Slide):
    def construct(self):
        definition = Tex(r"Niech $f$ będzie określona w pewnym otoczeniu $U(x_0, h)$ punktu $x_0 \in X$. Wówczas wyrażenie",
            r"$$\Delta^1_s f(x_0, h) = f(x_0 + h) - f(x_0 - h)$$",   
            r"nazywamy ",
            r"\emph{pierwszą (parzystą) różnicą symetryczną funkcji} ",
            r"\( f \) w punkcie \( x_0 \).",
        tex_environment="flushleft").scale(0.7)

        definition_label = Tex(r"\textbf{Definicja}").set_color(YELLOW)
        box = SurroundingRectangle(definition, color = YELLOW, buff=0.5, corner_radius=0.2)
        definition_label.next_to(box, UP)

        self.play(Create(box), Write(definition_label))
        self.play(Write(definition))
        self.next_slide()

        self.play(definition[-4].animate.set_color(YELLOW))
        self.next_slide()

        self.play(definition[-2].animate.set_color(YELLOW))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_2(Slide):
    def construct(self):
        definition = Tex(
            r"Niech $f$ będzie określona w pewnym otoczeniu $U(x_0, h)$ punktu $x_0 \in X$. \\",
            r"\emph{Pochodną symetryczną funkcji}",
            r" $f$ w punkcie $x_0$ nazywamy granicę (o ile istnieje)",
        tex_environment="flushleft")

        eq1 = MathTex(r"\lim\limits_{h \to 0} \frac{\Delta_s^1 f(x_0, h)}{2h}").next_to(definition, DOWN)
        lub = Tex(r"lub równoważnie", tex_environment="flushleft").next_to(definition, 6 * DOWN, aligned_edge=LEFT)
        eq2 = MathTex(r"\lim\limits_{h \to 0} \frac{f(x_0 + h) - f(x_0 - h)}{2h}").next_to(definition, 8 * DOWN)
        oznaczamy = Tex(r"i oznaczamy ",
                       r"$f^*(x_0)$", tex_environment="flushleft").next_to(definition, 14 * DOWN, aligned_edge=LEFT)
        
        group = VGroup(definition, eq1, lub, eq2, oznaczamy).scale(0.7).move_to(ORIGIN)
        
        definition_label = Tex(r"\textbf{Definicja}").set_color(YELLOW)
        box = SurroundingRectangle(group, color = YELLOW, buff=0.5, corner_radius=0.2)
        definition_label.next_to(box, UP)

        self.play(Create(box), Write(definition_label))
        self.play(Write(group))
        self.next_slide()

        self.play(definition[-2].animate.set_color(YELLOW))
        self.next_slide()
        self.play(eq1.animate.set_color(YELLOW))
        self.next_slide()
        self.play(eq2.animate.set_color(YELLOW))
        self.next_slide()

        self.play(oznaczamy[-1].animate.set_color(YELLOW))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
    
# przyklad f(x) = |x|
class Scene_3(Slide):
    def construct(self):
        fact_label = Tex(r"\textbf{Fakt}").set_color(PURPLE)
        fact = Tex(r"Funkcja $f : \mathbb{R} \to \mathbb{R}$ dana wzorem",
                   r"$$f(x) = |x|$$",
                   r"\textbf{nie jest różniczkowalna}",
                   r" w punkcie ",
                   r"$x_0 = 0$")
        fact[2].set_color(PURPLE)
        fact[4].set_color(PURPLE)

        box = SurroundingRectangle(fact, color = PURPLE, buff=0.5, corner_radius=0.2)
        fact_label.next_to(box, UP)

        self.play(Create(box), Write(fact_label))
        self.play(Write(fact))
        self.next_slide()

        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        # Create modified fact with changed wording
        statement = Tex(r"Funkcja $f : \mathbb{R} \to \mathbb{R}$ dana wzorem",
                    r"$$f(x) = |x|$$",
                    r"\textbf{jest symetrycznie różniczkowalna}",
                    r" w punkcie ",
                    r"$x_0 = 0$")
        
        statement_box = SurroundingRectangle(statement, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(box, UP)

        statement[2].set_color(BLUE)
        statement[4].set_color(BLUE)

        self.play(
            TransformMatchingTex(fact_label, statement_label), 
            TransformMatchingTex(fact, statement), 
            Transform(box, statement_box)
        )
        self.next_slide()
        self.play(FadeOut(*self.mobjects))

        # dowod f(x) = |x| symetrycznie rozniczkowalna
        eq1 = MathTex(r"\lim_{h \to 0} \frac{f(x_0+h) - f(x_0-h)}{2h}")
        eq2 = MathTex(r"\lim_{h \to 0} \frac{|0+h| - |0-h|}{2h}")
        eq3 = MathTex(r"\lim_{h \to 0} \frac{|h| - |-h|}{2h}")
        eq4 = MathTex(r"\lim_{h \to 0} \frac{|h| - |h|}{2h}")
        eq5 = MathTex(r"\lim_{h \to 0} \frac{0}{2h}")
        eq6 = MathTex(r"\lim_{h \to 0} \frac{0}{2h} = 0")
        eq7 = MathTex(r"\lim_{h \to 0} \frac{f(x_0+h) - f(x_0-h)}{2h} = 0")
        eq8 = MathTex(r"f^*(0) = 0")

        self.play(Write(eq1))
        self.next_slide()
        self.play(TransformByGlyphMap(eq1, eq2,
            ([6], []), # f -> _
            ([7], [6]), # ( -> |
            ([12], [10]), # ) -> |
            ([14], []), # f -> _
            ([15], [12]), # f -> | 
            ([20], [16]),
            ([8,9], [7]),
            ([16,17], [13]),
            ([10], [8]),
            ([18], [14]),
            ([13], [11]),
            ([21], [17]),
            ([22,23], [18,19]),      
        ))
        self.next_slide()
        self.play(TransformByGlyphMap(eq2, eq3,
            ([7,8], []),
            ([13], []),

        ))
        self.next_slide()
        self.play(TransformByGlyphMap(eq3, eq4, 
            ([11], [])         
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq4, eq5,
            ([6,7,8,9,10,11,12], []),
            ([], [6])             
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq5, eq6,
            ([], [10,11])                 
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq6, eq7,
            ([6], []),
            ([], [_ for _ in range(6, 21)])                          
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq7, eq8,
            ([_ for _ in range(0, 24)], []),
            ([], [0,1,2,3,4])          
        ))
        self.next_slide()

        statement = Tex(r"$f$ ", 
            r"\textbf{jest symetrycznie różniczkowalna}", 
            r" w ", 
            r"$x_0 = 0$", 
            r".")
        
        statement[1].set_color(BLUE)
        statement[-2].set_color(BLUE)

        statement.next_to(eq8, 4 * DOWN)

        box = SurroundingRectangle(eq8, color = BLUE, buff=0.5, corner_radius=0.2)
        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()), Write(statement))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_4(Slide):
    def construct(self):
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        # Create modified fact with changed wording
        statement = Tex(
                    r"Jeśli pochodna funkcji $f$",
                    r" w punkcie $x \in X$ ",
                    r"istnieje",
                    r" to ",
                    r" pochodna symetryczna funkji $f$ ",
                    r" w tym punkcie",
                    r" też isnieje ",
                    r" oraz ",
                    r" zachodzi równość: ",
                    r"$$f^*(x) = f'(x).$$", tex_environment="flushleft").scale(0.7)
        
        statement_box = SurroundingRectangle(statement, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(statement_box, UP)

        self.play(Create(statement_box), Write(statement_label))
        self.play(Write(statement))
        self.next_slide()

        wniosek_label = Tex(r"\textbf{Wniosek}").set_color(ORANGE)
        wniosek = Tex(r"""
                      $f(x) = |x|$ \textbf{jest symetrycznie różniczkowalna} dla każdego $x$ oraz
                      \[
                        f^*(x) = 
                            \begin{cases}
                                1 & \text{dla } x > 0, \\
                                0 & \text{dla } x = 0, \\
                               -1 & \text{dla } x < 0.    
                            \end{cases}
                \]""").scale(0.8)
        wniosek_box = SurroundingRectangle(wniosek, color = ORANGE, buff=0.5, corner_radius=0.2)
        wniosek_label.next_to(wniosek_box, UP)

         # Color part of the text
        wniosek[0][8:38].set_color(ORANGE)  # Color 'f' red

        self.play(
            TransformMatchingTex(statement_label, wniosek_label), 
            TransformMatchingTex(statement, wniosek), 
            Transform(statement_box, wniosek_box)
        )
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# Uwaga 2 implikacja odwrotna nie zachodzi 
class Scene_5(Slide):
    def construct(self):
        uwaga_label = Tex(r"\textbf{Uwaga}").set_color(RED)

        # Create modified fact with changed wording
        uwaga = Tex(r"""
            Implikacja odwrotna nie zachodzi. Weźmy ponownie funkcję $f(x) = |x|$.
            Pochodna symetryczna istnieje dla każdego $x$, ale dla $x = 0$ pochodna klasyczna w tym punkcie nie istnieje.
        """, tex_environment="flushleft").scale(0.8)
        
        uwaga_box = SurroundingRectangle(uwaga, color = RED, buff=0.5, corner_radius=0.2)
        uwaga_label.next_to(uwaga_box, UP)

        self.play(Create(uwaga_box), Write(uwaga_label))
        self.play(Write(uwaga))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_6(Slide):
    def construct(self):
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        # Create modified fact with changed wording
        statement = Tex(r"""
            Jeśli $f$ ma pochodne jednostronne w punkcie $x \in X$, 
            to $f$ ma pochodną symetryczną w tym punkcie oraz
        """, tex_environment="flushleft")

        eq = MathTex(r"f^*(x) = \frac{f'_+(x) + f'_-(x)}{2}").next_to(statement, DOWN)

        group = VGroup(statement, eq).scale(0.8).move_to(ORIGIN)
        
        statement_box = SurroundingRectangle(group, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(statement_box, UP)

        self.play(Create(statement_box), Write(statement_label))
        self.play(Write(group))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# przyklad 4 pochodne jednostronne
class Scene_7(Slide):
    def construct(self):
        # Labelka z definicją
        label = Tex(r"$f(x) = \begin{cases} \frac{x}{1+e^{\frac{1}{x}}}, & x \neq 0 \\ 0, & x = 0 \end{cases}$")
        self.play(Write(label))
        self.next_slide()

        self.play(label.animate.move_to(2*UP))

        # Funkcja kawałkowa
        def piecewise_func(x):
            if x != 0:
                return x / (1 + np.exp(1 / x))
            else:
                return 0

        axes = Axes(
            x_range=[-0.5, 2, 0.5],
            y_range=[-0.5, 1.5, 0.5],
            x_axis_config = {
                "color": BLUE,
                "font_size": 30,
            },
            y_axis_config={
                "color": BLUE,
                "font_size": 30,
            },
        ).add_coordinates()

        graph = axes.plot(
            piecewise_func,
            color=WHITE,
        )

         # Create the dot at x = 0, f(0) = 0
        dot = Dot(axes.c2p(0, 0), color=WHITE)

        # Dodajemy
        self.play(Create(axes))
        self.play(Create(graph), Create(dot))

        self.next_slide()

        self.play(FadeOut(axes), FadeOut(graph), FadeOut(dot))
        self.next_slide()

        eq_lewa_1 = MathTex(r"f'_+(0) = \lim_{h \to 0^+}\frac{f(0+h) - f(0)}{h}")
        eq_lewa_2 = MathTex(r"f'_+(0) = \lim_{h \to 0^+}\frac{\frac{h}{1 + e^{\frac{1}{h}}}-0}{h}")
        eq_lewa_3 = MathTex(r"f'_+(0) = \lim_{h \to 0^+}\frac{\frac{h}{1+e^{\frac{1}{h}}}}{h}")
        eq_lewa_4 = MathTex(r"f'_+(0) = \lim_{h \to 0^+}\frac{1}{1 + e^{\frac{1}{h}}}")
        eq_lewa_5 = MathTex(r"f'_+(0) = 0")

        eq_prawa_1 = MathTex(r"f'_+(0) = \lim_{h \to 0^-}\frac{f(0+h) - f(0)}{h}")
        eq_prawa_2 = MathTex(r"f'_+(0) = \lim_{h \to 0^-}\frac{1}{1 + e^{\frac{1}{h}}}")
        eq_prawa_3 = MathTex(r"f'_+(0) = 1")

        self.play(Write(eq_lewa_1))
        self.next_slide()
        self.play(TransformByGlyphMap(eq_lewa_1, eq_lewa_2,
            ([_ for _ in range(14, 20)], []),
            ([], [_ for _ in range(14, 22)]),
            ([20], [22]),
            ([21,22,23,24], []),
            ([], [23])
        ))
        self.next_slide()
        self.play(TransformByGlyphMap(eq_lewa_2, eq_lewa_3,
            ([22,23], [])))
        self.next_slide()
        self.play(TransformByGlyphMap(eq_lewa_3, eq_lewa_4,
            ([22,23], [])
        ))
        self.next_slide()
        self.play(TransformByGlyphMap(eq_lewa_4, eq_lewa_5, ([_ for _ in range(7, 22)], []), ([], [7])))
        self.next_slide()

        eq_prawa_1.next_to(eq_lewa_5, DOWN)
        eq_prawa_2.next_to(eq_lewa_5, DOWN)
        eq_prawa_3.next_to(eq_lewa_5, DOWN)

        self.play(Write(eq_prawa_1))
        self.next_slide()

        self.play(TransformByGlyphMap(eq_prawa_1, eq_prawa_2,
            ([_ for _ in range(14, 25)], []),
            ([], [14]),
            ([25], [15]),
            ([26],[]),
            ([], [_ for _ in range(16,22)])
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq_prawa_2, eq_prawa_3, ([_ for _ in range(7,22)], []), ([], [7])))
        self.next_slide()

        eq_podsumowanie = MathTex(r"f_-'(0) \neq f_+'(0)")
        eq_label = Tex(r"$f$ ", r"\textbf{nie jest rózniczkowalna}", r" w ", r"$x_0 = 0$").next_to(eq_podsumowanie, 2 * DOWN)

        eq_label[-1].set_color(RED)
        eq_label[1].set_color(RED)

        group = VGroup(eq_prawa_3, eq_lewa_5)

        self.play(TransformMatchingTex(group, eq_podsumowanie))
        self.next_slide()

        box = SurroundingRectangle(eq_podsumowanie, color = RED, buff=0.5, corner_radius=0.2)
        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()), Write(eq_label))
        self.next_slide()

        self.play(FadeOut(eq_podsumowanie, eq_label))
        self.next_slide()

        eq = MathTex(r"f^*(0)")
        eq1 = MathTex(r"f^*(0) = \lim_{h \to 0}\frac{f(0+h) - f(0-h)}{2h}")
        eq2 = MathTex(r"f^*(0) = \lim_{h \to 0}\frac{\frac{h}{1+e^{\frac{1}{h}}} - \frac{-h}{1 + e^{\frac{1}{-h}}}}{2h}")
        eq3 = MathTex(r"f^*(0) = \lim_{h \to 0}\frac{1}{2}\Big(\frac{1}{1+e^{\frac{1}{h}}} + \frac{1}{1 + e^{\frac{1}{-h}}}\Big)")
        eq4 = MathTex(r"f^*(0) = \frac{1}{2}\left(f_+'(0) + f_-'(0)\right)")

        self.play(Write(eq))
        self.next_slide()
        self.play(TransformByGlyphMap(eq, eq1, 
            ([], [_ for _ in range(5, 28)]),
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq1, eq2,
            ([_ for _ in range(12, 18)], []),
            ([], [_ for _ in range(12, 20)]),
            ([18], [20]),
            ([25], [31]),
            ([26,27], [32,33]),
            ([_ for _ in range(19, 25)], []),
            ([], [_ for _ in range(21, 31)])
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq2, eq3, 
            ([_ for _ in range(12, 34)], []),
            ([], [_ for _ in range(12, 35)])
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq3, eq4,
            ([_ for _ in range(6, 12)], []),
            ([12,13,14], [6,7,8]),
            ([15], [9]),
            ([34], [23]),
            ([_ for _ in range(16, 24)], []),
            ([], [_ for _ in range(10, 16)]),
            ([24], [16]),
            ([_ for _ in range(25, 34)], []),
            ([], [_ for _ in range(17, 23)]),
        ))
        self.next_slide()

        self.play(FadeOut(label))
        
        box = SurroundingRectangle(eq4, color = BLUE, buff=0.5, corner_radius=0.2)
        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()))

class Scene_8(Slide):
    def construct(self):
         # Label
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        # The general assumptions
        intro = Tex(
            r"Niech $f, g$ będą ciągłe na przedziale $[a,b]$ oraz niech $f, g$ będą symetrycznie różniczkowalne w punkcie $x \in (a,b)$.",
            tex_environment="flushleft"
        ).scale(0.6)

        # List of items (a) to (d)
        items = [
            r"(a) $(\alpha f)^*(x) = \alpha f^*(x)$ dla każdego $\alpha \in \mathbb{R}$,",
            r"(b) $(f+g)^*(x) = f^*(x) + g^*(x)$,",
            r"(c) $(fg)^*(x) = f(x)g^*(x) + f^*(x)g(x)$,",
            r"(d) $\Big(\frac{f}{g}\Big)^*(x) = \frac{g(x)f^*(x) - g^*(x)f(x)}{g^2(x)}$, dla $g(x) \neq 0$.",
        ]

        item_mobjs = []
        for i, item in enumerate(items):
            tex_item = Tex(item).scale(0.6).align_to(intro, LEFT)
            if i == 0:
                tex_item.next_to(intro, DOWN, aligned_edge=LEFT)
            else:
                tex_item.next_to(item_mobjs[-1], DOWN, aligned_edge=LEFT)
            item_mobjs.append(tex_item)

        # Create the box
        group = VGroup(intro, *item_mobjs).move_to(ORIGIN)

        box = SurroundingRectangle(group, color=BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(box, UP)

        # Display the header and assumptions
        self.play(Write(statement_label), Create(box))
        self.play(Write(intro))
        self.next_slide()

        # Display each item one at a time
        for item in item_mobjs:
            self.play(Write(item))
            self.next_slide()

        # Optional fade out at end
        self.next_slide()
        self.play(FadeOut(*self.mobjects))

class Scene_9(Slide):
    def construct(self):
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        statement = Tex(r""" 
            Niech $f$ będzie ciągła na $[a,b]$ oraz symetrycznie różniczkowalna w punkcie $x \in (a,b)$.
            Niech $g$ będzie określona na przedziale $I$, który zawiera zbiór wartości funkcji $f$ i $g$ ma ciągłą pochodną symetryczną w punkcie $f(x)$.
            Jeśli
            $$
                z(x) = (g \circ f)(x), \quad a \leqslant x \leqslant b
            $$
            to pochodna symetryczna funkcji $z$ istnieje w punkcie $x$ oraz zachodzi
            $$
                z^*(x) = g^*(f(x)) \cdot f^*(x).
            $$
        """, tex_environment="flushleft").scale(0.6)

        statement_box = SurroundingRectangle(statement, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(statement_box, UP)

        self.play(Create(statement_box), Write(statement_label))
        self.play(Write(statement))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# przyklad 5 
class Scene_10(Slide):
    def construct(self):
        uwaga_label = Tex(r"\textbf{Uwaga}").set_color(RED)

        # Create modified fact with changed wording
        uwaga =  Tex(r"""
            Założenie o ciągłości pochodnej symetrycznej jest istotne.
        """, tex_environment="flushleft").scale(0.8)
        
        uwaga_box = SurroundingRectangle(uwaga, color = RED, buff=0.5, corner_radius=0.2)
        uwaga_label.next_to(uwaga_box, UP)

        self.play(Create(uwaga_box), Write(uwaga_label))
        self.play(Write(uwaga))
        self.next_slide()

        # przyklad zlozenia funkcji
        self.play(FadeOut(*self.mobjects))

        eqs = MathTex(r"""
            g(x) = \begin{cases}
                x, &x > 0, \\
                0, &x \leqslant 0,
            \end{cases} \quad 
            f(x) = \begin{cases}
                0, &x \geqslant 0, \\
                -x, &x < 0.
            \end{cases}
        """)

        self.play(Write(eqs))
        self.next_slide()

        self.play(eqs.animate.move_to(3 * UP).scale(0.6))
        self.next_slide()

        eqs_sym = MathTex(r"""
            g^*(x) = \begin{cases}
            1, &x > 0, \\
            \frac{1}{2}, &x = 0, \\
            0, &x < 0,
        \end{cases} \quad
        f^*(x) = \begin{cases}
            0, &x > 0, \\
            -\frac{1}{2}, &x = 0, \\
            -1, &x < 0.
        \end{cases}
        """)

        self.play(Write(eqs_sym))
        self.next_slide()

        self.play(eqs_sym.animate.next_to(eqs, DOWN).scale(0.6))
        self.next_slide()

        eq = MathTex(r"""
            z(x) = (g \circ f)(x) = \begin{cases}
            0, &x \geqslant 0, \\
            -x, &x < 0
        \end{cases}
        """).move_to(DOWN)

        self.play(Write(eq))
        self.next_slide()

        self.play(FadeOut(eqs), eqs_sym.animate.to_edge(UP))
        self.play(eq.animate.next_to(eqs_sym, DOWN).scale(0.6))
        self.next_slide()

        # .shift(3 * LEFT)

        eq_sym_z = MathTex(r"""
            z^*(x) = \begin{cases}
            0, &x > 0, \\
            -\frac{1}{2}, & x = 0, \\
            -1, &x < 0.
            \end{cases}
        """).shift(DOWN)

        self.play(Write(eq_sym_z))
        self.next_slide()

        self.play(FadeOut(eq), eqs_sym.animate.shift(2 * LEFT), eq_sym_z.animate.next_to(eqs_sym, RIGHT).shift(2.8 * LEFT).scale(0.6))
        self.next_slide()

        eq1 = MathTex(r"z^*(0) = g^*(f(0)) \cdot f^*(0)").scale(1.2)
        eq2 = MathTex(r"z^*(0) = g^*(0) \cdot f^*(0)").scale(1.2)
        eq3 = MathTex(r"z^*(0) =  g^*(0) \cdot \left( -\frac{1}{2} \right)").scale(1.2)
        eq4 = MathTex(r"z^*(0) = \frac{1}{2} \cdot \left( -\frac{1}{2} \right)").scale(1.2)
        eq5 = MathTex(r"z^*(0) = -\frac{1}{4}").scale(1.2)
        eq6 = MathTex(r"-\frac{1}{2} = z^*(0) = -\frac{1}{4}").scale(1.2)
        eq7 = MathTex(r"-\frac{1}{2} \neq -\frac{1}{4}").scale(1.2)
        eq_final = MathTex(r"z^*(0) \neq g^*(f(0)) \cdot f^*(0)").scale(1.2)

        box = SurroundingRectangle(eq_final, color=RED, buff=0.5, corner_radius=0.2)

        self.play(Write(eq1))
        self.next_slide()
        self.play(TransformByGlyphMap(eq1, eq2, ([9,10,12], [])))
        self.next_slide()
        self.play(TransformByGlyphMap(eq2, eq3, ([_ for _ in range(12,17)], []), ([], [_ for _ in range(12,18)])))
        self.next_slide()
        self.play(TransformByGlyphMap(eq3, eq4, ([_ for _ in range(6,11)], []), ([], [6,7,8])))
        self.next_slide()

        self.play(TransformByGlyphMap(eq4, eq5, ([_ for _ in range(6,16)], []), ([], [_ for _ in range(6,10)])))
        self.next_slide()

        self.play(TransformByGlyphMap(eq5, eq6, ([_ for _ in range(0,10)], [_ for _ in range(5,15)]), ([], [0,1,2,3,4])))
        self.next_slide()

        self.play(TransformByGlyphMap(eq6, eq7, ([4,5,6,7,8,9], []), ([10], [4,5]), ([11,12,13,14], [6,7,8,9])))
        self.next_slide()

        self.play(TransformByGlyphMap(eq7, eq_final, 
            ([0,1,2,3], []), 
            ([6,7,8,9], []),
            ([4,5], [5,6]),
            ([], [0,1,2,3,4]),
            ([], [_ for _ in range(7, 21)])
        ))
        self.next_slide()

        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_11(Slide):
    def construct(self):
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)
        common_text = Tex(r"""
            Jeśli $f$ jest różniczkowalna symetrycznie w punkcie $x$ oraz $f$ jest prawostronnie (lewostronnie) 
            różniczkowalna w punkcie $x$ to $f$ jest też lewostronnie (prawostronnie) różniczkowalna w tym punkcie.
        """, tex_environment="flushleft").scale(0.8)

        extra_text = Tex(r"""
            \\Co więcej, jeśli zachodzi równość
            $$
            f^*(x) = f'_+(x) \quad (\text{odpowiednio } f^*(x) = f'_{-}(x)),
            $$
            to również $f'_{-}(x) = f'_+(x)$ oraz
            pochodna w punkcie $x$ istnieje. 
        """, tex_environment="flushleft").scale(0.8)

        extra_text.next_to(common_text, DOWN, aligned_edge=LEFT)

        # Create initial box
        box = SurroundingRectangle(common_text, color=BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(box, UP)

        self.play(Create(box), Write(statement_label))
        self.play(Write(common_text))
        self.next_slide()

        # Create updated box that includes both
        group = VGroup(common_text, extra_text)
        new_box = SurroundingRectangle(group.copy().shift(UP), color=BLUE, buff=0.5, corner_radius=0.2)

        # Group the elements you want to shift up together
        everything = VGroup(extra_text, statement_label, common_text)

        # Create the animation
        self.play(
            Transform(box, new_box),
            FadeIn(extra_text, shift=UP),
            statement_label.animate.next_to(new_box, UP),
            everything.animate.shift(UP)
        )

        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_12(Slide):
    def construct(self):
        uwaga_label = Tex(r"\textbf{Uwaga}").set_color(RED)

        # Create modified fact with changed wording
        uwaga =  Tex(r"""
            Istnienie pochodnej symetrycznej w punkcie nie pociąga za sobą istnienia
            którejkolwiek z pochodnych jednostronnych.
        """, tex_environment="flushleft").scale(0.8)
        
        uwaga_box = SurroundingRectangle(uwaga, color = RED, buff=0.5, corner_radius=0.2)
        uwaga_label.next_to(uwaga_box, UP)

        self.play(Create(uwaga_box), Write(uwaga_label))
        self.play(Write(uwaga))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        formula = MathTex(
            r"f(x) = \begin{cases}"
            r"1, &x \in \mathbb{Q},\\"
            r"0, &x \in \mathbb{R} \setminus \mathbb{Q}"
            r"\end{cases}"
        )

        self.play(Write(formula))
        self.next_slide()

        self.play(formula.animate.to_edge(UP))
        self.next_slide()

        fact_label = Tex(r"\textbf{Fakt}").set_color(PURPLE)
        description = Tex(r"Funkcja $f$ ",
                          r"\textbf{nie ma pochodnych jednostronnych}",
                          r" w żadnym punkcie $x$").scale(0.8)
        description[-2].set_color(PURPLE)

        box = SurroundingRectangle(description, color=PURPLE, buff=0.5, corner_radius=0.2)
        fact_label.next_to(box, UP)

        self.play(Create(box), Write(fact_label))
        self.play(Write(description))
        self.next_slide()

        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)
        statement = Tex(r"Funkcja $f$ ",
                        r"\textbf{ma pochodną symetryczną}",
                        r" dla ",
                        r"$x \in \mathbb{Q}$")
        
        statement_box = SurroundingRectangle(statement, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(box, UP)
        
        statement[-1].set_color(BLUE)
        statement[1].set_color(BLUE)

        self.play(
            TransformMatchingTex(fact_label, statement_label), 
            TransformMatchingTex(description, statement), 
            Transform(box, statement_box)
        )
        self.next_slide()

        self.play(FadeOut(statement_label, statement), FadeOut(box))
        self.next_slide()

        case_intro = Tex(r"Weźmy punkt $x \in \mathbb{Q}$.").scale(0.7)

        case_a = Tex(r"(a) Jeśli $h$ jest liczbą wymierną, to $x+h$, $x-h$ też są liczbami wymiernymi.").scale(0.7)
        calc_a = MathTex(r"f(x+h) - f(x-h) = 1 - 1 = 0").scale(0.7)

        case_b = Tex(r"(b) Jeśli $h$ jest niewymierne, to $x+h$, $x-h$ też są niewymierne.").scale(0.7)
        calc_b = MathTex(r"f(x+h) - f(x-h) = 0 - 0 = 0").scale(0.7)

        conclusion_intro = Tex(r"Zatem $f^*(x) = \lim\limits_{h \to 0} \frac{f(x+h) - f(x-h)}{2h} = \lim\limits_{h \to 0} \frac{0}{2h} = 0$").scale(0.7)

        group = VGroup(
            case_intro, case_a, calc_a, case_b, calc_b, conclusion_intro
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(formula, DOWN)

        box = SurroundingRectangle(conclusion_intro, color=BLUE, buff=0.3, corner_radius=0.2)

        for mobj in group:
            self.play(Write(mobj))
            self.next_slide()

        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# przyklad 7 funkcja ktora nie jest ciagla w zadnym punkcie i ma pochodna w punkcie gdzie nie jest zdefiniowana
class Scene_13(Slide):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-10, 10, 2],
            x_length=15,
            y_length=15,
            axis_config={"include_numbers": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Add a title
        formula = Tex(r"$f(x) = \begin{cases} \left| \frac{1}{x} \right|, & x \in \mathbb{Q} \setminus \{0\} \\[3pt] -\left| \frac{1}{x} \right|, & x \in \mathbb{R} \setminus \mathbb{Q} \end{cases}$")

        self.play(Write(formula))
        self.next_slide()

        self.play(formula.animate.to_edge(UL).scale(0.7))
        self.next_slide()

        self.play(Create(axes), Write(labels))

        # Create x values with more density near zero
        left = np.linspace(-5, -0.1, 50)
        right = np.linspace(0.1, 5, 50)
        x_vals = np.concatenate((left, right))

        rational_dots = VGroup()
        irrational_dots = VGroup()

        for x in x_vals:
            y = abs(1 / x)

            # Rational (simulated): blue
            dot_rational = Dot(point=axes.c2p(x, y), radius=0.035, color=BLUE)

            # Irrational (simulated): red, slightly offset
            dot_irrational = Dot(point=axes.c2p(x + 0.02, -y), radius=0.035, color=BLUE)

            rational_dots.add(dot_rational)
            irrational_dots.add(dot_irrational)

        self.play(Create(rational_dots), Create(irrational_dots))
        self.next_slide()

        self.play(FadeOut(axes, labels, rational_dots, irrational_dots), formula.animate.move_to(ORIGIN).to_edge(UP))
        self.next_slide()

        case_intro = Tex(r"Weźmy punkt $x = 0$ ($x \in \mathbb{Q}$).").scale(0.7).next_to(formula, DOWN).to_edge(LEFT)
        self.play(Write(case_intro))
        self.next_slide()

        case_a = Tex(r"(a) Jeśli $h$ jest liczbą wymierną, to $x+h$, $x-h$ też są liczbami wymiernymi.").scale(0.7).next_to(case_intro, DOWN).to_edge(LEFT)
        calc_a_1 = MathTex(r"f(x+h) - f(x-h)").scale(0.7).next_to(case_a, DOWN)
        calc_a_2 = MathTex(r"f(x+h) - f(x-h) = \left| \frac{1}{h} \right| - \left| \frac{1}{-h} \right|").scale(0.7).next_to(case_a, DOWN)
        calc_a_3 = MathTex(r"f(x+h) - f(x-h) = \left| \frac{1}{h} \right| - \left| \frac{1}{-h} \right| = \left| \frac{1}{h} \right| - \left| \frac{1}{h} \right|").scale(0.7).next_to(case_a, DOWN)
        calc_a_4 = MathTex(r"f(x+h) - f(x-h) = \left| \frac{1}{h} \right| - \left| \frac{1}{-h} \right| = \left| \frac{1}{h} \right| - \left| \frac{1}{h} \right| = 0").scale(0.7).next_to(case_a, DOWN)

        self.play(Write(case_a))
        self.next_slide()
        self.play(Write(calc_a_1))
        self.next_slide()

        self.play(TransformByGlyphMap(calc_a_1, calc_a_2, ([], [_ for _ in range(13, 38)])))
        self.next_slide()

        self.play(TransformByGlyphMap(calc_a_2, calc_a_3, ([], [_ for _ in range(38, 62)])))
        self.next_slide()

        self.play(TransformByGlyphMap(calc_a_3, calc_a_4, ([], [62,63])))
        self.next_slide()

        case_b = Tex(r"(b) Jeśli $h$ jest niewymierne, to $x+h$, $x-h$ też są niewymierne.").scale(0.7).next_to(calc_a_4, DOWN).to_edge(LEFT)
        calc_b_1 = MathTex(r"f(x+h) - f(x-h)").scale(0.7).next_to(case_b, DOWN)
        calc_b_2 = MathTex(r"f(x+h) - f(x-h) = - \left| \frac{1}{h} \right| - \left( -\left| \frac{1}{-h} \right| \right)").scale(0.7).next_to(case_b, DOWN)
        calc_b_3 = MathTex(r"f(x+h) - f(x-h) = - \left| \frac{1}{h} \right| - \left( -\left| \frac{1}{-h} \right| \right) = - \left| \frac{1}{h} \right| + \left| \frac{1}{h} \right|").scale(0.7).next_to(case_b, DOWN)
        calc_b_4 = MathTex(r"f(x+h) - f(x-h) = - \left| \frac{1}{h} \right| - \left( -\left| \frac{1}{-h} \right| \right) = - \left| \frac{1}{h} \right| + \left| \frac{1}{h} \right| = 0").scale(0.7).next_to(case_b, DOWN)

        self.play(Write(case_b))
        self.next_slide()
        self.play(Write(calc_b_1))
        self.next_slide()

        self.play(TransformByGlyphMap(calc_b_1, calc_b_2, ([], [_ for _ in range(13, 42)])))
        self.next_slide()

        self.play(TransformByGlyphMap(calc_b_2, calc_b_3, ([], [_ for _ in range(42, 67)])))
        self.next_slide()

        self.play(TransformByGlyphMap(calc_b_3, calc_b_4, ([], [67,68])))
        self.next_slide()

        conclusion_intro = Tex(r"Zatem $f^*(x) = \lim\limits_{h \to 0} \frac{f(x+h) - f(x-h)}{2h} = \lim\limits_{h \to 0} \frac{0}{2h} = 0$").scale(0.7).next_to(calc_b_4, DOWN).to_edge(LEFT)
        self.play(Write(conclusion_intro))

        box = SurroundingRectangle(conclusion_intro, color=BLUE, buff=0.2, corner_radius=0.2)

        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        wniosek_label = Tex(r"\textbf{Wniosek}").set_color(ORANGE)
        wniosek = Tex(r"Funkcja ", 
                      r"\textbf{może posiadać pochodną symetryczną}",
                      r" w punkcie, ",
                      r"\textbf{nawet jeśli}",
                      r" sama ",
                      r"\textbf{nie jest}",
                      r" w tym punkcie ",
                      r"\textbf{określona}.").scale(0.7)
        
        wniosek[-1].set_color(ORANGE)
        wniosek[-3].set_color(ORANGE)
        wniosek[-5].set_color(ORANGE)
        wniosek[-7].set_color(ORANGE)

        wniosek_box = SurroundingRectangle(wniosek, color = ORANGE, buff=0.5, corner_radius=0.2)
        wniosek_label.next_to(wniosek_box, UP)

        self.play(Write(wniosek_label), Create(wniosek_box))
        self.next_slide()

        self.play(Write(wniosek))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# Intro do C.E Aulla i jego prac
class Scene_14(Slide):
    def construct(self):
        info = Tex(r"Charles Edward Aull")

        born_and_died = Tex(r"1927 - 2009")
        born_and_died.next_to(info, DOWN)

        info_book = Tex(r"The first symmetric derivative (1967)")
        info_book.next_to(born_and_died, DOWN)
        
        self.play(Write(info))
        self.play(Write(born_and_died))
        self.next_slide()

        self.play(Write(info_book))
        self.next_slide()

        self.play(FadeOut(info), FadeOut(born_and_died), info_book.animate.to_edge(UP))
        self.next_slide()

        lemat_label = Tex(r"\textbf{Lemat}").set_color(GREEN)

        lemat = Tex(r"""
            Niech $f$ będzie ciągła na przedziale $[a,b]$ oraz symetrycznie różniczkowalna na $(a,b)$.
            Niech $f(b) > f(a)$ ($f(b) < f(a)$). Wówczas istnieje punkt $c \in (a,b)$ taki, że 
            $f^*(c) \geqslant 0$ ($ f^*(c)\leqslant 0$).
        """, tex_environment="flushleft").scale(0.6)

        lemat_box = SurroundingRectangle(lemat, color=GREEN, buff=0.5, corner_radius=0.2)
        lemat_label.next_to(lemat_box, UP)

        self.play(Create(lemat_box), Write(lemat_label))
        self.play(Write(lemat))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# tw rolle'a -> quasi twierdzenie rollea'
class Scene_15(Slide):
    def construct(self):
        rolle_label = Tex(r"\textbf{Twierdzenie Rolle'a}").set_color(BLUE)

        rolle = Tex(r"""
            Niech $f$ będzie ciągła na $[a,b]$ oraz różniczkowalna na $(a,b)$. \\
            Niech $f(a) = f(b) = 0$. Wówczas istnieje punkt $c \in (a,b)$ taki, że
        """, tex_environment="flushleft").scale(0.8)
        rolle_tex = MathTex(r"f'(c) = 0").scale(0.8).next_to(rolle, DOWN)

        group = VGroup(rolle, rolle_tex)

        rolle_box = SurroundingRectangle(group, color=BLUE, buff=0.5, corner_radius=0.2)
        rolle_label.next_to(rolle_box, UP)

        self.play(Create(rolle_box), Write(rolle_label))
        self.next_slide()

        self.play(Write(rolle))
        self.play(Write(rolle_tex))
        self.next_slide()

        quasi_rolle_label = Tex(r"\textbf{Quasi Twierdzenie Rolle'a}").set_color(BLUE)

        quasi_rolle = Tex(r"""
            Niech $f$ będzie ciągła na $[a,b]$ oraz symetrycznie różniczkowalna na $(a,b).$ \\
            Niech $f(a) = f(b) = 0$. Wówczas istnieją punkty $c_1,c_2 \in (a,b)$ takie, że 
        """, tex_environment="flushleft").scale(0.8)
        quasi_rolle_tex = MathTex(r"f^*(c_1) \geqslant 0 \quad \text{oraz} \quad f^*(c_2) \leqslant 0.").scale(0.8).next_to(quasi_rolle, DOWN)

        group2 = VGroup(quasi_rolle, quasi_rolle_tex)
        
        quasi_rolle_box = SurroundingRectangle(group2, color=BLUE, buff=0.5, corner_radius=0.2)
        quasi_rolle_label.next_to(quasi_rolle_box, UP)

        self.play(
            TransformByGlyphMap(rolle_label, quasi_rolle_label, ([], [0,1,2,3,4])),
            FadeTransform(rolle, quasi_rolle),
            FadeTransform(rolle_tex, quasi_rolle_tex),
            Transform(rolle_box, quasi_rolle_box)
            )
        self.next_slide()

class Scene_16(Slide):
    def construct(self):
        statement = Tex(r""" 
            Niech $f$ będzie ciągła na $[a,b]$ oraz różniczkowalna na $(a,b)$. \\ 
            Wówczas istnieje punkt $c \in (a,b)$ taki, że
        """, tex_environment="flushleft").scale(0.8)
        statement_tex = MathTex(r"f'(c) = \frac{f(b) - f(a)}{b-a} ").scale(0.8).next_to(statement, DOWN)

        group = VGroup(statement, statement_tex)

        statement_label = Tex(r"\textbf{Twierdzenie Lagrange'a o Wartości Średniej} ").set_color(BLUE)

        statement_box = SurroundingRectangle(group, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(statement_box, UP)

        self.play(Create(statement_box), Write(statement_label))
        self.next_slide()

        self.play(Write(group))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        # uwaga do tw Lagrange'a
        uwaga_label = Tex(r"\textbf{Uwaga}").set_color(RED)

        # Create modified fact with changed wording
        uwaga = Tex(r"""
           Poprzednie twierdzenie nie przenosi się poprzez \\
           analogie na przypadek pochodnej symetrycznej
        """, tex_environment="flushleft")
        
        uwaga_box = SurroundingRectangle(uwaga, color = RED, buff=0.5, corner_radius=0.2)
        uwaga_label.next_to(uwaga_box, UP)

        self.play(Create(uwaga_box), Write(uwaga_label))
        self.next_slide()

        self.play(Write(uwaga))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        # przyklad do tw Lagrange'a
        function = Tex(r"$f(x) = |x|$ na przedziale $[-1, 2]$")
        self.play(Write(function))
        self.next_slide()

        sym_derivative = MathTex(r"""f^*(x) = \begin{cases} 
             1 & x > 0, \\
             0 & x = 0, \\
            -1 & x < 0.
        \end{cases}""")

        rectange = SurroundingRectangle(sym_derivative, color=PURPLE, buff=0.5, corner_radius=0.2)

        sym_values = MathTex(r"""f^*(x) \in \{-1, 0, 1\}""")

        rectange2 = SurroundingRectangle(sym_values, color=PURPLE, buff=0.5, corner_radius=0.2)

        self.play(function.animate.to_edge(UP))
        self.play(Create(rectange))
        self.play(Write(sym_derivative))
        self.next_slide()

        self.play(TransformByGlyphMap(sym_derivative, sym_values, 
            ([5], [5]),
            ([_ for _ in range(6,27)], []), 
            ([], [_ for _ in range(6,14)])), 
            Transform(rectange, rectange2))
        self.next_slide()

        self.play(FadeOut(rectange))
        self.play(sym_values.animate.next_to(function, DOWN))
        self.next_slide()

        take_c = MathTex(r"c \in (-1, 2)")

        self.play(Write(take_c))
        self.next_slide()

        self.play(take_c.animate.next_to(sym_values, DOWN))
        self.next_slide()

        eq = MathTex(r"f^*(c) = \frac{f(2) - f(-1)}{2 - (-1)}")
        eq1 = MathTex(r"f^*(c) = \frac{f(2) - f(-1)}{2 - (-1)} = \frac{|2| - |-1|}{2 + 1}")
        eq2 = MathTex(r"f^*(c) = \frac{f(2) - f(-1)}{2 - (-1)} = \frac{|2| - |-1|}{2 + 1} = \frac{1}{3}")
        eq3 = MathTex(r"f^*(c) = \frac{1}{3}")
        eq4 = MathTex(r"f^*(c) = \frac{1}{3} \notin \{-1, 0, 1\}")

        self.play(Write(eq))
        self.next_slide()

        self.play(TransformByGlyphMap(eq, eq1, ([], [_ for _ in range(23, 36)])))
        self.next_slide()

        self.play(TransformByGlyphMap(eq1, eq2, ([], [36,37,38,39])))
        self.next_slide()

        self.play(TransformByGlyphMap(eq2, eq3, 
            ([_ for _ in range(6,37)], []),
        ))
        self.next_slide()

        self.play(TransformByGlyphMap(eq3, eq4, ([], [_ for _ in range(9, 19)])))
        self.next_slide()

        box = SurroundingRectangle(eq4, color=RED, buff=0.5, corner_radius=0.2)
        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        self.play(FadeIn(statement, statement_box, statement_label, statement_tex))
        self.next_slide()

        statement2_label = Tex(r"\textbf{Twierdzenie Aull'a o Wartości Średniej}").set_color(BLUE)

        statement2 = Tex(r"""
            Niech $f$ będzie ciągła na $[a,b]$ oraz symetrycznie różniczkowalna w $(a,b)$. \\ 
            Wówczas istnieją punkty $c_1, c_2 \in (a,b)$ takie, że
        """, tex_environment="flushleft").scale(0.8)

        statement2_tex = MathTex(r"f^*(c_1) \leqslant \frac{f(b) - f(a)}{b-a} \leqslant f^*(c_2)").scale(0.8).next_to(statement2, DOWN)

        group2 = VGroup(statement2, statement2_tex)

        statement2_box = SurroundingRectangle(group2, color = BLUE, buff=0.5, corner_radius=0.2)
        statement2_label.next_to(statement2_box, UP)

        self.play(
            FadeTransform(statement_label, statement2_label),
            FadeTransform(statement, statement2),
            FadeTransform(statement_tex, statement2_tex),
            Transform(statement_box, statement2_box)
            )
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_17(Slide):
    def construct(self):
        # Title and box
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        # Main statement without items
        intro = Tex(r"Niech $f$ będzie ciągła na $[a,b]$ oraz symetrycznie różniczkowalna na $(a,b)$.",
                    tex_environment="flushleft").scale(0.7).move_to(UP)

        # List items separated
        item_a = Tex(r"(a) Jeżeli $f^*(x) \geqslant 0$ dla każdego $x \in (a,b)$, to $f$ jest rosnąca.", tex_environment="flushleft").scale(0.7)
        item_b = Tex(r"(b) Jeżeli $f^*(x) = 0$ dla każdego $x \in (a,b)$, to $f$ jest stała.", tex_environment="flushleft").scale(0.7)
        item_c = Tex(r"(c) Jeżeli $f^*(x) \leqslant 0$ dla każdego $x \in (a,b)$, to $f$ jest malejąca.", tex_environment="flushleft").scale(0.7)

        # Positioning
        item_a.next_to(intro, DOWN, aligned_edge=LEFT)
        item_b.next_to(item_a, DOWN, aligned_edge=LEFT)
        item_c.next_to(item_b, DOWN, aligned_edge=LEFT)

        # Box and label
        statement_box = SurroundingRectangle(VGroup(intro, item_a, item_b, item_c), color=BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(statement_box, UP)

        self.play(Create(statement_box), Write(statement_label))

        # Show header
        self.play(Write(intro))
        self.next_slide()

        # Show each item with separate clicks
        self.play(Write(item_a))
        self.next_slide()

        self.play(Write(item_b))
        self.next_slide()

        self.play(Write(item_c))
        self.next_slide()

        # Fade out everything at the end
        self.play(FadeOut(*self.mobjects))


class Scene_18(Slide):
    def construct(self):
        definition = Tex(r"""
            Niech $f : [a,b] \to \mathbb{R}$ będzie ciągła. Mówimy, że $f$ ma własność Darboux, \\
            jeśli dla dowolnego $y$ spełniającego $f(a) < y < f(b)$ ($f(a) > y > f(b)$) \\
            istnieje $x \in (a,b)$ takie, że
        """, tex_environment="flushleft").scale(0.8)

        definition_tex = MathTex(r"f(x) = y").scale(0.8).next_to(definition, DOWN)
        definition_label = Tex(r"\textbf{Definicja}").set_color(YELLOW)

        group = VGroup(definition, definition_tex)

        box = SurroundingRectangle(group, color = YELLOW, buff=0.5, corner_radius=0.2)

        definition_label.next_to(box, UP)

        self.play(Create(box), Write(definition_label))
        self.play(Write(group))
        self.next_slide()

        fact = Tex(r"""
            Każda funkcja ciągła $f$ określona na przedziale $[a,b]$ ma własność Darboux.
        """, tex_environment="flushleft").scale(0.7)
        
        fact_label = Tex(r"\textbf{Fakt}").set_color(PURPLE)
        fact_box = SurroundingRectangle(fact, color = PURPLE, buff=0.5, corner_radius=0.2)
        fact_label.next_to(fact_box, UP)

        self.play(Transform(definition_label, fact_label), FadeOut(group), FadeIn(fact), Transform(box, fact_box))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

class Scene_19(Slide):
    def construct(self):
        statement = Tex(r"""
            Niech $f$ będzie ciągła na przedziale $[a,b]$ oraz symetrycznie różniczkowalna na $(a,b)$. 
            Jeśli pochodna symetryczna $f$ ma własność Darboux, to istnieje $x \in (a,b)$ taki, że 
        """, tex_environment="flushleft").scale(0.7)

        statement_tex = MathTex(r"f^*(x) = \frac{f(b) - f(a)}{b-a}").scale(0.7).next_to(statement, DOWN)
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        group = VGroup(statement, statement_tex)

        statement_box = SurroundingRectangle(group, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(statement_box, UP)

        self.play(Create(statement_box), Write(statement_label))
        self.play(Write(group))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_20(Slide):
    def construct(self):
        statement = Tex(r"""
            Niech $f$ będzie ciągła na przedziale $[a,b]$ oraz symetrycznie różniczkowalna w sposób ciągły na $(a,b)$.
            Wówczas $f$ jest różniczkowalna oraz
            \[
                f'(x) = f^*(x)
            \]
            dla każdego $x \in (a,b)$.
        """, tex_environment="flushleft").scale(0.7)
        
        statement_label = Tex(r"\textbf{Twierdzenie}").set_color(BLUE)

        statement_box = SurroundingRectangle(statement, color = BLUE, buff=0.5, corner_radius=0.2)
        statement_label.next_to(statement_box, UP)

        self.play(Create(statement_box), Write(statement_label))
        self.play(Write(statement))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

class Scene_30(Slide):
    def construct(self):
        uwaga_label = Tex(r"\textbf{Uwaga}").set_color(RED)
        uwaga = Tex(r"""
            Poprzednie twierdzenie nie zachodzi, gdy $f$ i $f^*$ są ciągłe w jednym punkcie z przedziału $(a,b)$. 
            Twierdzenie wymagało, aby funkcja i jej pochodna symetryczna były ciągłe w każdym punkcie przedziału. 
        """, tex_environment="flushleft").scale(0.7)

        uwaga_box = SurroundingRectangle(uwaga, color = RED, buff=0.5, corner_radius=0.2)
        uwaga_label.next_to(uwaga_box, UP)

        self.play(Create(uwaga_box), Write(uwaga_label))
        self.play(Write(uwaga))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        # przyklad

        function_tex = MathTex(r""" f(x) = \begin{cases}
            |x|, &x = \frac{1}{n} \quad (n = \pm 1, \pm 2, \ldots) \\
            x^2, &\text{w przeciwnym wypadku}
        \end{cases}
        """)

        self.play(Write(function_tex))
        self.next_slide()

        # fakt f jest ciagla w zerze

        fact_label = Tex(r"\textbf{Fakt}").set_color(PURPLE)
        fact = Tex(r"$f$ jest ciągła w $x_0 = 0$")

        box = SurroundingRectangle(fact, color = PURPLE, buff=0.5, corner_radius=0.2)
        fact_label.next_to(box, UP)

        self.play(function_tex.animate.to_edge(UP))
        self.next_slide()

        self.play(Create(box), Write(fact_label))
        self.play(Write(fact))
        self.next_slide()

        fact2 = Tex(r"$f$ jest ciągła w $x_0 = 0$, $f^*(x) = 2x$ dla każdego $x$")

        box2 = SurroundingRectangle(fact2, color = PURPLE, buff=0.5, corner_radius=0.2)
        facts = Tex(r"\textbf{Fakty}").next_to(box2, UP).set_color(PURPLE)

        self.play(Transform(fact_label, facts), Transform(box, box2))
        self.play(TransformByGlyphMap(fact, fact2, ([], [_ for _ in range(16,36)])))
        self.next_slide()

        self.play(FadeOut(box, fact_label), fact2.animate.next_to(function_tex, 2 * DOWN))

        iloraz = MathTex(r"\frac{f(0+h) - f(0)}{h} = \frac{f(h)}{h} = \begin{cases} h, &h \neq \frac{1}{n} \\ \frac{|h|}{h}, &h = \frac{1}{n} \end{cases}").next_to(fact2, 2* DOWN)

        self.play(Write(iloraz))
        self.next_slide()

        box = SurroundingRectangle(iloraz, buff=0.25, corner_radius=0.2, color=RED)

        self.play(Create(box))
        self.play(Uncreate(box.reverse_direction()))
        self.next_slide()

        podsumowanie = Tex(r"$f$ ", r"\textbf{nie jest różniczkowalna}", r" w punkcie ", r"$x_0 = 0$").next_to(iloraz, DOWN)
        podsumowanie[-1].set_color(RED)
        podsumowanie[1].set_color(RED)

        self.play(Write(podsumowanie))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))


class Zastosowania(Slide):
    def construct(self):
        title = Tex(r"\textbf{Zastosowania i Motywacje}").set_color(ORANGE)
       
        a = Tex(r"(a) rozwiązywanie problemów programowania matematycznego z warunkami optymalności Kuhna-Tuckera", tex_environment="flushleft").next_to(title, DOWN, aligned_edge=LEFT)
        b = Tex(r"(b) rozwiązywanie problemów optymalizacyjnych w układach nieliniowych", tex_environment="flushleft").next_to(a, DOWN, aligned_edge=LEFT)
        c = Tex(r"(c) numeryczne metody przybliżania wartości funkcji", tex_environment="flushleft").next_to(b, DOWN, aligned_edge=LEFT)
        d = Tex(r"(d) wprowadzenie do szerszej teorii zagadnień symetrycznych (ciągłość, całkowalność)", tex_environment="flushleft").next_to(c, DOWN, aligned_edge=LEFT)

        group = VGroup(a,b,c, d).scale(0.7).move_to(ORIGIN)

        box = SurroundingRectangle(group, color = ORANGE, buff = 0.5, corner_radius = 0.2)
        title.next_to(box, UP)

        self.play(Write(title), Create(box))
        self.next_slide()

        self.play(Write(a))
        self.next_slide()

        self.play(Write(b))
        self.next_slide()

        self.play(Write(c))
        self.next_slide()

        self.play(Write(d))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
        self.next_slide()

class Literature(Slide):
    def construct(self):
        literature_label = Tex(r"$\textbf{Literatura}$").set_color(ORANGE)
        literature = Tex(r"""
            \begin{itemize}
                \item Minch, R. A. (1971). Applications of symmetric derivatives in mathematical programming
                \item Haines, S. L. (1965). The Symmetric Derivative.
                \item Wilczyński, W. (2015). Funkcje lub ciągi funkcyjne o specjalnych własnościach, których konstrukcje zawdzięczamy polskim matematykom.
                \item Aull, C.E (1967). The First Symmetric Derivative.
                \item Thomson, B.S (1994). Symmetric properties of real functions
            \end{itemize}
        """).scale(0.7)

        box = SurroundingRectangle(literature, color = ORANGE, buff = 0.5, corner_radius=0.2)
        literature_label.next_to(box, UP)

        self.play(Create(box), Write(literature_label))
        self.play(Write(literature))

        self.next_slide()
