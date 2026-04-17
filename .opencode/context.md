# Contexto do Projeto: Dashboard Solicitação de Gás

## Visão Geral
Dashboard para visualização e análise de dados de solicitação de gás. Utiliza Python, Dash, Plotly e PostgreSQL. O projeto busca dados da tabela `trx_gas_request` e apresenta em gráficos e filtros interativos.

## Stack Técnica
- **Frontend**: Dash (Python)
- **Gráficos**: Plotly
- **Banco de dados**: PostgreSQL (Supabase)
- **Conexão BD**: psycopg2

## Credenciais DEV (Supabase)
- Host: aws-0-sa-east-1.pooler.supabase.com
- Port: 5432
- Database: postgres
- User: bi_user.jmwcemtewbxfzwzbklou

## Estrutura do Projeto
```
dashboardSolicitacaoDeGas/
├── .env          # Credenciais
├── .opencode/    # Contexto do projeto
├── app.py        # Dashboard principal (Dash + Plotly)
├── db.py         # Conexão com banco de dados
├── treatment.py  # Tratamento de dados
└── assets/       # CSS e assets estáticos
```

## Tarefas em Andamento
- [ ] [Tarefa atual]
- [ ] [Próxima tarefa]

## Tarefas Concluídas
- [x] Configurar estrutura base do projeto
- [x] Preencher credenciais no .env
- [x] Criar db.py com conexão ao banco
- [x] Criar treatment.py para tratar dados da trx_gas_request
- [x] Criar app.py com dashboard, gráficos e filtros
- [x] Criar requirements.txt

## Dependências Importantes
- dash
- plotly
- psycopg2
- python-dotenv
- pandas

## Views Criadas
- `vw_bi_gas_request` - View com dados tratados da trx_gas_request

## Problemas Conhecidos / Débitos Técnicos
- Warning do pandas sobre psycopg2 - considerar usar SQLAlchemy para conexão
- Sem permissão para criar views (usuário bi_user é read-only)