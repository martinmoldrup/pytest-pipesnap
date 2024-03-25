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
