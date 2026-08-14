# API Notes

Comprehensive notes on the Student CRUD API (`app.py`) built with **FastAPI** and **MongoDB**.

## 1. What is an API?

**API (Application Programming Interface)** is a set of rules that lets two applications talk to each other. One application (the **client**) sends a request, and another application (the **server**) processes it and sends back a response.

**Real-world example:** Think of a restaurant. You (the client) don't walk into the kitchen to cook your own food. You give your order to a waiter (the API), the waiter takes it to the kitchen (the server/database), and brings the food (response) back to you. You never need to know how the kitchen works internally — you just need to know how to order. A mobile app works the same way: it never touches a company's database directly. It sends a request to an API, the API talks to the database, and sends the result back as a response (usually in JSON).

## 2. What is FastAPI?

FastAPI is a Python **framework** used to build APIs quickly. A framework is prebuilt code that handles the repetitive, low-level work (routing requests, validating data, generating docs) so you only write the business logic.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Student CRUD Operation",
    description="Simple CRUD API using FastAPI and Mongo",
    version="1.0"
)
```

- `app` is the core object of your API — every route (endpoint) you create is attached to it.
- `title`, `description`, `version` are metadata shown on the auto-generated docs page (`/docs`).
- `HTTPException` is imported so you can later return proper error responses (e.g. "404 student not found") instead of letting the app crash silently.

**Analogy:** If Python is the language, FastAPI is like a ready-made restaurant kitchen setup — you don't build the stove and sink from scratch, you just start cooking (writing endpoints).

## 3. Libraries used in this project

A **library** is prewritten, reusable code you install instead of writing yourself.

| Library | Purpose |
|---|---|
| `fastapi` | Framework to build the API and its routes |
| `uvicorn` | Server that actually runs the FastAPI app |
| `pymongo` | Lets Python talk to a MongoDB database |

All libraries a project needs are listed in **`requirements.txt`**:

```
fastapi
uvicorn
pymongo
```

Anyone cloning the project installs them in one shot with `pip install -r requirements.txt`.

**Real-world example:** `requirements.txt` is like a grocery list. Instead of telling every new teammate "go install these 3 things one by one," you hand them the list and they install everything with one command.

## 4. Connecting to the database

```python
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["training_db"]
collection = db["students"]
```

- `client` → the connection to the MongoDB server running on your machine, on port `27017` (MongoDB's default port).
- `db` → a specific database inside that server, here `training_db`. MongoDB creates it automatically the first time you write data to it.
- `collection` → similar to a "table" in SQL; here it's called `students` and holds student documents (records). A **document** in MongoDB is basically a JSON object — e.g. `{"name": "Pranav", "age": "25"}`.
- `ObjectId` → MongoDB's special internal ID type. Every document's `_id` is stored as an `ObjectId`, not a plain string, so whenever you receive an ID as a string from a URL (like `student_id`), you must wrap it in `ObjectId(...)` before using it to query MongoDB.

MongoDB itself runs inside a **Docker container** (see `setup.md` for the exact commands).

## 5. HTTP Methods (the "verbs" of an API)

| Method | Purpose | Real-world analogy |
|---|---|---|
| `POST` | Create new data | Placing a new order |
| `GET` | Read/fetch existing data | Checking your order status |
| `PUT` | Update existing data | Changing your order before it's cooked |
| `DELETE` | Remove data | Cancelling your order |

This maps directly to **CRUD**: Create, Read, Update, Delete — the four basic operations any application performs on data.

## 6. Endpoints in this API

### Create — `POST /students`

```python
@app.post("/students")
def create_student(student: dict):
    result = collection.insert_one(student)
    return {
        "message": "student data has been created",
        "_id": str(result.inserted_id)
    }
