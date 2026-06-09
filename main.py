from fastapi import FastAPI

from api.routes import (
    router
)

from api.middleware import (
    log_requests
)

app = FastAPI(

    title="Government Grievance AI System",

    description=(
        "AI-powered grievance classification, "
        "sentiment analysis and urgency detection system."
    ),

    version="1.0.0"
)

# Register Middleware

app.middleware(
    "http"
)(
    log_requests
)

# Register Routes

app.include_router(

    router,

    prefix="/api/v1",

    tags=["Grievance AI"]
)


@app.get("/")
def root():

    return {

        "message":
            "Government Grievance AI System",

        "swagger":
            "/docs",

        "version":
            "1.0.0"
    }