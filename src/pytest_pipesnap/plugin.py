from dataclasses import dataclass
from .pipesnap import ProduceTestData
from functools import partial
import pathlib
import pytest


def pytest_addoption(parser):
    group = parser.getgroup("pipesnap")
    group.addoption(
        "--pipesnap-update",
        action="store_true",
        default=False,
        help="Update the pipeline snapshot files with the new output",
    )


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    # TODO Handle when no parametrization is used
    # TODO Handle when parametrizations are used
    # Check for pipeline_input marker
    pipeline_output_marker = metafunc.definition.get_closest_marker("produce_test_data")
    if pipeline_output_marker and len(metafunc.fixturenames) == 1:
        name_of_test_function = metafunc.function.__name__
        parameters = [name_of_test_function]  # TODO: Get the parameters from the marker
        final_parameters = []
        for param in parameters:
            pipeline_output = ProduceTestData(
                path=pathlib.Path(f"pipeline_output/{name_of_test_function}"),
                param_name=str(param),
            )
            final_parameters.append(pipeline_output)
        metafunc.parametrize(metafunc.fixturenames[0], final_parameters)

    pipeline_input_marker = metafunc.definition.get_closest_marker("consume_test_data")
    if pipeline_input_marker:
        input_name = pipeline_input_marker.args[0]
        path = pathlib.Path(f"pipeline_output/{input_name}")
        file_paths = list(path.glob("*.txt"))
        metafunc.parametrize(metafunc.fixturenames[0], file_paths)
