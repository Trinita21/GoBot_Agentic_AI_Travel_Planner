# GoBot: Agentic-AI Travel Planner

This is the repository for **GoBot: Agentic-AI Travel Planner**. This project explores advanced AI-driven agentic workflows for an AI-assisted Travel Planner designed to generate personalized trip plans through conversational user input. It takes into account the Location, Weather, Exchange Rate and Currency, and Expense Calculation during the planning process. So this is not "just a chatbot"!

<img width="1039" height="675" alt="Screenshot 2025-07-31 at 16 12 18" src="https://github.com/user-attachments/assets/6d1eb3e8-3653-4948-9e23-1565de6110ec" />


---

## Overview

This repository contains:

- An **agentic workflow engine** that uses graph-based reasoning and modular AI components for flexible task execution.
- A **Travel Planner application** featuring:
  - A FastAPI backend serving AI-driven travel plan generation via `/query` endpoint.
  - A Streamlit frontend providing an interactive chat interface.
  - Visualization of reasoning workflows saved as PNG images.
- Integration with large language models and knowledge graphs for explainable AI planning.

---

## Repository Structure

agentic_ai_projects/
├── agent/ # Core agentic workflow code
├── utils/ # Utility scripts (e.g., document saving)
├── streamlit_app.py # Streamlit frontend for Travel Planner UI
├── main.py # FastAPI backend API server
├── requirements.txt # Python dependencies
└── README.md # This file


---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/Trinita21/GoBot_Agentic_AI_Travel_Planner.git
cd agentic_ai_projects
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate 
```

3. Install Requirements.

```bash
pip install -r requirements.txt
```

4. Start the backend server
```bash
uvicorn main:app --reload --port 8000
```


5. Start the frontend UI

```bash
streamlit run streamlit_app.py
```


## How It Works
The frontend collects user input describing their travel plans.
It sends a POST request with the query to the backend /query endpoint.
The backend executes an agentic AI workflow to generate a travel plan.
The workflow reasoning graph is saved as my_graph.png.
The AI-generated plan is sent back and displayed on the frontend.

## Contributing
Contributions and suggestions are welcome! Please open issues or pull requests for improvements.
