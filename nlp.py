def generate():
	import random
	stack = ['S']
	while stack:
		#print stack
		item = stack.pop()
		if item not in grammar and item not in lexicon and '*' not in item:
			print item,
		else:
			result = expand(item)
			if type(result) is ListType:
				for item in result:
					stack.append(item)
			else: stack.append(result)

		if len(stack) == 0:
			break
def expand(x):
	if '*' in x:
		x = x[0:len(x)-1]
		i = random.randint(0,1)
		tempList = [ ]
		while i > 0:
			tempList.append(x)
			i -= 1
		return tempList
	elif x in lexicon:
		return lexicon[x][random.randint(0,len(lexicon[x])-1)]
	elif x in grammar:
		return grammar[x][random.randint(0,len(grammar[x])-1)]
	else: print "Stack Error"

lexicon = { 'N':['man', 'wagon', 'woman', 'child', 'dog', 'car', 'fence'], 'V':["eat", "drink", "push", "run", "see", "dream"], 'AUX':["can", "may", "will"], 'DET': ["the","a"], 'ADJ': ["green", "big", "strong", "small"], 'PREP': ["in", "on", "over", "under", "by", "with"] }

grammar={'S':[['.','VP','NP'],['?','VP','NP','AUX'],['!','VP','AUX','NP']],'NP':[['PP*','N','ADJ*','DET'],['PP*','N']], 'VP':[['NP','V'],['PP*','NP','V']],'PP':[['NP','PREP']] }


grammar={'S':[['. none','VP head','NP head:agent'],['? none','VP head','NP head:agent','AUX head:aux'],['! none','VP head','AUX head:aux','NP head:agent']],'NP':[['PP1* head','N head:type','ADJ1* head','DET head:determiner'],['PP1* head','N head:type']], 'VP':[['NP head:patient','V head:type head:time'],['PP1* head','NP head:patient','V head:type head:time']],'PP1':['PP to head:destination','PP at head:location'], 'ADJ1':['ADJ head:age','ADJ head:nationality'], 'PP':[['NPhead','PREP role']] }

def expand(x):
	if '*' in x.symbol:
		x.symbol = x.symbol[0:len(x.symbol)-1]
		i = random.randint(0,2)
		tempList = [ ]
		while i > 0:
			tempList.append(x.symbol)
			i -= 1
		return tempList
	elif x.symbol in lexicon:
		return lexicon[x][random.randint(0,len(lexicon[x])-1)]
	elif x.symbol in grammar:
		rules = grammar[x.symbol]
		for option in rules:
			if appropriate(x,option):
				return CreateList(x,option)
	else: print "Stack Error"


def CreateList(x,rule):
	for element in rule:
		obj = myclass()
		result = element.split()
		obj.symbol = result[0]
		for i in range(1,len(result)):
			if result[i] == 'head':
				obj.head = x.head
			elif '&' in result[i]:
				obj.param = 

def appropriate(x,rule):
	for element in rule:
		result = element.split()
		for i in range(1,len(result)):
			if ':' in result[i]:
				param = result[i].split(':')
				if param[1] not in x.head:
					return False


def CreateList(x,rule):
	for element in rule:
		obj = myclass()
		result = element.split()
		obj.symbol = result[0]
		for i in range(1,len(result)):
			if result[i] == 'head':
				obj.head = x.head
			elif '&' in result[i]:
				obj.param = x.param[result[i]]
			elif ':' in 




grammar={'S':[ [['.','none'],['VP','head'],['NP','head:agent']], \
	       [['?','none'],['VP','head'],['NP','head:agent'],['AUX','head:aux']], \
	       [['!','none'],['VP','head'],['AUX','head:aux'],['NP','head:agent']] ], \
	       'NP':[ [['PP1*','head'],['N','head:type'],['ADJ1*','head'],['DET','head:determiner']], \
		      [['PP1*','head'],['N','head:type']] ], \
	 'VP':[ [['NP','head:patient'],['V','head:type','head:time']], \
		[['PP1*','head'],['NP','head:patient'],['V','head:type','head:time']] ], \
		'PP1':[ [['PP','to','head:destination']], \
			[['PP','at','head:location']] ], \
	 'ADJ1':[ [['ADJ','head:age']], \
		  [['ADJ','head:nationality']] ], \
	 'PP':[ [['NP','head'],['PREP','role']] ] }

frame = { 'type':'eat', 'agent':{ 'type':'boy', 'nationality':'swiss', 'age':'7', 'determiner':'the' }, 'patient':{ 'type':'peach', 'color':'red', 'size':'big' }, 'location':{ 'type':'store', 'determiner':'the', 'age':'old' }, 'time':'past' }

def appropriate(x,rule):
	for element in rule:
		for i in range(1,len(element)):
			if ':' in element[i]:
				param = element[i].split(':')
				if param[0] not in x.param:
					print "Error in Grammar"
					return False
				elif param[1] not in x.param[param[0]]:
					return False

