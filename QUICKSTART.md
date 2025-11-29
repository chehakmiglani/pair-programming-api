# 🚀 Pair Programming Prototype - Quick Setup Guide

## What's Included

A complete **FastAPI backend** with real-time WebSocket collaboration, Postgres persistence, and mocked AI autocomplete.

```
c:\Users\Dell\Tredence\
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── models.py               # SQLModel Room model
│   │   ├── db.py                   # Async database
│   │   ├── schemas.py              # Pydantic schemas
│   │   ├── services/room_service.py  # CRUD logic
│   │   ├── routers/
│   │   │   ├── rooms.py            # POST /rooms
│   │   │   ├── autocomplete.py     # POST /autocomplete
│   │   │   └── websocket.py        # WS /ws/{room_id}
│   │   └── static/index.html       # Web UI (vanilla JS)
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example                # Config template
│   ├── .gitignore
│   └── README.md                   # Full documentation
├── docker-compose.yml              # PostgreSQL container
├── run.bat                         # Windows startup script
└── run.ps1                         # PowerShell startup script
```

---

## ⚡ Quick Start (3 Minutes)

### Step 1: Start PostgreSQL

**Option A: Docker (Recommended)**
```powershell
docker-compose up -d
```

**Option B: Local PostgreSQL**
```powershell
# Ensure PostgreSQL is running
psql -U postgres -c "CREATE DATABASE pairprog;"
```

### Step 2: Run the Backend

**Windows (Batch):**
```powershell
.\run.bat
```

**Windows (PowerShell):**
```powershell
.\run.ps1
```

**Manual (Any OS):**
```powershell
pip install -r backend/requirements.txt
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 3: Open the App

1. Open **http://localhost:8000/** in your browser
2. Click **"Create Room"** → Copy the Room ID
3. Open in another tab/window and click **"Join Room"** with the same ID
4. Start typing and watch real-time sync!

---

## 📡 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Web UI (vanilla HTML/JS) |
| `/docs` | GET | Interactive API documentation |
| `/rooms/` | POST | Create a new room |
| `/autocomplete/` | POST | Get mocked code suggestion |
| `/ws/{room_id}` | WS | Real-time code sync |

### Example: Create a Room
```bash
curl -X POST http://localhost:8000/rooms/
# Response: {"roomId": "550e8400-..."}
```

### Example: Get Autocomplete
```bash
curl -X POST http://localhost:8000/autocomplete/ \
  -H "Content-Type: application/json" \
  -d '{"code": "def ", "cursorPosition": 4, "language": "python"}'
# Response: {"suggestion": " my_function(args):\n    pass"}
```

---

## ✨ Features Implemented

✅ **Room Creation** – Generate unique room IDs  
✅ **Real-Time Sync** – WebSocket broadcasts to all users  
✅ **Persistent Storage** – PostgreSQL stores code  
✅ **Mocked Autocomplete** – Rule-based suggestions  
✅ **Web Demo UI** – No build tools needed  
✅ **API Documentation** – Swagger UI at `/docs`  
✅ **Last-Write-Wins** – Simple conflict resolution  
✅ **Async/Await** – Scalable database operations  

---

## 🧪 Testing Without React

The included **static/index.html** is a complete demo with:
- Room creation & joining
- Real-time code editor sync
- Read-only partner view
- Mocked autocomplete with 600ms debounce
- Language selector (Python, JavaScript, Java, C++)

**No frontend build required!** Everything runs in vanilla JS.

---

## 📊 Database Schema

Automatically created at startup. Single table:

```sql
CREATE TABLE room (
    id UUID PRIMARY KEY,
    code TEXT DEFAULT '',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔍 Key Technologies

- **FastAPI** – Modern, fast web framework
- **WebSockets** – Real-time bidirectional communication
- **SQLModel** – SQL + Pydantic integration
- **AsyncPG** – Async PostgreSQL driver
- **Uvicorn** – ASGI server

---

## 📝 Code Structure Highlights

### Clean Architecture
```
routers/           → HTTP endpoints (REST + WebSocket)
services/          → Business logic (CRUD, sync)
models.py          → Data schema (SQLModel)
db.py              → Database connection
schemas.py         → Request/Response validation
main.py            → FastAPI app setup
```

### Async-First Design
- All DB operations use `AsyncSession`
- Non-blocking I/O for handling multiple connections
- Efficient resource utilization

### Real-Time Sync
1. User A sends code update via WebSocket
2. Backend persists to PostgreSQL
3. Backend broadcasts to all other clients in the room
4. User B receives update instantly

---

## 🎯 Architecture Decision Notes

1. **Single Room Table** – Minimal for MVP; could add users, permissions later
2. **In-Memory Connections** – Fast, suitable for single server; scale with Redis
3. **Last-Write-Wins** – Simple; upgrade to CRDT/OT for complex merges
4. **Mocked Autocomplete** – Rule-based; integrate real AI later
5. **Vanilla JS Frontend** – No build tools; React version is optional

---

## 🚀 What's Next (Future Enhancements)

1. **CRDT/OT Sync** – Intelligent merge for simultaneous edits
2. **User Presence** – Show cursors and usernames
3. **Syntax Highlighting** – Monaco Editor or CodeMirror
4. **Real AI Autocomplete** – OpenAI or Hugging Face
5. **Authentication** – JWT login system
6. **Version History** – Git-like snapshots
7. **Horizontal Scaling** – Redis Pub/Sub + multiple servers
8. **Unit Tests** – Pytest for services
9. **Docker** – Containerized deployment
10. **TypeScript Frontend** – React + Redux (optional)

---

## ⚠️ Troubleshooting

### PostgreSQL Won't Start
```powershell
# Check Docker
docker ps

# Or check local PostgreSQL
psql -U postgres
```

### Port 8000 Already in Use
```powershell
# Kill process on port 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use different port
uvicorn app.main:app --port 8001
```

### Database Connection Error
- Verify `.env` DATABASE_URL matches your Postgres config
- Ensure Postgres is running and database exists
- Check user/password in `.env`

---

## 📚 Documentation

See **`backend/README.md`** for:
- Detailed API documentation
- WebSocket message format
- Deployment instructions
- Testing with Postman/cURL
- Architecture deep-dive

---

## 🎉 Ready to Go!

Run one of the startup scripts and start pair programming! 

**Questions?** Check `backend/README.md` for comprehensive docs.

---

Happy coding! 💻✨
