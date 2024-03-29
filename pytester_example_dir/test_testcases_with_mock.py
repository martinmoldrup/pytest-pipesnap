"""A simple example where looping through examples. Point is to check the "test_case" agument is added in the same order as mock adds arguments."""
from pytest_pipesnap.pipesnap import foreach_test_case_in_directory, CaseData
import pathlib
from unittest import mock
import pytest

@pytest.fixture
def dummy_fixture():
    return "Just a dummy fixture"

@foreach_test_case_in_directory(path=pathlib.Path("testcases"))
@mock.patch("builtins.open", mock.mock_open(read_data='dummy content'))
@mock.patch("pathlib.Path.open", mock.mock_open(read_data='dummy content'))
def test_loop_through_test_cases_with_mock(dummy_fixture: str, test_case: CaseData, mocked_open: mock.Mock, mocked_path_open: mock.Mock):
    content = test_case.read_file('content.txt')
    assert content == "dummy content"
