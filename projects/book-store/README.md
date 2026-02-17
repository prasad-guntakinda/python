# Book Store Management Application

```text
bookstore/
│
├── app/
│   ├── main.py              → entry point
│   ├── database.py          → DB connection
│   ├── models/              → DB tables
│   ├── schemas/             → request/response DTO
│   ├── routes/              → controllers
│   ├── services/            → business logic
│   ├── repository/          → DB queries
│   ├── core/                → config, logging
│   └── utils/
│
├── requirements.txt
└── .env


```

## 2. Why virtual environment? (VERY VERY important)

- We must use virtual environment in real projects.
- Every project needs their own packages and specific versions
- Without venv all projects share same packages because of that version conflicts will occurs.
- It's like maintaining different versions for different project

### Create virtual environment:

```shell
python -m venv venv
source venv/bin/activate # mac/linux
venv\Scripts\activate # windows
# now install packages
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy

# at the end we create requirements.txt file
pip freeze > requirements.txt
# install missing package
pip install python-dotenv
# Add to requirements:
pip freeze | grep python-dotenv >> requirements.txt
# deactivate venv
deactivate

```

### What is requirements.txt?
- This file contains all Python dependencies required for the project.

- Like:
```text
pom.xml (Maven)
build.gradle (Gradle)
```

- Example requirements.txt:

```text
fastapi
uvicorn
sqlalchemy
python-dotenv
passlib[bcrypt]
```

- Why needed?

- When someone downloads your project:

- They just run:

```shell
pip install -r requirements.txt
```

- All required libraries install automatically. Without this,  project won’t run on another machine.

#### How to generate this file automatically?

- After installing packages:
```shell
pip freeze > requirements.txt
```
---


## 3. How to run application?

- Inside project root:

```shell
uvicorn app.main:app --reload
```

- Meaning:
```text
uvicorn → server
app.main → file path
app → FastAPI object
--reload → auto restart on code change
```

- Open Server:  http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs
## 4. How to send this app to others? (like JAR/WAR)

Python apps don’t build jar/war normally.
We transfer as source project.

Method 1 — Zip project (simple)

Send folder:

bookstore/
 ├── app/
 ├── requirements.txt
 ├── .env
 └── README.md


Other person runs:

pip install -r requirements.txt
uvicorn app.main:app