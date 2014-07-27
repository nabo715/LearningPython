# Use words.txt as the file name

fname = raw_input("Enter file name:")

try:
    fh = open(fname)
except:
    print("Incorrect file name")
    exit()

for line in fh:
    line = line.rstrip()
    print line.upper()