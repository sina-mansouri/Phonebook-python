import mysql.connector
import time

#get start time for calculate execution time
start_time = time.time()

#date of report
start_date = 'Date1'
end_date = 'Date2'

list = {"azarbayejan_east", "azarbayejan_west", "ardebil","esfahan", "charmahalbakhtyari", "ilam", "markazi", "hamedan", "lorestan", "tehran", "alborz", "ghom", "ostan_khorasan", "kermanshah", "fars", "bushehr", "north_ostan_khorasan", "south_ostan_khorasan", "khuzestan", "khuzestan","kohgiloyevbourahmad", "zanjan", "ghazvin", "semnan", "systanvbalouchestan", "kordestan","kerman", "golestan","gilan", "mazandaran", "hormozgan", "yazd"}


#database connection data
host = 'IP Target'
user = 'Username'
passwd = 'Password'
database = 'Name of DB'

#database command for reporting any status of messages
total_command = 'select count(*), status from outbounds where date(creation_date) between \'' + start_date + '\' and \'' + end_date + '\' and username=\''
smsoper1_command = 'select count(*),status from outbounds where date(creation_date) between \'' + start_date + '\' and \'' + end_date + '\' and smsoper(dest_mobile_number)=1 and username=\''

#database connection command
mydb = mysql.connector.connect (host = host, user = user, passwd = passwd, database = database)
mycursor = mydb.cursor ()

#global variables
counter = 0
total = 0

for line in list :
	#percent calculation
	counter = counter + 1
	print ('percent : ' + str ((counter * 100) / len (list)))
	
	#printing of data readed in for loop
	print (line + " : ")
	query_time = time.time()
	mycursor.execute (total_command + line + '\' group by 2')
	total_myresult = mycursor.fetchall ()
	print (total_myresult)
	if (len(total_myresult) != 0) :
		for cnt in range(len(total_myresult)) :
			total = total + total_myresult[cnt][0]
		print ("total : " + str(total) + "\n")
		print ("smsoper1 count of status :\n")
		mycursor.execute (mci_command + line + '\' group by 2')
		mci_myresult = mycursor.fetchall ()
		print (mci_myresult)
		#nosmsoper1_myresult = total_myresult[0] - smsoper1_myresult[0]
	print ("execution of query time (seconds) : %s" % (time.time() - query_time))
	print ("execution time (seconds) : %s" % (time.time() - start_time))

#	total_dict.update( {line : {"total" : total, "test" : "test1"}} )
#	print (total_dict)

#for key, value in total_dict.items():
#	writer.writecol([key, value])

result_file.close()

print ("Done")
