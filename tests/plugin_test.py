import pytest
from pytest_pipesnap.pipesnap import ProduceTestData, ConsumeTestData

@pytest.mark.foreach(['a', 'b', 'c'])
def test_step_1(produce_test_data: ProduceTestData):
    produce_test_data.save_output("Hello World")

@pytest.mark.consume_test_data("test_step_1")
def test_step_2(consume_test_data: ConsumeTestData):
    assert consume_test_data.content == "Hello World"
