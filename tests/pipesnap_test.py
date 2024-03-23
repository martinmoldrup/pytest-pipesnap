from pytest import Pytester


def test_simple_testcases(pytester: Pytester) -> None:
    pytester.makefile(".txt",
                      content="dummy content",
                      name="testcases/case1/content.txt")
    pytester.makefile(".txt",
                      content="dummy content",
                      name="testcases/case2/content.txt")
    pytester.copy_example("test_simple_testcases.py")
    result = pytester.runpytest()
    result.assert_outcomes(passed=2)

def test_pipeline_output(pytester: Pytester) -> None:
    pytester.copy_example("test_pipeline_output.py")
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
    # TODO Assert files created in both output and snapshot directories

