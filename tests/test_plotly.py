import plotly.express as px
import plotly.graph_objects as go

from nicegui import ui

from .screen import Screen


def test_plotly(screen: Screen):
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[1, 2, 3], name='Trace 1'))
    fig.update_layout(title='Test Figure')
    plot = ui.plotly(fig)

    ui.button('Add trace', on_click=lambda: (
        fig.add_trace(go.Scatter(x=[0, 1, 2], y=[2, 1, 0], name='Trace 2')),
        plot.update()
    ))

    screen.open('/')
    screen.should_contain('Test Figure')

    screen.click('Add trace')
    screen.should_contain('Trace 1')
    screen.should_contain('Trace 2')
