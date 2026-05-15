from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Hello Render")
])

if __name__ == "__main__":
    app.run(debug=True)
