#!/usr/bin/python
import urllib2, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--download", nargs="+", help="Downloads the client files from GitHub by urls to the raw data")
parser.add_argument("-u", "--update", nargs="+", help="Checks if the users files are up to date with the GitHub files by urls to the raw data")
parser.add_argument("-m", "--merge", action="store_true", help="Merges the new temporary file with the original file")
args = parser.parse_args()

urls = []
Downloading = False
Updating = False
Merging = False

if args.download :
	Downloading = True
	for i in args.download :
		if i != "-m" or i != "-u" :
			urls.append(i)
		else :
			break
else :
	Downloading = False
	
if args.update :
	Updating = True
	for i in args.update :
		if i != "-d" or i != "-m" :
			urls.append(i)
		else :
			break
else :
	Updating = False
	
if args.merge :
	Merging = True
else :
	Merging = False

def download_files(u, downloading) :
	if downloading :
		print "[+] downloading the files"
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
	else :
		pass

def check_for_updates(u, updating) :
	if updating :
		print "[+] updating the files"
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
	else :
		pass
		
def merge_files(u, merging) :
	if merging :
		print "[+] merging the files"
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
	else :
		pass
	
	
def main(d, u, m) :
	download_files(urls, d)
	check_for_updates(urls, u)
	merge_files(urls, m)
	
main(Downloading, Updating, Merging)