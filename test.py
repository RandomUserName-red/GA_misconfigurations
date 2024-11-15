import yaml

# Read the YAML file
with open('test_result.yaml', 'r') as file:
    test_results = yaml.safe_load(file)

# Process the test results
print("Tests Run:", test_results['testsRun'])
print("Failures:", test_results['failures'])
print("Errors:", test_results['errors'])
print("Was Successful:", test_results['wasSuccessful'])