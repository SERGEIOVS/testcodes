file = open('test.txt','r')
timefile = open('data.txt','w')
file1=file.readlines()

datelist =[]
iplist =  []
resultList=[]
maclist = []

for i in file1:
    
    date , time , ip , result , mac = i.split(' ')[0] + "'" ,  "'" + i.split(' ')[1] , i.split(',')[1] , i.split(',')[2],i.split(',')[3]
    
    
    #print('|','date = ' , date + '   |   ','time : ' + time , ' | ','ip = ' , ip, '   |   ','result : ' , result , '   |   ','mac : ', mac,'|')
    
    datefile = open('data.txt','w')
    print('Обработка ... ')
    datefile.write( 'date = '+ str(date) + ',' + 'time' + str(time) + ',' +'ip = ' + str(ip) +','+'res = ' + str(result) + ',' + 'mac = ' + str(mac) )

    #print('ip0 = ' + ip.split('.')[0] + "'" , 'ip0 = ' , ip.split('.')[1] + "'" , 'ip0 = ' + ip.split('.')[2] , "'")
    print()
    print()
    
    datelist.append(date)
    iplist.append(ip)
    resultList.append(result)
    maclist.append(mac)


print( len(datelist) , len(iplist) , len(resultList) , len(maclist) )
print(datelist)

print('-----')
print('DONE!')
print('-----')
