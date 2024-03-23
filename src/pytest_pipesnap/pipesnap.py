import pathlib
from typing import Union, Optional, Dict, Any
from dataclasses import dataclass


def foreach_test_case_in_directory(
    path: Union[pathlib.Path, str],
    scenarios_file_name: Optional[str] = None,
): ...


@dataclass
class TestCase:
    scenario: Dict[str, Any]

    def read_file(self, filename: str) -> str: ...


@dataclass
class PipelineOutput:
    """Pipeline Output"""
    path: pathlib.Path

    def save_output(self, pipeline_output_content: str): ...

@dataclass
class PipelineInput:
    """Pipeline Input"""
    path: pathlib.Path
    content: str

    def read_input(self) -> str: ...