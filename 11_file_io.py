# Open a file
fo = open("data/00_sample.txt", "r+")
lines = fo.readlines()
for line in lines:
    print ("Read String is : ", line)
fo.close()


fo = open("data/00_sample.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()
