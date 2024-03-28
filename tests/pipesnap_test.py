import pytest
import pathlib
from pytest import Pytester
import yaml
import json


def test_simple_testcases(pytester: Pytester) -> None:
    for case_dir in ["case1", "case2"]:
        content_file_path = pytester.path / "testcases" / case_dir / "content.txt"
        content_file_path.parent.mkdir(parents=True, exist_ok=True)
        content_file_path.write_text("dummy content")
    pytester.copy_example("test_simple_testcases.py")
    result = pytester.runpytest()
    result.assert_outcomes(passed=2)

def test_simple_testcases_with_scenarios_yaml(pytester: Pytester) -> None:
    path_scenarios = pytester.copy_example("scenarios.yaml")

    for case_dir in ["case1", "case2"]:
        content_file_path = pytester.path / "testcases" / case_dir / "content.txt"
        content_file_path.parent.mkdir(parents=True, exist_ok=True)
        content_file_path.write_text("dummy content")
        # Copy scenarios file
        scenarios_file_path = pytester.path / "testcases" / case_dir / path_scenarios.name
        scenarios_file_path.write_text(path_scenarios.read_text())


    pytester.copy_example("test_simple_testcases_with_scenarios.py")
    result = pytester.runpytest('-vv')
    result.assert_outcomes(passed=4)

def test_simple_testcases_with_scenarios_json(pytester: Pytester) -> None:

    path_scenarios = pytester.copy_example("scenarios.yaml")

    for case_dir in ["case1", "case2"]:
        content_file_path = pytester.path / "testcases" / case_dir / "content.txt"
        content_file_path.parent.mkdir(parents=True, exist_ok=True)
        content_file_path.write_text("dummy content")
        # Copy scenarios file
        scenarios_file_path = pytester.path / "testcases" / case_dir / f"{path_scenarios.stem}.json"
        scenarios_content = path_scenarios.read_text()
        scenarios_content = json.dumps(yaml.safe_load(scenarios_content))  # Convert yaml to json
        scenarios_file_path.write_text(scenarios_content)


    pytester.copy_example("test_simple_testcases_with_scenarios.py")
    result = pytester.runpytest()
    result.assert_outcomes(passed=4)



# @pytest.mark.skip("Not implemented")
def test_pipeline_output(pytester: Pytester) -> None:
    pytester.copy_example("test_pipeline_output.py")
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
    # TODO Assert files created in both output and snapshot directories

