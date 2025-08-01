import unittest
import subprocess
import os

class GradescopeTests(unittest.TestCase):
    """
    Flexible test suite for evaluating a student script using stdin/stdout,
    with support for per-test point values and visible test names.
    """

    # Define test cases with name, input/output files, and points
    test_cases = {
        1: {
            "name": "Test Origin: (0,0) (1,0) (2,0)",
            "input_file": "tests/test1.txt",
            "output_file": "tests/test1-out.txt",
            "points": 10
        },
        2: {
            "name": "Test Non-Origin 1: (3,3) (2,2) (1,1)",
            "input_file": "tests/test2.txt",
            "output_file": "tests/test2-out.txt",
            "points": 10
        },
        3: {
            "name": "Test Non-Origin 2: (5,6) (4,8) (7,3)",
            "input_file": "tests/test3.txt",
            "output_file": "tests/test3-out.txt",
            "points": 10
        },
        4: {
            "name": "Test Float 1: (5.9,3) (6.7,3.2) (11.5,2)",
            "input_file": "tests/test4.txt",
            "output_file": "tests/test4-out.txt",
            "points": 10
        },
        5: {
            "name": "Test Float 2: (2.2,6.9) (4.2,6.7) (5.2,6.3)",
            "input_file": "tests/test5.txt",
            "output_file": "tests/test5-out.txt",
            "points": 10
        },
        6: {
            "name": "Test Negative 1: (-10,-3) (-8,-1) (-13,-6)",
            "input_file": "tests/test6.txt",
            "output_file": "tests/test6-out.txt",
            "points": 10
        },
        7: {
            "name": "Test Negative 2: (-10,5) (4,3) (5,-10)",
            "input_file": "tests/test7.txt",
            "output_file": "tests/test7-out.txt",
            "points": 10
        },
        8: {
            "name": "Test P2 at Inner 1: (2,2) (6,6) (4,4)",
            "input_file": "tests/test8.txt",
            "output_file": "tests/test8-out.txt",
            "points": 10
        },
        9: {
            "name": "Test P2 at Inner 2: (4.4,4.5) (7.2,-1) (6.3,0)",
            "input_file": "tests/test9.txt",
            "output_file": "tests/test9-out.txt",
            "points": 10
        },
        10: {
            "name": "Test Overlap 1: (3,3) (3,3) (4,4)",
            "input_file": "tests/test10.txt",
            "output_file": "tests/test10-out.txt",
            "points": 5
        },
        11: {
            "name": "Test Overlap 2: (1,1) (4,4) (4,4)",
            "input_file": "tests/test11.txt",
            "output_file": "tests/test11-out.txt",
            "points": 5
        },
    }

    def run_script_and_capture_output(self, script_path, input_data):
        """
        Runs the student's script and captures output.
        """
        try:
            result = subprocess.run(
                ["python", script_path],
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

    def run_single_test(self, test_number, name, input_file, output_file, points):
        """
        Runs and evaluates a single test case.
        """
        script_path = "pa1.py"
        if not os.path.exists(script_path):
            self.fail(f"Missing solution file: {script_path}")

        self.assertTrue(os.path.exists(input_file), f"Missing input: {input_file}")
        self.assertTrue(os.path.exists(output_file), f"Missing output: {output_file}")

        with open(input_file, 'r') as f:
            input_data = f.read()

        with open(output_file, 'r') as f:
            expected_output = f.read().strip()

        actual_output = self.run_script_and_capture_output(script_path, input_data)

        with self.subTest(test_number=test_number, name=name, points=points):
            self.assertEqual(actual_output, expected_output,
                             msg=(f"\n--- Test {test_number}: {name} ({points} pts) ---\n"
                                  f"Input:\n{input_data}\n"
                                  f"Expected Output:\n{expected_output}\n"
                                  f"Actual Output:\n{actual_output}\n"))

    def test_all(self):
        """
        Runs all test cases defined in the test_cases dictionary.
        """
        for test_number, data in self.test_cases.items():
            self.run_single_test(
                test_number,
                data.get("name", f"Test {test_number}"),
                data["input_file"],
                data["output_file"],
                data.get("points", 1)
            )


if __name__ == '__main__':
    unittest.main()
