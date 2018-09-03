import sys
import os

if len(sys.argv) > 2:
	targetGitHubUsername = sys.argv[2]
	print ( "Cloning from: " + gitUsernameToClone )
elif len(sys.argv) > 1:
	targetGitHubUsername = "qub3d"
	print ( "Cloning from qub3d" )
else:
	raise Exception( "Usage: python clone-repositories <option> <username of target>, where <option> is either 'clone' or 'pull'" )
	
if sys.argv[1] == 'clone':
	gitAction = "git clone "
elif sys.argv[1] == 'pull':
	gitAction = "git pull "
else:
	raise Exception( "Invalid option, option should be 'clone' or 'pull'." )

print ( "------------------ CONFIGURING ------------------" )
print ( "The Current Scripts Working Directory is: " + os.path.dirname(os.path.realpath(__file__)) ) # Print out the file's working directory. 

os.chdir( str( os.path.dirname( os.path.realpath(__file__) ) + "/../"  ) ) # Change dir to one above the File's Working Dir.
print ( "Destination: " + os.getcwd() ) # Get the new working dir and print it out.



githubBaseUrl = "https://github.com/" + targetGitHubUsername
print ( "The GitHub Base URI is: " + githubBaseUrl)

print ( "------------------ STARTING ACTION: %s ------------------" % gitAction.upper() )

os.system( gitAction + githubBaseUrl + "/Devutils devutils" )
os.system( gitAction + githubBaseUrl + "/qub3d-engine qub3d-engine" )
os.system( gitAction + githubBaseUrl + "/qub3d-render qub3d-renderer" )
os.system( gitAction + githubBaseUrl + "/qub3d-devdocs qub3d-devdocs" )
os.system( gitAction + githubBaseUrl + "/website qub3d-websites" )
os.system( gitAction + githubBaseUrl + "/sandblox-launcher sandblox-launcher" )
os.system( gitAction + githubBaseUrl + "/sandblox-client sandblox-client" )
os.system( gitAction + githubBaseUrl + "/sandblox-marketplace sandblox-marketplace" )
os.system( gitAction + githubBaseUrl + "/sandblox-server sandblox-server" )
