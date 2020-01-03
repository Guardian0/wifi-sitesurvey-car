import dash
#import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# making data frame from csv file
df = pd.read_csv('test.csv')

(x0, y0) = df.shape
def generate_table(dataframe, max_rows=x0):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='csv to read'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
