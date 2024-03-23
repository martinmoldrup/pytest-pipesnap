# pytest-pipesnap
A library for testing complicated data structures, doing snapshot testing and testing pipelines in an easier way. The package is structured around test cases stored in files, and outputs stored in files.


# Purpose

- To quickly setup tests on a data heavy (pandas and numpy functions) based on real examples
- Being able to easily add more examples containing edge cases or issues
- More easily understand and debug code by enabling opening real examples of the intemediate calculations
- Handle flaky tests by using a flexible snapshot testing approach. Write full file, but do exclusions on runtime
- Split the test cases from the code