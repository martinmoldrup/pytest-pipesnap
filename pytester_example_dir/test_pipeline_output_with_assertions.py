from pytest_pipesnap.pipesnap import PipelineOutput
import pytest

@pytest.mark.pipeline_output(3)
def test_step_1(pipeline_output: PipelineOutput):
    pipeline_output.save_output("Hello World")
    pipeline_output.assert_immutable()
    pipeline_output.assert_type(List[int])
    pipeline_output.expect_column_values_to_not_be_null("pickup_datetime")
    pipeline_output.expect_column_values_to_be_between(
        "passenger_count", min_value=1, max_value=6
    )
    pipeline_output.expect_column_values_to_be_json_parseable()
