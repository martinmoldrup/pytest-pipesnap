"""Functions and decorators to be imported and used by the user to configure tests."""
import logging
import os
import pathlib
from dataclasses import dataclass
from functools import wraps
from typing import Callable, List, Optional, Union

import pytest
import yaml

logger = logging.getLogger(__name__)
SCENARIOS_FILE_NAMES = ["scenarios.yaml", "scenarios.yml", "scenarios.json"]

class ExceptionDuringTestSetupError(Exception):
    """Error raised when an exception is raised during the setup of the tests."""


def get_scenarios(test_case: pathlib.Path, scenarios_file_name: Optional[str], test_case_location: pathlib.Path) -> Optional[List[dict]]:
    if scenarios_file_name is not None:
        location = test_case_location / scenarios_file_name
        if not location.is_file():
            raise FileNotFoundError(f"Could not find scenarios file {scenarios_file_name} in {test_case_location}")
    else:
        for scenarios_file_name in SCENARIOS_FILE_NAMES:
            location = test_case / scenarios_file_name
            if location.is_file():
                break
        else:
            return None

    with open(location) as f:
        return yaml.safe_load(f)["scenarios"]




def foreach_test_case_in_directory(
    path: Union[pathlib.Path, str],
    scenarios_file_name: Optional[str] = None,
) -> Callable[[Callable], Callable]:
    """Decorator to run a test for each test case in a directory."""
    if isinstance(path, str):
        test_case_location = pathlib.Path(path)
    else:
        test_case_location = path



    def get_test_cases_and_scenarios() -> List[CaseData]:

        test_cases = pathlib.Path(test_case_location)
        out = []
        for test_case in test_cases.iterdir():
            if not test_case.is_dir():
                continue
            try:
                scenarios = get_scenarios(test_case, scenarios_file_name, test_case_location)
            except FileNotFoundError as e:
                # Case where no scenarios file was found, but it was expected
                raise ExceptionDuringTestSetupError(f"Could not find scenarios file for test case {test_case}: {e!s}") from e
            else:
                if scenarios is None:
                    # Case where no scenarios file was found
                    out.append(
                        CaseData(
                            path=test_case,
                            scenario=None,
                        ),
                    )
                    continue
                for scenario in scenarios:
                    out.append(
                        CaseData(
                            path=test_case,
                            scenario=scenario,
                        ),
                    )
        return out

    def create_id(x: CaseData) -> Optional[str]:
        try:
            if x.scenario:
                return f"{x.path.stem}_{x.scenario['name']}"
            else:
                return f"{x.path.stem}"
        except (KeyError, TypeError):
            logger.warning("Could not setup id for test case")
            return None

    def decorator(func):
        try:
            test_cases = get_test_cases_and_scenarios()
        except Exception as e:
            test_cases = [CaseData(path=pathlib.Path(), scenario={}, _exception=e)]
        if not test_cases:
            raise ExceptionDuringTestSetupError("No test cases found")

        @pytest.mark.get_test_cases_and_scenarios()
        # @pytest.mark.contains_snapshot(test_case_location=test_case_location)
        @pytest.mark.parametrize("test_case", test_cases, ids=create_id)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@dataclass
class CaseData:
    path: pathlib.Path
    scenario: Optional[dict]
    _exception: Optional[Exception] = None

    def __getattribute__(self, name: str):
        """If an exception was raised during the setup of the tests, raise an exception when trying to access the attribute."""
        exception = object.__getattribute__(self, "_exception")
        if exception is not None and os.getenv("PYTEST_CURRENT_TEST"):
            raise ExceptionDuringTestSetupError(f"When during setup of the tests an error was raised: {exception}") from exception
        return object.__getattribute__(self, name)


    def read_file(self, filename: str) -> str:
        """Read a file in the test case directory."""
        return (self.path / filename).read_text()

@dataclass
class ProduceTestData:
    """Pipeline Output"""

    path: pathlib.Path
    param_name: str

    def save_output(self, pipeline_output_content: str):
        self._save_output(pipeline_output_content, self.param_name)

    def _save_output(self, pipeline_output_content: str, param_name: str):
        file_path = self.path / f"{param_name}.txt"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(pipeline_output_content)

@dataclass
class ConsumeTestData:
    """Pipeline Input."""

    path: pathlib.Path
    content: str

    def read_input(self) -> str:
        raise NotImplementedError()
