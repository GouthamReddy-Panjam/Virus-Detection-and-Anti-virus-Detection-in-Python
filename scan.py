#virus scan program
import re,glob,os,csv
#scan for signatures just like semantic or other antivirus software
def checkForSignatures():
print("#### checking for virus signatures #####")
programs = glob.glob("*.py")
for p in programs:
thisFileInfected=False
file = open(p,"r")
lines = file.readlines()
file.close()
for line in lines:
if(re.search("^#start",line)):
# found virus
print("!!!! virus found in file"+p)
thisFileInfected = True
if thisFileInfected == False:
print(p+"no virus")
print("#### end section ####")
def getFileData():
# get an intial scan of file size and data modified. save
programs = glob.glob("*.py")
programList=[]
for p in programs:
programSize= os.path.getsize(p)
programModified= os.path.getmtime(p)
programData=[p,programSize,programModified]
programList.append(programData)
return programList
def WriteFileData(programs):
if os.path.exists("fileData.txt"):
return
with open("fileData.txt","w") as file:
wr=csv.writer(file)
wr.writerows(programs)
def checkForChanges():
print("###### check for heuristic changes in files")
# open the fileData.txt file and compare each line
# to the current file size and dates
with open("fileData.txt") as file:
fileList=file.read().splitlines()
orginalFileList=[]
for each in fileList:
items = each.split(',')
orginalFileList.append(items)
# get current data from directory
currentFileList=getFileData()
#compare old and new
for c in currentFileList:
for o in orginalFileList:
if(c[0]==o[0]):
if str(c[1])!=str(o[1]) or str(c[2])!=str(o[2]):
print("File mismatch")
#print data of each file
print("current values= "+str(c))
print("orginal values= "+str(0))
else:
print("file "+c[0]+"appears to be unchanged")
print("##### finished checking for changes")
WriteFileData(getFileData())
checkForSignatures()
checkForChanges()