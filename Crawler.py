import urllib2
import datetime
import sys

def download_nyc_rawdata(db, untilYear):
	db = str(db)
	if db != "yellow" and db != "green" and db != "fhv":
		print('Ungueltige Datenbasis!\nVerfuegbare Optionen:\n -green\n -yellow\n -fhv\n')
		return
	untilYear = int(untilYear)
	now = datetime.datetime.now()
	dir = "/home/hadoop/Import/"+db+"/"+db
	print(db, untilYear,now.month,now.year)
	urlRoot = "https://s3.amazonaws.com/nyc-tlc/trip+data/"
	if untilYear == now.year:
		for x in range (1,now.month):
			if x > 10:
				date = str(now.year)+"-"+str(x)
			else:
				date = str(now.year)+"-0"+str(x)
			csvUrl = urlRoot+db+"_tripdata_"+date+".csv"
			print (csvUrl)
			try:
				response = urllib2.urlopen(csvUrl)
			except urllib2.HTTPError, e:
				print(e.code,"NYC Rohdaten nicht auf aktuellem Stand.")
				fx.close()
				return
			csv = response.read()
			csv_str = str(csv)
			lines = csv_str.split("\\n")
			dest_url = r''+dir+".csv"
			fx = open(dest_url, "a")
			for line in lines:
				fx.write(line + "\n")
			fx.close()
	elif untilYear <= now.year:
                for x in range (1,12):
			if x > 10:
                                date = str(untilYear)+"-"+str(x)
                        else:
                                date = str(untiYear)+"-0"+str(x)
                        csvUrl = urlRoot+db+"_tripdata_"+date+".csv"
                        print (csvUrl)
                        response = urllib2.urlopen(csvUrl)
                        csv = response.read()
                        csv_str = str(csv)
                        lines = csv_str.split("\\n")
                        dest_url = r''+dir+".csv"
                        fx = open(dest_url, "a")
                        for line in lines:
                                fx.write(line + "\n")
                        fx.close()
	else:
		print("Falsche Jahresangabe.")

print (sys.argv[1],sys.argv[2])
download_nyc_rawdata(sys.argv[1],sys.argv[2])
print sys.argv
