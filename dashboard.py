import pandas as pd
import plotly.graph_objs as go
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


data = pd.read_csv("gapminder.csv")
bangladesh_data = data[data['country'] == 'Bangladesh']


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                title="Bangladesh Dashboard",
                assets_folder="assets")

app._favicon = "flag.png"

app.layout = dbc.Container(
    fluid=True,
    children=[
        
        # First Header
        dbc.Row(
            dbc.Col(
                html.H1(
                    "Gapminder Data Dashboard",
                    style={
                        'color': 'white',
                        'textAlign': 'center',
                        'padding': '20px',
                        'background': 'linear-gradient(to right, #4b6cb7, #182848)'
                    }
                ),
                width=12
            ),
            style={'margin-bottom': '20px'}
        ),
        
        # First Row
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id='scatter-plot',
                        figure={
                            'data': [
                                go.Scatter(
                                    x=data['pop'],
                                    y=data['gdpPercap'],
                                    mode='markers',
                                    marker=dict(
                                        size=10,
                                        color=data['lifeExp'],
                                        colorscale='Viridis',
                                        showscale=True,
                                        opacity=0.7,
                                        line=dict(width=0.5, color='white')
                                    ),
                                    text=data['country'],
                                    hoverinfo='text+x+y'
                                )
                            ],
                            'layout': go.Layout(
                                title='Population vs GDP per Capita (All Countries)',
                                xaxis={'title': 'Population', 'type': 'log'},
                                yaxis={'title': 'GDP per Capita (USD)', 'type': 'log'},
                                plot_bgcolor='rgba(240,240,240,0.8)',
                                paper_bgcolor='rgba(240,240,240,0.5)',
                                hovermode='closest'
                            )
                        }
                    ),
                    md=6
                ),
                
                dbc.Col(
                    dcc.Graph(
                        id='box-plot',
                        figure={
                            'data': [
                                go.Box(
                                    x=data['gdpPercap'],
                                    name='GDP Distribution',
                                    marker_color='#4b6cb7',
                                    boxmean=True
                                )
                            ],
                            'layout': go.Layout(
                                title='GDP per Capita Distribution (All Countries)',
                                xaxis={'title': 'GDP per Capita (USD)'},
                                plot_bgcolor='rgba(240,240,240,0.8)',
                                paper_bgcolor='rgba(240,240,240,0.5)'
                            )
                        }
                    ),
                    md=6
                )
            ],
            style={'margin-bottom': '20px'}
        ),
        
        # Second Header
        dbc.Row(
            dbc.Col(
                html.H2(
                    "Bangladesh Analysis",
                    style={
                        'color': '#2c3e50',
                        'textAlign': 'center',
                        'padding': '15px',
                        'background': 'linear-gradient(to right, #f5f7fa, #c3cfe2)'
                    }
                ),
                width=12
            )
        ),
        
        # Third Row
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id='bangladesh-line',
                        figure={
                            'data': [
                                go.Scatter(
                                    x=bangladesh_data['year'],
                                    y=bangladesh_data['gdpPercap'],
                                    mode='lines+markers',
                                    marker=dict(
                                        size=10,
                                        color='#e74c3c'
                                    ),
                                    line=dict(width=3),
                                    name='GDP per Capita'
                                )
                            ],
                            'layout': go.Layout(
                                title='Bangladesh: GDP Growth Over Time',
                                xaxis={'title': 'Year'},
                                yaxis={'title': 'GDP per Capita (USD)'},
                                plot_bgcolor='rgba(240,240,240,0.8)',
                                paper_bgcolor='rgba(240,240,240,0.5)',
                                hovermode='closest'
                            )
                        }
                    ),
                    md=6
                ),
                
                dbc.Col(
                    dcc.Graph(
                        id='bangladesh-line1',
                        figure={
                            'data': [
                                go.Scatter(
                                    x=bangladesh_data['year'],
                                    y=bangladesh_data['lifeExp'],
                                    mode='lines+markers',
                                    marker=dict(
                                        size=10,
                                        color='#e74c3c',
                                        line=dict(width=1, color='white')
                                    ),
                                    line=dict(width=3, color='#e74c3c'),
                                    name='Life Expectancy'
                                )
                            ],
                            'layout': go.Layout(
                                title='Bangladesh: Life Expectancy Over Time',
                                xaxis={'title': 'Year'},
                                yaxis={'title': 'Life Expectancy (years)'},
                                plot_bgcolor='rgba(240,240,240,0.8)',
                                paper_bgcolor='rgba(240,240,240,0.5)',
                                hovermode='closest'
                            )
                        }
                    ),
                    md=6
                )            
            ],
            style={'margin-bottom': '20px'}
        ),

        # Forth Row
        dbc.Row(
            [
                dbc.Col(
                        dcc.Graph(
                            id='bangladesh-population',
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=bangladesh_data['year'],
                                        y=bangladesh_data['pop'],
                                        mode='lines+markers',
                                        marker=dict(
                                            size=10,
                                            color='#3498db'
                                        ),
                                        line=dict(width=3),
                                        name='Population'
                                    )
                                ],
                                'layout': go.Layout(
                                    title='Bangladesh: Population Growth Over Time',
                                    xaxis={'title': 'Year'},
                                    yaxis={'title': 'Population'},
                                    plot_bgcolor='rgba(240,240,240,0.8)',
                                    paper_bgcolor='rgba(240,240,240,0.5)',
                                    hovermode='closest'
                                )
                            }
                        ),
                        md=6
                    ),
                
                dbc.Col(
                    dcc.Graph(
                        id='gdp-lifeexp',
                        figure={
                            'data': [
                                go.Scatter(
                                    x=bangladesh_data['gdpPercap'],
                                    y=bangladesh_data['lifeExp'],
                                    mode='markers+lines',
                                    marker=dict(
                                        size=12,
                                        color=bangladesh_data['year'],
                                        colorscale='Viridis',
                                        showscale=True,
                                        line=dict(width=0.5, color='white')
                                    ),
                                    line=dict(width=2, color='#7f8c8d'),
                                    text=bangladesh_data['year'],
                                    hoverinfo='text+x+y',
                                    name='Bangladesh'
                                )
                            ],
                            'layout': go.Layout(
                                title='Bangladesh: GDP vs Life Expectancy (1952-2007)',
                                xaxis={'title': 'GDP per Capita (USD)', 'type': 'log'},
                                yaxis={'title': 'Life Expectancy (years)'},
                                plot_bgcolor='rgba(240,240,240,0.8)',
                                paper_bgcolor='rgba(240,240,240,0.5)',
                                hovermode='closest',
                                coloraxis=dict(colorbar={'title': 'Year'})
                            )
                        }
                    ),
                    md=6
                )
            
            ],
            style={'margin-bottom': '20px'}
        )
    
    
    ],
    style={
        'padding': '20px',
        'background-color': '#f8f9fa'
    }
)



if __name__ == '__main__':
    app.run(debug=True)