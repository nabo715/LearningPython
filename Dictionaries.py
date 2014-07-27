'''
Created on Jul 25, 2014

Write a program to read through the mbox-short.txt and figure 
out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program 
creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through 
the dictionary using a maximum loop to find the most prolific committer.

@author: AllinOne
'''
fname = raw_input("Enter file name: ")
fh = open(fname)
most_name_count = dict()
lst = list()
counts = None

#creates seperate lines, then splits into each word and creates the list
for line in fh:
    line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split() 
    # the second word in each line is the email
    words = words[1]
    lst.append(words)
#updates the dictionary to count the same number of keys
for word in lst:    
    most_name_count[word] = most_name_count.get(word,0) + 1    
#using two iternation variables we determine which word from the dictionary is
#repeated the most and updates the count 
for word,count in most_name_count.items():
    if counts is None or count > counts:
        most_name = word
        counts = count
#prints the final key and value information
print most_name, counts