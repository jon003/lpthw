from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write those to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally. we close it."
target.close()

# study drills
# 1. I understood it.  not hard.
# 2. see ex16.2.py
# 3. see ex16.3.py
# 4. open defaults to read only.  passing 'w' specifies we can also write to the file.
# 5. nope with w truncates by default. to not truncate use w+ instead of w.