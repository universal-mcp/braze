from unittest.mock import MagicMock

import pytest
from universal_mcp.utils.testing import (
    check_application_instance,
)

from universal_mcp_braze.app import BrazeApp

@pytest.fixture
def app_instance():
    mock_integration = MagicMock()
    mock_integration.get_credentials.return_value = {"access_token": "dummy_access_token"}
    return BrazeApp(integration=mock_integration)

def test_application(app_instance):
    check_application_instance(app_instance, app_name="braze")
