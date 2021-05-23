# Create Project 
    mkdir app-fast-api
    cd app-fast-api
    touch Pipfile

# Run Project
    uvicorn sql_app.main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn mongo_app.main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

https://mkdev.me/en/posts/rails-5-vue-js-how-to-stop-worrying-and-love-the-frontend
https://github.com/rescaty/mvp/blob/master/backend/config/config.ci.yml
#### Dependencies

- python `3.6`
- DB `MongoDB and Sqlite3`
- fastapi = "*"
- uvicorn = "*"
- sqlalchemy = "*"
- async-exit-stack = "*"
- async-generator = "*"
- pymongo = {extras = ["srv"],version = "*"}
- motor = "==2.0"
- python-dotenv = "==0.10.1"
- pyjwt = "==1.7"
- databases = "==0.2.1"
- python-slugify = "==3.0"
- pydantic = "*"
- passlib = "==1.7"}


✔ Successfully created virtual environment!
Virtualenv location: /home/axel/.local/share/virtualenvs/
app-fast-api-9sq-dWl8
Creating a Pipfile for this project…

. /home/axel/.local/share/virtualenvs/app-fast-api-9sq-dWl8/bin/activate

Activate virtual environment
pipenv shell