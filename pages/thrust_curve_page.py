import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

import thrust_curve as tc
from app import app

pathname = '/thrust_curves'
page_name = 'Thrust curves'

# The option for the dropdown. List of pairs of motor names and file names.
motor_options = [{'label': m, 'value': f} for m, f in zip(tc.motor_names, tc.thrust_files)]


def get_layout(data):
    # Load the current motor from Store
    if data:
        cur_motor = data['motor_file']
    else:
        cur_motor = tc.thrust_files[0]

    return html.Div([
        html.H3(page_name),
        dcc.Dropdown(
            id='thrust-curve-dropdown',
            options=motor_options,
            value=cur_motor),
        dcc.Graph(id='thrust-curve'),
    ],
        style={
            'margin-left': '2rem',
            'margin-right': '2rem'
        }
    )


@app.callback(
    Output('thrust-curve', 'figure'),
    Output('thrust-curve-data', 'data'),
    Input('thrust-curve-dropdown', 'value'))
def plot_thrust_curve(file_name: str):
    if file_name is None:
        return go.Figure()
    thrust_curve = tc.ThrustCurve(file_name)
    return (tc.get_thrust_curve_plot(thrust_curve.thrust_curve, thrust_curve.avg_thrust, str(thrust_curve)),
            save_data(file_name))


def save_data(file_name: str):
    current_motor = ''
    for m in motor_options:
        if m['value'] == file_name:
            current_motor = m['label']
    data = {'motor_name': current_motor, 'motor_file': file_name}
    return data
