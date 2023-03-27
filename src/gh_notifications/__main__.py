from gh_notifications import lib as ghn_lib

gh = ghn_lib.gh_session()
ghn_lib.list_notifications(gh)
