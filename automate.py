import os
from git import Repo


repo_path = os.environ.get("REPO_PATH")
if not repo_path:
    raise("REPO_PATH env variable is required")

repo = Repo(repo_path)
git = repo.git

def make_changes_locally():
    with open("test.py","a") as file:
        file.write("#new sample test")

def create_new_branch(branch_name):
    if branch_name not in git.branch():
        git.checkout("HEAD", b=branch_name)
    else:
        print("Branch already exists")

def commit_and_push_changes(commit_message, branch_name):
    try:
        git.add("-A")
        git.commit("-m", commit_message)
        git.push("origin", branch_name)
    except Exception as e:
        print(e.message)
        raise e

def delete_branch(branch_name):
    git.branch("-D", branch_name)

def create_pr(title, body, source_branch, target_branch="main"):
    pass


branch_name = 'test'
commit_message = "commiting automate change"

make_changes_locally()
create_new_branch(branch_name)
commit_and_push_changes(commit_message, branch_name)
create_pr("testing", "automated PR", branch_name)

