from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# برای تست مرورگر یا curl
@app.get("/")
async def root():
    return {"status": "Server is running"}

# مسیر وبهوک تلگرام
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Incoming update:", data)  # چاپ پیام دریافتی در لاگ
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
