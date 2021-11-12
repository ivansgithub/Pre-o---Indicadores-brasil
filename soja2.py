import dash
from dash.dependencies import Input, Output,State
import dash_core_components as dcc
import dash_html_components as html
import requests
import json
import datetime, pytz
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd
import dash_table
import plotly.express as px
from flask import request
from fake_useragent import UserAgent
ua = UserAgent()

header = {'User-Agent':str(ua.chrome)}

url_soja='https://www.cepea.esalq.usp.br/br/indicador/soja.aspx'

tabla_soja=tabla_soja=pd.read_html(requests.get(url_soja,headers=header ).text)
tablo_soja=tabla_soja[0]

url_trigo='https://www.cepea.esalq.usp.br/br/indicador/trigo.aspx'
tabla_trigo=tabla_soja=pd.read_html(requests.get(url_trigo,headers=header ).text)
tablo_trigo=tabla_trigo[0]

url_milho='https://www.cepea.esalq.usp.br/br/indicador/milho.aspx'
tabla_milho=tabla_soja=pd.read_html(requests.get(url_milho,headers=header ).text)
tablo_milho=tabla_milho[0]

url_boi='https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx'
tabla_boi=tabla_soja=pd.read_html(requests.get(url_boi,headers=header ).text)
tablo_boi=tabla_boi[0]
url_bezerro='https://www.cepea.esalq.usp.br/br/indicador/bezerro.aspx'
tabla_bezerro=tabla_soja=pd.read_html(requests.get(url_bezerro,headers=header ).text)
tablo_bezerro=tabla_bezerro[0]

url_algodao='https://www.cepea.esalq.usp.br/br/indicador/algodao.aspx'
tabla_algodao=pd.tabla_soja=pd.read_html(requests.get(url_algodao,headers=header ).text)
tablo_rl_algodao=tabla_algodao[0]

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX,FONT_AWESOME])



temperatura =    ['Soja','Trigo','Milho','Boi','Bezerro','Algodao'] 

horas=['VAR./DIA','VAR./MES','VALOR US$','VALOR R$']
        
    
   

app.layout = html.Div([

    html.Div(className='mb-4'),

    html.Div(
    dbc.Row(dbc.Col(
    dcc.Dropdown(
        id='countries-dropdown', 
    
        options=[{'label': k, 'value': k} for k in horas],
        value='VALOR R$',
        clearable=False,style={    
                    'color': '#565555',
                    'borderStyle':'solid',
                    # 'width': '50%',                  
                    'font-size': '15px',
                    'textAlign': 'center'}),
    width=6, md={'size':4,'offset':4}),className='mb-4',),),
        
    

    html.Div(
    dbc.Row(dbc.Col(
    dcc.Dropdown(
        id='cities-dropdown',clearable=False, style={    
                    'color': '#565555',
                    'borderStyle':'solid',
                    # 'width': '50%',                  
                    'font-size': '15px',
                    'textAlign': 'center'}  ), 
    width=6,md={'size':4,'offset':4}),className='mb-4',),),

    

    dbc.Row(dbc.Col(html.Div(id='display-selected-values', className="text-center",style={    
                    'color': '#565555',  
                    'font-size': '30px',
                    'font': 'sans-serif',
                    'font-weight': 'bolder',
                    } ),width=12,md={'size':4,'offset':4},className='mb-4',),),

    dcc.Store(id='display-selected-values2'),

    dcc.Store(id='storage2'),

    dcc.Store(id='storage3'),
  
   dbc.Button(
            
            id="collapse-button",
            className="fas fa-chart-line",
            color="btn btn-outline-secondary",
            n_clicks=0,
            style={
            'margin': '0 auto',
            'display': 'block',
            'textAlign': 'center'},
            
        ),
        dbc.Col(dbc.Collapse(
            dcc.Graph(id='graph-with-slider'),
            id="collapse",
            is_open=False,
        ),width=6, md={'size':6,'offset':3},),

       # html.Iframe(src="YOUR PAGE",
        #        style={"height": "1067px", "width": "100%"}),
 
]
)


