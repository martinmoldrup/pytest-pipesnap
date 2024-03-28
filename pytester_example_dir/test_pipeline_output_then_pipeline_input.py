from pytest_pipesnap.pipesnap import ProduceTestData, ConsumeTestData
import pytest

@pytest.mark.produce_test_data("step_1_output")  # produce_test_data, share_test_output
def test_step_1(save_output_func: ProduceTestData):
    save_output_func.save_output("Hello World")

@pytest.mark.consume_test_data("step_1_output") # consume_test_data, consume_shared_input
@pytest.mark.produce_test_data("step_2_output")
def test_step_2(pipeline_input: ConsumeTestData, save_output_func: ProduceTestData):
    save_output_func.save_output(pipeline_input.content)
