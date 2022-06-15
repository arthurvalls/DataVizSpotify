import dash
from dash import dcc
from dash import html 
from dash import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Poppins:wght@300;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Spotbar"

df = pd.read_csv("topArtists.csv")
fig = px.bar(
df, x="name", y="popularity", 
color="popularity", color_continuous_scale= 'sunsetdark').update_layout(
    xaxis_title="Artist's name", yaxis_title="Popularity").update_coloraxes(showscale=False)

fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font_color': 'rgba(255,255,255, 0.9)',
'hovermode': False,
'xaxis': {'title': None, 'visible': True, 'showticklabels': True},'yaxis':{'visible': False, 'showgrid': False},
})


df2 = pd.read_csv("topGenres.csv")
fig2 = px.bar(
df2, x="genre", y="popularity", 
color="popularity", color_continuous_scale= 'sunsetdark').update_layout(
    xaxis_title="Genre", yaxis_title="Popularity").update_coloraxes(showscale=False)

fig2.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font_color': 'rgba(255,255,255, 0.9)',
'hovermode': False,
'xaxis': {'title': None,'visible': True, 'showticklabels': True}, 'yaxis':{'visible': False, 'showgrid': False}
})


app.layout = html.Div([
    html.H4('Visualizing Spotify Data',className="H4"),
    html.P("User's recently most listened artists:", className= "P"),
    dcc.Graph(figure=fig,),
    html.P("User's recently most listened genres:", className= "P"),
    dcc.Graph(figure=fig2,),

])


if __name__ == "__main__":
    app.run_server(debug=True)