from datetime import datetime


def searchQuery(data_arr):
    query = str(input("Enter Query:"))
    searchlist = list(set(query.lower().split()))
    dt1 = datetime.now()
    if ('or' in searchlist and 'and' not in searchlist):
        searchlist.remove('or')
        print ("Performing OR search for:" + ('\t').join(searchlist))
        for quote in data_arr:
            for word in searchlist:
                found_at = quote[1].find(word)
                if found_at>0:
                    found_once = True
                    print("Found At " + quote[0]+" "+quote[2]+" "+quote[3])
                    break
        if found_once == False:
                print ("Query Not Found")
    else:
        if ('and' in searchlist and 'or' not in searchlist):
            searchlist.remove('and')
        elif ('and' in searchlist and 'or' in searchlist):
            searchlist.remove('and')
            searchlist.remove('or')
        else:
            searchlist = searchlist
        print ("Performing AND search for:" + ('\t').join(searchlist))
        for quote in data_arr:
            for word in searchlist:
                found_at = quote[1].find(word)
                if found_at == -1:
                    flag = False
                    break
                else: flag = True
            if flag == True:
                found_once = True
                print("Found At " + quote[0]+" "+quote[2]+" "+quote[3])
        if flag == False:
                print ("Query Not Found")
                            
    dt2= datetime.now()
    print("Execution time:", dt2.microsecond-dt1.microsecond)
