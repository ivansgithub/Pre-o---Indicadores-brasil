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
url_bezerro='https://www.cepea.esalq.usp.br/br/indicador/bezerro.aspx'
tabla_bezerro=tabla_soja=pd.read_html(requests.get(url_bezerro,headers=header ).text)
tablo_bezerro=tabla_bezerro[0]

nuevos_numeros4=[]
for i in tablo_bezerro['Valor R$*']:
    num = str(i)
    num_str = (str(num))
    
        
    nuevos_numeros4.append('{}'.format(num_str[:5]+','+num_str[5:8]))
tablo_bezerro['Valor R$*']=nuevos_numeros4
nuevos_numeros24=[]
for i in tablo_bezerro['Valor US$*']:
    

    num = str(i)
    
    num_str = (str(num))
    a = int(len(num_str) / 2)
    nuevos_numeros24.append('{}'.format(num_str[:2]+','+num_str[2:]))
    
   
    
tablo_bezerro['Valor US$*']=nuevos_numeros24
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

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX,FONT_AWESOME])
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


@app.callback(
Output('graph-with-slider',component_property="figure"),
[dash.dependencies.Input('countries-dropdown', 'value'),
    dash.dependencies.Input('cities-dropdown', 'value'),
    Input('storage2','data')])

def tabla(selected_country,selected_city,df_del_json):
    grafico=''

    fig=''
   

        
    data=json.loads(df_del_json)
    columns = data['columns']
    data_dentro=data['data']
    df = pd.DataFrame(data_dentro, columns = columns)

    print(df)
    print(selected_country)
    print(selected_city)
    if selected_country=='VALOR R$' and selected_city=='Soja':
        df = df.set_index(' ')
        df['Valor R$*']=df['Valor R$*'].str.replace(',','.').astype(float)
        fig = px.bar(x=df.index, y=df['Valor R$*'])
        min=df['Valor R$*'].min()-1
        max=df['Valor R$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
        

       
    elif selected_country=='VAR./DIA' and selected_city=='Soja':
        df = df.set_index(' ')
        df['Var./Dia']=df['Var./Dia'].str.replace(',','.')
        df['Var./Dia']=df['Var./Dia'].str.replace('%','')
        df['Var./Dia']=df['Var./Dia'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Dia'])
        min=df['Var./Dia'].min()-1
        max=df['Var./Dia'].max()+1
        fig.update(layout_yaxis_range =[min,max])
        


    elif selected_country=='VAR./MES' and selected_city=='Soja':
        df = df.set_index(' ')
        df['Var./Mês']=df['Var./Mês'].str.replace(',','.')
        df['Var./Mês']=df['Var./Mês'].str.replace('%','')
        df['Var./Mês']=df['Var./Mês'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Mês'])
        min=df['Var./Mês'].min()-1
        max=df['Var./Mês'].max()+1
        fig.update(layout_yaxis_range =[min,max])

    elif selected_country=='VALOR US$' and selected_city=='Soja':
        df = df.set_index(' ')
        df['Valor US$*']=df['Valor US$*'].str.replace(',','.').astype(float)
        fig = px.bar(x=df.index, y=df['Valor US$*'])
        min=df['Valor US$*'].min()-1
        max=df['Valor US$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
        


    elif selected_country=='VALOR R$' and selected_city=='Trigo':
        
        df = df.set_index(' ')
        df['Valor R$/t*']=df['Valor R$/t*'].str.replace('.','')
        df['Valor R$/t*']=df['Valor R$/t*'].str.replace(',','.').astype(float)
      
        fig = px.bar(x=df.index, y=df['Valor R$/t*'])
        min=df['Valor R$/t*'].min()-1
        max=df['Valor R$/t*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
        


    elif selected_country=='VAR./DIA' and selected_city=='Trigo':
        df = df.set_index(' ')
        df['Var./Dia']=df['Var./Dia'].str.replace(',','.')
        df['Var./Dia']=df['Var./Dia'].str.replace('%','')
        df['Var./Dia']=df['Var./Dia'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Dia'])
        min=df['Var./Dia'].min()-1
        max=df['Var./Dia'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./MES' and selected_city=='Trigo':
        df = df.set_index(' ')
        df['Var./Mês']=df['Var./Mês'].str.replace(',','.')
        df['Var./Mês']=df['Var./Mês'].str.replace('%','')
        df['Var./Mês']=df['Var./Mês'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Mês'])
        min=df['Var./Mês'].min()-1
        max=df['Var./Mês'].max()+1
        fig.update(layout_yaxis_range =[min,max])
        

    elif selected_country=='VALOR US$' and selected_city=='Trigo':
        df = df.set_index(' ')
        df['Valor US$/t*']=df['Valor US$/t*'].str.replace('.','')
        df['Valor US$/t*']=df['Valor US$/t*'].str.replace(',','.').astype(float)
        fig = px.bar(x=df.index, y=df['Valor US$/t*'])
        min=df['Valor US$/t*'].min()-1
        max=df['Valor US$/t*'].max()+1
        fig.update(layout_yaxis_range =[min,max])

        
    elif selected_country=='VALOR R$' and selected_city=='Milho':
        df = df.set_index(' ')
        df['Valor R$*']=df['Valor R$*'].str.replace('.','')
        df['Valor R$*']=df['Valor R$*'].str.replace(',','.').astype(float)
      
        fig = px.bar(x=df.index, y=df['Valor R$*'])
        min=df['Valor R$*'].min()-1
        max=df['Valor R$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./DIA' and selected_city=='Milho':
        df = df.set_index(' ')
        df['Var./Dia']=df['Var./Dia'].str.replace(',','.')
        df['Var./Dia']=df['Var./Dia'].str.replace('%','')
        df['Var./Dia']=df['Var./Dia'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Dia'])
        min=df['Var./Dia'].min()-1
        max=df['Var./Dia'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./MES' and selected_city=='Milho':
        df = df.set_index(' ')
        df['Var./Mês']=df['Var./Mês'].str.replace(',','.')
        df['Var./Mês']=df['Var./Mês'].str.replace('%','')
        df['Var./Mês']=df['Var./Mês'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Mês'])
        min=df['Var./Mês'].min()-1
        max=df['Var./Mês'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VALOR US$' and selected_city=='Milho':
        df = df.set_index(' ')

        df['Valor US$*']=df['Valor US$*'].str.replace(',','.').astype(float)
        fig = px.bar(x=df.index, y=df['Valor US$*'])
        min=df['Valor US$*'].min()-1
        max=df['Valor US$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])

    elif selected_country=='VALOR R$' and selected_city=='Boi':
        df = df.set_index(' ')
        df['Valor R$*']=df['Valor R$*'].str.replace('.','')
        df['Valor R$*']=df['Valor R$*'].str.replace(',','.').astype(float)
      
        fig = px.bar(x=df.index, y=df['Valor R$*'])
        min=df['Valor R$*'].min()-1
        max=df['Valor R$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./DIA' and selected_city=='Boi':
        df = df.set_index(' ')
        df['Var./Dia']=df['Var./Dia'].str.replace(',','.')
        df['Var./Dia']=df['Var./Dia'].str.replace('%','')
        df['Var./Dia']=df['Var./Dia'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Dia'])
        min=df['Var./Dia'].min()-1
        max=df['Var./Dia'].max()+1
        fig.update(layout_yaxis_range =[min,max])

    elif selected_country=='VAR./MES' and selected_city=='Boi':
        df = df.set_index(' ')
        df['Var./Mês']=df['Var./Mês'].str.replace(',','.')
        df['Var./Mês']=df['Var./Mês'].str.replace('%','')
        df['Var./Mês']=df['Var./Mês'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Mês'])
        min=df['Var./Mês'].min()-1
        max=df['Var./Mês'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VALOR US$' and selected_city=='Boi':
        df = df.set_index(' ')
        df['Valor US$*']=df['Valor US$*'].str.replace(',','.').astype(float)
        fig = px.bar(x=df.index, y=df['Valor US$*'])
        min=df['Valor US$*'].min()-1
        max=df['Valor US$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VALOR R$' and selected_city=='Bezerro':
        df = df.set_index(' ')
        df['Valor R$*']=df['Valor R$*'].str.replace('.','')
        df['Valor R$*']=df['Valor R$*'].str.replace(',','.').astype(float)
      
        fig = px.bar(x=df.index, y=df['Valor R$*'])
        min=df['Valor R$*'].min()-1
        max=df['Valor R$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./DIA' and selected_city=='Bezerro':
        df = df.set_index(' ')
        df['Var./Dia']=df['Var./Dia'].str.replace(',','.')
        df['Var./Dia']=df['Var./Dia'].str.replace('%','')
        df['Var./Dia']=df['Var./Dia'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Dia'])
        min=df['Var./Dia'].min()-1
        max=df['Var./Dia'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./MES' and selected_city=='Bezerro':
        df = df.set_index(' ')
        df['Var./Mês']=df['Var./Mês'].str.replace(',','.')
        df['Var./Mês']=df['Var./Mês'].str.replace('%','')
        df['Var./Mês']=df['Var./Mês'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Mês'])
        min=df['Var./Mês'].min()-1
        max=df['Var./Mês'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VALOR US$' and selected_city=='Bezerro':
        df = df.set_index(' ')
        df['Valor US$*']=df['Valor US$*'].str.replace(',','.').astype(float)
        fig = px.bar(x=df.index, y=df['Valor US$*'])
        min=df['Valor US$*'].min()-1
        max=df['Valor US$*'].max()+1
        fig.update(layout_yaxis_range =[min,max])
        
    elif selected_country=='VALOR R$' and selected_city=='Algodao':
        df = df.set_index(' ')
        df['Centavos R$/lp']=df['Centavos R$/lp'].str.replace('.','')
        df['Centavos R$/lp']=df['Centavos R$/lp'].str.replace(',','.').astype(float)
      
        fig = px.bar(x=df.index, y=df['Centavos R$/lp'])
        min=df['Centavos R$/lp'].min()-1
        max=df['Centavos R$/lp'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./DIA' and selected_city=='Algodao':
        df = df.set_index(' ')
        df['Var./Dia']=df['Var./Dia'].str.replace(',','.')
        df['Var./Dia']=df['Var./Dia'].str.replace('%','')
        df['Var./Dia']=df['Var./Dia'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Dia'])
        min=df['Var./Dia'].min()-1
        max=df['Var./Dia'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VAR./MES' and selected_city=='Algodao':
        df = df.set_index(' ')
        df['Var./Mês']=df['Var./Mês'].str.replace(',','.')
        df['Var./Mês']=df['Var./Mês'].str.replace('%','')
        df['Var./Mês']=df['Var./Mês'].astype(float)
        
        fig = px.bar(x=df.index, y=df['Var./Mês'])
        min=df['Var./Mês'].min()-1
        max=df['Var./Mês'].max()+1
        fig.update(layout_yaxis_range =[min,max])
    elif selected_country=='VALOR US$' and selected_city=='Algodao':
        df = df.set_index(' ')
        df['Prazo pgto. (dias)']=df['Prazo pgto. (dias)'].str.replace(',','.').astype(float)
        fig = px.bar(x=df.index, y=df['Prazo pgto. (dias)'])
        min=df['Prazo pgto. (dias)'].min()-1
        max=df['Prazo pgto. (dias)'].max()+1
        fig.update(layout_yaxis_range =[min,max])
   

  
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
    
