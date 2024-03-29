# pytest-pipesnap
A library for testing complicated data structures, doing snapshot testing and testing pipelines in an easier way. The package is structured around test cases stored in files, and outputs stored in files.


# Purpose
To solve the problems that data scientists have when testing their code in python. The purpose is:

- To quickly setup tests on a data heavy (pandas and numpy functions) based on real examples
- Being able to easily add more examples containing edge cases or issues
- More easily understand and debug code by enabling opening real examples of the intermediate calculations
- Handle flaky tests by using a flexible snapshot testing approach. Write full file, but do exclusions on runtime
- Split the test cases from the code
- Making tests dependent on each other for testing integrations, while still keeping errors isolated 

# Features
- Define test cases in folder and scenarios in a file
- Snapshot testing
- Assertions on built-in types
- Expections on pandas dataframes and numpy data structures

# The testing heirarchy
The testing heirarchy is as follows:
- *CaseExample*: A single test case that is run by pytest. A case can have multiple scenarios.
- *Scenario*: A scenario is a single configuration of the test case. A scenario can have multiple test data sets.
- *Assertion*: An assertion is a single check that is run on the test data. An assertion can have multiple checks.

- **Test Function**: Uses: Case Examples [the pytest function that runs the test cases]
  - **CaseData**: Uses: Case Data, Scenarios [a single test case with a single scenario to be ran]
    - **path** [files used as inputs]
    - **Scenario**: Uses: Input Configuration, Assertions, Expections [there might be multiple scenarios, for one case data]
        - **Input configuration** [input arguments and configurations for the test]
        - **Assertion** [assertions on the output]
        - **Expection** [fuzzy expections on the output]


# Fixtures provided
- `case_data` - A fixture that provides the test case data, use @pytest.mark.test_case to parametrize with more test cases.
- `produce_test_data` - A fixture that produces test data to be used in other tests. Use @pytest.mark.produce_test_data() to configure.
- `consume_test_data` - A fixture that consumes test data from other tests. Use @pytest.mark.consume_test_data() to configure.


# Contribute
This project is in an early stage and I would love to get feedback on the concept and the implementation. Please open an issue if you have any feedback or ideas for improvements.

Tasks:
- [ ] Define library API
- [ ] Implement tests
- [ ] Implement test cases feature
- [ ] Add CD automation pipeline
- [ ] Add CI automation pipeline
- [ ] Implement pipeline feature
- [ ] Implement assertion feature
- [ ] Implement snapshot feature 
- [ ] Write documentation
