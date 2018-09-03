import sys
import os
from lib.repositories.repoTools import RepoTools

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
print ( "Cloning from: " + targetGitHubUsername )

print ( "The Current Scripts Working Directory is: " + os.path.dirname(os.path.realpath(__file__)) ) # Print out the file's working directory. 

newDir = str( os.path.dirname( os.path.realpath(__file__) ) + "/../" )
print ( "Destination: " + newDir ) # Get the new destination dir and print it out.

githubBaseUrl = "https://github.com/"
print ( "The GitHub Base URI is: " + githubBaseUrl)

repoWorker = RepoTools(githubBaseUrl, targetGitHubUsername, newDir)

print ( "------------------ STARTING ACTION: %s ------------------" % gitAction.upper() )


if gitAction == "clone" and targetGitHubUsername == "qub3d":
	repositoriesToClone = ["qub3d-libdeps", "qub3d-engine", "qub3d-devdocs", "website", 
	"sandblox-launcher", "sandblox-client", "sandblox-server", "sandblox-marketplace" ]

	repoWorker.clone(repositoriesToClone)