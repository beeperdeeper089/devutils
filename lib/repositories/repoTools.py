import sys
import os

class RepoTools(object):
    def __init__(self, gitBaseUrl, targetGitHubUser, workingDirectory):
        self.targetUser = targetGitHubUser
        self.gitBaseUrl = gitBaseUrl
        self.repoWorkingDir = workingDirectory
        print ("RepoTools Initialised!")

    def clone(self, repoNames):
        os.chdir(self.repoWorkingDir)
        os.mkdir(self.targetUser)
        os.chdir(self.repoWorkingDir + "/" + self.targetUser)

        for repo in repoNames:
            os.system("git clone " + self.gitBaseUrl + self.targetUser + "/" + repo + ".git" + " " + repo)
