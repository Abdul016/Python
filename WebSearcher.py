import WebParser
from datetime import datetime

def webSearcher(data_list):
        newDataList = {str(i+1): data_list[i].lower().split() for i in range(0, len(data_list))}
        Query = str(input("Enter Your Word:"))
        queryList = list(set(Query.lower().split()))
        t1 = datetime.now()
        if ('or' in queryList and 'and' not in queryList):
            queryList.remove('or')
            print ("Performing OR search for:" + ('\t').join(queryList))
            for key,value in newDataList.items():
                for word in queryList:
                    if word in value:
                        found = True
                        print("Found At " + str(key)+'  ' +  data_list[int(key)]  )
                        break
            if found == False:
                    print ("None")
        else:
            if ('and' in queryList and 'or' not in queryList):
                queryList.remove('and')
            elif ('and' in queryList and 'or' in queryList):
                queryList.remove('and')
                queryList.remove('or')
            else:
                queryList = queryList
            print ("Performing AND search for:" + ('\t').join(queryList))
            for key,value in newDataList.items():
                for word in queryList:
                    if word not in value:
                        flag = False
                        break
                    else: flag = True
                if flag == True:
                    found_once = True
                    print("Found At " + str(key)+'  ' +  data_list[int(key)] )
            if flag == False:
                    print ("None")
        t2 = datetime.now()
        print("Execution time:", t2.microsecond-t1.microsecond)


def webSearchCall():
    web_data = WebParser.webData()
    webSearcher(web_data)
