from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

mainDF = pd.read_csv("data\processedData.csv")
nDF=mainDF.loc[mainDF["Region"]=="north"].filter(["Date","Sales"])
sDF=mainDF.loc[mainDF["Region"]=="south"].filter(["Date","Sales"])
eDF=mainDF.loc[mainDF["Region"]=="east"].filter(["Date","Sales"])
wDF=mainDF.loc[mainDF["Region"]=="west"].filter(["Date","Sales"])


fig = go.Figure()
fig.add_trace(go.Scatter(x=nDF["Date"], y=nDF["Sales"], name="North", mode="lines"))
fig.add_trace(go.Scatter(x=sDF["Date"], y=sDF["Sales"], name="South", mode="lines"))
fig.add_trace(go.Scatter(x=eDF["Date"], y=eDF["Sales"], name="East", mode="lines"))
fig.add_trace(go.Scatter(x=wDF["Date"], y=wDF["Sales"], name="West", mode="lines"))

fig.update_layout(
    title="Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?",
     xaxis_title="Date", yaxis_title="Sales"
)

app.layout = html.Div(children=[
    html.H1(children='Soul Foods pink morsel sales data'),
    dcc.Graph(
        id='salesGraph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
