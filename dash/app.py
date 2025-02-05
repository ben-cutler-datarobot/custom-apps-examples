import os
from dash import Dash, html

base_path = f'/custom_applications/{os.getenv("APPLICATION_ID")}/'

# Initialize the Dash app
app = Dash(__name__,
    requests_pathname_prefix=f"{base_path}",
)


app.layout = [html.Div(children='Hello World')]

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0', port=8080)
