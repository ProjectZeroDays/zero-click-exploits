import panel as pn

class C2Dashboard:
    def render(self):
        return pn.Column(
            "### Command and Control Dashboard",
            pn.pane.Markdown("Welcome to the C2 Dashboard. Here you can manage and monitor your operations.")
        )
