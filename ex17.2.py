from sys import argv
from os.path import exists

script, from_file, to_file = argv


# in_file = open(from_file)
# indata = in_file.read()
#collapses into:
#indata = open(argv[1]).read()

# out_file = open(to_file, 'w')
# out_file.write(indata)
#collapses into:
#open(argv[2],'w').write(indata)

# argv[2].write(argv[1].open)

# now lets see if we can oneline it.
open(argv[2],'w').write(open(argv[1]).read())

# one liner!  

