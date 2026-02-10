
# 🤖 AI Chatbot using LangGraph

An AI-powered conversational chatbot built using **LangGraph**, **LangChain**, and **OpenAI API**, designed to support context-aware conversations with memory persistence and real-time response streaming. The application provides a clean chat interface using **Streamlit** and maintains conversation history across multiple chat sessions.

---


---

## 🚀 Features

✅ AI-powered conversational chatbot  
✅ Context-aware responses using conversation memory  
✅ LangGraph-based state management  
✅ Multi-threaded chat sessions  
✅ Persistent conversation history  
✅ Real-time streaming responses  
✅ Interactive Streamlit UI  
✅ Scalable architecture for future AI workflows  

---

## 🧠 Architecture Overview

The project follows a modular architecture:

### 🔹 LangGraph Backend
- Defines conversation state  
- Handles message flow  
- Manages memory using checkpointer  
- Invokes OpenAI LLM for responses  

### 🔹 Streamlit Frontend
- Chat interface  
- Conversation display  
- Session management  
- Multiple chat threads  

### 🔹 LLM Layer
- OpenAI Chat Model  
- Processes user input  
- Generates contextual responses  

---

## 🛠️ Technologies Used

- Python  
- LangChain  
- LangGraph  
- OpenAI API  
- Streamlit  
- dotenv  
- UUID (session handling)  

---

## 📂 Project Structure

```
├── langraph_backend.py      # LangGraph workflow and chatbot logic
├── streamlit_frontend.py    # Streamlit UI and chat interface
├── assets/
│   └── langgraph-chatbot-ui.png
├── .env                     # API keys (not included in repo)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rishu511/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

```bash
streamlit run streamlit_frontend.py
```

The chatbot interface will open in your browser.

---

## 💡 How It Works

1. User sends a message through Streamlit UI.  
2. Message is passed to LangGraph workflow.  
3. Conversation state is updated using memory checkpointer.  
4. OpenAI model generates a response.  
5. Response is streamed back to the UI in real time.  

---

## 📈 Future Improvements

- Add Retrieval-Augmented Generation (RAG)  
- Database-based memory storage  
- Authentication for users  
- Deployment using Docker & Cloud  
- Tool calling and agent workflows  

---

## 👨‍💻 Author

**Rishu Raj**

- LinkedIn: https://www.linkedin.com/in/rishu-raj-335865290/  
- GitHub: https://github.com/rishu511

