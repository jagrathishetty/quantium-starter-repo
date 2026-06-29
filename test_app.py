
from app import app

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#header")

def test_graph_exists(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-chart")

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-filter")
