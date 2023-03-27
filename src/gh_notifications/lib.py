import os
from collections import defaultdict

from github import Github

def gh_session(pat:str = "") -> Github:
    # assume cred in environment if not supplied
    if not pat:
        pat = os.environ.get("GITHUB_TOKEN", "<bogus>")
    gh:Github = Github(pat)
    return gh

def list_notifications(gh:Github=None):
    me = gh.get_user()
    print(f"{me.login} has {me.get_notifications().totalCount} notifications.")
    notifications = me.get_notifications()

    notifications_by_repo = defaultdict(list)
    for notification in notifications:
        # group by repository
        full_name = notification.repository.full_name
        notifications_by_repo[full_name].append(notification)
        
    for repo, notes in notifications_by_repo.items():
        print(f"{repo} has {len(notes)} unread notifications:")
        for n in notes:
            print(f"   {n.subject.type}: {n.subject.title}")

