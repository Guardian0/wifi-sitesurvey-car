import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# making data frame from csv file
df = pd.read_csv('test.csv')
# sorting data frame by Team and then By names
df.sort_values(['ssid', 'ntp', 'dBm'], axis=0, ascending=[True, True, True], inplace=True)
df.to_csv('min.csv', index=False)
df1 = pd.read_csv('min.csv')
df2 = df1.groupby(['ssid']).min()
df2.to_csv('mingroup.csv', index=False)

df4 = pd.read_csv('mingroup.csv')
(x0, y0) = df4.shape
df5 = pd.read_csv('min.csv')
df6 = df5.groupby(['ssid']).min()
col_name=df4.columns.tolist()
col_name.insert(0, 'ssid')
df4 = df4.reindex(columns=col_name)
df4['ssid']= df6.index.values.tolist()
df4.to_csv('minoutput.csv', index=False)
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
    generate_table(df4)
])

if __name__ == '__main__':
    app.run_server(debug=True)