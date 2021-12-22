from git import Repo

PATH_OF_GIT_REPO = r'/Users/polee/IdeaProjects/gitpython-test/.git'

COMMIT_MESSAGE = 'test the first commit'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)

        origin = repo.remote(name='origin')
        repo.git.pull('origin', 'master')
        repo.git.push('origin', 'master')

    except:
        print('Some error occurred while pushing the code')

git_push()