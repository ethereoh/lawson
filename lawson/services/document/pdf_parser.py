from langchain_community.document_loaders import (
    PyPDFium2Loader,
    PyMuPDFLoader,
    PyPDFDirectoryLoader,
    PyPDFLoader,
    PDFMinerLoader,
    PDFPlumberLoader,
)

from lawson.core.config import settings
from lawson.common import setup_logger, get_exception_message
from lawson.schemas.law_doc import LawsonResponse
from lawson.services.base import BaseService

logger = setup_logger(name=settings.LOGGER)


class PdfParserService(BaseService):
    """
    A class to handle PDF parsing using various services.
    """

    SERVICE_LOADERS = {
        "pypdf": PyPDFLoader,
        "pypdfium2": PyPDFium2Loader,
        "pymupdf": PyMuPDFLoader,
        "pdfminer": PDFMinerLoader,
        "pdfplumber": PDFPlumberLoader,
        "pypdfdir": PyPDFDirectoryLoader,
    }

    def inference(
        files: list[str] | str, service: str = "pypdf", **kwargs
    ) -> LawsonResponse:
        """
        Parses PDF files using the specified service.

        Args:
            files (list[str] | str): Path(s) to the PDF file(s).
            service (str): The parsing service to use (default: 'pypdf').

        Returns:
            list[Document]: Parsed documents.

        Raises:
            ValueError: If an exception occurs during parsing or the service is unsupported.
        """
        try:
            loader_class = PdfParserService.SERVICE_LOADERS.get(service)
            if not loader_class:
                raise ValueError(f"Unsupported service: {service}")

            loader = loader_class(
                file_path=files, **kwargs
            ).load()  # => list[langchain.Document]
            return {"success": True, "data": loader}
        except Exception as e:
            message = "Failed to fetch documents using PDF parser"
            msg = get_exception_message(message=message, exception=e)
            logger.error(msg)
            return {"sucess": False, "detail": message}


pdf_parser_service = PdfParserService()
