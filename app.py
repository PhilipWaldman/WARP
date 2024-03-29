import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                title='WARP',
                update_title='Loading...',
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.FLATLY])
server = app.server
