#import random
import numpy.random as nprnd # numpy is about ten times faster than random.sample
import json
import datetime


dateNow = datetime.datetime.now() # get the current datetime

numbers_to_test = 50 # the amount of random numbers that i want to pick up
randoms_range = 1000 # the multiplier to create the range of the total selection (from where i choose the random numbers)
number_to_test_range = numbers_to_test * randoms_range # the range of the total selection from where i choose the random numbers

randoms = []
randoms_freq = [0]*number_to_test_range # each index is the random number
randoms_freq_perc = []

digits_shift_multiplier = 10000 # will use this to shift the decimal, in order to keep an Int() type. More like a personal taste.
freq_divisor = digits_shift_multiplier * numbers_to_test / number_to_test_range # the divisor in order to get the final frequency in randoms_freq_perc.

def getNewRandoms():
	#randomsList = random.sample(range(0,number_to_test_range), numbers_to_test)
	randomsList = nprnd.randint(number_to_test_range, size=numbers_to_test)
	return randomsList

def saveToFile(filename,data,loops):
	with open( datetime.datetime.now().strftime('%m-%d-%H-%M-%S') + "_Loops" + str(loops) + '_' + filename, 'w') as outfile: # filename will be: Months-Days-Hours-Minutes-Seconds_Loops####_randomsFreq.txt
		json.dump(data,outfile)
		outfile.write('\n' + "Loops Done: " + str(loops) + '\n')


print("Let's Start!")
for n in range(0,numbers_to_test): 			# Breaking the total Loops in Order to save the checkpoints
	for i in range(0,number_to_test_range): # that's gonna be 2.500.000 loops running a subloop (j) of 50*250.000 at max!  This script is running in a single core old cpu, so no messing up with  Python's somehow-multithreading...
		print('Loop: #' + str( (n+1)*(i+1) )) # some console feedback
		
		randoms = getNewRandoms()
		randoms.sort()
	    
		randoms_freq_index = 0 # Since the random numbers list (randoms) is sorted, i don't want to check everytime the whole numbers_to_test_range for each chosen random number.
		for num in randoms:
			for j in range(randoms_freq_index,number_to_test_range):
				if (num == j): # increase the n frequency of the this particual number
					randoms_freq[j] += 1
					randoms_freq_index += 1
					break
	print('Saving to Files...') # some console feedback
	randoms_freq_perc = [(x*digits_shift_multiplier * freq_divisor) for x in randoms_freq] # of course the frequence percentage of a number will be less than 1, so just multiply by "digits_shift_multiplier" to get get rid off those "0.000". Yeah i still prefer Int()...
	saveToFile('randomsFreq.txt', randoms_freq_perc, (n+1)*(i+1))
print('...that was the hell of loops!')
print('Script has finished! ...go get a life!')



#
#TODO: check the idea to represent the matrix of the numbers as a binary converted in hex/decimal string.
#		since each cell of the matrix just a boolean value, if the number is chosen or not for each time we construct it
#