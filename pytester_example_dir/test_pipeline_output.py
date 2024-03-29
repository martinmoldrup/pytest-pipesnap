from pytest_pipesnap.pipesnap import ProduceTestData
import pytest

@pytest.mark.produce_test_data
def test_step_1(produce_test_data: ProduceTestData):
    produce_test_data.save_output("Hello World")
