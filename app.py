from lib.lib import *
#Setup for Layout, seperate pages, etc.

from home import home_updateLayout
#from page1 import p1_updateLayout, renewable, energie, get_worldMaps_page_1_2, world_map_page1_1, world_map_page1_2, world_map_page1_3, get_worldMaps_page_1_1, temperature_page1
from page1 import p1_updateLayout, get_worldMaps_page_1_2, get_worldMaps_page_1_1
from page2 import p2_updateLayout
from page3 import p3_updateLayout
from page4 import p4_updateLayout
from page5 import p5_updateLayout
from page5 import get_pie
from data.Economic_Impact.graphs import get_dmgEU, get_dropGDP, get_dropGDP_W ,get_RiskindexWorldmap2, get_RiskindexWorldmap1
from info_box.infop4 import get_infoBox4
from info_box.infop3 import get_infoBox3
from info_box.infop5 import get_infoBox5 
from info_box.infop1 import get_infoBox1
from info_box.infop2 import get_infoBox2

from data.technology_patents.maps import get_world_map_pct_total, get_world_map_uspto_total, get_world_map_epo_total, get_world_map_pct_env,get_world_map_uspto_env, get_world_map_epo_env
from data.technology_patents.maps2 import get_world_map_epo_rel, get_world_map_uspto_rel, get_world_map_pct_rel
from data.technology_patents.graphs import get_world_graph_epo_env, get_world_graph_uspto_env, get_world_graph_pct_env, get_world_graph_epo_relative, get_world_graph_uspto_relative, get_world_graph_pct_relative, get_world_graph_epo_total, get_world_graph_uspto_total, get_world_graph_pct_total
from data.technology_patents.histograms import *
import time

#Redis Server for Worker Queue  ==> BG BOOStING
conn = Redis(
host='redis-14803.c239.us-east-1-2.ec2.cloud.redislabs.com',
port=14803,
password='Q0v0ws9bfxdBzOx6c21miQL7ur9zqEYP')
queue = Queue(connection=conn)



#Inititalise app    and it's style for the theme
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.FLATLY, '/assets/style.css'])
server = app.server


cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

'''
    queue.enqueue(get_worldMaps_page_1_1, job_id='WM1_1', result_ttl=86400)
    queue.enqueue(get_worldMaps_page_1_2, job_id='WM1_2', result_ttl=86400)
    queue.enqueue(get_graphs_patent_relative, id='G_rel', result_ttl=86400)
    queue.enqueue(get_graphs_patent_env, id='G_env', result_ttl=86400)
    queue.enqueue(get_graphs_patent_total, id='G_tot', result_ttl=86400)
    queue.enqueue(get_maps_patent, id='WM3_tot', result_ttl=86400)
    queue.enqueue(get_maps_patent_relative, id='WM3_rel', result_ttl=86400)
'''


