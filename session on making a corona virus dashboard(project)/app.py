import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output,callback

pateints=pd.read_csv(r"IndividualDetails.csv")
total=pateints.shape[0]
active=pateints.query("current_status=='Hospitalized'").shape[0]
recovered=pateints.query("current_status=='Recovered'").shape[0]
death=pateints.query("current_status=='Deceased'").shape[0]

state=pateints['detected_state'].value_counts().reset_index()

hospitalized_bar=pateints.query("current_status=='Hospitalized'")['detected_state'].value_counts().reset_index()
recovered_bar=pateints.query("current_status=='Recovered'")['detected_state'].value_counts().reset_index()
deceased_bar=pateints.query("current_status=='Deceased'")['detected_state'].value_counts().reset_index()


opt=[
    {'label':'All','value':'All'},
    {'label':'Active','value':'Active'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
]

external_stylesheets=[{ 'href':"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
                       'rel':"stylesheet" ,
                       'integrity':"sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" ,
                       'crossorigin':"anonymous"}]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([html.Div([html.H1('Coronavirus Dashboard',style={'color':'white','text-align':'center'}),
                               html.Div([html.Div([html.Div([html.H2("Total Cases"),
                                                             html.H4(total)],className='card-body')]
                                                  ,className='card bg-danger')]
                                        ,className='col-md-3'),
                               html.Div([html.Div([html.Div([html.H2("Active"),
                                                             html.H4(active)],className='card-body')]
                                                  ,className='card bg-success')]
                                        ,className='col-md-3'),
                               html.Div([html.Div([html.Div([html.H2("Recovered"),
                                                             html.H4(recovered)],className='card-body')]
                                                  ,className='card bg-warning')]
                                        ,className='col-md-3'),
                               html.Div([html.Div([html.Div([html.H2("Deaths"),
                                                             html.H4(death)],className='card-body')]
                                                  ,className='card bg-info')]
                                        ,className='col-md-3')]
                               ,className='row'),


                     #2nd row          
                     html.Div(style={'margin-top': '20px'}),
                     html.Div([html.Div([html.Div([html.Div([dcc.Dropdown(id='picker',options=opt,value='All'),
                                                             dcc.Graph(id='Bar')]
                                                            ,className='card-body')]
                                                  ,className='card')]
                                        ,className='col-md-12')]
                              ,className='row'),    


                     #3rd row
                     html.Div(style={'margin-top': '20px'}),
                     html.Div([html.Div([html.Div([dcc.Graph(id='pie chart',
                                                             figure=px.pie(state,names='detected_state',values='count'))],
                                                  className='card-body')]
                         ,className='card')],className='row')

                     ]

                     ,className='container')

@app.callback(Output('Bar','figure'),Input('picker','value'))
def update_graph(type):

    if type=='All':
       return px.bar(state,x='detected_state',y='count')
    elif type=="Active":
        return px.bar(hospitalized_bar,x='detected_state',y='count',title="active cases")
    elif type=="Recovered":
        return px.bar(recovered_bar,x='detected_state',y='count',title="recovered cases")
    else:
        return px.bar(deceased_bar,x='detected_state',y='count',title='deceased cases')
    

if __name__=='__main__':
    app.run()