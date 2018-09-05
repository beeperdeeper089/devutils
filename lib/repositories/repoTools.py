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
<<<<<<< HEAD
        os.mkdir(self.targetUser)
        os.chdir(self.repoWorkingDir + "/" + self.targetUser)

=======
>>>>>>> e8adc52e9a659f1bdae08c6706cf85d3ac2fea52
        for repo in repoNames:
            os.system("git clone " + self.gitBaseUrl + self.targetUser + "/" + repo + ".git" + " " + repo)