# the styles for the main content position it to the right of the sidebar and
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
#Sidebar containing the menu
sidebar = html.Div(
    [   html.Div(html.H3("Climate Change"),className='titleSidebar'),
        html.Hr(),
        html.P(
            "Topics", className="lead"
        ),

        #Navbar containing the menu list
        dbc.Nav(
            [    dbc.Row([dbc.NavItem(dbc.Col([dbc.NavLink([html.I( className='fas fa-home', style={'padding-right':20}), html.A("Home")], href="/", active="exact",)],width=12),style={ 'width':'100%'}), ], className='sidebar-navigation'),
                dbc.Row([dbc.NavItem(dbc.Col([dbc.NavLink([html.I( className='fas fa-globe-europe', style={'padding-right':20}), html.A("Global Situation")], href="/page1", active="exact",)],width=12),style={ 'width':'100%'}), ], className='sidebar-navigation'),
                dbc.Row([dbc.NavItem(dbc.Col([dbc.NavLink([html.I( className='fas fa-university', style={'padding-right':20}), html.A("Governmental efforts")], href="/page2", active="exact",)],width=12),style={ 'width':'100%'}), ], className='sidebar-navigation'),
                dbc.Row([dbc.NavItem(dbc.Col([dbc.NavLink([html.I( className='fas fa-microscope', style={'padding-right':20}), html.A("Patents on technology")], href="/page3", active="exact",)],width=12),style={ 'width':'100%'}), ], className='sidebar-navigation'),
                dbc.Row([dbc.NavItem(dbc.Col([dbc.NavLink([html.I( className='fas fa-industry', style={'padding-right':20}), html.A("Economic Impact")], href="/page4", active="exact",)],width=12),style={ 'width':'100%'}), ], className='sidebar-navigation'),
                dbc.Row([dbc.NavItem(dbc.Col([dbc.NavLink([html.I( className='fa fa-group', style={'padding-right':20}), html.A("Population attitude")], href="/page5", active="exact",)],width=12),style={ 'width':'100%'}), ], className='sidebar-navigation'),
            ],
            vertical=True,
            pills=True,
                ),
        html.Hr(),
        html.Div(id='infoBox', className='infoFrame'),
        

        
    ],
    className='sidebar', 
)

#Footer
footer = dbc.Container(html.Div(dbc.Container("This app is an university project resulting from a Franco-German (University of Strasbourg, Karlsruher Institute for Technology) cross-border collaboration.", className='text-center p-3',),
    className='container-fluid',),  )


app.layout = html.Div([dcc.Location(id="url"), html.Div(id='page-content'), footer], style={ 'width' : '100%', 'height' : '100%',},) 

#Routing for the mutiple pages

