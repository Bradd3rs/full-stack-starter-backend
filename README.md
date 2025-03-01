# 🚀 FastAPI + PostgreSQL: The Simplest Backend Ever!

Hey there, fellow developer! Welcome to this super simple FastAPI backend with PostgreSQL. This repo is designed to be your hassle-free backend solution that plays nicely with any frontend, especially Next.js. No complicated setup, no headaches - just pure API goodness!

## ✨ What's in the Box?

- 🔥 **FastAPI** - Lightning-fast API with automatic docs (seriously, it's FAST!)
- 🐘 **PostgreSQL** - Reliable database that just works
- 🐳 **Docker** - One command to rule them all
- 🔄 **CORS** - Already configured for your frontend needs
- 📝 **Todo API** - Ready-to-use example endpoints

## 🏁 Getting Started in 60 Seconds

### 🐳 The Docker Way (Recommended)

```bash
# 1. Clone this repo
git clone <repository-url>
cd fastApi-example

# 2. Fire up the engines!
docker-compose up -d

# 3. That's it! 🎉
```

Your API is now running at http://localhost:8000 - how easy was that?! Docker automatically:

- Starts your FastAPI application
- Sets up the PostgreSQL database
- Connects everything together

Just check out:

- 📚 API docs: http://localhost:8000/docs (interactive & awesome!)
- 📋 OpenAPI spec: http://localhost:8000/api/v1/openapi.json

### 🐍 The Python Way (For Local Development Only)

If you prefer to develop without Docker (though Docker is easier!), you'll need to:

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install the goodies
pip install -r requirements.txt

# 3. Set up your PostgreSQL database separately
# 4. Update the .env file with your database connection details

# 5. Launch the app manually
uvicorn app.main:app --reload
```

## 🔌 API Endpoints - Ready to Use!

- `GET /api/v1/todos` - Get all your todos
- `POST /api/v1/todos` - Create a shiny new todo
- `GET /api/v1/todos/{todo_id}` - Get a specific todo
- `PUT /api/v1/todos/{todo_id}` - Update a todo
- `DELETE /api/v1/todos/{todo_id}` - Banish a todo to the void

## 🔧 Environment Variables - Already Set Up!

Everything's pre-configured in the `.env` file:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/fastapi_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fastapi_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Feel free to change these for production! 🔒

## 🤝 Perfect Pair: The Next.js Frontend Companion

Want a beautiful UI to go with this API? Check out our [full-stack-starter-frontend](https://github.com/Bradd3rs/full-stack-starter-frontend) repo!

It's pre-configured to connect to this backend and includes:

- 🚀 **Next.js 15** with React 19
- 🎭 **Tailwind + Radix UI** for beautiful components
- 🌗 **Dark Mode** support
- 🔄 **SWR** for magical data fetching
- 🔌 **API Integration** already set up!

Getting it running is as simple as:

```bash
# Clone the frontend repo
git clone <frontend-repository-url>
cd full-stack-starter-frontend

# Install dependencies
npm install

# Create a .env.local file
echo "API_URL=http://localhost:8000/api/v1" > .env.local

# Start the development server
npm run dev
```

Then visit [http://localhost:3000](http://localhost:3000) to see your full-stack app in action!

## 🔗 Connecting to Your Frontend

### 🌟 CORS is Already Set Up!

The API is already configured to accept requests from your frontend. For a complete frontend implementation that works with this backend, check out our [Next.js Frontend Companion](https://github.com/Bradd3rs/full-stack-starter-backend).

```python
# It's already done in app/main.py!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL here
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

### 🔄 Fetching Data from Next.js

Here's a quick example of how to fetch data from your Next.js app:

```typescript
// In your Next.js component
const fetchTodos = async () => {
  const response = await fetch('http://localhost:8000/api/v1/todos')
  const data = await response.json()
  return data
}
```

That's it! No complex setup, no authentication hoops (unless you want them).

## 📁 Project Structure

```
fastApi-example/
├── app/                     # Where the magic happens
│   ├── api/                 # API endpoints
│   ├── core/                # Core configuration
│   ├── crud/                # Database operations
│   ├── db/                  # Database connection
│   ├── models/              # Database models
│   ├── schemas/             # Data validation
│   └── main.py              # The app entry point
├── .env                     # Environment variables
├── docker-compose.yml       # Docker configuration
├── Dockerfile               # More Docker stuff
├── requirements.txt         # Python dependencies
└── README.md                # You are here! 👋
```

## 🚀 Ready to Build Something Awesome?

This backend is designed to get out of your way so you can focus on building your amazing frontend. No complex setup, no unnecessary features - just a solid, reliable API that works.

Happy coding! 🎉
