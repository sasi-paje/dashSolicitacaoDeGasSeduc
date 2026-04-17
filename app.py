import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from treatment import get_gas_requests, treat_data
from datetime import datetime

df = get_gas_requests()
df = treat_data(df)

app = dash.Dash(__name__)
app.title = "Dashboard - Solicitação de Gás"

server = app.server

app.layout = html.Div(
    style={
        'fontFamily': 'Inter, -apple-system, BlinkMacSystemFont, sans-serif',
        'backgroundColor': '#F0F2F4',
        'minHeight': '100vh',
        'padding': '20px',
        'color': '#1e293b'
    },
    children=[
        html.Header(
            style={'marginBottom': '30px'},
            children=[
                html.H1(
                    "Dashboard de Solicitação de Gás",
                    style={'fontSize': '28px', 'fontWeight': '700', 'margin': '0', 'color': '#1e293b'}
                ),
                html.P(
                    f"Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                    style={'fontSize': '14px', 'color': '#64748b', 'margin': '8px 0 0 0'}
                )
            ]
        ),

        html.Div(
                    style={
                        'display': 'flex',
                        'gap': '16px',
                        'marginBottom': '24px',
                        'flexWrap': 'wrap',
                        'backgroundColor': '#FFFFFF',
                        'padding': '20px',
                        'borderRadius': '12px',
                        'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'
                    },
            children=[
                html.Div(
                    style={'flex': '1', 'minWidth': '200px'},
                    children=[
                        html.Label("Município", style={'fontSize': '14px', 'color': '#64748b', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='municipio-filter',
                            options=[{'label': m, 'value': m} for m in df['municipio'].unique()] if 'municipio' in df.columns else [],
                            value=None,
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '200px'},
                    children=[
                        html.Label("Tipo de Gás", style={'fontSize': '14px', 'color': '#64748b', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='tipo-gas-filter',
                            options=[{'label': t, 'value': t} for t in df['tipo_gas'].unique()] if 'tipo_gas' in df.columns else [],
                            value=None,
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '200px'},
                    children=[
                        html.Label("Status", style={'fontSize': '14px', 'color': '#64748b', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='status-filter',
                            options=[{'label': s, 'value': s} for s in df['status_name'].unique()] if 'status_name' in df.columns else [],
                            value=None,
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '200px'},
                    children=[
                        html.Label("Justificativa", style={'fontSize': '14px', 'color': '#64748b', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='justificativa-filter',
                            options=[{'label': j, 'value': j} for j in df['justificativa'].unique()] if 'justificativa' in df.columns else [],
                            value=None,
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '200px'},
                    children=[
                        html.Label("Período", style={'fontSize': '14px', 'color': '#64748b', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.DatePickerRange(
                            id='date-filter',
                            start_date=df['created_at'].min() if 'created_at' in df.columns else None,
                            end_date=df['created_at'].max() if 'created_at' in df.columns else None,
                            style={'width': '100%'}
                        )
                    ]
                )
            ]
        ),

        html.Div(
            style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '16px', 'marginBottom': '24px'},
            children=[
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                    children=[
                        html.P("Total de Solicitações", style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '0 0 8px 0'}),
                        html.H2(f"{len(df)}", style={'fontSize': '32px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'})
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                    children=[
                        html.P("Total de Botijões", style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '0 0 8px 0'}),
                        html.H2(f"{df['quantidade'].sum() if 'quantidade' in df.columns else 0}", style={'fontSize': '32px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'})
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                    children=[
                        html.P("Unidades Solicitantes", style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '0 0 8px 0'}),
                        html.H2(f"{df['unidade'].nunique() if 'unidade' in df.columns else 0}", style={'fontSize': '32px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'})
                    ]
                )
            ]
        ),

        html.Div(
            style={'display': 'flex', 'flexDirection': 'column', 'gap': '24px'},
            children=[
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                    children=[
                        html.H3("Solicitações por Data", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#1e293b'}),
                        dcc.Graph(id='date-chart')
                    ]
                ),
                html.Div(
                    style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '24px'},
                    children=[
                        html.Div(
                            style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                            children=[
                                html.H3("Por Tipo de Gás", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#1e293b'}),
                                dcc.Graph(id='tipo-gas-chart')
                            ]
                        ),
                        html.Div(
                            style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                            children=[
                                html.H3("Por Justificativa", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#1e293b'}),
                                dcc.Graph(id='justificativa-chart')
                            ]
                        )
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                    children=[
                        html.H3("Por Status", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#1e293b'}),
                        dcc.Graph(id='status-chart')
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'},
                    children=[
                        html.H3("Top 10 Unidades com Mais Solicitações", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#1e293b'}),
                        dcc.Graph(id='unidades-chart')
                    ]
                )
            ]
        )
    ]
)

@app.callback(
    [dash.dependencies.Output('date-chart', 'figure'),
     dash.dependencies.Output('tipo-gas-chart', 'figure'),
     dash.dependencies.Output('justificativa-chart', 'figure'),
     dash.dependencies.Output('status-chart', 'figure'),
     dash.dependencies.Output('unidades-chart', 'figure')],
    [dash.dependencies.Input('municipio-filter', 'value'),
     dash.dependencies.Input('tipo-gas-filter', 'value'),
     dash.dependencies.Input('status-filter', 'value'),
     dash.dependencies.Input('justificativa-filter', 'value'),
     dash.dependencies.Input('date-filter', 'start_date'),
     dash.dependencies.Input('date-filter', 'end_date')]
)
def update_charts(municipio, tipo_gas, status, justificativa, start_date, end_date):
    filtered_df = df.copy()

    if municipio:
        filtered_df = filtered_df[filtered_df['municipio'] == municipio]
    if tipo_gas:
        filtered_df = filtered_df[filtered_df['tipo_gas'] == tipo_gas]
    if status:
        filtered_df = filtered_df[filtered_df['status_name'] == status]
    if justificativa:
        filtered_df = filtered_df[filtered_df['justificativa'] == justificativa]
    if start_date:
        filtered_df = filtered_df[filtered_df['created_at'] >= pd.to_datetime(start_date)]
    if end_date:
        filtered_df = filtered_df[filtered_df['created_at'] <= pd.to_datetime(end_date)]

    date_chart = px.bar(
        filtered_df.groupby(filtered_df['created_at'].dt.date).size().reset_index(name='count'),
        x='created_at',
        y='count',
        color_discrete_sequence=['#6366f1']
    )
    date_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        xaxis=dict(gridcolor='#e2e8f0', color='#64748b'),
        yaxis=dict(gridcolor='#e2e8f0', color='#64748b')
    )

    tipo_gas_chart = px.bar(
        filtered_df.groupby('tipo_gas').size().reset_index(name='count'),
        x='tipo_gas',
        y='count',
        color_discrete_sequence=['#6366f1']
    )
    tipo_gas_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        xaxis=dict(gridcolor='#e2e8f0', color='#64748b'),
        yaxis=dict(gridcolor='#e2e8f0', color='#64748b')
    )

    justificativa_chart = px.bar(
        filtered_df.groupby('justificativa').size().reset_index(name='count'),
        x='justificativa',
        y='count',
        color_discrete_sequence=['#10b981']
    )
    justificativa_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        xaxis=dict(gridcolor='#e2e8f0', color='#64748b'),
        yaxis=dict(gridcolor='#e2e8f0', color='#64748b')
    )

    status_chart = px.bar(
        filtered_df.groupby('status_name').size().reset_index(name='count'),
        x='count',
        y='status_name',
        orientation='h',
        color_discrete_sequence=['#8b5cf6']
    )
    status_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        xaxis=dict(gridcolor='#e2e8f0', color='#64748b'),
        yaxis=dict(gridcolor='#e2e8f0', color='#64748b')
    )

    top_unidades = filtered_df.groupby('unidade').size().reset_index(name='count').sort_values('count', ascending=False).nlargest(10, 'count')
    unidades_chart = px.bar(
        top_unidades,
        x='count',
        y='unidade',
        orientation='h',
        color_discrete_sequence=['#ec4899']
    )
    unidades_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        xaxis=dict(gridcolor='#e2e8f0', color='#64748b'),
        yaxis=dict(gridcolor='#e2e8f0', color='#64748b')
    )

    return date_chart, tipo_gas_chart, justificativa_chart, status_chart, unidades_chart

if __name__ == '__main__':
    app.run(debug=True)