def expand(x):
	if '*' in x.symbol:
		x.symbol = x.symbol[0:len(x.symbol)-1]
		i = random.randint(0,2)
		tempList = [ ]
		while i > 0:
			tempList.append(x)
			i -= 1
		return tempList
	elif x.symbol in lexicon:
		return lexicon[x][random.randint(0,len(lexicon[x])-1)]
	elif x.symbol in grammar:
		rules = grammar[x.symbol]
		for rule in rules:
			if appropriate(x,rule):
				return CreateList(x,rule)
	else: print "Stack Error"



def CreateList(x,rule):
	for element in rule:
		obj = myclass()
		obj.symbol = element[0]
		obj.param = { }
		for i in range(1,len(element)):
			if ':' in element[i]:
				param = element[i].split(':')
				if param[0] not in x.param and param[1] not in x.param[param[0]]:
					print "Told u so..."
					return [ ]
				else:
					obj.param[]=x.param[param[0]][param[1]]


def CreateList(x,rule):
	objList = [ ]
	for element in rule:
		obj = myclass()
		obj.symbol = element[0]
		obj.param = { }
		for i in range(1,len(element)):
			if ':' in element[i]:
				param = element[i].split(':')
				if param[0] not in x.param and param[1] not in x.param[param[0]]:
					print "Told u so..."
					return [ ]
				else:
					obj.param[param[0]]=x.param[param[0]][param[1]]
			elif element[i] in x.param:
				obj.param[element[i]]=x.param[element[i]]
			else:
				print "No such parameter"
				return [ ]
		objList.append(obj)
	return objList



def expand(x):
	if x.symbol in grammar:
		AllRuleTails = grammar[x.symbol]
		for EachRuleTail in AllRuleTails:
			ReturnList = [ ]
			TryNextRule = False
			for EachPhraseObject in EachRuleTail:
				NewRuleHead = copy.copy(EachPhraseObject)
				for paramIndex in range(0,len(EachPhraseObject.param)):
					if isInstance(EachPhraseObject.param[paramIndex],int):
						FrameNode = x.param[EachPhraseObject.param[paramIndex]]
						NewRuleHead.param[paramIndex] = FrameNode
					elif isInstance(EachPhraseObject.param[paramIndex],str):
						pass
					else:
						NestingList = EachPhraseObject.param[paramIndex]
						FrameNode = x.param[NestingList[0]]
						
						for NestingIndex in range(1,len(NestingList)):
							if NestingList[NestingIndex] not in FrameNode:
								TryNextRule = True
								break
							FrameNode = FrameNode[NestingList[NestingIndex]]
						if TryNextRule is True:
							break;
						else:
							NewRuleHead.param[paramIndex] = FrameNode
				if TryNextRule is True:
					break;
				else:
					ReturnList.append(NewRuleHead)
			if TryNextRule is False:
				print "Rule match"
				return ReturnList
		print "No rule found"
		# if no rule, return something to backtrack
	elif x.symbol in lexicon:
		return x.symbol
	else:
		print "Symbol not in both"							






def read_file(filename):
	grammar = { }
	paramCheck = { }
	IncompleteLine = False
	ToJoin = [ ]
	for line in fileinput.input(filename):

		line = line.lower()
		splitLine = line.split()
		line = join(splitLine)

		if IncompleteLine == False:
			splitLine = line.split('=')
			if len(splitLine) is not 2:
				print "Symbol '=' bifurcates line."
				continue
			ruleHead = splitLine[0]
			ruleHead = ruleHead[0:len(ruleHead)-1]
			splitRuleHead = ruleHead.split('[')
			if len(splitPhrase) is not 2:
				print "Incorrect parameter braces."
				break
			ruleHead = splitRuleHead[0]
			ruleParamList = splitRuleHead[1].split(',')
			if ruleHead in paramCheck:
				if paramCheck[ruleHead] != len(ruleParamList):
					print "Different # of parameters"
					break
			else:
				paramCheck[ruleHead] = len(ruleParamList)
			line = splitLine[1]
			ToJoin = [ ]
				
		if line[len(line-1)] == '|':
			IncompleteLine = True
			ToJoin.append(line)
			continue
		IncompleteLine = False
		ToJoin.append(line)
		RulesLine = join(ToJoin)
			
		AllRuleTails = RulesLine.split('|')
		RuleTailList = [ ]
		for RuleTail in AllRuleTails:
			PhraseList = RuleTail.split(']')
			PhraseList = PhraseList[0:len(PhraseList)-1]
			PhraseList.reverse()
			PhraseObjList = [ ]
			for phrase in PhraseList:
				splitPhrase = phrase.split('[')
				if len(splitPhrase) is not 2:
					print "Incorrect parameter braces."
					break
				phraseHead = splitPhrase[0]
				ParamList = splitPhrase[1].split(',')
				PhraseObj = RuleHead()
				PhraseObj.symbol = phraseHead
				for paramIndex in range(0,len(ParamList)):
					if '#' in ParamList[paramIndex]:
						literal = ParamList[paramIndex]
						literal = literal[0:len(literal)-1]
						PhraseObj.param.append(literal)
					elif ':' in ParamList[paramIndex]:
						splitParam = ParamList[paramIndex].split(':')
						for Index in range(0,len(ruleParamList)):
							if ruleParamList[Index] == splitParam[0]:
								splitParam[0] = Index
								break
						if isinstance(splitParam[0],str):
							print "Parameter not found in Rule Head."
							continue
						PhraseObj.param.append(splitParam)
					else:
						found = False
						for Index in range(0,len(ruleParamList)):
							if ruleParamList[Index] == ParamList[paramIndex]:
								PhraseObj.param.append(Index)
								found = True
								break
						if found is False:
							print "Parameter not found in Rule Head."
							continue
				if PhraseObj.symbol in paramCheck:
					if paramCheck[PhraseObj.symbol] != len(PhraseObj.param):
						print "Different # of parameters"
						break
				else:
					paramCheck[PhraseObj.symbol] = len(PhraseObj.param)
				PhraseObjList.append(PhraseObj)
			RuleTailList.append(PhraseObjList)
		
	


