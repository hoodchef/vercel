from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("Polygon proxy placeholder")
    await ws.close()
