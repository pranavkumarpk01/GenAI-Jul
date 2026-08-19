# API Setup Guide

Comprehensive, step-by-step notes to get the Student CRUD API (FastAPI + MongoDB) running on your machine.

## 1. Install Docker

Docker lets you run software (like MongoDB) inside an isolated **container**, without installing it directly on your system.

- **Windows/Mac:** download and install **Docker Desktop** from https://www.docker.com/products/docker-desktop/. Once installed, open Docker Desktop and make sure it shows "Docker is running" before continuing.
- **Linux:** install Docker Engine using your distro's package manager, e.g. on Ubuntu:
  ```
  sudo apt-get update
  sudo apt-get install docker.io
  sudo systemctl start docker
  sudo systemctl enable docker
  ```

Verify the install worked:

```
docker --version
```

**Real-world example:** Docker is like a shipping container for software. Instead of installing MongoDB and configuring it manually (which can differ across machines and operating systems), you get a pre-packaged, identical MongoDB environment every time — on any computer that has Docker.

## 2. Pull and run MongoDB

**Pull** the MongoDB image (version 7) from Docker Hub — this downloads the MongoDB software packaged as a container image:

```
docker pull mongo:7
```

**Run** it as a container:

```
docker run -d -p 27017:27017 mongo:7
```

Breaking this command down:

| Part | Meaning |
|---|---|
| `docker run` | Start a new container from an image |
| `-d` | Detached mode — runs in the background, so your terminal stays free |
| `-p 27017:27017` | Port mapping — maps port `27017` on your machine to port `27017` inside the container. `27017` is MongoDB's default port |
| `mongo:7` | Which image to use — MongoDB, version 7 |

Once this runs, MongoDB is live at `mongodb://localhost:27017/` — which is exactly the address `app.py` connects to:

```python
client = MongoClient("mongodb://localhost:27017/")
```

**Check it's running:**

```
docker ps
```

You should see a row with `mongo:7` and status `Up`.

**Optional — name your container** so it's easier to manage later (stop/start/remove by name):

```
docker run --name my-mongo -d -p 27017:27017 mongo:7
```

**Common Docker commands you'll need:**

| Command | Purpose |
|---|---|
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped ones) |
| `docker stop <container>` | Stop a running container |
| `docker start <container>` | Start a previously stopped container |
| `docker rm <container>` | Remove a stopped container |

## 3. Create a virtual environment and install dependencies

A **virtual environment (venv)** is an isolated space for this project's Python packages, so they don't clash with packages from other projects on your system.

**Create it:**

```
python -m venv .venv
```

**Get into it (activate it):**

- macOS/Linux:
  ```
  source .venv/bin/activate
  ```
- Windows:
  ```
  .venv\Scripts\activate
  ```

Once activated, your terminal prompt usually shows `(.venv)` at the start of the line — that confirms you're inside the virtual environment, and any `pip install` from here only affects this project.

**Install all required libraries:**

Every Python project should have a `requirements.txt` listing everything it depends on. This project's file contains:

```
fastapi
uvicorn
pymongo
```

Install all of them in one shot:

```
pip install -r requirements.txt
```

You never need to run `pip install fastapi`, `pip install uvicorn`, `pip install pymongo` one at a time — the `-r requirements.txt` flag reads the file and installs everything listed inside it, in order.

**Real-world example:** a virtual environment is like giving each project its own separate toolbox, instead of one shared toolbox where tools from different projects could conflict (e.g. one project needing an old version of a library, another needing the newest).

## 4. Run the application

Start the FastAPI app with **uvicorn** — the server that actually runs it:

```
uvicorn app:app --reload
```

Breaking this down:

| Part | Meaning |
|---|---|
| First `app` | The filename `app.py` (Python drops the `.py`) |
| `:app` | The `FastAPI()` object defined inside that file — i.e. the line `app = FastAPI(...)` |
| `--reload` | Automatically restarts the server whenever you save a code change — very useful during development, but should be turned off in production |

Once running, you'll see terminal output like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

That means the API is live and listening for requests on port `8000`.

## 5. Test the API

FastAPI automatically generates an interactive docs page. With the server running, open your browser to:

```
http://127.0.0.1:8000/docs
```

From here you can try out every endpoint directly in the browser — no separate tool needed:

- `POST /students` — create a student
- `GET /students/get` — list all students
- `PUT /students/{student_id}` — update a student
- `DELETE /students/{student_id}` — delete a student

## 6. Full checklist, start to finish

1. Install Docker and confirm it's running (`docker --version`).
2. Pull the MongoDB image: `docker pull mongo:7`.
3. Run the MongoDB container: `docker run -d -p 27017:27017 mongo:7`.
4. Confirm it's up: `docker ps`.
5. Create a virtual environment: `python -m venv .venv`.
6. Activate it: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows).
7. Install dependencies: `pip install -r requirements.txt`.
8. Run the app: `uvicorn app:app --reload`.
9. Open `http://127.0.0.1:8000/docs` and test each endpoint.

## 7. Troubleshooting tips

- **"Connection refused" to MongoDB:** the container probably isn't running — check with `docker ps` and restart it if needed.
- **"Port already in use" (27017 or 8000):** something else is already using that port. Stop the conflicting process, or map to a different host port, e.g. `-p 27018:27017`, and update the connection string accordingly.
- **`ModuleNotFoundError: No module named 'fastapi'`:** your virtual environment likely isn't activated, or `pip install -r requirements.txt` wasn't run inside it.
- **Changes not reflecting:** make sure you started uvicorn with `--reload`, and that you saved the file.


To deploy api applciation

build the image -> docker build -t student-api .

run the container -> docker run -d \            
  --name student-api \
  -p 8000:8000 \
  student-api