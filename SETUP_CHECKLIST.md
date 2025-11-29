# Pair Programming Prototype - Setup & Verification Checklist

## ✅ Project Structure Verification

All files have been created in `c:\Users\Dell\Tredence\`:

### Root Level
- ✅ `backend/` – Main backend application
- ✅ `docker-compose.yml` – PostgreSQL container config
- ✅ `run.bat` – Windows batch startup script
- ✅ `run.ps1` – PowerShell startup script
- ✅ `QUICKSTART.md` – Quick setup guide
- ✅ `SETUP_CHECKLIST.md` – This file

### Backend Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI application
│   ├── db.py                        # Database configuration
│   ├── models.py                    # SQLModel definitions
│   ├── schemas.py                   # Pydantic schemas
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── rooms.py                # POST /rooms
│   │   ├── autocomplete.py         # POST /autocomplete
│   │   └── websocket.py            # WS /ws/{room_id}
│   ├── services/
│   │   ├── __init__.py
│   │   └── room_service.py         # Database operations
│   └── static/
│       └── index.html              # Web UI demo
├── requirements.txt                 # Python dependencies
├── .env.example                    # Environment config template
├── .gitignore                      # Git ignore rules
└── README.md                       # Full documentation
```

---

## 🚀 Installation & Verification Steps

### Step 1: Verify Python Installation
```powershell
python --version
# Should show Python 3.9 or higher
```

### Step 2: Create Virtual Environment
```powershell
cd c:\Users\Dell\Tredence
python -m venv venv
```

### Step 3: Activate Virtual Environment
**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
.\venv\Scripts\activate.bat
```

### Step 4: Install Dependencies
```powershell
pip install -r backend/requirements.txt
```

**Expected output:** All packages installed successfully without errors

### Step 5: Verify Module Imports
```powershell
cd backend
python -c "from app.models import Room; print('✓ Models OK')"
python -c "from app.schemas import CreateRoomResponse; print('✓ Schemas OK')"
python -c "from app.services.room_service import create_room; print('✓ Services OK')"
```

### Step 6: Start PostgreSQL
**Option A: Docker**
```powershell
docker-compose up -d
# Wait 10 seconds for Postgres to start
```

**Option B: Local PostgreSQL**
```powershell
# Ensure PostgreSQL service is running
# Windows Services → PostgreSQL
```

### Step 7: Verify Database Connection
```powershell
# From backend folder
python -c "
import asyncio
from app.db import create_db_and_tables
asyncio.run(create_db_and_tables())
print('✓ Database tables created')
"
```

### Step 8: Start the Backend Server
```powershell
# From backend folder
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Creating database tables...
INFO:     Database tables created.
INFO:     Application startup complete
```

### Step 9: Test API Endpoints

**In a new terminal:**

**Test Create Room:**
```powershell
curl -X POST http://localhost:8000/rooms/
# Should return: {"roomId": "<UUID>"}
```

**Test Autocomplete:**
```powershell
curl -X POST http://localhost:8000/autocomplete/ `
  -H "Content-Type: application/json" `
  -d '{
    "code": "def ",
    "cursorPosition": 4,
    "language": "python"
  }'
# Should return a suggestion
```

### Step 10: Test Web UI
1. Open **http://localhost:8000/** in your browser
2. You should see the Pair Programming editor interface
3. Click "Create Room" → a room ID should appear
4. Open the URL in another tab with the same room ID
5. Type code in one tab and see it sync to the other

---

## 🧪 Integration Testing Checklist

- [ ] Backend starts without errors
- [ ] Database tables are created
- [ ] POST /rooms/ returns a valid UUID
- [ ] POST /autocomplete/ returns a suggestion string
- [ ] Web UI loads at http://localhost:8000/
- [ ] Can create a room from the UI
- [ ] Can join a room with the same ID
- [ ] Typing in one editor shows in the other (real-time)
- [ ] Autocomplete suggestion appears after 600ms idle
- [ ] Can accept an autocomplete suggestion
- [ ] Code persists when refreshing the page

---

## 📊 Expected File Sizes

| File | Size (approx) |
|------|---------------|
| app/main.py | 1.5 KB |
| app/db.py | 700 B |
| app/models.py | 300 B |
| app/schemas.py | 300 B |
| app/services/room_service.py | 1.1 KB |
| app/routers/rooms.py | 400 B |
| app/routers/autocomplete.py | 1.8 KB |
| app/routers/websocket.py | 2.4 KB |
| app/static/index.html | 14 KB |
| requirements.txt | 100 B |
| README.md | 12+ KB |

---

## 🔧 Quick Troubleshooting

### "ModuleNotFoundError: No module named 'fastapi'"
→ Run: `pip install -r backend/requirements.txt`

### "psycopg2 connection error"
→ Ensure PostgreSQL is running and DATABASE_URL is correct

### "Address already in use"
→ Change port: `uvicorn app.main:app --port 8001`

### "WebSocket connection failed"
→ Check browser console; ensure port 8000 is open in firewall

### "No tables created"
→ Check database credentials in `.env`; manually run DB init

---

## 📝 Environment Configuration

Copy `backend/.env.example` to `backend/.env`:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/pairprog
HOST=0.0.0.0
PORT=8000
DEBUG=1
```

**Adjust for your local setup:**
- Change `postgres:postgres` if you use different credentials
- Change `localhost:5432` if Postgres is on different host/port
- Keep `pairprog` as database name (or create it first)

---

## 🎯 Success Criteria

### Backend is Running ✓
- [ ] Terminal shows "Application startup complete"
- [ ] http://localhost:8000/docs loads Swagger UI
- [ ] API endpoints respond to requests

### Database is Connected ✓
- [ ] "Database tables created" message appears on startup
- [ ] CREATE ROOM returns a valid UUID
- [ ] Room data persists across requests

### Real-Time Sync Works ✓
- [ ] Two browser tabs can join the same room
- [ ] Typing in one tab appears in the other instantly
- [ ] Code persists after page refresh

### Frontend Works ✓
- [ ] Web UI is responsive and styled
- [ ] Autocomplete appears after 600ms idle
- [ ] Language selector works
- [ ] Status shows "Connected"

---

## 📞 Support & Next Steps

### If Something Breaks
1. Check error messages in the terminal
2. Review `backend/README.md` troubleshooting section
3. Verify dependencies: `pip list`
4. Clear Python cache: `rmdir -r backend\__pycache__`
5. Reinstall: `pip install --upgrade -r backend/requirements.txt`

### To Customize
1. Modify autocomplete rules in `app/routers/autocomplete.py`
2. Update UI styling in `app/static/index.html`
3. Add new endpoints in new `app/routers/` files
4. Extend database schema in `app/models.py`

### To Deploy
1. Build Docker image: `docker build -t pairprog-backend .`
2. Deploy to cloud (AWS, Heroku, Railway, etc.)
3. Update CORS if frontend on different origin
4. Use production database (managed Postgres)
5. Set up CI/CD pipeline

---

## 🎉 Ready to Launch!

Once all checks pass, your full-stack pair programming prototype is ready.

**Run the startup script:**
```powershell
.\run.bat
# or
.\run.ps1
```

Then visit **http://localhost:8000/** and start collaborating!

---

**Created:** November 28, 2025  
**Framework:** FastAPI + WebSockets + SQLModel + PostgreSQL  
**Status:** ✅ Complete & Ready to Run
