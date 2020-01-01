import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('maxoutput.csv')
x = (df['ntp']).tolist()
xmin = min(x)
x = (df['ntp'] - xmin).tolist()
#print(x)
y = (df['dBm']+100).tolist()
#print(y)
xssid = (df['ssid']).tolist()
ydBm = (df['dBm']).tolist()
for i in range(len(x)):
    xssid[i] = [xssid[i]] + [ydBm[i]]
#print(xssid)
(x0, y0) = df.shape
colors = ['rgb(50, 100, 255)',] * x0
#if y0 > 0 {}
#colors[9] = 'crimson'
xx=[]
yy=[]
app.layout = html.Div(children=[

    dcc.Graph(
        id='example-graph',
        figure=dict(data=[
            go.Bar(
                x=x, y=y,
                text=xssid,
                width=[0.8] * x0,
                name='A',
                marker_color=colors,
                textposition='auto',
            ),
            # go.Bar(x=[100], y=[90],text=y, name= 'H', marker_color='rgb(225, 0, 0)',width=[4],),
            # {'x': xx, 'y': yy, 'type': 'red', 'name': 'TRUE'},
        ], layout={
            # width=0.5,
            'title': 'dBm'
        })
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)