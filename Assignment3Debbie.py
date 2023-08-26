from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Read your CSV data
data_url = "https://raw.githubusercontent.com/DeborahMMU2023/DataVisualization/spotifydata/data.csv"
dataSpotify = pd.read_csv(data_url)

# Define a function to create the boxplot using Plotly Express
def create_boxplot(data):
    fig = px.box(data, y='acousticness')
    fig.update_layout(title='Acousticness')
    
    return fig


# Define a function to create the polar line chart using Plotly Express
def create_polar_line_chart(data):
    popular_songs = data['song_title'].value_counts().sort_values(ascending=False)[:10]
    popular_songs = pd.DataFrame(popular_songs).reset_index()
    popular_songs = popular_songs.rename(columns={"index": "Songs", "song_title": "Count"})
    
    fig = px.line_polar(data_frame=popular_songs, r='Count', theta='Songs', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(title={'text': "Top 10 Songs from Mr. X Spotify Data"})
    
    return fig

def create_pie_chart(data):
    popular_artists = data['artist'].value_counts().sort_values(ascending=False)[:10]
    popular_artists = pd.DataFrame(popular_artists).reset_index()
    popular_artists = popular_artists.rename(columns={"index": "Artist", "artist": "Count"})
    
    fig = px.pie(popular_artists, values="Count", names="Artist", 
                 title="Top 10 Artists from Mr. X Spotify Data")
    
    return fig 

# Call the create_boxplot function to generate the Plotly Express boxplot
boxplot_figure = create_boxplot(dataSpotify)
pie_chart_figure = create_pie_chart(dataSpotify)
polar_line_chart_figure = create_polar_line_chart(dataSpotify)

app.layout = html.Div(
    [
        html.H1("Data Visualization"),
        html.H2("Dashboard showing graphs"),
        dcc.Graph(figure=boxplot_figure),
        dcc.Graph(figure=polar_line_chart_figure),
        dcc.Graph(figure=pie_chart_figure)

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8052)