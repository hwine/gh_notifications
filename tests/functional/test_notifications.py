import os
import pytest

from gh_notifications import lib

valid_pat = os.environ.get("GITHUB_TOKEN")

@pytest.mark.skipif(not valid_pat, reason="No valid PAT supplied")
def test_list_notifications():
    # GIVEN: a valid pat
    # WHEN: notifications are requested
    gh = lib.gh_session(valid_pat)
    lib.list_notifications(gh)

    # THEN.1: the command succeeds
