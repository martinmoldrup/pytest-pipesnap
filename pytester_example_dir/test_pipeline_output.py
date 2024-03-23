from pytest_pipesnap.pipesnap import PipelineOutput
import pytest

@pytest.mark.pipeline_output(3)
def test_step_1(save_output_func: PipelineOutput):
    save_output_func.save_output("Hello World")
