import os, fnmatch, sys, getopt
 
dir_to_search = ''
search_pattern = ''

def showerror():
	print('\tCorrect usage is:')
	print ('\tfind.py -d <dir_to_search> -p <pattern_to_search>')
	sys.exit(2)

try:
	## Parsing option and argument variable 
	opts, args = getopt.getopt(sys.argv[1:],"hd:p:",["dir=","pattern="])
	# print(opts, args)
except getopt.GetoptError:
	showerror()
	
for opt, arg in opts:
	if opt == '-h':
		print ('find.py -d <dir_to_search> -p <pattern_to_search>')
		sys.exit()
	elif opt in ("-d", "--dir"):
		dir_to_search = arg
	elif opt in ("-p", "--pattern"):
		search_pattern = arg
		
## Check directory path exist or not if not then assign it current directory		
if len(dir_to_search) == 0:
	dir_to_search = os.getcwd()

## Check search pattern has any value or not if not then throw error
if len(search_pattern) == 0:
	showerror()
	
print(dir_to_search, search_pattern)


# Walk through directory
exclude_prefixes = '$RECYCLE.BIN'
for dirpath, dirnames, filenames in os.walk(dir_to_search):
	if exclude_prefixes not in dirpath:
		for fileName in filenames:
			if fnmatch.fnmatch(fileName, search_pattern): # Match search string
				print(os.path.join(dirpath, fileName))
