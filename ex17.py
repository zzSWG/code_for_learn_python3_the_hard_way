from sys import argv
from os.path import exists
# the function of this script is COPY one to another file
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output files exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
# warning: you should run this script like this(on windows):
# 1) make a sample file on CMD.exe
#		$ echo "This is a test file." > test.txt
# 2) python ex17.py test.txt new_file.txt