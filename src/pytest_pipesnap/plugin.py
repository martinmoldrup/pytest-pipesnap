import pathlib

import pytest

from .pipesnap import CaseData, ConsumeTestData, ProduceTestData


def pytest_addoption(parser):
    group = parser.getgroup("pipesnap")
    group.addoption(
        "--pipesnap-update",
        action="store_true",
        default=False,
        help="Update the pipeline snapshot files with the new output",
    )
@pytest.fixture()
def produce_test_data(request: pytest.FixtureRequest) -> ProduceTestData:
    """"""
    test_function_name = request.node.originalname
    # If a parameter is provided
    if hasattr(request, "param"):
        return ProduceTestData(
            path=pathlib.Path(f"pipeline_output/{test_function_name}/{request.param}"),
            param_name=request.param,
        )
    return ProduceTestData(
        path=pathlib.Path(f"pipeline_output/{test_function_name}"),
        param_name=test_function_name,
    )

@pytest.fixture()
def consume_test_data(request: pytest.FixtureRequest) -> ConsumeTestData:
    """"""
    param: str = request.param
    return ConsumeTestData(
        path=pathlib.Path(f"pipeline_output/{param}"),
        content="",
    )

@pytest.fixture()
def test_data(request: pytest.FixtureRequest) -> CaseData:
    test_function_name = request.node.originalname
    if hasattr(request, "param"):
        return CaseData(
            path=pathlib.Path(f"pipeline_output/{test_function_name}/{request.param}"),
            scenario=request.param,
        )
    return CaseData(
        path=pathlib.Path(f"pipeline_output/{test_function_name}"),
        scenario={},
    )

def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    pipeline_output_marker = metafunc.definition.get_closest_marker("foreach")
    if pipeline_output_marker:
        parameters = pipeline_output_marker.args[0]
        metafunc.parametrize("produce_test_data", parameters, indirect=True)

    pipeline_input_marker = metafunc.definition.get_closest_marker("consume_test_data")
    if pipeline_input_marker:
        input_name = pipeline_input_marker.args[0]
        path = pathlib.Path(f"pipeline_output/{input_name}")
        subdirectories = [p.stem for p in path.glob("*") if p.is_dir()]
        if subdirectories:
            metafunc.parametrize("consume_test_data", subdirectories, indirect=True)

