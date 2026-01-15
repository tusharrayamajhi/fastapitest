from fastapi import FastAPI
from fastapi.responses import JSONResponse
app  = FastAPI(title="fast api test in vercel",description="this is test to host fast vapi in vercel",version=1.0)


@app.get("/")
async def getDate():
    return JSONResponse({"message":"hello from vercel test ",})


if __name__ == "__index__":
    import uvicorn
    uvicorn.run("index.py",host='0.0.0.0',port=8000,reload=True)