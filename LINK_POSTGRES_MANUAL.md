# 🔧 MANUAL POSTGRES LINKING ON RAILWAY

The PostgreSQL password is not being passed to the app service. This means they need to be explicitly linked.

## How to Link PostgreSQL to pair-programming-api

### Step 1: Go to Postgres Service Settings
1. Open your Railway project: **zoological-forgiveness**
2. Click on **postgres** service
3. Click the **Settings** tab (scroll down if needed)
4. Look for section: **"Links"** or **"Connect this database to a service"**

### Step 2: Link to pair-programming-api
1. Find button: **"Link"** or **"+ Add Link"** or **"Connect database"**
2. Click it
3. Select: **pair-programming-api** from the dropdown
4. Railway will automatically set all required variables

### Alternative: If No Link Button Exists
1. Go to **pair-programming-api** service
2. Click **Variables** tab
3. You should see an option to **"+ Add Service Reference"** or **"Link Database"**
4. Click it
5. Select: **postgres** service
6. Railway will auto-populate all required variables

---

## After Linking

Once linked, Railway will automatically set:
- ✅ PGUSER
- ✅ PGPASSWORD  
- ✅ PGHOST
- ✅ PGPORT
- ✅ PGDATABASE
- ✅ DATABASE_URL (optional)

---

## Then Redeploy

1. Go to **pair-programming-api** service
2. Click **Deployments** tab
3. Click the **...** (three dots) on the Active deployment
4. Click **Redeploy**
5. Wait for build (~2 minutes)

**Expected logs should show:**
```
📝 PG Environment: user=postgres, host=postgres.railway.internal, port=5432, db=railway
✅ Constructed DATABASE_URL with password
🔌 Database connection configured
💡 Database initialization deferred to first use
✅ Application startup complete!
INFO:     Uvicorn running on http://0.0.0.0:8080
```

---

## Test After Redeploy

1. Visit: `https://pair-programming-api-production.up.railway.app`
2. You should see the Pair Programming UI ✅
3. Click **Create Room**
4. This will initialize the database for the first time
5. You'll get a room ID and link
6. Open it in another tab and test real-time sync!

---

## If Still Not Working

Make sure:
- ✅ PostgreSQL service shows **✅ Active** status (not red)
- ✅ After linking, the Variables section shows database variables
- ✅ You redeployed AFTER linking
- ✅ Check deploy logs for any remaining errors

---

**The linking is a one-time setup - after that, everything works automatically!** 🚀

