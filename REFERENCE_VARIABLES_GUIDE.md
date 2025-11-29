# 🔗 Link PostgreSQL Using Reference Variables (Railway Method)

Based on Railway's documentation, here's the exact way to link services using Reference Variables.

## What You Need to Do

### Step 1: Go to pair-programming-api Service Variables
1. Click on **pair-programming-api** service
2. Click **Variables** tab
3. You should see a form to add variables

### Step 2: Add Reference Variables (One at a Time)

For each of these variables, click **"+ New Variable"** and add:

#### Variable 1: PGUSER
- **Name:** `PGUSER`
- **Value:** `${{ postgres.PGUSER }}`

#### Variable 2: PGPASSWORD
- **Name:** `PGPASSWORD`
- **Value:** `${{ postgres.PGPASSWORD }}`

#### Variable 3: PGHOST
- **Name:** `PGHOST`
- **Value:** `${{ postgres.PGHOST }}`

#### Variable 4: PGPORT
- **Name:** `PGPORT`
- **Value:** `${{ postgres.PGPORT }}`

#### Variable 5: PGDATABASE
- **Name:** `PGDATABASE`
- **Value:** `${{ postgres.PGDATABASE }}`

#### Variable 6 (Optional): DATABASE_URL
- **Name:** `DATABASE_URL`
- **Value:** `${{ postgres.DATABASE_URL }}`

---

## How to Add Them

For each variable:
1. Click **"+ New Variable"** button
2. Type the variable **Name** (e.g., `PGUSER`)
3. Click in the **Value** field
4. Type: `${{ postgres.VARIABLE_NAME }}`
5. An autocomplete dropdown might appear - select the postgres service variable
6. Click **Save** or the checkmark button
7. Repeat for the next variable

---

## After Adding All Variables

Once you've added all 6 reference variables:

1. You should see them listed in the Variables tab
2. The values will show as `${{ postgres.XXX }}`
3. This is normal - Railway will resolve them at runtime
4. You'll see a button to **Review** or **Deploy** the changes
5. Click the deploy/review button to apply the changes

---

## Then Redeploy Your App

1. Go to **Deployments** tab
2. Click the **...** (three dots) on the latest Active deployment
3. Click **Redeploy**
4. Wait for the build to complete (~2 minutes)

**Check logs for:**
```
✅ Constructed DATABASE_URL with password
🔌 Database connection configured
💡 Database initialization deferred to first use
✅ Application startup complete!
INFO:     Uvicorn running on http://0.0.0.0:8080
```

---

## Test Your App

Once deployed:
1. Visit: `https://pair-programming-api-production.up.railway.app`
2. You should see the Pair Programming UI
3. Click **Create Room**
4. Share the link and test in multiple tabs
5. Type code in one tab, watch it sync in real-time ✨

---

## Why This Works

- `${{ postgres.PGUSER }}` references the PGUSER variable from the postgres service
- Railway automatically substitutes these at runtime
- Your app gets all the PostgreSQL connection details it needs
- No manual copying/pasting of secrets required

---

## If Autocomplete Shows Up

When you're typing the value field, Railway might show:
- A dropdown with suggestions
- Just select **postgres.PGUSER** (or whatever variable you're referencing)
- The syntax will be filled in automatically

---

**This is the proper Railway way to connect services!** 🚀

