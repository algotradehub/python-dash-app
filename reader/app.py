import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import redis
import json
import plotly.graph_objs as go

redis_client = redis.Redis(host='redis', port=6379, db=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Redis Random Numbers"),
    dcc.Graph(id='number-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])


@app.callback(Output('number-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph(n):

    numbers = redis_client.hget('random', 'nums')
    if numbers:
        numbers = json.loads(numbers)
    else:
        numbers = []

    figure = {
        'data': [
            go.Scatter(
                y=numbers,
                mode='lines+markers',
            )
        ],
        'layout': {
            'title': 'Random Numbers',
        }
    }
    return figure


if __name__ == '__main__':

    app.run_server(host='0.0.0.0', debug=True)