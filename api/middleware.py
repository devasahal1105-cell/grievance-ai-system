import logging
import time
import os

os.makedirs(
    "logs",
    exist_ok=True
)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


async def log_requests(
    request,
    call_next
):

    start_time = time.time()

    response = await call_next(
        request
    )

    process_time = (
        time.time() - start_time
    )

    logging.info(
        f"{request.method} "
        f"{request.url.path} "
        f"{process_time:.4f}s"
    )

    return response