from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'get': 'teste na raiz'}
