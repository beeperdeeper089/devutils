import os


class Settings:

    def __init__(self, settingsFileName):
        self.fileName = settingsFileName

    def parseRepoList(self):
        # Open the file and initialise a self variable as a list/array
        fileHandle = open(self.fileName, "r")
        self.repoList = []

        # Go through every line, checking if there is a # at the front
        # and ignore all lines starting with a #
        for line in fileHandle:
            if not line[0] == '#':
                # Append the line onto the array if there isn't a # at the front
                # And strip the newline character from the end of every line.
                self.repoList.append(line.rstrip('\n'))

        # Close the file afterwards.
        fileHandle.close()