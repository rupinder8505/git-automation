import os
from git import Repo

repo_path = os.environ.get("REPO_PATH")

if not repo_path:
    raise("REPO_PATH env variable is required")

repo = Repo(repo_path)
git = repo.git

if "my_new_branch" not in git.branch():
    git.checkout("HEAD", b="my_new_branch")  # create a new branch
git.branch("another-new-one")
import pdb; pdb.set_trace()
git.branch("-D", "another-new-one")  # pass strings for full control over argument order