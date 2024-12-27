import pytest


@pytest.fixture
def pseudo_data(): 
    file = "/home/octoopt/Desktop/CodingLab/Personal/lawson/docs/data_samples/GDPR_2018.pdf"
    files = [...]

    return {
        "file": file, 
        "files": files
    }