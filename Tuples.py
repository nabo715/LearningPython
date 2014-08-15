'''
Created on Aug 5, 2014

Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day 
for each of the messages. You can pull the hour out 
from the 'From ' line by finding the time and then 
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below. 
Note that the autograder does not have support for 
the sorted() function.

@author: Nabeel
'''

file_name = raw_input("Enter file:")

file_handle = open(file_name,'r')

counts = dict()
lst = list()
for line in file_handle:
    if not line.startswith("From "):
        continue
    else:
        #words = line.split()
        end_pos = line.find(':')
        words = line[end_pos-2:end_pos]
        
        counts[words] = counts.get(words, 0) + 1
        
for key, value in counts.items():
    lst.append((key,value))

lst.sort()

for key,value in lst:
    print key, value