import unittest
# import sys, os
# sys.path.append("..")
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_exception_revised.txt'

from tests.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_dummy_exceptional_testcase(self):
        test_obj = TestUtils()
        try:
            test_obj.yakshaAssert("TestDummyExceptionalTestCases", True, "exception")
            print("TestDummyExceptionalTestCases = Passed")
        except:
            test_obj.yakshaAssert("TestDummyExceptionalTestCases", False, "exception")
            print("TestDummyExceptionalTestCases = Failed")
