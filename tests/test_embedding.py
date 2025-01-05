import pytest
import numpy as np

passages = [
    "Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.",
    "Berlin is well known for its museums.",
    "In 2014, the city state Berlin had 37,368 live births (+6.6%), a record number since 1991.",
    "The urban area of Berlin comprised about 4.1 million people in 2014, making it the seventh most populous urban area in the European Union.",
    "The city of Paris had a population of 2,165,423 people within its administrative city limits as of January 1, 2019",
    "An estimated 300,000-420,000 Muslims reside in Berlin, making up about 8-11 percent of the population.",
    "Berlin is subdivided into 12 boroughs or districts (Bezirke).",
    "In 2015, the total labour force in Berlin was 1.85 million.",
    "In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.",
    "Berlin has a yearly total of about 135 million day visitors, which puts it in third place among the most-visited city destinations in the European Union.",
]


@pytest.mark.parametrize("passage", [passages[np.random.randint(0, len(passages))]])
def test_embedding_one_input(init_embedding_service, passage):
    embed_results = init_embedding_service.inference(passage).get("result")
    assert isinstance(embed_results, list)


@pytest.mark.parametrize("passages", [passages])
def test_embedding_many_inputs(init_embedding_service, passages):
    embed_results = init_embedding_service.inference(passages).get("result")
    assert isinstance(embed_results, list)
    assert isinstance(embed_results[0], list)
