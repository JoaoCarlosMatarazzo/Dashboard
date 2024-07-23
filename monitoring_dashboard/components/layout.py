from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Dashboard de Monitoramento de Serviços"), className="text-center")
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='service-status-chart'), width=6),
            dbc.Col(dcc.Graph(id='performance-metrics-chart'), width=6)
        ]),
        dbc.Row([
            dbc.Col(html.Div(id='alerts'), width=12)
        ]),
        dcc.Interval(
            id='interval-component',
            interval=60*1000,  # Atualização a cada minuto
            n_intervals=0
        )
    ])

