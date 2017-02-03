# Output features to be used with maximum entropy modeling package - megam

def read_labels():	
	f = file("d://receive/nlp/classes.txt","r")
	d = f.readlines()
	label_convert = { }
	for index in range(0,len(d)):
		label_convert[d[index].split()[0]] = index
	f.close()
	return label_convert



def find_features(data):
	featureList = [ ]
	labelList = [ ]
	for index in range(0,len(data)):
		featureList.append(get_features(index,data))
		labelList.append(label_convert[data[index]['ledu'].split()[0]])
	return [featureList,labelList]


def write_features(f,label_features):
	features = label_features[0]
	labels = label_features[1]
	for index in range(0,len(labels)):
		to_write = str(labels[index])
		for j in range(0,len(features[index])):
			to_write = to_write+"\t"+features[index][j]
		f.write(to_write+"\n")


def first_word(curr_data,featureList):
	featureList.append("FIRST_WORD="+curr_data['ledu'].split()[1])
	return featureList

>>> def contains_say(curr_data,featureList):
	wordlist = curr_data['ledu'].split()
	if "say" in wordlist or "said" in wordlist or "says" in wordlist or "told" in wordlist or "tell" in wordlist:
		featureList.append("CONTAINS_SAY")
	return featureList

def get_features(current,data):
	features = [ ]
	features = first_word(data[current],features)
	features = contains_say(data[current],features)
	return features

>>> def read_data(filename):
	f = file("d://receive/nlp/filelist-train","r")
	filelist = f.readlines()
	f.close()
	out = file("d://receive/nlp/"+filename,"w")	
	for filename in filelist:
		f = file("d://receive/nlp/train/"+filename.split()[0]+".ledu")
		ledu = f.readlines()
		f.close()
		f = file("d://receive/nlp/train/"+filename.split()[0]+".tag")
		tag = f.readlines()
		f.close()
		data = [ ]
		for index in range(0,len(tag)):
			new = { }
			new['ledu']=ledu[index]
			new['tag'] = tag[index]
			data.append(new)
		featureList = find_features(data)
		write_features(out,featureList)
	out.close()

def labels_read():
	f = file("d://receive/nlp/classes.txt","r")
	d = f.readlines()
	convert_label = { }
	for index in range(0,len(d)):
		convert_label[index]=d[index].split()[0]
	f.close()
	return convert_label


def convert_back(filename):
	f = file("d://receive/nlp/"+filename,"r")
	temp = f.readlines()
	f.close()
	results = [ ]
	for each in temp:
		results.append(int(each.split()[0]))
	i = 0
	f = file("d://receive/nlp/filelist-dev","r")
	filelist = f.readlines()
	f.close()

	for filename in filelist:
		f = file("d://receive/nlp/train/"+filename.split()[0]+".ledu","r")
		ledu = f.readlines()
		f.close()
		out = file("d://receive/nlp/out/"+filename.split()[0]+".ledu","w")	
		
		for each in ledu:
			temp = each.split()
			temp[0] = convert_label[results[i]]
			i = i+1
			for word in temp:
				out.write(word+" ")
			out.write("\n")

			if i == len(results):
				break
		if i == len(results):
			out.close()
			break
		out.close()


def make_test(filename):
	f = file("d://receive/nlp/filelist-dev","r")
	filelist = f.readlines()
	f.close()
	out = file("d://receive/nlp/"+filename,"w")	
	for filename in filelist:
		f = file("d://receive/nlp/train/"+filename.split()[0]+".ledu")
		ledu = f.readlines()
		f.close()
		f = file("d://receive/nlp/train/"+filename.split()[0]+".tag")
		tag = f.readlines()
		f.close()
		data = [ ]
		for index in range(0,len(tag)):
			new = { }
			new['ledu']=ledu[index]
			new['tag'] = tag[index]
			data.append(new)
		featureList = find_features(data)
		write_features(out,featureList)
	out.close()
