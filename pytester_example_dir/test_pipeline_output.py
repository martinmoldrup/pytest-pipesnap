from pytest_pipesnap.pipesnap import ProduceTestData
import pytest

@pytest.mark.produce_test_data
def test_step_1(save_output_func: ProduceTestData):
    save_output_func.save_output("Hello World")
