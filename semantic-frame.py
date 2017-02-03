# returns test frame

def frame_process(filename):
	frame = { }
	inFrame = False
	number = 'nothing'
	for line in fileinput.input(filename):
		if '+' in line:
			if inFrame is True:
				print "\nId:", frame['id']
				if 'time' not in frame['content']:
					frame['content']['time'] = 'past'
				if number == 'nothing':
					frame['content']['number'] = 'singular'
				else: frame['content']['number'] = number
				return frame_convert(frame)
			
			frame = { }
			inFrame = True
			number = 'nothing'
			continue
		elif line.isspace() or inFrame is False:
			continue
		
		splitLine = line.split()
		if len(splitLine) != 2:
			print "Frame not correct = ", splitLine
			inFrame = False
			continue
		
		value = splitLine[1]
		
		FrameNodes = splitLine[0].split('.')
		if FrameNodes[len(FrameNodes)-1] == 'agent':
			if value[len(value)-1] == 's':
				number = 'plural'
			else: number = 'singular'
		elif value[len(value)-1] == 's':
			if number == 'nothing':
				number = 'plural'
		
		#print "FrameNodes = ", FrameNodes
		frameTrav = frame
		for i in range(1,len(FrameNodes)):
			if FrameNodes[i] not in frameTrav:
				frameTrav[FrameNodes[i]] = { }
			if i == len(FrameNodes)-1:
				if frameTrav[FrameNodes[i]]:
					print "Value assigned twice = ", line
					#inFrame = False
				frameTrav[FrameNodes[i]] = value
			frameTrav = frameTrav[FrameNodes[i]]
		#print "Frame = ", frame
	fileinput.close()

def choose(dist, frame):
	cond = dist[0]
	myprob = dist[1]
	sent = dist[2]
	values = [ ]
	for eachstr in sent:
		myval = 0
		for item in frame.items():
			myval = myval + cond[item].freq(eachstr) * myprob(item)
		values.append(myval)
	themax = 0
	ans = 0
	for i in range(0,len(values)):
		if values[i] > themax:
			ans = i
			themax = values[i]
	return ans


def frame_process(filename):
	frame = { }
	inFrame = False
	number = 'nothing'
	cond = ConditionalFreqDist()
	itemfreq = FreqDist()
	mystr = [ ]
	for line1 in fileinput.input("d:\\sentence.txt"):
		if line1.isspace():
			continue
		else:
			mystr.append(line1)
	fileinput.close()
	mystr.reverse()
	returnstr = [ ]
	for line in fileinput.input(filename):
		if '+' in line:
			if inFrame is True:
				print "\nId:", frame['id']
				if 'time' not in frame['content']:
					frame['content']['time'] = 'past'
				if number == 'nothing':
					frame['content']['number'] = 'singular'
				else: frame['content']['number'] = number
				newframe = frame_convert(frame)
				sentence = mystr.pop()
				returnstr.append(sentence)
				print "Sentence = ", sentence, "Frame = ", newframe
				for item in newframe:
					cond[item].inc(sentence)
					itemfreq.inc(item)
				
			frame = { }
			inFrame = True
			number = 'nothing'
			continue
		elif line.isspace() or inFrame is False:
			continue
		
		splitLine = line.split()
		if len(splitLine) != 2:
			print "Frame not correct = ", splitLine
			inFrame = False
			continue
		
		value = splitLine[1]
		
		FrameNodes = splitLine[0].split('.')
		if FrameNodes[len(FrameNodes)-1] == 'agent':
			if value[len(value)-1] == 's':
				number = 'plural'
			else: number = 'singular'
		elif value[len(value)-1] == 's':
			if number == 'nothing':
				number = 'plural'
		
		#print "FrameNodes = ", FrameNodes
		frameTrav = frame
		for i in range(1,len(FrameNodes)):
			if FrameNodes[i] not in frameTrav:
				frameTrav[FrameNodes[i]] = { }
			if i == len(FrameNodes)-1:
				if frameTrav[FrameNodes[i]]:
					print "Value assigned twice = ", line
					#inFrame = False
				frameTrav[FrameNodes[i]] = value
			frameTrav = frameTrav[FrameNodes[i]]
		#print "Frame = ", frame
	fileinput.close()
	return [ cond, itemfreq, returnstr ]
