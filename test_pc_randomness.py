#import random
import numpy.random as nprnd # numpy is about ten times faster than random.sample
#import simplejson
import json
import datetime


dateNow = datetime.datetime.now()

numbers_to_test = 100
randoms_range = 100
number_to_test_range = numbers_to_test * randoms_range

randoms = []
randoms_freq = [0]*number_to_test_range # each index is the random number
randoms_freq_perc = []


def getNewRandoms():
	#randomsList = random.sample(range(0,number_to_test_range), numbers_to_test)
	randomsList = nprnd.randint(number_to_test_range, size=numbers_to_test)
	return randomsList

def saveToFile(filename,data,loops):
	with open( datetime.datetime.now().strftime('%m-%d-%H-%M-%S') + "_Loops" + str(loops) + '_' + filename, 'w') as outfile: # filename will be: Months-Days-Hours-Minutes-Seconds_Loops####_randomsFreq.txt
		json.dump(data,outfile)
		outfile.write('\n' + "Loops Done: " + str(loops) + '\n')
    #f = open(filename, 'w')
    #simplejson.dump(data, f)
    #f.close()


print("Let's Start!")
for n in range(0,numbers_to_test): 			# Breaking the total Loops in Order to save the checkpoints
	for i in range(0,number_to_test_range): # that's gonna be 1.000.000 loops running a subloop (j) of 10.000 at max!  This script is running in a single core old cpu, so no messing with  Python's somehow-multithreading...
		print('Loop: #' + str( (n+1)*(i+1) )) # some console feedback
		
		randoms = getNewRandoms()
		randoms.sort()
	    
		randoms_freq_index = 0
		for num in randoms:
			for j in range(randoms_freq_index,number_to_test_range):
				if (num == j):
					randoms_freq[j] += 1
					randoms_freq_index += 1
					break
	print('Saving to Files...') # some console feedback
	freq_divisor = numbers_to_test / number_to_test_range / ( (n+1)*(i+1) )
	randoms_freq_perc = [(x*10000 * freq_divisor) for x in randoms_freq] # of course the frequence of a number will be less than 1, so just multiply by "10000" to get get rid off those "0.000"
	saveToFile('randomsFreq.txt', randoms_freq_perc, (n+1)*(i+1))
print('Script has finished! ...go get a life!')