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

nuevos_numeros=[]
for i in tablo_soja['Valor R$*']:
    num = str(i)
    num_str = (str(num))
    a = int(len(num_str) / 3)
        
    nuevos_numeros.append('{}'.format(num_str[:3*a]+','+num_str[3*a:]))
tablo_soja['Valor R$*']=nuevos_numeros
tablo_soja['Unnamed: 0']=tablo_soja['Unnamed: 0'].str.replace('/2021','/21')


nuevos_numeros2=[]
for i in tablo_soja['Valor US$*']:
    

    num = str(i)
    
    num_str = (str(num))
    a = int(len(num_str) / 2)
    nuevos_numeros2.append('{}'.format(num_str[:2]+','+num_str[2:]))
tablo_soja['Valor US$*']=nuevos_numeros2




url_trigo='https://www.cepea.esalq.usp.br/br/indicador/trigo.aspx'
tabla_trigo=tabla_soja=pd.read_html(requests.get(url_trigo,headers=header ).text)
tablo_trigo=tabla_trigo[0]

nuevos_numeros1=[]
for i in tablo_trigo['Valor R$/t*']:
    num = str(i)
    num_str = (str(num))
    
        
    nuevos_numeros1.append('{}'.format(num_str[:5]+','+num_str[5:8]))
tablo_trigo['Valor R$/t*']=nuevos_numeros1

nuevos_numeros21=[]
for i in tablo_trigo['Valor US$/t*']:
    

    num = str(i)
    
    num_str = (str(num))
    a = int(len(num_str) / 2)
    nuevos_numeros21.append('{}'.format(num_str[:2]+','+num_str[2:]))      
tablo_trigo['Valor US$/t*']=nuevos_numeros21
tablo_trigo['Unnamed: 0']=tablo_trigo['Unnamed: 0'].str.replace('/2021','/21')


url_milho='https://www.cepea.esalq.usp.br/br/indicador/milho.aspx'
tabla_milho=tabla_soja=pd.read_html(requests.get(url_milho,headers=header ).text)
tablo_milho=tabla_milho[0]

nuevos_numeros2=[]
for i in tablo_milho['Valor R$*']:
    num = str(i)
    num_str = (str(num))
    a = int(len(num_str) / 3)
        
    nuevos_numeros2.append('{}'.format(num_str[:3*a]+','+num_str[3*a:]))
tablo_milho['Valor R$*']=nuevos_numeros2
nuevos_numeros22=[]
for i in tablo_milho['Valor US$*']:
    

    num = str(i)
    
    num_str = (str(num))
    a = int(len(num_str) / 2)
    nuevos_numeros22.append('{}'.format(num_str[:2]+','+num_str[2:]))
    
    
tablo_milho['Valor US$*']=nuevos_numeros22
tablo_milho['Unnamed: 0']=tablo_milho['Unnamed: 0'].str.replace('/2021','/21')

url_boi='https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx'
tabla_boi=tabla_soja=pd.read_html(requests.get(url_boi,headers=header ).text)
tablo_boi=tabla_boi[0]
nuevos_numeros3=[]
for i in tablo_boi['Valor R$*']:
    num = str(i)
    num_str = (str(num))
    a = int(len(num_str) / 3)
        
    nuevos_numeros3.append('{}'.format(num_str[:3*a]+','+num_str[3*a:]))
tablo_boi['Valor R$*']=nuevos_numeros3

nuevos_numeros23=[]
for i in tablo_boi['Valor US$*']:
    

    num = str(i)
    
    num_str = (str(num))
    a = int(len(num_str) / 2)
    nuevos_numeros23.append('{}'.format(num_str[:2]+','+num_str[2:]))
    
    
    
tablo_boi['Valor US$*']=nuevos_numeros23
tablo_boi['Unnamed: 0']=tablo_boi['Unnamed: 0'].str.replace('/2021','/21')
url_bezerro='https://www.cepea.esalq.usp.br/br/indicador/bezerro.aspx'
tabla_bezerro=tabla_soja=pd.read_html(requests.get(url_bezerro,headers=header ).text)
tablo_bezerro=tabla_bezerro[0]

nuevos_numeros4=[]
for i in tablo_bezerro['Valor R$*']:
    num = str(i)
    num_str = (str(num))
    if len(num_str) > 5:
        nuevos_numeros4.append('{}'.format(num_str[:5]+','+num_str[5:9]))
    else:
        nuevos_numeros4.append(num_str)
    
        
tablo_bezerro['Valor R$*']=nuevos_numeros4
nuevos_numeros24=[]
for i in tablo_bezerro['Valor US$*']:
    

    num = str(i)
    
    num_str = (str(num))
    a = int(len(num_str) / 2)
    
    nuevos_numeros24.append('{}'.format(num_str[:2]+','+num_str[2:]))
    
   
    