@app.callback(
    dash.dependencies.Output('cities-dropdown', 'options'),
    [dash.dependencies.Input('countries-dropdown', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in temperatura]

@app.callback(
    dash.dependencies.Output('cities-dropdown', 'value'),
    [dash.dependencies.Input('cities-dropdown', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    Output('storage2','data'),
    [dash.dependencies.Input('countries-dropdown', 'value'),
     dash.dependencies.Input('cities-dropdown', 'value')])
def set_display_children(selected_country, selected_city):

    print(selected_country)

            


    if selected_country == 'VAR./DIA' and selected_city=='Soja' :
        final=tabla_soja[0].iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Soja':
        final=tabla_soja[0].iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Soja':
        final=tabla_soja[0].iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Soja':
        final=tabla_soja[0].iloc[:, 2:6:2]


    elif selected_country == 'VAR./DIA' and selected_city=='Trigo' :
        final=tabla_trigo[0].iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Trigo':
        final=tabla_trigo[0].iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Trigo':
        final=tabla_trigo[0].iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Trigo':
        final=tabla_trigo[0].iloc[:, 2:6:2]

    elif selected_country == 'VAR./DIA' and selected_city=='Milho' :
        final=tabla_milho[0].iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Milho':
        final=tabla_milho[0].iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Milho':
        final=tabla_milho[0].iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Boi':
        final=tabla_milho[0].iloc[:, 2:6:2]

    elif selected_country == 'VAR./DIA' and selected_city=='Boi' :
        final=tabla_boi[0].iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Boi':
        final=tabla_boi[0].iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Boi':
        final=tabla_boi[0].iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Boi':
        final=tabla_boi[0].iloc[:, 2:6:2]

    elif selected_country == 'VAR./DIA' and selected_city=='Bezerro' :
        final=tabla_bezerro[0].iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Bezerro':
        final=tabla_bezerro[0].iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Bezerro':
        final=tabla_bezerro[0].iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Bezerro':
        final=tabla_bezerro[0].iloc[:, 2:6:2]

    elif selected_country == 'VAR./DIA' and selected_city=='Algodao' :
        final=tabla_algodao[0].iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Algodao':
        final=tabla_algodao[0].iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Algodao':
        final=tabla_algodao[0].iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Algodao':
        final=tabla_algodao[0].iloc[:, 2:6:2]

    final = final.rename(columns={'Unnamed: 0': ' '})
    final=final[0:5]

    return dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in final.columns],
    data=final.to_dict('records'),
    
    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in [' ', 'VAR./DIA']
    ],

    style_as_list_view=True,
),final.to_json(date_format='iso', orient='split')


@app.callback(
Output('graph-with-slider',component_property="figure"),
[dash.dependencies.Input('countries-dropdown', 'value'),
    dash.dependencies.Input('cities-dropdown', 'value'),
    Input('storage2','data')])

def tabla(selected_country,selected_city,df_del_json):
    grafico=''
    data=json.loads(df_del_json)
    columns = data['columns']
    data_dentro=data['data']
    df = pd.DataFrame(data_dentro, columns = columns)

    print(df.columns)
    if selected_country=='VALOR R$' and selected_city=='Soja':
        grafico={'Dia':df[' '],'Indicadores':df['Valor R$*']}
    elif selected_country=='VAR./DIA' and selected_city=='Soja':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Dia']}
    elif selected_country=='VAR./MES' and selected_city=='Soja':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Mês']}
    elif selected_country=='VALOR US$' and selected_city=='Soja':
        grafico={'Dia':df[' '],'Indicadores':df['Valor US$*']}
    elif selected_country=='Valor R$' and selected_city=='Trigo':
        grafico={'Dia':df[' '],'Indicadores':df['Valor R$*']}
    elif selected_country=='VAR./DIA' and selected_city=='Trigo':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Dia']}
    elif selected_country=='VAR./MES' and selected_city=='Trigo':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Mês']}
    elif selected_country=='VALOR US$' and selected_city=='Trigo':
        grafico={'Dia':df[' '],'Indicadores':df['Valor US$*']}
    elif selected_country=='Valor R$' and selected_city=='Milho':
        grafico={'Dia':df[' '],'Indicadores':df['Valor R$*']}
    elif selected_country=='VAR./DIA' and selected_city=='Milho':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Dia']}
    elif selected_country=='VAR./MES' and selected_city=='Milho':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Mês']}
    elif selected_country=='VALOR US$' and selected_city=='Milho':
        grafico={'Dia':df[' '],'Indicadores':df['Valor US$*']}
    elif selected_country=='Valor R$' and selected_city=='Boi':
        grafico={'Dia':df[' '],'Indicadores':df['Valor R$*']}
    elif selected_country=='VAR./DIA' and selected_city=='Boi':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Dia']}
    elif selected_country=='VAR./MES' and selected_city=='Boi':
        grafico={'Dia':df[' '],'Indicadore':df['Var./Mês']}
    elif selected_country=='VALOR US$' and selected_city=='Boi':
        grafico={'Dia':df[' '],'Indicadores':df['Valor US$*']}
    elif selected_country=='Valor R$' and selected_city=='Bezerro':
        grafico={'Dia':df[' '],'Indicadores':df['Valor R$*']}
    elif selected_country=='VAR./DIA' and selected_city=='Bezerro':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Dia']}
    elif selected_country=='VAR./MES' and selected_city=='Bezerro':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Mês']}
    elif selected_country=='VALOR US$' and selected_city=='Bezerro':
        grafico={'Dia':df[' '],'Indicadores':df['Valor US$*']}
    elif selected_country=='Valor R$' and selected_city=='Algodao':
        grafico={'Dia':df[' '],'Indicadores':df['Valor R$*']}
    elif selected_country=='VAR./DIA' and selected_city=='Algodao':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Dia']}
    elif selected_country=='VAR./MES' and selected_city=='Algodao':
        grafico={'Dia':df[' '],'Indicadores':df['Var./Mês']}
    elif selected_country=='VALOR US$' and selected_city=='Algodao':
        grafico={'Dia':df[' '],'Indicadores':df['Valor US$*']}
   

    dfg=pd.DataFrame(grafico)
    print(df.head(5))

    fig=px.bar(data_frame=dfg,x='Dia',y='Indicadores')
    return fig
    


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
    