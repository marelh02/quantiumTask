import dash
from dash import html


def test_bsly001_falsy_child(dash_duo):
    
    app = dash.Dash(__name__)
    app.layout = html.Div(id="nully-wrapper", children=0)
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)
    assert dash_duo.find_element("h1")
    assert dash_duo.find_element("div#radio")
    assert dash_duo.find_element("div#salesGraph")