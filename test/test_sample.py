import unittest
import yaml
import os

class TestSample(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)
        output = {
    'testsRun': result.testsRun,
    'failures': len(result.failures),
    'errors': len(result.errors),
    'wasSuccessful': result.wasSuccessful()
}

    # Write the result to a YAML file
        with open('test/test_result.yaml', 'w') as f:
            os.system("pwd")
            yaml.dump(output, f)
            os.system("ls -R")

if __name__ == '__main__':
    result = unittest.TextTestRunner().run(unittest.makeSuite(TestSample))
    output = {
    'testsRun': result.testsRun,
    'failures': len(result.failures),
    'errors': len(result.errors),
    'wasSuccessful': result.wasSuccessful()
}

    # Write the result to a YAML file
    with open('test/test_result.yaml', 'w') as f:
        os.system("pwd")
        yaml.dump(output, f)
        os.system("ls -R")
    
    # Prepare the result to save as YAML
