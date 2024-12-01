from fastapi import FastAPI 


app = FastAPI()


@app.get("/")
def get_health(result: str = "Good"):
    return {"result": result}

if __name__ == "__main__":
    import uvicorn 

    uvicorn.run("main:app", reload=True)