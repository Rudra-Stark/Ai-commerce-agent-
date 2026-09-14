# AI Commerce Agent

 An AI-powered shopping assistant that helps users find products using natural language.

 Instead of manually applying filters, a user can simply describe what they are looking for.

 For example:

 > Find me wireless headphones under ₹3000 with good battery life.

 The AI understands the request, decides when it needs product information, searches the product catalogue using a tool, and uses the results to give a recommendation.

 ## How It Works

```
User
  ↓
FastAPI
  ↓
AI Agent
  ↓
Qwen 1.7B (Ollama)
  ↓
Product Search Tool
  ↓
SQLite Database
  ↓
Product Results
  ↓
AI Agent
  ↓
Final Recommendation
```

 The important part of the project is that the AI is not only generating text. It can use a Python tool to search the actual product database.

 ## Current Features

 - Natural-language product requests
- Product catalogue stored in SQLite
- Product search and filtering
- Filtering by category, price, and rating
- Local LLM using Ollama
- Qwen3 1.7B integration
- AI tool calling
- AI-powered product recommendations
- FastAPI backend
- Interactive API documentation with Swagger

 ## Tech Stack

 - Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Ollama
- Qwen3 1.7B
- Git & GitHub

 ## Project Structure

```
ai-commerce-agent/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── seed.py
│   ├── tools.py
│   ├── ai_test.py
│   ├── test_tools.py
│   ├── agent_test.py
│   └── agent.py
│
├── data/
├── frontend/
├── .gitignore
├── requirements.txt
└── README.md
```

 ## API

 ### GET `/`

 Checks whether the backend is running.

 ### GET `/health`

 Returns the health status of the application.

 ### GET `/products`

 Returns products from the catalogue.

 Examples:

```
/products?category=headphones
/products?max_price=3000
/products?min_rating=4.5
```

 Filters can also be combined:

```
/products?category=headphones&max_price=3000
```

 ### POST `/chat`

 Accepts a natural-language shopping request.

 Example:

```
{
  "message": "Find me headphones under ₹3000"
}
```

 The AI can use the product search tool to find matching products and generate a response.

 ## Running Locally

 ### 1\. Clone the repository

```
git clone <your-repository-url>
cd ai-commerce-agent
```

 ### 2\. Create a virtual environment

 Windows:

```
python -m venv venv
venv\Scripts\activate
```

 ### 3. Install dependencies

```
pip install -r requirements.txt
```

 ### 4\. Install the Qwen model

 This project uses Ollama to run Qwen locally.

```
ollama pull qwen3:1.7b
```

 ### 5\. Create the product database

```
python -m backend.seed
```

 ### 6\. Start the backend

```
uvicorn backend.main:app --reload
```

 The API will run at:

```
http://127.0.0.1:8000
```

 Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

 ## Project Status

 ### Completed

 - [x] FastAPI backend
- [x] SQLite database
- [x] SQLAlchemy models
- [x] Product catalogue
- [x] Product filtering
- [x] Ollama setup
- [x] Qwen3 integration
- [x] Product search tool
- [x] AI tool calling
- [x] Basic agent loop

 ### Next

 - [ ] Connect the agent to the main `/chat` API
- [ ] Build the frontend
- [ ] Add product comparison
- [ ] Add cart functionality
- [ ] Add order creation
- [ ] Integrate Razorpay test payments
- [ ] Improve recommendations
- [ ] Add testing and error handling
- [ ] Deploy the application

 ## About

 This project is being built to explore AI agents and agentic commerce, with a focus on using AI to make product discovery and purchasing more natural.