"""
GREP Plugin for DoS Failure to Release Resources (OWASP-DS-007)
https://www.owasp.org/index.php/Testing_for_DoS_Failure_to_Release_Resources_%28OWASP-DS-007%29
NOTE: GREP plugins do NOT send traffic to the target and only grep the HTTP Transaction Log
"""

from owtf.dependency_management.dependency_resolver import ServiceLocator


DESCRIPTION = "Searches transaction DB for timing information"


def run(PluginInfo):
    return ServiceLocator.get_component("plugin_helper").FindTopTransactionsBySpeed()
