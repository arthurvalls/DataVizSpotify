import dash
from dash import dcc
from dash import html
from matplotlib import artist
from matplotlib.pyplot import title
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
app.title = "Spotibar"

def createGraph(colorway,csv,y,cmin,cmax):
    df = pd.read_csv(csv)
    fig = px.bar(
        df, x="popularity", y=y,
        color="popularity", width=500, height=600, color_continuous_scale=colorway, title="User's recently most listened "+y+":",).update_layout(
        title={'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_family='Poppins',
    ).update_yaxes(
        automargin=True,
        ticksuffix=" ",
    ).update_coloraxes(cmin=cmin, cmax=cmax,
        showscale=True)

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'font_color': 'rgba(255,255,255, 0.9)',
        'font_family': 'Poppins',
        'hovermode': False,
        'yaxis': {'title': None, 'visible': True, 'showticklabels': True, 'fixedrange': True, 'tickfont': dict(size=15)},
        'xaxis': {'visible': False, 'showgrid': False, 'fixedrange': True},
        'bargap': 0.30,
    })

    fig.update_traces(marker_line_width=0)
    return fig

# df2 = pd.read_csv("topTracks.csv")
# fig2 = px.bar(
#     df2, x="popularity", y="name",
#     color="popularity", width=500, height=600, color_continuous_scale='peach', title="User's recently most listened tracks:",).update_layout(
#     title={'y': 0.9,
#            'x': 0.5,
#            'xanchor': 'center',
#            'yanchor': 'top'},
#     xaxis_title="Artist's name", yaxis_title="Popularity", title_font_family='Poppins', ).update_yaxes(automargin=True, ticksuffix=" ").update_coloraxes(showscale=False)

# fig2.update_layout({
#     'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
#     'font_color': 'rgba(255,255,255, 0.9)',
#     'font_family': 'Poppins',
#     'hovermode': False,
#     'yaxis': {'title': None, 'visible': True, 'showticklabels': True, 'side': 'left', 'mirror': "allticks", 'fixedrange': True, 'ticklabelposition': 'outside', 'tickfont': dict(size=15)},
#     'xaxis': {'visible': False, 'showgrid': False, 'fixedrange': True},
#     'bargap': 0.30,
# })

# fig2.update_traces(marker_line_width=0)

# df3 = pd.read_csv("topGenres.csv")
# fig3 = px.bar(
#     df3, x="popularity", y="genre",
#     color="popularity",
#     color_continuous_scale='tealgrn',
#     title="User's recently most listened genres:").update_layout(
#     title={'y': 0.9,
#            'x': 0.5,
#            'xanchor': 'center',
#            'yanchor': 'top'},
#     title_font_family='Poppins', width=500, height=600).update_coloraxes(showscale=False).update_yaxes(automargin=True, ticksuffix="  ")

# fig3.update_layout({
#     'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
#     'font_color': 'rgba(255,255,255, 0.9)',
#     'font_family': 'Poppins',
#     'hovermode': False,
#     'yaxis': {'title': None, 'visible': True, 'showticklabels': True, 'side': 'left', 'mirror': "allticks", 'fixedrange': True, 'tickfont': dict(size=15)},
#     'xaxis': {'visible': False, 'showgrid': False, 'fixedrange': True},
#     'bargap': 0.30,
# })

# fig3.update_traces(marker_line_width=0)



app.layout = html.Div([
    html.H1('Spotibar: Visualizing Spotify Data', className="header-title"),
    html.H4('This website takes data from spotify\'s own API and displays it in form of horizontal bar charts.',
            className="header-description"),

    html.Div([
        dcc.Graph(className='graph1', figure=createGraph('sunsetdark',"topArtists.csv",'artists',0,100)),
        dcc.Graph(className='graph2', figure=createGraph('peach',"topTracks.csv",'tracks',0,100)),
        dcc.Graph(className='graph3', figure=createGraph('tealgrn',"topGenres.csv",'genres',0,6)),
    ], className="flex-graph")
])


if __name__ == "__main__":
    app.run_server(debug=True)
