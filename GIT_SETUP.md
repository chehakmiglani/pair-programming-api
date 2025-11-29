# Initialize Git Repository

This guide helps you set up a Git repository for the Pair Programming prototype.

## Prerequisites
- Git installed ([git-scm.com](https://git-scm.com/))
- GitHub account (optional, but recommended for hosting)

## Steps

### 1. Initialize Git Repository
```powershell
cd c:\Users\Dell\Tredence
git init
```

### 2. Add All Files
```powershell
git add .
```

### 3. Make Initial Commit
```powershell
git commit -m "Initial commit: Pair Programming prototype with FastAPI, WebSockets, and PostgreSQL"
```

### 4. (Optional) Add Remote Repository

If you have a GitHub repository ready:

```powershell
git remote add origin https://github.com/your-username/pair-programming.git
git branch -M main
git push -u origin main
```

Replace `your-username` with your GitHub username and repo name.

## What's Tracked

The `.gitignore` file automatically excludes:
- `__pycache__/` – Python cache files
- `*.pyc` – Compiled Python
- `venv/` – Virtual environment
- `.env` – Local environment variables
- `.idea/`, `.vscode/` – IDE files
- `*.log` – Log files

## Typical Workflow

```powershell
# After making changes
git add .
git commit -m "Describe what changed"
git push origin main
```

## Useful Git Commands

```powershell
# Check status
git status

# View commit history
git log --oneline

# See changes before commit
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Revert to last commit (discard changes)
git reset --hard HEAD
```

## Repository Structure for Submission

When submitting, ensure these are present:
- ✅ `backend/` folder with all source code
- ✅ `backend/README.md` with setup instructions
- ✅ `requirements.txt` with dependencies
- ✅ `.gitignore` excluding unnecessary files
- ✅ Commit history showing development progress
- ✅ Clear commit messages

---

Good luck with your pair programming platform! 🚀
