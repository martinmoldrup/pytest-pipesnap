from pytest_pipesnap.pipesnap import PipelineOutput, PipelineInput
import pytest

@pytest.mark.pipeline_output("step_1_output")
def test_step_1(save_output_func: PipelineOutput):
    save_output_func.save_output("Hello World")

@pytest.mark.pipeline_input("step_1_output")
@pytest.mark.pipeline_output("step_2_output")
def test_step_2(pipeline_input: PipelineInput, save_output_func: PipelineOutput):
    save_output_func.save_output(pipeline_input.content)