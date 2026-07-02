from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
def test(request: Request):
    print(request.body)
    return {"message": "Hello World"}