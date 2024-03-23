"""
A simple example where looping through examples, that have scenarios for each test case.

In this example a custom name is used for the scenario file.
"""
from pytest_pipesnap.pipesnap import foreach_test_case_in_directory, TestCase
import pathlib

@foreach_test_case_in_directory(path=pathlib.Path("testcases"), scenarios_file_name="examples.json")
def test_loop_through_test_cases(test_case: TestCase):
    content = test_case.read_file('content.txt')
    assert content == "dummy content"
    assert test_case.scenario['content'] == "dummy scenario"
