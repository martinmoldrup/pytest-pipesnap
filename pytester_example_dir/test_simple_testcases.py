"""A simple example where looping through examples."""
from pytest_pipesnap.pipesnap import foreach_test_case_in_directory, TestCase
import pathlib

@foreach_test_case_in_directory(path=pathlib.Path("testcases"))
def test_loop_through_test_cases(test_case: TestCase):
    content = test_case.read_file('content.txt')
    assert content == "dummy content"