def read_file(filename):
	grammar = { }
	paramCheck = { }
	IncompleteLine = False
	ToJoin = [ ]
	for line in fileinput.input(filename):

		line = line.lower()
		splitLine = line.split()
		line = splitLine[0]
		for i in range(1,len(splitLine)):
			line = line + splitLine[i]
		print line
		
		if IncompleteLine == False:
			splitLine = line.split('=')
			if len(splitLine) is not 2:
				print "Symbol '=' bifurcates line."
				continue
			ruleHead = splitLine[0]
			ruleHead = ruleHead[0:len(ruleHead)-1]
			print "RuleHead ", ruleHead
			
			splitRuleHead = ruleHead.split('[')
			if len(splitRuleHead) is not 2:
				print "Incorrect parameter braces."
				break
			ruleHead = splitRuleHead[0]
			ruleParamList = splitRuleHead[1].split(',')
			if ruleHead in paramCheck:
				if paramCheck[ruleHead] != len(ruleParamList):
					print "Different # of parameters"
					break
			else:
				paramCheck[ruleHead] = len(ruleParamList)
			line = splitLine[1]
			ToJoin = [ ]
				
		if line[len(line)-1] == '|':
			IncompleteLine = True
			ToJoin.append(line)
			continue
		IncompleteLine = False
		ToJoin.append(line)
		RulesLine = ToJoin[0]
		for i in range(1,len(ToJoin)):
			RulesLine = Rulesline + ToJoin[i]

		print "RulesLine ", RulesLine
		
		AllRuleTails = RulesLine.split('|')
		RuleTailList = [ ]
		for RuleTail in AllRuleTails:
			PhraseList = RuleTail.split(']')
			PhraseList = PhraseList[0:len(PhraseList)-1]
			PhraseList.reverse()
			PhraseObjList = [ ]

			print "PhraseList ", PhraseList
			for phrase in PhraseList:
				splitPhrase = phrase.split('[')
				if len(splitPhrase) is not 2:
					print "Incorrect parameter braces."
					break
				phraseHead = splitPhrase[0]
				ParamList = splitPhrase[1].split(',')
				PhraseObj = RuleHead()
				PhraseObj.symbol = phraseHead
				for paramIndex in range(0,len(ParamList)):
					if '#' in ParamList[paramIndex]:
						literal = ParamList[paramIndex]
						literal = literal[0:len(literal)-1]
						PhraseObj.param.append(literal)
					elif ':' in ParamList[paramIndex]:
						splitParam = ParamList[paramIndex].split(':')
						for Index in range(0,len(ruleParamList)):
							if ruleParamList[Index] == splitParam[0]:
								splitParam[0] = Index
								break
						if isinstance(splitParam[0],str):
							print "Parameter not found in Rule Head."
							continue
						PhraseObj.param.append(splitParam)
					else:
						found = False
						for Index in range(0,len(ruleParamList)):
							if ruleParamList[Index] == ParamList[paramIndex]:
								PhraseObj.param.append(Index)
								found = True
								break
						if found is False:
							print "Parameter not found in Rule Head."
							continue
				if PhraseObj.symbol in paramCheck:
					if paramCheck[PhraseObj.symbol] != len(PhraseObj.param):
						print "Different # of parameters b "
						break
				else:
					paramCheck[PhraseObj.symbol] = len(PhraseObj.param)
				PhraseObjList.append(PhraseObj)
			RuleTailList.append(PhraseObjList)
		grammar[ruleHead] = RuleTailList
	fileinput.close()
	