tablo_bezerro['Valor US$*']=nuevos_numeros24
tablo_bezerro['Unnamed: 0']=tablo_bezerro['Unnamed: 0'].str.replace('/2021','/21')
url_algodao='https://www.cepea.esalq.usp.br/br/indicador/algodao.aspx'
tabla_algodao=pd.tabla_soja=pd.read_html(requests.get(url_algodao,headers=header ).text)
tablo_algodao=tabla_algodao[0]

nuevos_numeros5=[]
for i in tablo_algodao['Centavos R$/lp']:
    num = str(i)
    num_str = (str(num))
    a = int(len(num_str) / 2)
    nuevos_numeros5.append('{}'.format(num_str[:3]+','+num_str[3:]))
    
        
tablo_algodao['Centavos R$/lp']=nuevos_numeros5
nuevos_numeros25=[]
for i in tablo_algodao['Prazo pgto. (dias)']:
    

    num = str(i)
    
    num_str = (str(num))
    
    nuevos_numeros25.append('{}'.format(num_str[:1]+','+num_str[1:8]))
    
 
tablo_algodao['Prazo pgto. (dias)']=nuevos_numeros25
tablo_algodao['Unnamed: 0']=tablo_algodao['Unnamed: 0'].str.replace('/2021','/21')

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX,FONT_AWESOME],meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],)
server=app.server



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
    width=6, md={'size':4,'offset':4},xs={'size':6,'offset':3}),className='mb-4',),),
        
    

    html.Div(
    dbc.Row(dbc.Col(
    dcc.Dropdown(
        id='cities-dropdown',clearable=False, style={    
                    'color': '#565555',
                    'borderStyle':'solid',
                    # 'width': '50%',                  
                    'font-size': '15px',
                    'textAlign': 'center'}  ), 
    width=6,md={'size':4,'offset':4},xs={'size':6,'offset':3}),className='mb-4',),),

    

    dbc.Row(dbc.Col(html.Div(id='display-selected-values', className="text-center",style={    
                    'color': '#565555',  
                    #'font-size': '30px',
                    'font': 'sans-serif',
                    'font-weight': 'bolder',
                    } ),width=12,md={'size':4,'offset':4,'font-size':'30px'},xs={'size':4,'offset':3,'font-size':'15px'},className='mb-4',),),

    dcc.Store(id='display-selected-values2'),

    dcc.Store(id='storage2'),

    dcc.Store(id='storage3'),
  
          
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
    final=''

          


    if selected_country == 'VAR./DIA' and selected_city=='Soja' :
        final=tablo_soja.iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Soja':
        final=tablo_soja.iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Soja':
        final=tablo_soja.iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Soja':
        final=tablo_soja.iloc[:, 0:7:4]


    elif selected_country == 'VAR./DIA' and selected_city=='Trigo' :
        final=tablo_trigo.iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Trigo':
        final=tablo_trigo.iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Trigo':
        final=tablo_trigo.iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Trigo':
        final=tablo_trigo.iloc[:, 0:7:4]

    elif selected_country == 'VAR./DIA' and selected_city=='Milho' :
        final=tablo_milho.iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Milho':
        final=tablo_milho.iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Milho':
        final=tablo_milho.iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Boi':
        final=tablo_milho.iloc[:, 0:7:4]

    elif selected_country == 'VAR./DIA' and selected_city=='Boi' :
        final=tablo_boi.iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Boi':
        final=tablo_boi.iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Boi':
        final=tablo_boi.iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Boi':
        final=tablo_boi.iloc[:, 0:7:4]

    elif selected_country == 'VAR./DIA' and selected_city=='Bezerro' :
        final=tablo_bezerro.iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Bezerro':
        final=tablo_bezerro.iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Bezerro':
        final=tablo_bezerro.iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Bezerro':
        final=tablo_bezerro.iloc[:, 0:7:4]

    elif selected_country == 'VAR./DIA' and selected_city=='Algodao' :
        final=tablo_algodao.iloc[:, :3:2]
    elif selected_country=='VALOR R$' and selected_city=='Algodao':
        final=tablo_algodao.iloc[:, :2:]
    elif selected_country=='VAR./MES' and selected_city=='Algodao':
        final=tablo_algodao.iloc[:, 0::3] 
    elif selected_country=='VALOR US$' and selected_city=='Algodao':
        final=tablo_algodao.iloc[:, 0:7:4]

    print(final)
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


if __name__ == '__main__':
    app.run_server(debug=True)
    
    
