import pytest
from langchain_core.documents import Document
from app.services import pdf_parser_service

samples = pseudo_data()

def test_pdf_parsing():
    file_path = samples['file']
    results = pdf_parser_service.inference(files=file_path)
    assert type(results) == list[Document]
