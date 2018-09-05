import sys
import os
from lib.repositories.repoTools import RepoTools
from lib.querying.query import QuestionUser


if len(sys.argv) > 2:
	targetGitHubUsername = sys.argv[2]
elif len(sys.argv) > 1:
	targetGitHubUsername = "qub3d"
else:
	raise Exception( "Usage: python3 main <option> <username of target>, where <option> is either 'clone' or 'pull'" )
	
if sys.argv[1] == 'clone':
	gitAction = "clone"
elif sys.argv[1] == 'pull':
	raise NotImplementedError("Pulling has not been implemented yet!")
else:
	raise Exception( "Invalid option, should be either 'clone' or 'pull'." )

print ( "------------------ CONFIGURING ------------------" )
print ( "Cloning from: " + targetGitHubUsername + "\'s Repositories!")

newDir = str( os.path.dirname( os.path.realpath(__file__) ) + "/../" )
print ( "Destination: " + newDir ) # Get the new destination dir and print it out.

githubBaseUrl = "https://github.com/"
print ( "The GitHub Base URI is: " + githubBaseUrl)

repoWorker = RepoTools(githubBaseUrl, targetGitHubUsername, newDir)

print ( "------------------ STARTING ACTION: %s ------------------" % gitAction.upper() )

if os.path.isdir(newDir + targetGitHubUsername):
	raise Exception("User repository Directory already exists, you may have already cloned, pulling instead!")

if gitAction == "clone":
	repositoriesToClone = ["devutils"]

	repoWorker.clone(repositoriesToClone)

questionCMake = "Would you like the respective CMake to be generated?"
if QuestionUser.query(questionCMake, "yes"):
	print("Generating CMake!")
