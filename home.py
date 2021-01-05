import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output


def home_updateLayout():
#Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div([
    html.H1('Home'),
    dcc.Dropdown(
        id='home-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='home-content')])
    rightSpace = html.Div("Rechter Space")

    #Including and external graph via iFrame
    bot_leftSpace = html.Iframe( src = "https://datahub.io/core/glacier-mass-balance/view/0", style ={'width' : "100%", 'overflow' : 'hidden', 'height' : 475, 'frameborder' :0,} )
    bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div("Rechter Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#59FF00'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-8',style ={'padding':20}),
            dbc.Col(
            [rightSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-2', style ={'padding':20}),],
            ),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-4'),
            dbc.Col(
            [bot_midSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-4', style ={'padding':20}),
            dbc.Col(
            [bot_rightSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-4',style ={'padding':20}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content
