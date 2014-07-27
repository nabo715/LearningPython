# Use words.txt as the file name
# Use the file name mbox-short.txt as the file name
sum_final = 0
count =0
fname = raw_input("Enter file name: ")
try:
    fh = open(fname, r)
   
except:
    print("Enter a valid file name")
    exit()
    
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        strt_pos = line.find('.')
        num = line[strt_pos-1:]
        try:
            num =float(num)
        except:
            print("Invalid float")
            exit()
                
        sum_final = sum_final + num 
        count = count +1
            
average = sum/count
print "Average spam confidence:",average
    
