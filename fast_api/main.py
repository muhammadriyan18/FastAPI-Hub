# from fastapi import FastAPI

# app = FastAPI()

# items = [
#     {"id": 1, "name": "Issue 1", "status": "open"},
#     {"id": 2, "name": "Issue 2", "status": "closed"},
#     {"id": 3, "name": "Issue 3", "status": "in progress"},
# ]

# @app.get("/health")
# def health_check():
#     return{"status":"ok"}

# @app.get("/items")
# def get_item():
#     return items

# @app.get("/items/{item_id}")
# def items_get(item_id:int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#         return {"error" : "Item Not Found"}

# @app.post("/items")
# def create_item(item: dict):
#     items.append(item)
#     return item
from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware
# After app is created

# app = FastAPI(
#     title="Issue Tracker API",
#     version="0.1.0",
#     description="A mini production-style API built with FastAPI",
# )

app = FastAPI()
# @app.get("/health")
# def health_check():
#     return {"status": "ok"}
app.middleware("http")(timing_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(issues_router)