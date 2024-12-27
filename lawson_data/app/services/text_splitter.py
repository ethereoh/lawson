from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
)

from app.models.law_doc import LawsonResponse

def split_text(
    text: str, 
    splitter_type: str = "recursive", 
    chunk_size: int = 1000, 
    chunk_overlap: int = 200, 
    **kwargs
) -> LawsonResponse:
    """
    Splits text into chunks using the specified text splitter.

    Args:
        text (str): The text to be split.
        splitter_type (str): Type of splitter to use ('recursive' or 'character').
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The overlap between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    if splitter_type == "recursive":
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap, **kwargs
        )
    elif splitter_type == "character":
        splitter = CharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap, **kwargs
        )
    else:
        raise ValueError("Invalid splitter_type. Choose 'recursive' or 'character'.")

    return splitter.split_documents(text)               # TODO: Check type if string or Document