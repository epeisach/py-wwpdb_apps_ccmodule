##
# File:    ChemCompDpUtilityTests.py
# Date:    25-Feb-2021
#
# Updates:
# 25-Feb-2021 wmb Testing some ligand lite operations migrated to the backend
##

__docformat__ = "restructuredtext en"
__author__    = "Weslley Morellato Bueno"
__email__     = "wbueno@ebi.ac.uk"
__license__   = "Creative Commons Attribution 3.0 Unported"
__version__   = "V1.0"

import sys, unittest, traceback
import time, os, os.path
from wwpdb.apps.ccmodule.utils.ChemCompDpUtility import ChemCompDpUtility, ChemCompDpInputs

class ChemCompDpUtilityTests(unittest.TestCase):
    """This class tests the API for requesting files generated by
    the chemical components report.
    """

    def setUp(self):
        self.__verbose = False
        self.__lfh = sys.stderr
        self.__topPath = os.getenv('WWPDB_CCMODULE_TOP_PATH')
        
        self._ccDpUtility = ChemCompDpUtility('D_800004', self.__verbose, self.__lfh)
        self._ccAssignFile = os.path.join(os.path.dirname(__file__), 'fixtures', 'D_800004_cc-assign_P1.cif.V1')
        self._testCcInstanceFilePath = os.path.join(os.path.dirname(__file__), 'fixtures', '1_H_0G7_701_.cif')

    def test_process_cc_assign(self):
        # missing cc assign file
        with self.assertRaises(RuntimeError):
            self._ccDpUtility._processCcAssignFile()

        self._ccDpUtility.addInput(ChemCompDpInputs.FILE_CC_ASSIGN, '/tmp/foobar')
        with self.assertRaises(IOError):
            self._ccDpUtility._processCcAssignFile()
    
    def test_gen_report_data(self):
        # testing experimental instance reports
        self._ccDpUtility._genLigandReportData('1_H_0G7_701_', self._testCcInstanceFilePath, 'exp')

        repPath = os.path.join(self._ccDpUtility._ccReportPath, '1_H_0G7_701_', 'report')
        self.assertTrue(os.path.exists(os.path.join(repPath, '1_H_0G7_701__report.html')))
        self.assertTrue(os.path.exists(os.path.join(repPath, '1_H_0G7_701_.cif')))
        self.assertTrue(os.path.exists(os.path.join(repPath, 'report.log')))

        with self.assertRaises(Exception):
            # just expect a generic exception
            self._ccDpUtility._genLigandReportData('1_H_0G7_701_', '/fake/path', 'exp')
        
        # testing reference reports

        self._ccDpUtility._genLigandReportData('0G7', None, 'ref')

        repPath = os.path.join(self._ccDpUtility._ccReportPath, 'rfrnc_reports', '0G7')
        self.assertTrue(os.path.exists(os.path.join(repPath, '0G7_report.html')))
        self.assertTrue(os.path.exists(os.path.join(repPath, '0G7_ideal.cif')))
        self.assertTrue(os.path.exists(os.path.join(repPath, 'report.log')))

        with self.assertRaises(Exception):
            # just expect a generic exception
            self._ccDpUtility._genLigandReportData('---', None, 'ref')

    @unittest.skip
    def test_do_analysis(self):
        self._ccDpUtility.addInput(ChemCompDpInputs.FILE_CC_ASSIGN, self._ccAssignFile)
        self._ccDpUtility.doAnalysis()
    
if __name__ == '__main__':
    unittest.main()