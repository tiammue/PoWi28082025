from manim import *

class Kommunalpolitik(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Scene 1: Introduction
        title = Text("Kommunalpolitik: Was es ist und warum es wichtig ist").scale(0.75)
        self.play(FadeIn(title), Write(title))
        self.wait(2)

        self.play(FadeOut(title))
        self.wait(1)

        # Scene 2: What Does a Kommune Do?
        kommune_tasks = Text("Was macht eine Kommune?").scale(0.75)
        self.play(FadeIn(kommune_tasks), Write(kommune_tasks))
        self.wait(2)
        self.play(FadeOut(kommune_tasks))
        self.wait(1)

        tasks = BulletedList(
                    "Öffentliche Dienstleistungen",
                    "Lokale Infrastruktur",
                    "Gemeinschaftsentwicklung"
                ).scale(0.6)
        self.play(FadeIn(tasks), Write(tasks))
        self.wait(3)
        self.play(FadeOut(tasks))
        self.wait(1)

        # Scene 3: How Is It Organized?
        organization = Text("Wie ist sie organisiert?").scale(0.75)
        self.play(FadeIn(organization), Write(organization))
        self.wait(2)
        self.play(FadeOut(organization))
        self.wait(1)

        # Create a diagram illustrating the structure of Kommunalpolitik
        rat = Text("Rat").scale(0.5)
        verwaltung = Text("Verwaltung").scale(0.5)
        burgermeister = Text("Bürgermeister:in").scale(0.5)

        rat.to_edge(UP)
        burgermeister.move_to(ORIGIN)
        verwaltung.to_edge(DOWN)

        self.play(FadeIn(rat), FadeIn(verwaltung), FadeIn(burgermeister), Write(rat), Write(verwaltung), Write(burgermeister))
        self.wait(3)
        self.play(FadeOut(rat), FadeOut(verwaltung), FadeOut(burgermeister))
        self.wait(1)

        # Scene 4: Get Involved!
        get_involved = Text("Mach mit!").scale(0.75)
        self.play(FadeIn(get_involved), Write(get_involved))
        self.wait(2)
        self.play(FadeOut(get_involved))
        self.wait(1)

        involvement_methods = BulletedList(
                    "Wählen",
                    "Bürgerinitiativen",
                    "Ratssitzungen"
                ).scale(0.6)
        self.play(FadeIn(involvement_methods), Write(involvement_methods))
        self.wait(3)
        self.play(FadeOut(involvement_methods))
        self.wait(1)

        # Scene 5: Kommunalpolitik in Your Daily Life
        daily_life = Text("Kommunalpolitik in deinem Alltag").scale(0.75)
        self.play(FadeIn(daily_life), Write(daily_life))
        self.wait(2)
        self.play(FadeOut(daily_life))
        self.wait(1)

        daily_life_examples = BulletedList(
                    "Schulen",
                    "Transport",
                    "Parks",
                    "Abfallwirtschaft"
                ).scale(0.6)
        self.play(FadeIn(daily_life_examples), Write(daily_life_examples))
        self.wait(3)
        self.play(FadeOut(daily_life_examples))
        self.wait(1)

        # Scene 6: Hamm Examples
        hamm_examples = Text("Kommunalpolitik in Hamm").scale(0.75)
        self.play(FadeIn(hamm_examples), Write(hamm_examples))
        self.wait(2)
        self.play(FadeOut(hamm_examples))
        self.wait(1)

        # TODO: Add ASH logo here

        # TODO: Add picture of Rathaus Hamm here

        # TODO: Add pictures of mayoral candidates (Marc Herter and Jochen Dornseifer) here

        mayor_candidates = BulletedList(
            "Marc Herter (SPD)",
            "Jochen Dornseifer (CDU)",
            "Marc Herter: [Placeholder for platform]",
            "Jochen Dornseifer: [Placeholder for platform]"
        ).scale(0.6)
        self.play(FadeIn(mayor_candidates), Write(mayor_candidates))
        self.wait(3)
        self.play(FadeOut(mayor_candidates))
        self.wait(1)

        # Scene 7: Why Vote?
        why_vote = Text("Warum wählen?").scale(0.75)
        self.play(FadeIn(why_vote), Write(why_vote))
        self.wait(2)
        self.play(FadeOut(why_vote))
        self.wait(1)

        voting_importance = Text("Gestalte die Zukunft deiner Gemeinde!").scale(0.6)
        self.play(FadeIn(voting_importance), Write(voting_importance))
        self.wait(1)
        self.play(FadeOut(voting_importance))
        self.wait(1)

        voting_is_crucial = Text("Deine Stimme zählt!").scale(0.7)
        self.play(FadeIn(voting_is_crucial), Write(voting_is_crucial))
        self.wait(2)
        self.play(FadeOut(voting_is_crucial))
        self.wait(1)

        # TODO: Add a visual element (e.g., a map of Germany zooming into Hamm) in the introduction.
        # TODO: Use icons or animations to represent the different municipal services.
        # TODO: Add transitions between scenes for better visual flow.
        # TODO: Adjust the timing of animations and pauses for optimal pacing.
        # TODO: Add background music or sound effects to enhance the animation.
        # TODO: Consider adding more detailed information about the candidates and their platforms.

        # Scene 8: Conclusion
        conclusion = Text("Kommunalpolitik: Essentiell für eine blühende Gemeinde!").scale(0.75)
        self.play(FadeIn(conclusion), Write(conclusion))
        self.wait(3)
        self.play(FadeOut(conclusion))
        self.wait(1)