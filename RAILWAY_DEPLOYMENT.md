# Railway Deployment Guide

Your Pair Programming Prototype is ready to deploy to Railway!

## 🚀 Step-by-Step Deployment (5 Minutes)

### Step 1: Create GitHub Repository

1. Go to **https://github.com/new**
2. Create a new repository (e.g., `pair-programming-api`)
3. Do NOT initialize with README (we already have files)
4. Click **"Create repository"**
5. Copy the HTTPS URL (e.g., `https://github.com/YOUR-USERNAME/pair-programming-api.git`)

### Step 2: Push to GitHub

```powershell
cd c:\Users\Dell\Tredence

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR-USERNAME/pair-programming-api.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 3: Deploy to Railway

1. Go to **https://railway.app/dashboard**
2. Click **"New Project"**
3. Select **"Deploy from GitHub"**
4. Authorize Railway to access your GitHub
5. Select your `pair-programming-api` repository
6. Click **"Deploy"**
7. Wait 1-2 minutes for deployment

### Step 4: Add PostgreSQL Service

1. In Railway dashboard, click **"+ Add Service"**
2. Search for **"PostgreSQL"**
3. Click to add PostgreSQL
4. Railway will automatically set `DATABASE_URL` environment variable
5. Your app will use this automatically

### Step 5: Get Your Live URL

1. In Railway dashboard, find your project
2. Click on the FastAPI service
3. Look for **"Domains"** section
4. You'll see a URL like: `https://pair-programming-production.up.railway.app`

---

## ✅ Verify Deployment Works

Once Railway deploys:

1. **Visit your live URL:**
   ```
   https://[your-project].up.railway.app
   ```

2. **Test the endpoints:**
   ```
   GET    https://[your-project].up.railway.app/
   GET    https://[your-project].up.railway.app/docs (Swagger)
   POST   https://[your-project].up.railway.app/rooms/
   POST   https://[your-project].up.railway.app/autocomplete/
   WS     wss://[your-project].up.railway.app/ws/{room_id}
   ```

3. **Test real-time sync:**
   - Open the URL in two browser tabs
   - Create a room
   - Join in the second tab
   - Type code in one tab
   - Watch it sync to the other tab

---

## 🔧 Environment Variables

Railway automatically handles these:

| Variable | Set By | Value |
|----------|--------|-------|
| DATABASE_URL | PostgreSQL Service | Auto-generated |
| PORT | Railway | Auto-set (8080) |
| HOST | Procfile | 0.0.0.0 |

You don't need to manually configure anything!

---

## 📊 Railway Dashboard Features

Once deployed, you can:

✅ **View Logs** – See real-time application logs  
✅ **Monitor Metrics** – CPU, memory, requests  
✅ **Manage Secrets** – Add environment variables  
✅ **Rollback Deployments** – Go back to previous versions  
✅ **View Domains** – Get your live URL  
✅ **Manage Database** – PostgreSQL admin  

---

## 🎯 Your Submission Information

After successful deployment, you'll have:

```
GitHub Repository:
https://github.com/YOUR-USERNAME/pair-programming-api

Live Demo (Railway):
https://[your-project].up.railway.app

Key Files:
- backend/app/main.py (FastAPI entry point)
- backend/app/routers/websocket.py (Real-time sync)
- backend/app/static/index.html (Web UI)
- Procfile (Railway configuration)

Features:
✅ FastAPI + WebSockets
✅ PostgreSQL persistence
✅ Real-time code sync
✅ Mocked autocomplete
✅ Production-ready
```

---

## 📝 Troubleshooting Railway Deployment

### "Build failed"
- Check Railway logs for errors
- Ensure `requirements.txt` is correct
- Verify `Procfile` syntax

### "PostgreSQL not connecting"
- Railway auto-sets `DATABASE_URL`
- Your app code reads it from `os.getenv("DATABASE_URL")`
- Check app logs: `await create_db_and_tables()` should succeed

### "Port binding error"
- Procfile uses `$PORT` (Railway sets this)
- Ensure `--port $PORT` in your Procfile

### "App keeps restarting"
- Check Railway logs
- Verify all dependencies in `requirements.txt`
- Look for runtime errors in logs

---

## 🚀 Next Steps

1. ✅ Create GitHub repository
2. ✅ Push code with `git push`
3. ✅ Create Railway project
4. ✅ Add PostgreSQL service
5. ✅ Get live URL
6. ✅ Test real-time sync
7. ✅ Share submission link

---

## 📱 Share Your Live Demo

Once deployed, share this with evaluators:

```
🎉 Pair Programming Prototype

GitHub: https://github.com/YOUR-USERNAME/pair-programming-api
Live Demo: https://[your-project].up.railway.app

Features:
- Real-time code sync (WebSockets)
- PostgreSQL persistence
- Mocked AI autocomplete
- Multi-user support
- Professional web UI
- Production-ready FastAPI backend

Try it:
1. Visit the live demo link
2. Click "Create Room"
3. Open in another tab and join same room
4. Type code and watch it sync instantly!
```

---

## 💡 Railway Pro Tips

1. **Custom Domain** – Add your own domain (paid feature)
2. **Environment Variables** – Manage secrets in Railway dashboard
3. **Database Backups** – Automatic PostgreSQL backups
4. **Logs** – View all application logs in real-time
5. **Deployments** – One-click rollback to previous versions

---

**Your live demo will be ready in 5 minutes! 🚀**

Next: Push to GitHub, deploy to Railway, share your link!
