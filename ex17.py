from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copy from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)
# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CNTRL-C to abort."
# raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."
out_file.close()
in_file.close()

# study drills
# 1. commented out the asking part, above.
# 2. see ex17.2.py  nearly a one liner!
# 3. i know about cat.
# 4. closes out the filehandle and frees up the system resources.  
# 5. The Python Library Reference has a good list of the modules and methods.
