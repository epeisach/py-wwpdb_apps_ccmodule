import os
import sys
import tempfile
import unittest
from unittest.mock import patch, Mock, MagicMock

sessions_top_dir = tempfile.mkdtemp()
config_info = {
    'SITE_DEPOSIT_STORAGE_PATH': tempfile.mkdtemp(),
    'SITE_PREFIX': 'PDBE_LOCALHOST',
    'SITE_WEB_APPS_TOP_SESSIONS_PATH': sessions_top_dir,
    'SITE_WEB_APPS_SESSIONS_PATH': os.path.join(sessions_top_dir, 'sessions'),
}

config_info_mock_config = {
    'return_value': config_info,
}

config_mock = MagicMock(**config_info_mock_config)

sys.modules['wwpdb.utils.config.ConfigInfo'] = Mock(ConfigInfo=config_mock)

from wwpdb.apps.ccmodule.utils import Exceptions
from wwpdb.apps.ccmodule.utils.LigandAnalysisState import LigandAnalysisState

class ReportFilesRequestTest(unittest.TestCase):
    '''This class tests the API for requesting files generated by
    the chemical components report.

    '''
    def setUp(self):
        self._lfh = sys.stderr
        self._verbose = False

        self._lig_state = LigandAnalysisState()
    
    def test_read_progress(self):
        pass

    def test_update_progress(self):
        pass
    
    def test_notify_listeners(self):
        pass

    def test_get_ligand_state(self):
        pass