import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
from data.Economic_Impact.graphs import get_iGreenBondData, get_dropGDP, get_dropGDP_W
#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p4_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div(dcc.Graph(figure=get_dropGDP_W()))
    rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Iframe( src = "https://datahub.io/core/glacier-mass-balance/view/0", style ={'width' : "100%", 'overflow' : 'hidden', 'height' : 475, 'frameborder' :0,} )
    bot_midSpace = html.Div(dcc.Graph(figure=get_dropGDP()))
    bot_rightSpace = html.Div(dcc.Graph(figure=get_iGreenBondData()))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#FFFB00'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            midSpace,
            className='col-8',style ={'padding':20}),
            dbc.Col(
            [rightSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-2', style ={'padding':20}),],
            ),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-4'),
            dbc.Col(
            bot_midSpace, className='col-4', style ={'padding':20}),
            dbc.Col(
            bot_rightSpace, className='col-4',style ={'padding':20}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content