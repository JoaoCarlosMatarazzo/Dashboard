import dash
import dash_bootstrap_components as dbc
from dash import html
from components.layout import create_layout
from components.callbacks import register_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard de Monitoramento de Serviços"
app.layout = create_layout()
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)

 
