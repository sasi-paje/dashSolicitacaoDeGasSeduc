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
        'backgroundColor': '#0f172a',
        'minHeight': '100vh',
        'padding': '20px',
        'color': '#e2e8f0'
    },
    children=[
        html.Header(
            style={'marginBottom': '30px'},
            children=[
                html.H1(
                    "Dashboard de Solicitação de Gás",
                    style={'fontSize': '28px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'}
                ),
                html.P(
                    f"Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                    style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '8px 0 0 0'}
                )
            ]
        ),

        html.Div(
            style={'display': 'grid', 'gridTemplateColumns': 'repeat(4, 1fr)', 'gap': '16px', 'marginBottom': '24px'},
            children=[
                html.Div(
                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                    children=[
                        html.P("Total de Solicitações", style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '0 0 8px 0'}),
                        html.H2(f"{len(df)}", style={'fontSize': '32px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'})
                    ]
                ),
                html.Div(
                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                    children=[
                        html.P("Municípios Únicos", style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '0 0 8px 0'}),
                        html.H2(f"{df['municipio'].nunique() if 'municipio' in df.columns else 0}", style={'fontSize': '32px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'})
                    ]
                ),
                html.Div(
                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                    children=[
                        html.P("Total de Botijões", style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '0 0 8px 0'}),
                        html.H2(f"{df['quantidade'].sum() if 'quantidade' in df.columns else 0}", style={'fontSize': '32px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'})
                    ]
                ),
                html.Div(
                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                    children=[
                        html.P("Unidades Únicas", style={'fontSize': '14px', 'color': '#94a3b8', 'margin': '0 0 8px 0'}),
                        html.H2(f"{df['unidade'].nunique() if 'unidade' in df.columns else 0}", style={'fontSize': '32px', 'fontWeight': '700', 'margin': '0', 'color': '#f8fafc'})
                    ]
                )
            ]
        ),

        html.Div(
            style={'display': 'grid', 'gridTemplateColumns': '250px 1fr', 'gap': '24px'},
            children=[
                html.Div(
                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                    children=[
                        html.H3("Filtros", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#f8fafc'}),

                        html.Label("Município", style={'fontSize': '14px', 'color': '#94a3b8', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='municipio-filter',
                            options=[{'label': m, 'value': m} for m in df['municipio'].unique()] if 'municipio' in df.columns else [],
                            value=None,
                            style={'marginBottom': '20px', 'backgroundColor': '#0f172a', 'color': '#1e293b'}
                        ),

                        html.Label("Tipo de Gás", style={'fontSize': '14px', 'color': '#94a3b8', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='tipo-gas-filter',
                            options=[{'label': t, 'value': t} for t in df['tipo_gas'].unique()] if 'tipo_gas' in df.columns else [],
                            value=None,
                            style={'marginBottom': '20px', 'backgroundColor': '#0f172a', 'color': '#1e293b'}
                        ),

                        html.Label("Status", style={'fontSize': '14px', 'color': '#94a3b8', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='status-filter',
                            options=[{'label': s, 'value': s} for s in df['status_name'].unique()] if 'status_name' in df.columns else [],
                            value=None,
                            style={'marginBottom': '20px', 'backgroundColor': '#0f172a', 'color': '#1e293b'}
                        ),

                        html.Label("Justificativa", style={'fontSize': '14px', 'color': '#94a3b8', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Dropdown(
                            id='justificativa-filter',
                            options=[{'label': j, 'value': j} for j in df['justificativa'].unique()] if 'justificativa' in df.columns else [],
                            value=None,
                            style={'marginBottom': '20px', 'backgroundColor': '#0f172a', 'color': '#1e293b'}
                        ),

                        html.Label("Data Inicial", style={'fontSize': '14px', 'color': '#94a3b8', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.DatePickerRange(
                            id='date-filter',
                            start_date=df['created_at'].min() if 'created_at' in df.columns else None,
                            end_date=df['created_at'].max() if 'created_at' in df.columns else None,
                            style={'marginBottom': '20px'}
                        )
                    ]
                ),

                html.Div(
                    style={'display': 'flex', 'flexDirection': 'column', 'gap': '24px'},
                    children=[
                        html.Div(
                            style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                            children=[
                                html.H3("Solicitações por Data", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#f8fafc'}),
                                dcc.Graph(id='date-chart')
                            ]
                        ),
                        html.Div(
                            style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '24px'},
                            children=[
                                html.Div(
                                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                                    children=[
                                        html.H3("Por Município", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#f8fafc'}),
                                        dcc.Graph(id='municipio-chart')
                                    ]
                                ),
                                html.Div(
                                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                                    children=[
                                        html.H3("Por Tipo de Gás", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#f8fafc'}),
                                        dcc.Graph(id='tipo-gas-chart')
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '24px'},
                            children=[
                                html.Div(
                                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                                    children=[
                                        html.H3("Por Status", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#f8fafc'}),
                                        dcc.Graph(id='status-chart')
                                    ]
                                ),
                                html.Div(
                                    style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                                    children=[
                                        html.H3("Por Justificativa", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#f8fafc'}),
                                        dcc.Graph(id='justificativa-chart')
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            style={'background': '#1e293b', 'borderRadius': '12px', 'padding': '20px'},
                            children=[
                                html.H3("Top 10 Unidades com Mais Solicitações", style={'fontSize': '18px', 'fontWeight': '600', 'margin': '0 0 20px 0', 'color': '#f8fafc'}),
                                dcc.Graph(id='unidades-chart')
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

@app.callback(
    [dash.dependencies.Output('date-chart', 'figure'),
     dash.dependencies.Output('municipio-chart', 'figure'),
     dash.dependencies.Output('tipo-gas-chart', 'figure'),
     dash.dependencies.Output('status-chart', 'figure'),
     dash.dependencies.Output('justificativa-chart', 'figure'),
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
        paper_bgcolor='#1e293b',
        plot_bgcolor='#1e293b',
        font_color='#e2e8f0',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155')
    )

    municipio_chart = px.pie(
        filtered_df.groupby('municipio').size().reset_index(name='count'),
        values='count',
        names='municipio',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    municipio_chart.update_layout(
        paper_bgcolor='#1e293b',
        font_color='#e2e8f0'
    )

    tipo_gas_chart = px.bar(
        filtered_df.groupby('tipo_gas').size().reset_index(name='count'),
        x='tipo_gas',
        y='count',
        color_discrete_sequence=['#22c55e']
    )
    tipo_gas_chart.update_layout(
        paper_bgcolor='#1e293b',
        plot_bgcolor='#1e293b',
        font_color='#e2e8f0',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155')
    )

    status_chart = px.pie(
        filtered_df.groupby('status_name').size().reset_index(name='count'),
        values='count',
        names='status_name',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    status_chart.update_layout(
        paper_bgcolor='#1e293b',
        font_color='#e2e8f0'
    )

    justificativa_chart = px.bar(
        filtered_df.groupby('justificativa').size().reset_index(name='count'),
        x='justificativa',
        y='count',
        color_discrete_sequence=['#f59e0b']
    )
    justificativa_chart.update_layout(
        paper_bgcolor='#1e293b',
        plot_bgcolor='#1e293b',
        font_color='#e2e8f0',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155')
    )

    top_unidades = filtered_df.groupby('unidade').size().reset_index(name='count').nlargest(10, 'count')
    unidades_chart = px.bar(
        top_unidades,
        x='count',
        y='unidade',
        orientation='h',
        color_discrete_sequence=['#ec4899']
    )
    unidades_chart.update_layout(
        paper_bgcolor='#1e293b',
        plot_bgcolor='#1e293b',
        font_color='#e2e8f0',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155')
    )

    return date_chart, municipio_chart, tipo_gas_chart, status_chart, justificativa_chart, unidades_chart

if __name__ == '__main__':
    app.run(debug=True)