```

- `@app.post("/students")` is a **decorator** — it tells FastAPI "run this function when a POST request hits `/students`".
- `student: dict` is the **request body** — the data the client sends, e.g. `{"name": "Pranav", "course": "AI"}`.
- `collection.insert_one(student)` saves the document into MongoDB.
- `result.inserted_id` is the auto-generated `ObjectId` MongoDB assigned to the new document. It's converted with `str()` before sending it back, because JSON responses can't contain a raw `ObjectId` — only plain text, numbers, booleans, lists, and objects.

#### `insert_one()` in detail

`insert_one()` is a built-in **pymongo** function responsible for inserting a single document into the database's collection.

- It takes one argument: a Python dictionary representing the document to store.
- MongoDB automatically stores it and returns a result object. That result object has an `inserted_id` attribute — the unique ID MongoDB generated for this new record.
- There's also `insert_many()` if you ever need to insert multiple documents at once (a list of dictionaries) — not used in this project, but good to know.

**Real-world example:** `insert_one()` is like filling out a new admission form for a student and filing it in the records room — the school automatically stamps it with a unique roll number (`_id`) so it can be found again later.

### Read — `GET /students/get`

```python
@app.get("/students/get")
def get_students():
    students = []
    for student in collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return students
```

- `collection.find()` fetches **all** documents in the collection.
- Every document's `_id` is converted to a string before returning it, for the same JSON reason as above.
- `students.append(student)` builds up the final list one document at a time.

#### `find()` in detail

`find()` is a built-in pymongo function responsible for finding (retrieving) data from the database.

- Called with no arguments — `collection.find()` — it returns **every** document in the collection.
- It doesn't return a plain list directly; it returns a **cursor** (an iterable object) that you loop over with a `for` loop, pulling one document at a time.
- You can also filter results by passing a query dictionary, e.g. `collection.find({"course": "AI"})` would return only students enrolled in AI — this project's version doesn't filter, so it returns everyone.
- There's also `find_one()`, which returns just a single matching document instead of a cursor of many — useful if you only ever expect one match (like looking up a student by ID).

**Real-world example:** `find()` is like asking the school office for "the full list of students" — the clerk pulls out the entire filing cabinet and hands you every folder, one at a time, rather than a single record.

#### `append` in detail

`append()` is a built-in Python **list** method (not MongoDB-specific) — it adds a value to the end of a list.

```python
students = []
students.append(student)   # adds one student dict to the end of the list
```

It's used here to build the `students` list one document at a time as we loop through the MongoDB cursor from `find()`. Every document is converted (its `_id` turned into a string) and then appended, so the final list is ready to be returned as clean JSON.

**Real-world example:** `append` is like adding one more name to a sign-up sheet — each new entry goes at the bottom of the same list, without disturbing the ones already written.

### Update — `PUT /students/{student_id}`

```python
@app.put("/students/{student_id}")
def update_student(student_id: str, student: dict):
    result = collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student}
    )
    return {"message": "student updated"}
```

- `{student_id}` in the URL is a **path parameter** — a value passed directly in the URL, e.g. `/students/64f1a2...`.
- `ObjectId(student_id)` converts the string from the URL back into MongoDB's internal ID format, since MongoDB stores `_id` as an `ObjectId`, not plain text.
- `{"$set": student}` only updates the fields you send — it doesn't wipe out the rest of the document. E.g. sending `{"course": "DevOps"}` updates only the `course` field, leaving `name`, `age`, etc. untouched.

#### `update_one()` in detail

`update_one()` is a built-in pymongo function that finds the document matching a given condition, and performs an update on it.

It takes **two** arguments:

1. A **filter** — which document to update, e.g. `{"_id": ObjectId(student_id)}` (find the student with this exact ID).
2. An **update operation** — what to change, e.g. `{"$set": student}`.

`$set` is a MongoDB **operator** that means "set these specific fields to these values, and leave everything else alone." For example:

```
$set: {
  "course": "DevOps"
}
```

...only changes the `course` field. This is different from replacing the whole document — it's a targeted, partial update. `update_one()` only touches the **first** matching document (there's also `update_many()` for multiple matches, not used here).

**Real-world example:** `update_one()` is like correcting a single field on a student's admission form — you don't reprint the whole form, you just cross out the old course name and write in the new one, leaving the rest of the form untouched.

### Delete — `DELETE /students/{student_id}`

```python
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    result = collection.delete_one({"_id": ObjectId(student_id)})
    return {"message": "Student data deleted"}
