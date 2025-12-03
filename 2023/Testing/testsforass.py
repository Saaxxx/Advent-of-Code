from datetime import datetime

i = "3/1/2012 16:00:00"

j = "2/16/2012 16:56:15"

print(datetime.strptime(i, '%m/%d/%Y %H:%M:%S') - datetime.strptime(j, '%m/%d/%Y %H:%M:%S'))

l = [0,1,2,3,4,5,6,7,8,9]
print(max(l[-3::]))