import tempfile
from pathlib import Path
from fastapi import APIRouter, HTTPException, UploadFile, File

from lawson.services import pdf_parser_service
from lawson.schemas.law_doc import LawsonResponse

router = APIRouter()


@router.post("/inference", status_code=200, response_model=LawsonResponse)
async def parsing_pdf_document(file: UploadFile = File(...)):
    """
    Parsing an upload document
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(await file.read())

        result = pdf_parser_service.inference(temp_file_path)

        if result.get("success"):
            return result.get("data")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    finally:
        Path(temp_file_path).unlink(missing_ok=True)
