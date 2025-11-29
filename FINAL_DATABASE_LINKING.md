# 🔗 FINAL STEP: Link PostgreSQL to pair-programming-api

## Current Status
✅ PostgreSQL is **ACTIVE** and running
✅ All database variables are set up
❌ pair-programming-api doesn't have access to DATABASE_URL yet

## What You Need to Do (2 Steps)

### Step 1: Go to pair-programming-api Service
1. In Railway Dashboard, find your project
2. Click on **pair-programming-api** service (the FastAPI app)
3. Click the **Variables** tab

### Step 2: Add PostgreSQL Connection Variable
In the Variables tab, you should see a section to add variables.

**Option A: Manual Variable Addition** (Recommended)
1. Click **+ New Variable** button
2. In the "Key" field, type: `DATABASE_URL`
3. In the "Value" field, copy and paste:
   ```
   postgresql+asyncpg://postgres:PASSWORD@postgres.railway.internal:5432/railway
   ```
   
   **IMPORTANT:** Replace `PASSWORD` with the actual password from:
   - Go back to **Postgres** service
   - Click **Variables** tab
   - Find **POSTGRES_PASSWORD** variable
   - Copy the value (the masked one, click to reveal)
   - Paste it in place of PASSWORD

   **OR** Use the full connection string from Postgres:
   - Go to **Postgres** service → **Variables** tab
   - Find **DATABASE_URL** variable
   - Copy its complete value
   - Paste into pair-programming-api's DATABASE_URL variable

4. Click **Save** or **Add Variable**

**Option B: Link via Postgres Service** (If Available)
1. In **Postgres** service → Look for "Link this database" button
2. Click it
3. Select **pair-programming-api** service
4. Railway will auto-populate DATABASE_URL ✅

---

## Verify the Connection

After adding DATABASE_URL:

1. Go to **pair-programming-api** service
2. Click **Deployments** tab
3. Find the latest deployment (should be red/failed)
4. Click **Redeploy** button
5. Select **Redeploy from latest commit**
6. Wait for build (~2-3 minutes)

**Expected Success:**
```
🚀 Starting Pair Programming API...
✅ All routers included successfully
✅ Static files mounted from /app/app/static
✅ Application startup complete!
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)

(No "Connection refused" errors!)
```

---

## Then Test

Once deployment shows ✅ **Active**:

1. Visit your live URL: `https://pair-programming-api-production.up.railway.app`
2. You should see the Pair Programming UI load ✨
3. Try creating a room
4. Open it in another tab and test real-time sync

---

## If You Get Stuck

The DATABASE_URL format should be:
```
postgresql+asyncpg://postgres:[PASSWORD]@postgres.railway.internal:5432/railway
```

Where:
- `postgres` = username (default)
- `[PASSWORD]` = the POSTGRES_PASSWORD from Postgres service Variables
- `postgres.railway.internal` = private Railway network hostname
- `5432` = PostgreSQL port
- `railway` = database name

---

## Summary of What's Ready

✅ **Code:** All on GitHub and deployed to Railway
✅ **App Startup:** Working, listens on port 8080
✅ **Database:** PostgreSQL running and ready
✅ **Only Missing:** DATABASE_URL environment variable linked to app

**→ 2 minutes to complete linking → Everything works! 🚀**

