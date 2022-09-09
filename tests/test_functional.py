# import sys, os
# sys.path.append("..")
import unittest
import mysql.connector
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'
#test_qry = open(os.path.dirname(os.path.realpath(__file__)) + "/fE4kl5sQvr.txt").readlines()
dataBase = mysql.connector.connect(
                         host = "localhost",
                         user = "root",
                         passwd = "pwd",
                         database = "employees")

from tests.TestUtils import TestUtils
# preparing a cursor object

class FuctionalTests(unittest.TestCase):
    '''def __init__(self):

        self.dataBase = mysql.connector.connect(
                         host = "localhost",
                         user = "root",
                         passwd = "pwd",
                         database = "employees")
        test_qry = open(os.path.dirname(os.path.realpath(__file__)) + "/fE4kl5sQvr.txt").readlines()

    def __del__(self):

        self.dataBase.close()'''

    def test_query1(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view1"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()

            query2 = test_qry[0]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery1", True, "functional")
                print("TestQuery1 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery1", False, "functional")
                print("TestQuery1 = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery1", False, "functional")
            print("TestQuery1 = Failed")
        assert passed

    def test_query2(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view2"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()

            query2 = test_qry[1]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery2", True, "functional")
                print("TestQuery2 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery2", False, "functional")
                print("TestQuery2 = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery2", False, "functional")
            print("TestQuery2 = Failed")
        assert passed

    def test_query3(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view3"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()

            query2 = test_qry[2]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery3", True, "functional")
                print("TestQuery3 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery3", False, "functional")
                print("TestQuery3 = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery3", False, "functional")
            print("TestQuery3 = Failed")
        assert passed

    def test_query4(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view4"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()

            query2 = test_qry[3]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery4", True, "functional")
                print("TestQuery4 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery4", False, "functional")
                print("TestQuery4 = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery4", False, "functional")
            print("TestQuery4 = Failed")
        assert passed

    def test_query5(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view5"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()
            query2 = test_qry[4]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery5", True, "functional")
                print("TestQuery5 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery5", False, "functional")
                print("TestQuery5 = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery5", False, "functional")
            print("TestQuery5 = Failed")
        assert passed

    def test_query6(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view6"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()
            query2 = test_qry[5]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery6", True, "functional")
                print("TestQuery6 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery6", False, "functional")
                print("TestQuery6= Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery6", False, "functional")
            print("TestQuery6 = Failed")
        assert passed

    def test_query7(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view7"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()
            query2 = test_qry[6]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery7", True, "functional")
                print("TestQuery7 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery7", False, "functional")
                print("TestQuery7 = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery7", False, "functional")
            print("TestQuery7 = Failed")
        assert passed

    def test_query8(self):
        test_obj = TestUtils()
        try:
            query1 = "SELECT * FROM view8"
            cursorObject = dataBase.cursor()
            cursorObject.execute(query1)
            result1 = cursorObject.fetchall()
            query2 = test_qry[7]
            cursorObject.execute(query2)
            result2 = cursorObject.fetchall()
            if result1 == result2:
                passed = True
                test_obj.yakshaAssert("TestQuery8", True, "functional")
                print("TestQuery8 = Passed")
            else:
                passed = False
                assert passed
                test_obj.yakshaAssert("TestQuery8", False, "functional")
                print("TestQuery8 = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestQuery8", False, "functional")
            print("TestQuery8 = Failed")
        assert passed

FuctionalTests()
