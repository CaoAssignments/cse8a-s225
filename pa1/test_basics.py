import unittest
import subprocess
import os

from gradescope_utils.autograder_utils.decorators import weight, visibility

class TestPA1(unittest.TestCase):
    """
    Gradescope-compatible unit tests for pa1.py
    """

    SUBMISSION_DIR = "/autograder/submission"
    SCRIPT_PATH = os.path.join(SUBMISSION_DIR, "pa1.py")
    TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")

    def run_script(self, input_data):
        try:
            result = subprocess.run(
                ["python3", self.SCRIPT_PATH],
                input=input_data,
                capture_output=True,
                text=True,
                check=True,
                timeout=5
            )
            output = result.stdout.strip()
            search_string = "Area of ring shape ="
            if search_string in output:
                start_index = output.rfind(search_string)
                final_output = output[start_index:].strip()
                return final_output.splitlines()[-1]
            return output
        except subprocess.CalledProcessError as e:
            return f"ERROR: Script crashed with exit code {e.returncode}. Stderr:\n{e.stderr}"
        except FileNotFoundError:
            return "ERROR: Python executable not found."
        except subprocess.TimeoutExpired:
            return "ERROR: Script timed out after 5 seconds."

    def run_case(self, input_file, output_file):
        input_path = os.path.join(self.TESTS_DIR, input_file)
        output_path = os.path.join(self.TESTS_DIR, output_file)

        with open(input_path, 'r') as f:
            input_data = f.read()
        with open(output_path, 'r') as f:
            expected_output = f.read().strip()

        actual_output = self.run_script(input_data)
        return input_data, expected_output, actual_output

    @weight(10)
    @visibility('visible')
    def test_1(self):
        input_data, expected, actual = self.run_case("test1.txt", "test1-out.txt")
        self.assertEqual(actual, expected, f"\nInput:\n{input_data}\nExpected:\n{expected}\nGot:\n{actual}")

    @weight(10)
    @visibility('visible')
    def test_2(self):
        input_data, expected, actual = self.run_case("test2.txt", "test2-out.txt")
        self.assertEqual(actual, expected)

    @weight(10)
    @visibility('visible')
    def test_3(self):
        input_data, expected, actual = self.run_case("test3.txt", "test3-out.txt")
        self.assertEqual(actual, expected)

    @weight(10)
    @visibility('visible')
    def test_4(self):
        input_data, expected, actual = self.run_case("test4.txt", "test4-out.txt")
        self.assertEqual(actual, expected)

    @weight(10)
    @visibility('visible')
    def test_5(self):
        input_data, expected, actual = self.run_case("test5.txt", "test5-out.txt")
        self.assertEqual(actual, expected)

    @weight(10)
    @visibility('visible')
    def test_6(self):
        input_data, expected, actual = self.run_case("test6.txt", "test6-out.txt")
        self.assertEqual(actual, expected)

    @weight(10)
    @visibility('visible')
    def test_7(self):
        input_data, expected, actual = self.run_case("test7.txt", "test7-out.txt")
        self.assertEqual(actual, expected)

    @weight(10)
    @visibility('visible')
    def test_8(self):
        input_data, expected, actual = self.run_case("test8.txt", "test8-out.txt")
        self.assertEqual(actual, expected)

    @weight(10)
    @visibility('visible')
    def test_9(self):
        input_data, expected, actual = self.run_case("test9.txt", "test9-out.txt")
        self.assertEqual(actual, expected)

    @weight(5)
    @visibility('visible')
    def test_10(self):
        input_data, expected, actual = self.run_case("test10.txt", "test10-out.txt")
        self.assertEqual(actual, expected)

    @weight(5)
    @visibility('visible')
    def test_11(self):
        input_data, expected, actual = self.run_case("test11.txt", "test11-out.txt")
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
