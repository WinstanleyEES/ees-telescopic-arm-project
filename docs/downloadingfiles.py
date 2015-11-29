import urllib2, os

urls = ["https://raw.githubusercontent.com/WinstanleyEES/ees-telescopic-arm-project/master/docs/client.py", "https://raw.githubusercontent.com/WinstanleyEES/ees-telescopic-arm-project/master/docs/launcher.sh"]

def check_for_updates(u) :
	for url in u :
		try :
			fnametocheck = "downloads/TMP_" + url.split('/')[-1]
			fnameoriginal = "downloads/" + url.split('/')[-1]
			
			u = urllib2.urlopen(url)
			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			
			fnew = open(fnametocheck, "w")
			foriginal = open(fnameoriginal, "r")
			
			foriginaldata = foriginal.read().split("\n")
			
			file_size_dl = 0
			block_size = 256
			while True:
				data = u.read(block_size)
				if not data:
					break

				file_size_dl += len(data)
				fnew.write(data)
			fnew.close()
			fnew = open(fnametocheck, "r")
			fnewdata = fnew.read().split("\n")
			
			# check the lengths of the files
			if (len(foriginaldata) == len(fnewdata)) :
				for data in xrange(0, len(foriginaldata)) :
					if foriginaldata[data] != fnewdata[data] :
						update = True
						break
					else :
						update = False
			else :
				update = True
				
			fnew.close()
			foriginal.close()
			
			if update :
				print "Files out of date - update required"
			else :
				print "Files up to date - no update requred"
				os.remove(fnametocheck)
		except :
			print "Sorry the file '{0}' wasn't found - try downloading the file with the download command.".format(fnameoriginal.split('/')[-1])
			fnew.close()
			os.remove(fnametocheck)
		
		
def download_files(u, d) :
	for url in u :
		file_name = "downloads/" + url.split('/')[-1]
		u = urllib2.urlopen(url)
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		f = open(file_name, "w")
		
		print "Downloading: {0} Bytes: {1}".format(file_name, file_size)
		
		file_size_dl = 0
		block_size = 16
		while True:
			data = u.read(block_size)
			if not data:
				break

			file_size_dl += len(data)
			f.write(data)
			
			status = round(file_size_dl * 100. / file_size, 2)
			print "\tDownloaded: {0} [{1}% : 100.0%] ".format(file_size_dl, status) + "\r",

		f.close()
		print "\n\t{0} has finished downloading.\n".format(file_name.split('/')[-1])
		
def merge_files(u) :
	for url in u :
		try :
			fnametocheck = "downloads/TMP_" + url.split('/')[-1]
			fnameoriginal = "downloads/" + url.split('/')[-1]
			
			u = urllib2.urlopen(url)
			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			
			fnew = open(fnametocheck, "r")
			foriginal = open(fnameoriginal, "w")
			
			fnewdata = fnew.read()		
			foriginal.write(fnewdata)
				
			fnew.close()
			foriginal.close()
			
			os.remove(fnametocheck)
		except :
			pass
			
	print "All files are up to date"