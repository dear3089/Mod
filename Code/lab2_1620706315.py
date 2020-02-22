from pandas import *
data = read_csv('files/pm25.csv')

df = DataFrame()
df['zone'] = data['ZONE']
df['pm2.5'] = data['PM2.5']

print("%-5s %-30s %s"%('AQI',' ','ZONE'))
for row in zip(df['zone'],df['pm2.5']):
    if row[1] > 300:
        print("%-5d %-30s %s"%(row[1],'Hazardous',row[0],))
        #Hazardous
    elif row[1] > 200:
        print("%-5d %-30s %s"%(row[1],'Very Unhealthy',row[0],))
        #Very Unhealthy
    elif row[1] > 150:
        print("%-5d %-30s %s"%(row[1],'Unhealthy',row[0],))
        #Unhealthy
    elif row[1] > 100:
        print("%-5d %-30s %s"%(row[1],'Unhealthy for Sensitive Groups',row[0],))
        #Unhealthy for Sensitive Groups
    elif row[1] > 50:
        print("%-5d %-30s %s"%(row[1],'Moderate',row[0],))
        #Moderate
    elif row[1] <=50:
        print("%-5d %-30s %s"%(row[1],'Good',row[0],))
        #Good

#testsss
#test@sadjkl;
#test
#tests
#testttttttt

#sadsadsadsad