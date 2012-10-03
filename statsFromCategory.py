import wikipedia
from category_customized import CategoryListifyRobot
import datetime
import shutil

#mode list or category change to declare
categoryNotList = False

#setup
editsByMonthFrame = {}

now = datetime.datetime.now()
nowMonthsSinceJan2001 = ((now.year - 2001)*12) + now.month

enwp = wikipedia.Site('en', 'wikipedia')

if categoryNotList: #use the categoryListifyRobot
    category = 'Pulitzer Prize winners'
    catList = CategoryListifyRobot(category, category, '',subCats = False).run()
    catList = catList.split('\n')[:-1]#removing the end value for some reason it's included
else: #manual entry
    category = "Manual list"
    catList = ('Barack Obama', 'Mitt Romney')
#'Barack Obama', 'Mitt Romney', 'Al Gore', 'George W. Bush', 'John Kerry', 'John McCain'
#helpers
def dictZeroer(dct):
    for i in range(0,nowMonthsSinceJan2001+1):
        dct[int(i)] = 0
    return dct

def monthify(verHist):
    """Takes in a versionHistory list and returns a dict whose 
    key is months since Jan 2001. (Jan 2001 = 1, Jan 2002 = 13, etc.) 
    and whose value is number of edits in that month """
    editsByMonth = dictZeroer({})
    for ver in verHist:
        timestamp = ver[1]
        #convert into month
        year = int(timestamp[:4]) - 2001
        month = int(timestamp[5:7])
        absMonth = (year * 12) + month
        editsByMonth[int(absMonth)] += 1
    return editsByMonth

def Rstr(ls):
    returnstr = ''
    for l in ls:
        l = str(l)
        l = l.replace (" ", "_")
        returnstr += l+' '
    return returnstr

def removeSpecialChars(listOfCats):
    """Removes special chars that are in Wikipedia article titles which R cannot allow as variable names. And eliminates spaces."""
    returnstr = ''
    for cat in listOfCats:
        cat = str(cat)
        cat = cat.translate(None, "',.():")
        cat = cat.replace(' ', '_')
        returnstr += cat+' '
    return returnstr
def RdataFrameify(editsByMonth):
    editsByMonthFile = open(str(category)+'.txt', 'w+')
    #write header
    editsByMonthFile.write('MonthsSinceJan2001 ')
    articleTitles = removeSpecialChars(editsByMonth.keys())
    editsByMonthFile.write(articleTitles + '\n')
    #write values acrosswise
    for i in range(0,nowMonthsSinceJan2001):
        editsByMonthFile.write(str(i)+' ')
        row = ''
        for j in editsByMonth:
            row += str(editsByMonth[j][i]) 
            row += ' '
        row.rstrip()
        editsByMonthFile.write(row)
        editsByMonthFile.write('\n')
    editsByMonthFile.close()
        
    
    

for page in catList:
        print 'working...'
        verHist = wikipedia.Page(enwp,page).getVersionHistory(forceReload=False, reverseOrder=False,
                          getAll=True, revCount=500)
        editsByMonthFrame[page] = monthify(verHist)


RdataFrameify(editsByMonthFrame)
shutil.copy(str(category)+'.txt', 'forR.txt') #copy to make our forR.txt file
print 'Finished. Something for you to eyeball: "'+ str(category)+'.txt"'
        
        
