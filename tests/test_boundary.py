import unittest
# import sys, os
# sys.path.append("..")
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_boundary_revised.txt'
from tests.TestUtils import TestUtils
class BoundaryTest(unittest.TestCase):
    def test_dummy_boundary_testcase(self):
        test_obj = TestUtils()
        try:
            test_obj.yakshaAssert("TestDummyBoundaryTestCases",True,"boundary")
            print("TestDummyBoundaryTestCases = Passed")
        except:
            test_obj.yakshaAssert("TestDummyBoundaryTestCases",False,"boundary")
            print("TestDummyBoundaryTestCases = Failed")