@app.callback(Output("page-content", "children"), [Input("url", "pathname")]) 
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(dcc.Loading(home_updateLayout(),type="default",fullscreen=True,color='#45bf55'),className='container-fluid'),
    elif pathname == "/page1":
        return dbc.Col([sidebar,html.Div(p1_updateLayout(),className='rightFrame'),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page2":
        return dbc.Col([sidebar,html.Div(p2_updateLayout(),className='rightFrame'),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page3":
        return dbc.Col([sidebar,html.Div(p3_updateLayout(),className='rightFrame'),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page4":
        return dbc.Col([sidebar,html.Div(p4_updateLayout(),className='rightFrame'),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page5":
        return dbc.Col([sidebar,html.Div(p5_updateLayout(),className='rightFrame'),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ])


@app.callback(
    Output('infoBox', 'children'),
    [Input('url', 'pathname')])
@cache.memoize(timeout=0)
def callback_func(pathname):
    if(pathname == '/page4'):
        return get_infoBox4(pathname)
    elif(pathname == '/page3'):
        return get_infoBox3(pathname)
    elif(pathname == '/page5'):
        return get_infoBox5(pathname)  
    elif(pathname == '/page2'):
        return get_infoBox2(pathname)
    else:
        return get_infoBox1(pathname)




# Callback for different patent worldmaps 
@app.callback(
    Output('scatter_patents_env', 'figure'),
    Input('dropdown_po', 'value'),
    Input('dropdown_number', 'value'))  
def get_patent_map(selection_x,selection_y):
    if(selection_x == '0' and selection_y == '1'):
        fig = get_world_graph_epo_env()
        return fig

    elif(selection_x == '1' and selection_y == '1'):
        fig = get_world_graph_uspto_env()
        return fig
    
    elif(selection_x == '2' and selection_y == '1'):
        fig = get_world_graph_pct_env()
        return fig

    elif(selection_x == '0' and selection_y == '2'):
        fig = get_world_graph_epo_total()
        return fig

    elif(selection_x == '1' and selection_y == '2'):
        fig = get_world_graph_uspto_total()
        return fig

    elif(selection_x == '2' and selection_y == '2'):
        fig = get_world_graph_pct_total()
        return fig 

    elif(selection_x == '0' and selection_y == '0'):
        fig = get_world_graph_epo_relative()
        return fig

    elif(selection_x == '1' and selection_y == '0'):
        fig = get_world_graph_uspto_relative()
        return fig

    elif(selection_x == '2' and selection_y == '0'):
        fig = get_world_graph_pct_relative()
        return fig 

'''
def get_patent_map(selection_x,selection_y):
    if(selection_x == '0' and selection_y == '1'):
        job = Job.fetch('WM3_tot', connection=conn)
        fig = job.result[0]
        return fig

    elif(selection_x == '1' and selection_y == '1'):
        job = Job.fetch('WM3_tot', connection=conn)
        fig = job.result[1]
        return fig
    
    elif(selection_x == '2' and selection_y == '1'):
        job = Job.fetch('WM3_tot', connection=conn)
        fig = job.result[2]
        return fig

    elif(selection_x == '0' and selection_y == '2'):
        job = Job.fetch('WM3_tot', connection=conn)
        fig = job.result[3]
        return fig

    elif(selection_x == '1' and selection_y == '2'):
        job = Job.fetch('WM3_tot', connection=conn)
        fig = job.result[4]
        return fig

    elif(selection_x == '2' and selection_y == '2'):
        job = Job.fetch('WM3_tot', connection=conn)
        fig = job.result[5]
        return fig 

    elif(selection_x == '0' and selection_y == '0'):
        job = Job.fetch('WM3_rel', connection=conn)
        fig = job.result[0]
        return fig

    elif(selection_x == '1' and selection_y == '0'):
        job = Job.fetch('WM3_rel', connection=conn)
        fig = job.result[1]
        return fig

    elif(selection_x == '2' and selection_y == '0'):
        job = Job.fetch('WM3_rel', connection=conn)
        fig = job.result[2]
        return fig 

''' 
# Callback for different scatter plots on evrionmental related technology patents
@app.callback(
    Output('worldmap_patents', 'figure'),
    Input('dropdown_po', 'value'),
    Input('dropdown_number', 'value'))
def get_graphs(selection_x, selection_y):
    if(selection_x == '0' and selection_y == '0'):
        fig = get_world_map_epo_rel()
        return fig

    elif(selection_x == '1' and selection_y == '0'):
        fig = get_world_map_uspto_rel()
        return fig
        # fig = get_graphs_patent()[1]
    
    elif(selection_x == '2' and selection_y == '0'):
        fig = get_world_map_pct_rel()
        return fig

    elif(selection_x == '0' and selection_y == '1'):
        fig = get_world_map_epo_env()
        return fig

    elif(selection_x == '1' and selection_y == '1'):
        fig = get_world_map_uspto_env()
        return fig

    elif(selection_x == '2' and selection_y == '1'):
        fig = get_world_map_pct_env()
        return fig
    
    elif(selection_x == '0' and selection_y == '2'):
        fig = get_world_map_epo_total()
        return fig
    
    elif(selection_x == '1' and selection_y == '2'):
        fig = get_world_map_uspto_total()
        return fig
    
    else:
        fig = get_world_map_pct_total()
        return fig 
'''
def get_graphs(selection_x, selection_y):
    if(selection_x == '0' and selection_y == '0'):
        job = Job.fetch('G_rel', connection=conn)
        fig = job.result[0]
        return fig

    elif(selection_x == '1' and selection_y == '0'):
        job = Job.fetch('G_rel', connection=conn)
        fig = job.result[1]
        return fig
        # fig = get_graphs_patent()[1]
    
    elif(selection_x == '2' and selection_y == '0'):
        job = Job.fetch('G_rel', connection=conn)
        fig = job.result[2]
        return fig

    elif(selection_x == '0' and selection_y == '1'):
        job = Job.fetch('G_env', connection=conn)
        fig = job.result[0]
        return fig

    elif(selection_x == '1' and selection_y == '1'):
        job = Job.fetch('G_env', connection=conn)
        fig = job.result[1]
        return fig

    elif(selection_x == '2' and selection_y == '1'):
        job = Job.fetch('G_env', connection=conn)
        fig = job.result[2]
        return fig
    
    elif(selection_x == '0' and selection_y == '2'):
        job= queue.enqueue(get_graphs_patent_total)
        job = Job.fetch('G_tot', connection=conn)
        fig = job.result[0]
        return fig
    
    elif(selection_x == '1' and selection_y == '2'):
        job = Job.fetch('G_tot', connection=conn)
        fig = job.result[1]
        return fig
    
    else:
        job = Job.fetch('G_tot', connection=conn)
        fig = job.result[2]
        return fig 
'''
@app.callback(
    Output('histogram_total_env', 'figure'),
    Input('dropdown_po', 'value'))


def get_patent_hist(selection):
    fig = get_hist_patents()[int(selection)] 
    return fig

@app.callback(
    Output('p1WorldMap', 'figure'),
    Input('p1WorldMap_dm', 'value'))

def update_output_page1_1(selection):
    #jobP1_1= queue.enqueue(get_worldMaps_page_1_1, job_id='WM1_1', result_ttl=86400)
    fig = get_worldMaps_page_1_1()[int(selection)] 

    #fig = get_worldMaps_page_1_1()[int(selection)]
    return fig



@app.callback(
    Output('p1WorldMap2', 'figure'),
    Input('p1WorldMap_dm2', 'value'))

def update_output_page1_2(selection):
    #jobP1_2= queue.enqueue(get_worldMaps_page_1_2, job_id='WM1_2', result_ttl=86400)
    fig = get_worldMaps_page_1_2()[int(selection)]
    return fig

#Callback Page 4 ==> EU Graph (Left Bottom)
@app.callback(
    Output('eu_fig', 'figure'),
    Input('eu_fig_rb', 'value'))


def update_figure_euDMG(selection):
    fig = get_dmgEU()[int(selection)]
    return fig

#Callback Page 4 ==> GDP Graph (Mid Bottom)
@app.callback(
    Output('gdp_fig', 'figure'),
    Input('gdp_fig_rb', 'value')) 


def update_figure_gdp(selection):
    fig = get_dropGDP()[int(selection)]
    return fig
    #fig=get_dropGDP()[int(selection)]
    

#Callback Page 4 ==> WorldMap
@app.callback(
    Output('p4WorldMap', 'figure'),
    Input('p4WorldMap_dm', 'value'))
def update_output(selection):
    if selection == '0':
        fig = get_dropGDP_W()
        return fig

    elif selection == '1':
        fig = get_RiskindexWorldmap2()
        return fig

    elif selection == '2': 
        fig = get_RiskindexWorldmap1()
        return fig

    

#Call back for the pop up box
@app.callback(
    Output("patent_modal1", "is_open"),
    [Input("patent_open1", "n_clicks"), 
    Input("patent_close1", "n_clicks")],
    [State("patent_modal1", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("patent_modal2", "is_open"),
    [Input("patent_open2", "n_clicks"), 
    Input("patent_close2", "n_clicks")],
    [State("patent_modal2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("patent_modal3", "is_open"),
    [Input("patent_open3", "n_clicks"), 
    Input("patent_close3", "n_clicks")],
    [State("patent_modal3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("patent_modal4", "is_open"),
    [Input("patent_open4", "n_clicks"), 
    Input("patent_close4", "n_clicks")],
    [State("patent_modal4", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("patent_modal5", "is_open"),
    [Input("patent_open5", "n_clicks"), 
    Input("patent_close5", "n_clicks")],
    [State("patent_modal5", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    

@app.callback(
    Output('p5pie', 'figure'),
    Input('p5pie_dm', 'value'))


def update_outputPie(selection):
    fig = get_pie()[int(selection)] 
    return fig


if __name__ == "__main__":
    app.server.run(threaded=True, debug=False)
    
