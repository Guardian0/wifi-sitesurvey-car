import dash
import dash_table
import pandas as pd

# making data frame from csv file
data = pd.read_csv("test.csv")

# sorting data frame by Team and then By names
data.sort_values(['ssid', 'ntp']).to_csv("output.csv", index=False)

df = pd.read_csv('output.csv')

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)