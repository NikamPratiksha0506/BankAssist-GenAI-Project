# 🏦 BankAssist — GenAI Project

**Industry:** Retail & Commercial Banking  
**Headquarters:** Mumbai, India  

BankAssist is a mid-sized retail bank serving **individual customers, SMEs, and corporate accounts**. Its services include:  

- Savings & Current Accounts  
- Loans & Mortgages  
- Credit Cards  
- Digital Banking Services  
- Compliance & Risk Management  

### 🚨 Problem Statement
Competitor banks like **NeoBankX** have launched **AI-driven virtual assistants** capable of:  
- Answering customer queries  
- Generating compliance summaries  
- Detecting fraud signals  
- Automating workflows  

BankAssist has been strong in **core banking automation** but **lags behind in Generative AI services**.  
The goal is to **upgrade the BankAssist IQ platform** with GenAI capabilities in **7 days**.

---

### 🔹 Task 2: AI Agent with External Tool Access

**Objective:** Build an AI agent that can use **external tools** to answer queries like loan EMI, currency conversion, and weather info.

**Tools & Tech:**  
- LangGraph (Orchestrator)  
- LangChain Tools: Calculator, PythonREPLTool, RequestsGetTool  
- Gemini API (LLM)

**Implementation Steps:**  
1. Install LangGraph:
   ```bash
   pip install langgraph

Define tools in LangChain using the Tool schema.

Implement a ReAct-style agent for multi-step reasoning.

Design prompt templates to instruct the agent which tool to use.

Example Query:

“What’s the EMI for a ₹10L loan over 5 years at 8.5% interest?”

**Code Example:**  

![Task 2 Code](C:\Users\HP\Desktop\Task5.png)

**Sample Output:**  

![Task 2 Output](screenshots/task2_output.png)


Task 5: SQL Q&A System (Banking Data)

Objective: Enable natural language queries on structured customer and transaction data.

Database Schema:

customers(id, name, account_type, balance, risk_profile)

transactions(id, customer_id, type, amount, date, branch)

clients(client_id, name, age, risk_profile, portfolio_value)

investments(investment_id, client_id, fund_name, amount_invested, date)

Implementation Steps:

Create SQLite database and populate ≥30 sample rows per table.

Use LangChain SQLDatabaseChain to translate natural queries to SQL.

Execute query and return readable output.

Use prompt templates for safe query construction.

Example Query:

“Show all customers with balance > ₹5L and more than 3 transactions this month.”

Code Example:


Sample Output:


🔹 Task 6: Document Summarization Engine

Objective: Summarize long banking and compliance documents efficiently.

Examples:

5-page KYC report → 3-paragraph summary

Credit risk analysis → executive briefing

Tools & Tech:

Gemini API

LangChain Summarization Chains: MapReduce, Refine

PyPDF or text loaders

Implementation Steps:

Load input document (PDF or text).

Chunk large documents if necessary.

Apply MapReduce or Refine summarization chains.

Generate concise outputs with Gemini LLM.

Data Sources: Fund reports, earnings calls, compliance docs

Code Example:


Sample Output:


🔹 Task 8: Workflow Automation with n8n

Objective: Automate workflows triggered by AI outputs from other modules.

Examples:

Alert RM via Slack if a transaction > ₹50L

Email compliance officer if fraud risk > threshold

Log chatbot queries into Google Sheets

Tools & Tech:

n8n.io (cloud, Docker, or local)

Nodes: Webhook, Slack, Gmail, HTTP

Implementation Steps:

Sign up at n8n.cloud
 or self-host.

Define workflow triggers (e.g., SQL query results, summarization output).

Transform data → Send notifications.

Integrate with LangChain outputs via webhook.

Code Example:


Sample Output:


Author

Pratiksha Nikam
Data Analyst | GenAI Enthusiast | B-Tech CSE

