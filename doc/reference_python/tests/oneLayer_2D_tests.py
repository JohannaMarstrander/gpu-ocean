import unittest
import sys
import time

import xmlrunner
# install xmlrunner by
# $ sudo easy_install unittest-xml-reporting

#import testUtils
from schemes.FBLtest import FBLtest
from schemes.CTCStest import CTCStest
from schemes.CDKLM16test import CDKLM16test

# In order to format the test report so that Jenkins can read it:
jenkins = False
if (len(sys.argv) > 1):
    if (sys.argv[1].lower() == "jenkins"):
        jenkins = True

if (jenkins):
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))


# Define the tests that will be part of our test suite:
test_classes_to_run = [FBLtest, CTCStest] #, CDKLM16test]
#test_classes_to_run = [CDKLM16test]

loader = unittest.TestLoader()
suite_list = []
for test_class in test_classes_to_run:
    suite = loader.loadTestsFromTestCase(test_class)
    suite_list.append(suite)

big_suite = unittest.TestSuite(suite_list)
unittest.TextTestRunner(verbosity=2).run(big_suite)
