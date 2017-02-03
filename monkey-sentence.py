# A script to automatically generate sentences using grammar rules

class RuleHead:
	symbol = ''
	param = [ ]

import copy
import fileinput


def inLexicon(x):
	if x.symbol == 'det' or x.symbol == 'n' or x.symbol == 'prep' or x.symbol == 'wh':
		return x.param[0]
	elif x.symbol == 'v':
		if x.param[1] not in lexicon:
			return x.param[1]
		return lexicon[x.param[1]][x.param[0]['content']['number']][x.param[0]['content']['time']]
	else: return "not in lexicon"


def expand(x):
	if x.symbol in grammar:
		AllRuleTails = grammar[x.symbol]
		for EachRuleTail in AllRuleTails:
			TryNextRule = False
			ReturnList = [ ]
			
			for EachPhraseObject in EachRuleTail:
#				print "Each Phrase Obj", EachPhraseObject.symbol,EachPhraseObject.param
				NewRuleHead = copy.deepcopy(EachPhraseObject)
				
				for paramIndex in range(0,len(NewRuleHead.param)):
					if isinstance(NewRuleHead.param[paramIndex],str):
						pass
					else:
						NestingList = NewRuleHead.param[paramIndex]

						FrameNode = x.param[NestingList[0]]
						
						for NestingIndex in range(1,len(NestingList)):
							if NestingList[NestingIndex] not in FrameNode:
								TryNextRule = True
								#print "Improper TryNextRule"
								break
							FrameNode = FrameNode[NestingList[NestingIndex]]
						if TryNextRule is True:
						#	print "breaking out"
							break;
						else:
							NewRuleHead.param[paramIndex] = FrameNode
	#				print "param pass = ", NewRuleHead.param
				if TryNextRule is True:
					#print "Improper try"
					break;
				else:
					if 'if' in NewRuleHead.symbol:
						if NewRuleHead.param[0] != NewRuleHead.param[1]:
							#print "Proper TryNextRule"
							TryNextRule = True
							break
					else:
						ReturnList.append(NewRuleHead)
			if TryNextRule is False:
#				print "Rule match"
				ReturnList.reverse()
				return ReturnList
#		print "No rule found"
		# if no rule, return something to backtrack
	else:
		return inLexicon(x)



def read_file(filename):
	grammar = { }
	paramCheck = { }
	IncompleteLine = False

	for line in fileinput.input(filename):

		if line.isspace():
			continue
		# convert to lower and remove spaces
		line = line.lower()
		splitLine = line.split()
		line = "".join(splitLine)
#		print line
		# if rules over > 1 line, incompleteLine = True
		if IncompleteLine == False:
			splitLine = line.split('=')

			# remove last ']' from rulehead
			ruleHead = splitLine[0]
			ruleHead = ruleHead[0:len(ruleHead)-1]
						
			splitRuleHead = ruleHead.split('[')
			if len(splitRuleHead) is not 2:
				print "Head Incorrect parameter braces.", line
				break
			
			ruleHead = splitRuleHead[0]
			ruleParamList = splitRuleHead[1].split(',')

			if ruleHead in paramCheck:
				if paramCheck[ruleHead] != len(ruleParamList):
					print "Head Different # of parameters ", paramCheck, ruleParamList
					continue
			line = splitLine[1]
			ToJoin = [ ]
				
		if line[len(line)-1] == '|':
			IncompleteLine = True
			ToJoin.append(line)
			continue
		IncompleteLine = False
		ToJoin.append(line)
		RulesLine = "".join(ToJoin)
		
		AllRuleTails = RulesLine.split('|')
		RuleTailList = [ ]
		for RuleTail in AllRuleTails:
			PhraseList = RuleTail.split(']')
			PhraseList = PhraseList[0:len(PhraseList)-1]
			PhraseObjList = [ ]
			for phrase in PhraseList:
				splitPhrase = phrase.split('[')
				if len(splitPhrase) is not 2:
					print "Phrase Incorrect parameter braces.", line
					break
				phraseHead = splitPhrase[0]
				ParamList = splitPhrase[1].split(',')
				
				PhraseObj = RuleHead()
				PhraseObj.symbol = phraseHead
				PhraseObj.param = [ ]
				
				for paramIndex in range(0,len(ParamList)):
					if '#' in ParamList[paramIndex]:
						literal = ParamList[paramIndex]
						literal = literal[1:len(literal)]
						PhraseObj.param.append(literal)
					else:
						if ':' in ParamList[paramIndex]:
							Param = ParamList[paramIndex].split(':')
						else:
							Param = [ ParamList[paramIndex] ]
						for Index in range(0,len(ruleParamList)):
							if ruleParamList[Index] == Param[0]:
								Param[0] = Index
								break
						if isinstance(Param[0],str):
							print "Parameter not found in Rule Head."
							continue
						PhraseObj.param.append(Param)
							
				if PhraseObj.symbol in paramCheck:
					if paramCheck[PhraseObj.symbol] != len(PhraseObj.param):
						print "B Different # of parameters = ", paramCheck, PhraseObj.param
						break
				else:
					paramCheck[PhraseObj.symbol] = len(PhraseObj.param)
								
				PhraseObjList.append(PhraseObj)
				#print "Adding Phrase Obj = ", PhraseObj.param
			RuleTailList.append(PhraseObjList)
			#print "Adding Rule"
		grammar[ruleHead] = RuleTailList
		#print "Adding RuleList."
	fileinput.close()
	print "Grammar Added"
	return grammar


lexicon = { 'do': {'singular': {'past':'did','present':'does','future':'will do'} , 'plural': { 'past':'did','present':'do','future':'will do'} }, 'is': { 'singular':{ 'past':'was','present':'is','future':'will be' } , 'plural':{ 'past':'were','present':'are','future':'will be'} }, 'give': { 'singular': {'past':'gave','present':'gives','future':'will give' }, 'plural':{'past':'gave','present':'give','future':'will give'} } }

def generate(frame):
	stack = []
	GrammarHead = RuleHead()
	GrammarHead.symbol = 's'
	GrammarHead.param = [ ]
	GrammarHead.param.append(frame)
	stack.append(GrammarHead)
	while stack:
		#print stack
		item = stack.pop()
		if isinstance(item,str):
			print item,
		else:
			result = expand(item)
			
			if isinstance(result,str):
				stack.append(result)
			#	print "Str Result = ", result
			else:
			#	print "List Result = ", result
				for item in result:
					stack.append(item)


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
				generate(frame)
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
		elif value[len(value)-1] == 's' and value != 'yes':
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
