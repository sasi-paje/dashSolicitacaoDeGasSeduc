import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
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
        html.Link(
            href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css',
            rel='stylesheet'
        ),

        html.Div(
            style={
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'space-between',
                'marginBottom': '24px'
            },
            children=[
                html.Div(
                    children=[
                        html.H1(
                            "Solicitações de Gás",
                            style={'fontSize': '22px', 'fontWeight': '700', 'margin': '0', 'color': '#1e293b'}
                        ),
                        html.P(
                            f"Atualizado hoje às {datetime.now().strftime('%H:%M')}",
                            style={'fontSize': '13px', 'color': '#64748b', 'margin': '4px 0 0 0'}
                        )
                    ]
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
                'padding': '20px 24px',
                'borderRadius': '12px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                'border': '1px solid #e2e8f0'
            },
            children=[
                html.Div(
                    style={'flex': '1', 'minWidth': '180px'},
                    children=[
                        html.Label("Município", style={'fontSize': '12px', 'fontWeight': '600', 'color': '#475569', 'marginBottom': '6px', 'display': 'block', 'textTransform': 'uppercase', 'letterSpacing': '0.5px'}),
                        dcc.Dropdown(
                            id='municipio-filter',
                            options=[{'label': m, 'value': m} for m in df['municipio'].unique()] if 'municipio' in df.columns else [],
                            value=None,
                            placeholder="Selecione...",
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b', 'fontSize': '13px'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '180px'},
                    children=[
                        html.Label("Tipo de Gás", style={'fontSize': '12px', 'fontWeight': '600', 'color': '#475569', 'marginBottom': '6px', 'display': 'block', 'textTransform': 'uppercase', 'letterSpacing': '0.5px'}),
                        dcc.Dropdown(
                            id='tipo-gas-filter',
                            options=[{'label': t, 'value': t} for t in df['tipo_gas'].unique()] if 'tipo_gas' in df.columns else [],
                            value=None,
                            placeholder="Selecione...",
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b', 'fontSize': '13px'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '180px'},
                    children=[
                        html.Label("Status", style={'fontSize': '12px', 'fontWeight': '600', 'color': '#475569', 'marginBottom': '6px', 'display': 'block', 'textTransform': 'uppercase', 'letterSpacing': '0.5px'}),
                        dcc.Dropdown(
                            id='status-filter',
                            options=[{'label': s, 'value': s} for s in df['status_name'].unique()] if 'status_name' in df.columns else [],
                            value=None,
                            placeholder="Selecione...",
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b', 'fontSize': '13px'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '180px'},
                    children=[
                        html.Label("Justificativa", style={'fontSize': '12px', 'fontWeight': '600', 'color': '#475569', 'marginBottom': '6px', 'display': 'block', 'textTransform': 'uppercase', 'letterSpacing': '0.5px'}),
                        dcc.Dropdown(
                            id='justificativa-filter',
                            options=[{'label': j, 'value': j} for j in df['justificativa'].unique()] if 'justificativa' in df.columns else [],
                            value=None,
                            placeholder="Selecione...",
                            style={'backgroundColor': '#FFFFFF', 'color': '#1e293b', 'fontSize': '13px'}
                        )
                    ]
                ),
                html.Div(
                    style={'flex': '1', 'minWidth': '180px'},
                    children=[
                        html.Label("Período", style={'fontSize': '12px', 'fontWeight': '600', 'color': '#475569', 'marginBottom': '6px', 'display': 'block', 'textTransform': 'uppercase', 'letterSpacing': '0.5px'}),
                        html.Div(
                            style={'display': 'flex', 'gap': '8px', 'alignItems': 'center'},
                            children=[
                                dcc.DatePickerRange(
                                    id='date-filter',
                                    start_date=df['created_at'].min() if 'created_at' in df.columns else None,
                                    end_date=df['created_at'].max() if 'created_at' in df.columns else None,
                                    style={'width': '100%', 'fontSize': '13px'}
                                ),
                                html.Button(
                                    'Limpar',
                                    id='clear-filters-btn',
                                    n_clicks=0,
                                    style={
                                        'padding': '6px 12px',
                                        'fontSize': '12px',
                                        'backgroundColor': '#ef4444',
                                        'color': '#FFFFFF',
                                        'border': 'none',
                                        'borderRadius': '6px',
                                        'cursor': 'pointer',
                                        'fontWeight': '500'
                                    }
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        html.Div(
            style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(3, 1fr)',
                'gap': '16px',
                'marginBottom': '24px'
            },
            children=[
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)', 'borderLeft': '4px solid #6366f1'},
                    children=[
                        html.Div(
                            style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center'},
                            children=[
                                html.Div(
                                    children=[
                                        html.P("Total de Solicitações", style={'fontSize': '13px', 'color': '#64748b', 'margin': '0 0 4px 0'}),
                                        html.H2(id='total-solicitacoes', children=f"{len(df)}", style={'fontSize': '28px', 'fontWeight': '700', 'margin': '0', 'color': '#1e293b'})
                                    ]
                                ),
                                html.I(className="bi bi-file-text", style={'fontSize': '24px', 'color': '#6366f1', 'opacity': '0.7'})
                            ]
                        )
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)', 'borderLeft': '4px solid #10b981'},
                    children=[
                        html.Div(
                            style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center'},
                            children=[
                                html.Div(
                                    children=[
                                        html.P("Total de Botijões", style={'fontSize': '13px', 'color': '#64748b', 'margin': '0 0 4px 0'}),
                                        html.H2(id='total-botijes', children=f"{df['quantidade'].sum() if 'quantidade' in df.columns else 0}", style={'fontSize': '28px', 'fontWeight': '700', 'margin': '0', 'color': '#1e293b'})
                                    ]
                                ),
                                html.I(className="bi bi-box-seam", style={'fontSize': '24px', 'color': '#10b981', 'opacity': '0.7'})
                            ]
                        )
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)', 'borderLeft': '4px solid #f59e0b'},
                    children=[
                        html.Div(
                            style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center'},
                            children=[
                                html.Div(
                                    children=[
                                        html.P("Unidades Solicitantes", style={'fontSize': '13px', 'color': '#64748b', 'margin': '0 0 4px 0'}),
                                        html.H2(id='unidades-solicitantes', children=f"{df['unidade'].nunique() if 'unidade' in df.columns else 0}", style={'fontSize': '28px', 'fontWeight': '700', 'margin': '0', 'color': '#1e293b'})
                                    ]
                                ),
                                html.I(className="bi bi-building", style={'fontSize': '24px', 'color': '#f59e0b', 'opacity': '0.7'})
                            ]
                        )
                    ]
                )
            ]
        ),

        html.Div(
            style={'display': 'flex', 'flexDirection': 'column', 'gap': '20px'},
            children=[
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)'},
                    children=[
                        html.Div(
                            style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center', 'marginBottom': '16px'},
                            children=[
                                html.H3("Solicitações por Mês", style={'fontSize': '16px', 'fontWeight': '600', 'margin': '0', 'color': '#1e293b'}),
                                html.Div(
                                    style={'display': 'flex', 'gap': '12px'},
                                    children=[
                                        html.Span(
                                            style={'display': 'flex', 'alignItems': 'center', 'gap': '4px', 'fontSize': '12px', 'color': '#64748b'}
                                        ),
                                        html.Span(style={'width': '12px', 'height': '12px', 'backgroundColor': '#f59e0b', 'borderRadius': '2px'}),
                                        html.Span("2025", style={'fontSize': '12px', 'color': '#64748b', 'marginRight': '8px'}),
                                        html.Span(style={'width': '12px', 'height': '12px', 'backgroundColor': '#6366f1', 'borderRadius': '2px'}),
                                        html.Span("2026", style={'fontSize': '12px', 'color': '#64748b'})
                                    ]
                                )
                            ]
                        ),
                        dcc.Graph(id='date-chart')
                    ]
                ),
                html.Div(
                    style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'},
                    children=[
                        html.Div(
                            style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)'},
                            children=[
                                html.H3("Por Tipo de Gás", style={'fontSize': '16px', 'fontWeight': '600', 'margin': '0 0 16px 0', 'color': '#1e293b'}),
                                dcc.Graph(id='tipo-gas-chart')
                            ]
                        ),
                        html.Div(
                            style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)'},
                            children=[
                                html.H3("Por Justificativa", style={'fontSize': '16px', 'fontWeight': '600', 'margin': '0 0 16px 0', 'color': '#1e293b'}),
                                dcc.Graph(id='justificativa-chart')
                            ]
                        )
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)'},
                    children=[
                        html.H3("Por Status", style={'fontSize': '16px', 'fontWeight': '600', 'margin': '0 0 16px 0', 'color': '#1e293b'}),
                        dcc.Graph(id='status-chart')
                    ]
                ),
                html.Div(
                    style={'background': '#FFFFFF', 'borderRadius': '12px', 'padding': '20px', 'boxShadow': '0 1px 3px rgba(0,0,0,0.08)'},
                    children=[
                        html.H3("Top 10 Unidades", style={'fontSize': '16px', 'fontWeight': '600', 'margin': '0 0 16px 0', 'color': '#1e293b'}),
                        dcc.Graph(id='unidades-chart')
                    ]
                )
            ]
        )
    ]
)

@app.callback(
    [dash.dependencies.Output('total-solicitacoes', 'children'),
     dash.dependencies.Output('total-botijes', 'children'),
     dash.dependencies.Output('unidades-solicitantes', 'children')],
    [dash.dependencies.Input('municipio-filter', 'value'),
     dash.dependencies.Input('tipo-gas-filter', 'value'),
     dash.dependencies.Input('status-filter', 'value'),
     dash.dependencies.Input('justificativa-filter', 'value'),
     dash.dependencies.Input('date-filter', 'start_date'),
     dash.dependencies.Input('date-filter', 'end_date')]
)
def update_cards(municipio, tipo_gas, status, justificativa, start_date, end_date):
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

    total = len(filtered_df)
    botijes = int(filtered_df['quantidade'].sum()) if 'quantidade' in filtered_df.columns else 0
    unidades = filtered_df['unidade'].nunique() if 'unidade' in filtered_df.columns else 0

    return str(total), str(botijes), str(unidades)

@app.callback(
    [dash.dependencies.Output('municipio-filter', 'value'),
     dash.dependencies.Output('tipo-gas-filter', 'value'),
     dash.dependencies.Output('status-filter', 'value'),
     dash.dependencies.Output('justificativa-filter', 'value'),
     dash.dependencies.Output('date-filter', 'start_date'),
     dash.dependencies.Output('date-filter', 'end_date')],
    [dash.dependencies.Input('clear-filters-btn', 'n_clicks')],
    [dash.dependencies.State('municipio-filter', 'value'),
     dash.dependencies.State('tipo-gas-filter', 'value'),
     dash.dependencies.State('status-filter', 'value'),
     dash.dependencies.State('justificativa-filter', 'value'),
     dash.dependencies.State('date-filter', 'start_date'),
     dash.dependencies.State('date-filter', 'end_date')]
)
def clear_filters(n_clicks, municipio, tipo_gas, status, justificativa, start_date, end_date):
    if n_clicks and n_clicks > 0:
        return None, None, None, None, None, None

    return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

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

    date_chart = go.Figure()
    months_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    month_labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    for year in sorted(filtered_df['created_at'].dt.year.unique()):
        year_data = filtered_df[filtered_df['created_at'].dt.year == year].groupby(filtered_df['created_at'].dt.month).size().reindex(months_order, fill_value=0)
        color = '#f59e0b' if year == 2025 else '#6366f1' if year == 2026 else '#94a3b8'
        date_chart.add_trace(go.Bar(
            x=month_labels,
            y=year_data.values,
            name=str(year),
            marker_color=color,
            hovertemplate='%{x}: %{y}<extra></extra>'
        ))

    date_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        font=dict(size=12),
        xaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        yaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        barmode='group',
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )

    tipo_gas_chart = px.bar(
        filtered_df.groupby('tipo_gas').size().reset_index(name='count'),
        x='tipo_gas',
        y='count',
        color_discrete_sequence=['#6366f1']
    )
    tipo_gas_chart.update_traces(hovertemplate='%{x}: %{y}<extra></extra>')
    tipo_gas_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        font=dict(size=12),
        xaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        yaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False
    )

    justificativa_chart = px.bar(
        filtered_df.groupby('justificativa').size().reset_index(name='count'),
        x='justificativa',
        y='count',
        color_discrete_sequence=['#10b981']
    )
    justificativa_chart.update_traces(hovertemplate='%{x}: %{y}<extra></extra>')
    justificativa_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        font=dict(size=12),
        xaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        yaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False
    )

    status_df = filtered_df.groupby('status_name').size().reset_index(name='count').sort_values('count', ascending=False)

    status_chart = px.bar(
        status_df,
        x='count',
        y='status_name',
        orientation='h',
        color_discrete_sequence=['#8b5cf6'],
        text='count'
    )
    status_chart.update_traces(textposition='outside', hovertemplate='%{y}: %{x}<extra></extra>')
    status_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        font=dict(size=12),
        xaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        yaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9', autorange='reversed'),
        margin=dict(l=20, r=40, t=20, b=20),
        showlegend=False
    )

    top_unidades = filtered_df.groupby('unidade').size().reset_index(name='count').sort_values('count', ascending=False).nlargest(10, 'count')
    unidades_chart = px.bar(
        top_unidades,
        x='count',
        y='unidade',
        orientation='h',
        color_discrete_sequence=['#ec4899'],
        text='count'
    )
    unidades_chart.update_traces(textposition='outside', hovertemplate='%{y}: %{x}<extra></extra>')
    unidades_chart.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font_color='#1e293b',
        font=dict(size=12),
        xaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9'),
        yaxis=dict(gridcolor='#f1f5f9', color='#94a3b8', linecolor='#f1f5f9', autorange='reversed'),
        margin=dict(l=150, r=20, t=20, b=20),
        showlegend=False
    )

    return date_chart, tipo_gas_chart, justificativa_chart, status_chart, unidades_chart

if __name__ == '__main__':
    app.run(debug=True)