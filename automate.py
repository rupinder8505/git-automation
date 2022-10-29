import os
from git import Repo
import subprocess


repo_path = os.environ.get("REPO_PATH")
if not repo_path:
    raise("REPO_PATH env variable is required")

repo = Repo(repo_path)
git = repo.git

def make_changes_locally():
    with open("test.py","a") as file:
        file.write("#new sample test\n")

def create_new_branch(branch_name):
    if branch_name not in git.branch():
        git.checkout("HEAD", b=branch_name)
        print(f"{branch_name} branch created")
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
    print(f"commit has been pushed to remote branch {branch_name}")

def delete_branch(branch_name):
    git.branch("-D", branch_name)
    print(f"{branch_name} branch deleted")

def create_pr(title, body, source_branch, target_branch="main"):
    """
    NOTE: this method expects GH_TOKEN env variable to be set
    """
    if not os.environ.get("GH_TOKEN"):
        raise("GH token must be set")
    
    command = 'gh pr create --title {} --body "{}" --base {} --head {}'.format(title, body, target_branch, source_branch)

    try:
        resp = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print(resp)
    except Exception as e:
        print(f"Error occured: {e.output}\n\n")
        raise(e)
    



branch_name = 'test'
commit_message = "commiting automate change"

make_changes_locally()
create_new_branch(branch_name)
commit_and_push_changes(commit_message, branch_name)
create_pr("testing", "automated testing pull request", branch_name)

