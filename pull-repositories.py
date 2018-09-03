import os

print ( "------------------ CONFIGURING ------------------" )
print ( "The Current Scripts Working Directory is: " + os.path.dirname(os.path.realpath(__file__)) ) # Print out the file's working directory. 

os.chdir( str( os.path.dirname( os.path.realpath(__file__) ) + "/../"  ) ) # Change dir to one above the File's Working Dir.

print ( "Repositories will be cloned into: " + os.getcwd() ) # Get the new working dir and print it out.

phab_base_uri = "https://phab.qub3d.tk"
print ( "The Phabricator Base URI is: " + phab_base_uri )

print ( "------------------ PULLING/UPDATING REPOSITORIES ------------------" )



