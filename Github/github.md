# Git & GitHub — End-to-End Notes

## 1. What is Version Control?
Version control is a system that tracks changes to your code over time, so you can:
- Go back to any previous version
- See who changed what and when
- Work with multiple people on the same project without overwriting each other's work

## 2. Git vs GitHub

| | Git | GitHub |
|---|---|---|
| What it is | Version control **tool** (software) | **Hosting platform** for Git repos |
| Where it runs | Locally on your machine | On the cloud (remote) |
| Repo type | Local repository | Remote repository |
| Alternatives | — | GitLab, Bitbucket |

**Repo (Repository)** → the place where you store your code along with its full history.

## 3. The 3 Areas of Git (Very Important)

```
Working Directory  →  Staging Area  →  Local Repo  →  Remote Repo (GitHub)
   (your files)       (git add)       (git commit)     (git push)
```

1. **Working Directory** — where you create/edit files
2. **Staging Area** — files marked to be saved (tracked) using `git add`
3. **Local Repository** — snapshots saved permanently using `git commit`
4. **Remote Repository** — code uploaded to GitHub using `git push`

## 4. First-Time Setup (only once per machine)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list          # verify configuration
```

## 5. Core Workflow (Local Repo)

### Step 1 — Create a local repo
```bash
git init
```
Creates an empty repository (a hidden `.git` folder) in your project directory.

### Step 2 — Check the status of files
```bash
git status
```
Shows which files are **untracked**, **modified**, or **staged**.

### Step 3 — Start tracking files (Staging)
```bash
git add <filename>     # track a single file
git add .              # track ALL files in the current directory
```

### Step 4 — Save (Commit)
```bash
git commit -m "your message"
```
- `-m` is the flag to specify a commit message
- A commit = a saved snapshot of your code at that point in time
- Write meaningful messages: `"added login feature"` not `"changes"`

### Step 5 — View commit history
```bash
git log                # full history
git log --oneline      # compact one-line view
```

## 6. Connecting Local ↔ Remote (GitHub)

### Link your local repo to GitHub
```bash
git remote add origin <repo-url>
git remote -v          # verify the link
```
- `origin` = the default nickname for your remote repo URL

### Push — send local commits to GitHub
```bash
git push origin main             # push to main branch
git push -u origin main          # -u sets upstream, later just 'git push'
```

### Pull — get changes FROM remote TO local
```bash
git pull origin main
```
Use this when the remote has changes your local doesn't (e.g., a teammate pushed code).

### Clone — copy an entire remote repo to local
```bash
git clone <repo-url>
```
Downloads the full project + history. No need for `git init` after cloning.

> **Pull vs Clone:**
> - `clone` → first time, copies the whole repo
> - `pull` → after cloning, fetches only the new changes

## 7. Branching (Working on Features Safely)

A branch is a separate line of development — you experiment without touching `main`.

```bash
git branch                     # list branches
git branch <branch-name>       # create a branch
git checkout <branch-name>     # switch to a branch
git checkout -b <branch-name>  # create + switch in one command
git merge <branch-name>        # merge that branch into current branch
git branch -d <branch-name>    # delete a branch
```

**Typical flow:**
```bash
git checkout -b feature-login   # create feature branch
# ... make changes, add, commit ...
git checkout main               # go back to main
git merge feature-login         # merge feature into main
git push origin main            # push to GitHub
```

## 8. Undoing Things

```bash
git restore <file>              # discard changes in working directory
git restore --staged <file>     # unstage a file (undo git add)
git commit --amend -m "msg"     # fix the last commit message
git reset --soft HEAD~1         # undo last commit, keep changes staged
git reset --hard HEAD~1         # undo last commit, DELETE changes (careful!)
git revert <commit-id>          # safely undo a commit by creating a new one
```

## 9. Useful Everyday Commands

```bash
git diff                # see unstaged changes
git diff --staged       # see staged changes
git stash               # temporarily save uncommitted changes
git stash pop           # bring stashed changes back
git fetch               # download remote changes WITHOUT merging
rm -rf .git             # remove git tracking from a folder (careful!)
```

## 10. .gitignore

A file listing things Git should NOT track (secrets, dependencies, junk files):

```
node_modules/
.env
__pycache__/
*.log
.DS_Store
```

## 11. GitHub Collaboration Concepts

- **Fork** — your own copy of someone else's repo on GitHub
- **Pull Request (PR)** — propose your changes to be merged into another branch/repo; team reviews before merging
- **Issues** — track bugs, tasks, and feature requests
- **README.md** — the front page/documentation of your repo

**Open-source contribution flow:**
Fork → Clone → Create branch → Commit changes → Push → Open Pull Request

## 12. Quick Reference — Daily Workflow

```bash
git pull origin main          # 1. get latest code
git checkout -b my-feature    # 2. create a branch
# ... edit files ...
git status                    # 3. check what changed
git add .                     # 4. stage changes
git commit -m "message"       # 5. save snapshot
git push origin my-feature    # 6. upload to GitHub
# 7. open a Pull Request on GitHub
```

## 13. One-Line Summary of Your Core Commands

| Command | Purpose |
|---|---|
| `git init` | Create an empty local repo |
| `git status` | Check state of each file |
| `git add <file>` / `git add .` | Start tracking / stage files |
| `git commit -m "msg"` | Save staged files locally |
| `git remote add origin <url>` | Link local repo with remote |
| `git push` | Send local commits to remote |
| `git pull` | Bring remote changes to local |
| `git clone <url>` | Copy remote repo to local |