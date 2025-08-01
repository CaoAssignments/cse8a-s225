import unittest
import subprocess
import os
from gradescope_utils.autograder_utils.decorators import weight, visibility

class TestPA1(unittest.TestCase):
    SUBMISSION_DIR = "/autograder/submission"
    SCRIPT_PATH = os.path.join(SUBMISSION_DIR, "pa1.py")
    TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")

    def run_script(self, input_data):
        try:
            input_lines = input_data.strip().split('\n')
            result = subprocess.run(
                ["python3", self.SCRIPT_PATH],
                input=input_data,
                capture_output=True,
                text=True,
                check=True,
                timeout=5
            )
            # Capture the printed prompts
            prompts = result.stdout.split('Area of ring shape')[0].strip().split(':')
            normalized_output = ""
            for i in range(len(input_lines)):
                prompt_text = prompts[i].strip() if i < len(prompts) else ""
                normalized_output += f"{prompt_text}:{input_lines[i]}\n"
            # Append the final result line (Area output)
            final_result_line = "Area of ring shape" + result.stdout.split('Area of ring shape')[1]
            normalized_output += final_result_line.strip()
            return normalized_output.strip()
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
            input_lines = f.read().splitlines()

        with open(output_path, 'r') as f:
            expected_output = f.read().strip()

        raw_input = '\n'.join(input_lines)
        actual_program_output = self.run_script(raw_input)

        # Don't echo prompts, just return what the script actually printed
        final_output = actual_program_output.strip()

        return expected_output, final_output


    def assert_equal_with_message(self, test_name, expected, actual):
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print(f"--- Test Origin: {test_name} ---")
            print(f"Expected Output:\n{expected}")
            print(f"\nActual Output:\n{actual}")
            raise  # Re-raise so unittest still fails the test

    @weight(10)
    @visibility('visible')
    def test_01_Origin(self):
        test_name = "Test Origin: (0,0) (1,0) (2,0)"
        expected, actual = self.run_case("test1.txt", "test1-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_02_Non_Origin_1(self):
        test_name = "Test Non-Origin 1: (3,3) (2,2) (1,1)"
        expected, actual = self.run_case("test2.txt", "test2-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_03_Non_Origin_2(self):
        test_name = "Test Non-Origin 2: (5,6) (4,8) (7,3)"
        expected, actual = self.run_case("test3.txt", "test3-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_04_Float_1(self):
        test_name = "Test Float 1: (5.9,3) (6.7,3.2) (11.5,2)"
        expected, actual = self.run_case("test4.txt", "test4-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_05_Float_2(self):
        test_name = "Test Float 2: (2.2,6.9) (4.2,6.7) (5.2,6.3)"
        expected, actual = self.run_case("test5.txt", "test5-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_06_Negative_1(self):
        test_name = "Test Negative 1: (-10,-3) (-8,-1) (-13,-6)"
        expected, actual = self.run_case("test6.txt", "test6-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_07_Negative_2(self):
        test_name = "Test Negative 2: (-10,5) (4,3) (5,-10)"
        expected, actual = self.run_case("test7.txt", "test7-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_08_P2_at_Inner_1(self):
        test_name = "Test P2 at Inner 1: (2,2) (6,6) (4,4)"
        expected, actual = self.run_case("test8.txt", "test8-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(10)
    @visibility('visible')
    def test_09_P2_at_Inner_2(self):
        test_name = "Test P2 at Inner 2: (4.4,4.5) (7.2,-1) (6.3,0)"
        expected, actual = self.run_case("test9.txt", "test9-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(5)
    @visibility('visible')
    def test_10_Overlap_1(self):
        test_name = "Test Overlap 1: (3,3) (3,3) (4,4)"
        expected, actual = self.run_case("test10.txt", "test10-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

    @weight(5)
    @visibility('visible')
    def test_11_Overlap_2(self):
        test_name = "Test Overlap 2: (1,1) (4,4) (4,4)"
        expected, actual = self.run_case("test11.txt", "test11-out.txt")
        self.assert_equal_with_message(test_name, expected, actual)

if __name__ == "__main__":
    unittest.main()
