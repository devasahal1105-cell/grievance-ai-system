import os
import json
import uuid
import pandas as pd

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

from api.schemas import ComplaintRequest
from api.services import predict_complaint

import pandas as pd

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from fastapi.responses import (
    FileResponse
)

from api.schemas import (
    ComplaintRequest
)

from api.services import (
    predict_complaint
)

router = APIRouter()


# =====================================
# Health Check
# =====================================

@router.get("/health")
def health():

    return {

        "status": "success",

        "department_model": "loaded",

        "sentiment_model": "loaded",

        "urgency_model": "loaded",

        "version": "1.0.0"
    }


# =====================================
# Full Prediction
# =====================================

@router.post("/predict")
def predict_api(
    request: ComplaintRequest
):

    result = predict_complaint(
        request.complaint
    )

    return result


# =====================================
# Department Prediction
# =====================================

@router.post("/department")
def department_api(
    request: ComplaintRequest
):

    result = predict_complaint(
        request.complaint
    )

    return {

        "department":
            result["department"]
    }


# =====================================
# Sentiment Prediction
# =====================================

@router.post("/sentiment")
def sentiment_api(
    request: ComplaintRequest
):

    result = predict_complaint(
        request.complaint
    )

    return {

        "sentiment":
            result["sentiment"]
    }


# =====================================
# Urgency Prediction
# =====================================

@router.post("/urgency")
def urgency_api(
    request: ComplaintRequest
):

    result = predict_complaint(
        request.complaint
    )

    return {

        "urgency":
            result["urgency"]
    }


# =====================================
# Bulk CSV Prediction
# =====================================

@router.post("/bulk-predict")
async def bulk_predict(
    file: UploadFile = File(...)
):

    request_id = str(
        uuid.uuid4()
    )

    upload_path = (
        f"uploads/{request_id}.csv"
    )

    output_path = (
        f"outputs/{request_id}.csv"
    )

    try:

        with open(
            upload_path,
            "wb"
        ) as buffer:

            buffer.write(
                await file.read()
            )

        df = pd.read_csv(
            upload_path
        )

        if "complaint" not in df.columns:

            raise HTTPException(
                status_code=400,
                detail=(
                    "CSV must contain "
                    "'complaint' column"
                )
            )

        predictions = []

        for complaint in df["complaint"]:

            result = predict_complaint(
                str(complaint)
            )

            predictions.append(
                result
            )

        prediction_df = pd.DataFrame(
            predictions
        )

        final_df = pd.concat(
            [
                df,
                prediction_df
            ],
            axis=1
        )

        final_df.to_csv(
            output_path,
            index=False
        )

        return {

            "request_id":
                request_id,

            "status":
                "completed",

            "download_url":
                (
                    f"/api/v1/"
                    f"bulk-predict/download/"
                    f"{request_id}"
                )
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================
# Download Prediction File
# =====================================

@router.get(
    "/bulk-predict/download/{request_id}"
)
def download_prediction(
    request_id: str
):

    file_path = (
        f"outputs/{request_id}.csv"
    )

    if not os.path.exists(
        file_path
    ):

        raise HTTPException(
            status_code=404,
            detail=(
                "Prediction file "
                "not found"
            )
        )

    return FileResponse(
        path=file_path,
        media_type="text/csv",
        filename=f"{request_id}.csv"
    )


# =====================================
# Metrics API
# =====================================

@router.get("/metrics")
def metrics():

    metrics_file = (
        "reports/metrics.json"
    )

    if not os.path.exists(
        metrics_file
    ):

        raise HTTPException(
            status_code=404,
            detail=(
                "metrics.json "
                "not found"
            )
        )

    with open(
        metrics_file,
        "r"
    ) as file:

        return json.load(
            file
        )


# =====================================
# Model Information
# =====================================

@router.get("/model-info")
def model_info():

    metrics_file = (
        "reports/metrics.json"
    )

    if not os.path.exists(
        metrics_file
    ):

        raise HTTPException(
            status_code=404,
            detail=(
                "metrics.json "
                "not found"
            )
        )

    with open(
        metrics_file,
        "r"
    ) as file:

        metrics = json.load(
            file
        )

    return {

        "department_model":
            metrics.get(
                "department_model"
            ),

        "sentiment_model":
            metrics.get(
                "sentiment_model"
            ),

        "urgency_model":
            metrics.get(
                "urgency_model"
            ),

        "version":
            metrics.get(
                "version"
            )
    }