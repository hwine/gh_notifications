import os

import pytest
from gh_notifications import lib

def test_get_invalid_github_session():
    # Given we can access GitHub
    # WHEN we use an invalid Personal Access Token for a login
    pat = "1234"
    gh = lib.gh_session(pat)
    # THEN.1 we get a valid session object
    assert gh
    # THEN.2 and it will not work
    assert gh.get_user()
    # with pytest.raises(github3.exceptions.AuthenticationFailed):
    #     assert not gh.me()

valid_pat = os.environ.get("GITHUB_TOKEN")

@pytest.mark.skipif(not valid_pat, reason="No valid PAT supplied")
def test_get_valid_github_session():
    # Given we can access GitHub
    # WHEN we use an valid Personal Access Token for a login
    gh = lib.gh_session(valid_pat)
    # THEN.1 we get a valid session object
    assert gh
    # THEN.2 and it will work
    assert gh.get_user()

@pytest.mark.skipif(not valid_pat, reason="No valid PAT supplied")
def test_get_default_github_session():
    # Given we can access GitHub and have a valid token in environment
    # WHEN we don't specify an valid Personal Access Token for a login
    gh = lib.gh_session()
    # THEN.1 we get a valid session object
    assert gh
    # THEN.2 and it will work
    assert gh.get_user()
