from fastapi import APIRouter, UploadFile, File, Form
import shutil
import uuid
import os

from app.config import UPLOAD_DIR, OUTPUT_DIR
from services.bg_remove import remove_background_with_color

router = APIRouter()


@router.post("/remove-bg")
async def remove_bg(
        file: UploadFile = File(...),
        r: int = Form(255),
        g: int = Form(255),
        b: int = Form(255)
):

    file_id = str(uuid.uuid4())

    input_path = os.path.join(UPLOAD_DIR, file_id + ".png")

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = os.path.join(OUTPUT_DIR, file_id + "_processed.png")

    remove_background_with_color(
        input_path,
        output_path,
        color=(r, g, b)
    )

    return {
        "message": "Image processed",
        "output": output_path
    }