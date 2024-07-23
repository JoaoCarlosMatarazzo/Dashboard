import html
from dash import dcc, Output, Input
import plotly.express as px
import pandas as pd

def register_callbacks(app):
    @app.callback(
        [Output('service-status-chart', 'figure'),
         Output('performance-metrics-chart', 'figure'),
         Output('alerts', 'children')],
        [Input('interval-component', 'n_intervals')]
    )
    def update_dashboard(n):
        # Função para obter dados (exemplo fictício)
        data = pd.read_csv('data/sample_data.csv')

        # Gráfico de Status dos Serviços
        service_status_fig = px.bar(data, x='Service', y='Status')

        # Gráfico de Métricas de Desempenho
        performance_metrics_fig = px.line(data, x='Time', y='Performance')

        # Alertas (exemplo fictício)
        alerts = []
        if data['Status'].min() < 50:
            alerts.append(html.Div("Alerta: Um dos serviços está com desempenho crítico!", className="alert alert-danger"))

        return service_status_fig, performance_metrics_fig, alerts
 
