# 📊 Documentação do Projeto — Fineasy

## 1. Visão Geral

O **Fineasy** é um sistema de organização financeira pessoal desenvolvido com foco no controle mensal e anual de movimentações financeiras.

A aplicação permite o registro e acompanhamento de:

* Entradas
* Saídas
* Investimentos

O objetivo principal do projeto é oferecer uma visão clara da saúde financeira do usuário por meio de organização temporal (mês/ano), resumos automáticos e visualização gráfica.

---

## 2. Objetivos do Projeto

* Centralizar o controle financeiro pessoal em uma única plataforma
* Organizar movimentações por mês e ano
* Calcular automaticamente saldos e totais
* Exibir resumos financeiros visuais
* Facilitar tomadas de decisão financeiras

---

## 3. Arquitetura Atual

Atualmente o projeto está dividido em duas camadas principais:

### 🔹 Back‑end (Python)

Responsável por:

* Regras de negócio
* Manipulação do banco de dados
* Criação de funções financeiras
* Organização mensal

### 🔹 Front‑end (HTML, CSS, JS)

Responsável por:

* Interface visual
* Experiência do usuário
* Layout dashboard financeiro
* Componentes gráficos

📌 **Observação:**
A integração entre front‑end e back‑end via API ainda não foi implementada.

---

## 4. Tecnologias Utilizadas

### Back‑end

* Python
* SQLite3

### Front‑end

* HTML5
* CSS3
* JavaScript
* Chart.js (visualização de dados)

### Versionamento

* Git / GitHub

---

## 5. Estrutura do Banco de Dados

### 📂 Tabela: categoria

Responsável por armazenar os tipos de categorias financeiras.

**Campos:**

* id
* nome
* tipo (Entrada / Saída / Investimento)

---

### 📂 Tabela: mes

Responsável pela organização temporal das movimentações.

**Campos:**

* id
* mes
* ano
* status (Aberto / Fechado)
* criado_em

**Regras:**

* Restrição UNIQUE (mes, ano)
* Impede duplicidade de meses no mesmo ano

---

### 📂 Outras tabelas (em evolução)

Previstas para armazenar:

* Movimentações
* Valores
* Datas
* Relação com categorias

---

## 6. Funcionalidades Já Implementadas

### ✅ Estruturação do Banco

* Criação automática de tabelas
* Relacionamentos iniciais

### ✅ Sistema de Categorias

* Criação de categorias
* Consulta por tipo
* Busca de ID por nome

### ✅ Inicialização de Meses

* Função para gerar os 12 meses de um ano
* Status padrão: **Fechado**
* Controle único por (mês/ano)

### ✅ Controle de Status do Mês

* Estrutura pronta para:

  * Abrir mês
  * Fechar mês

### ✅ Interface Dashboard

Implementação visual de:

* Header e navegação
* Card de mês atual
* Botão “Fechar mês”
* Formulário de nova movimentação
* Cards de resumo mensal
* Lista de últimas movimentações
* Área de gráfico de despesas

### ✅ Estilização Dark Mode

* Tema escuro completo
* Versão neon e versão dark neutra
* Uso de variáveis CSS planejado

### ✅ Gráfico Financeiro

* Integração com Chart.js
* Estrutura pronta para dados dinâmicos

---

## 7. Regras de Negócio Definidas

* Não é possível existir dois meses iguais no mesmo ano
* Meses precisam estar **Abertos** para receber movimentações
* Fechamento mensal é manual
* Controle financeiro é organizado por período

---

## 8. Funcionalidades em Desenvolvimento

* Cadastro de movimentações integrado ao banco
* Cálculo automático de:

  * Entradas
  * Saídas
  * Investimentos
  * Saldo
* Listagem real de movimentações
* Filtros por mês

---

## 9. Integração Back‑end ↔ Front‑end (Pendente)

A próxima etapa do projeto consiste na criação de uma **API** para comunicação entre as camadas.

### Objetivos da API:

* Criar movimentações
* Listar movimentações
* Buscar mês aberto
* Abrir/Fechar mês
* Gerar resumos

Tecnologias previstas:

* Flask ou FastAPI
* REST API
* Requisições via Fetch/Axios

---

## 10. Possíveis Melhorias Futuras

### 🔧 Funcionais

* Sistema de login
* Multiusuários
* Metas financeiras
* Controle de orçamento
* Alertas de gastos

### 📊 Analíticas

* Comparação entre meses
* Evolução patrimonial
* Relatórios anuais

### 🎨 Interface

* Responsividade mobile
* Dark/Light toggle
* Animações

### ⚙️ Técnicas

* Migração para PostgreSQL
* Deploy em nuvem
* Docker
* Cache de dados

---

## 11. Roadmap Resumido

**Fase 1 — Concluída**

* Estrutura do banco
* Categorias
* Meses
* Layout dashboard

**Fase 2 — Atual**

* Funções financeiras
* Integração com dados reais

**Fase 3 — Próxima**

* Criação da API
* Integração front/back

**Fase 4 — Futuro**

* Autenticação
* Relatórios avançados
* Deploy

---

## 12. Status Atual do Projeto

🟡 Em desenvolvimento ativo

O sistema já possui:

* Base estrutural sólida
* Regras financeiras definidas
* Interface completa

Faltando apenas a camada de integração (API) para funcionamento full‑stack.

---

## 13. Considerações Finais

O Fineasy encontra‑se em estágio avançado de estruturação, com back‑end funcional e front‑end projetado para consumo de dados dinâmicos.

A evolução natural do projeto é a implementação da API, transformando-o em uma aplicação web completa, escalável e pronta para uso real.

---

**Projeto desenvolvido para fins de organização financeira, prática de desenvolvimento full‑stack e portfólio profissional.**