```

#### `delete_one()` in detail

`delete_one()` is a built-in pymongo function responsible for deleting data from the database.

- It takes a filter (a condition), e.g. `{"_id": ObjectId(student_id)}`.
- MongoDB finds the **first** document matching that condition and permanently removes it from the collection.
- If no document matches the condition, nothing happens — no error is raised by default, `deleted_count` on the result would simply be `0`.
- There's also `delete_many()` for removing multiple documents at once — not used here, since deleting by a unique `_id` will only ever match one record.

**Real-world example:** `delete_one()` is like pulling a specific student's file out of the records room and shredding it — only that one file is affected, everyone else's records stay exactly as they were.

## 7. `_id` in detail

`_id` is the unique identifier **created by default by MongoDB** for every document, the moment it's inserted.

- You don't need to generate it yourself — MongoDB does this automatically when `insert_one()` runs.
- It's stored internally as an `ObjectId` (a special 12-byte MongoDB type), not a plain string.
- Because JSON (which APIs send over the network) doesn't understand `ObjectId`, every time `_id` is sent back to the client, it must first be converted with `str()` — this is why you see `str(result.inserted_id)` and `student["_id"] = str(student["_id"])` throughout `app.py`.
- Conversely, whenever a client sends an ID back to the API (as a plain string in a URL, like `/students/64f1a2...`), it must be converted back into an `ObjectId` before it can be used to query MongoDB — this is why you see `ObjectId(student_id)` in the update and delete endpoints.

**Real-world example:** `_id` is like a student's roll number auto-assigned by the school the moment they're admitted — unique, permanent, and used to look that exact student up again later, no matter how their other details (name, course, marks) change.

## 8. Path parameter vs request body — the key difference

| | Path parameter | Request body |
|---|---|---|
| Where it lives | In the URL itself, e.g. `/students/123` | In the data sent along with the request |
| Example here | `student_id: str` | `student: dict` |
| Used for | Identifying *which* record | Sending the *actual data* to save/update |

**Real-world example:** Think of an ATM. Your card number (path parameter) identifies *whose* account you're accessing. The amount you type to withdraw (request body) is the *data* for that action.

## 9. Full request/response flow (Create example)

1. Client sends `POST /students` with body `{"name": "Pranav", "course": "AI"}`.
2. FastAPI matches the URL + method to `create_student()`.
3. FastAPI parses the JSON body into the `student` dictionary.
4. `collection.insert_one(student)` inserts it into MongoDB; MongoDB auto-generates `_id`.
5. The function returns a dictionary; FastAPI automatically converts it to a JSON response.
6. The client receives `{"message": "student data has been created", "_id": "64f1a2..."}`.

## 10. Quick summary

| Concept | What it means here |
|---|---|
| API | The messenger between client and database |
| Framework (FastAPI) | Prebuilt structure to define routes quickly |
| Endpoint | A URL + method combination (`POST /students`) |
| Decorator (`@app.post`) | Connects a Python function to a specific route |
| CRUD | Create, Read, Update, Delete — the 4 basic data operations |
| `insert_one()` | Inserts one document into a MongoDB collection |
| `find()` | Retrieves documents from a MongoDB collection (as a cursor) |
| `append` | Python list method to add an item to the end of a list |
| `update_one()` | Finds a matching document and applies a partial update (`$set`) to it |
| `delete_one()` | Finds and permanently removes a matching document |
| `_id` | Unique ID auto-created by MongoDB for every document |
