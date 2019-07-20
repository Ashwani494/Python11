'''
open the file
   file name
   mode::read (r) write(w) append(a)
perform operation
  1.read
  2.write
  3. Append
close

'''

f=open("ram.txt","r")
print(f)
#to read all the data
#print(f.read())

# to read onle line
print(f.readline())

for data in f:
    print(data,end="")



