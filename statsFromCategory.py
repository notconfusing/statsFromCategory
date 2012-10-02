import wikipedia
from category import CategoryListifyRobot
import datetime
import shutil



#setup
editsByMonthFrame = {}

now = datetime.datetime.now()
nowMonthsSinceJan2001 = ((now.year - 2001)*12) + now.month

enwp = wikipedia.Site('en', 'wikipedia')

category = 'Black feminism books'


#catList = CategoryListifyRobot(category, category, '',subCats = False).run()
#catList = catList.split('\n')[:-1]


#manual entry
catList = ('The Hunger Games','Steve Jobs (book)', 'Fifty Shades of Grey', 'A Game of Thrones', 'The Help', 'Thinking, Fast and Slow', "Quiet: The Power of Introverts in a World That Can't Stop Talking")

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

def RdataFrameify(editsByMonth):
    editsByMonthFile = open(str(category)+' edits By Month.txt', 'w+')
    #write header
    editsByMonthFile.write('MonthsSinceJan2001 ')
    editsByMonthFile.write(Rstr(editsByMonth.keys()) + '\n')
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
    editsByMonthFile.close
    #Copy for automation
    shutil.copy2(str(category)+' edits By Month.txt', 'forR.txt')
        
    
    

for page in catList:
        print 'working...'
        verHist = wikipedia.Page(enwp,page).getVersionHistory(forceReload=False, reverseOrder=False,
                          getAll=True, revCount=500)
        editsByMonthFrame[page] = monthify(verHist)


RdataFrameify(editsByMonthFrame)
print 'Finished. Something for you to eyeball: '+ str(category)+' edits By Month.txt"'
        
        
