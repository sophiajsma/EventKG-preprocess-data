# output = open('./preprocess_data/event_beginend','w')
# for line in open('output/relations_base.nq'):
# 	if(line.find('<event') != -1 and line.find('sem:hasPlace') == -1 
# 		and (line.find('sem:hasBeginTimeStamp') != -1
# 		or line.find('sem:hasEndTimeStamp') != -1)):
# 		output.write(line)
# 	

#######
# <event_3723> sem:hasBeginTimeStamp "1797-03-12"^^xsd:date eventKG-g:event_kg .

# output = open('preprocess_data/event_beginToend','w')
# event_period = {}
# for line in open('preprocess_data/event_beginend'):
# 	parts = line.split(' ')
# 	if(event_period.has_key(parts[0])):
# 		if(parts[1].find('sem:hasBeginTimeStamp') != -1):
# 			event_period[parts[0]][0].append(parts[2])
# 			# elif(event_period.get(parts[0])[0] != parts[2]):
# 				# print 'Error: event %s already has begin time'%parts[0],event_period.get(parts[0])[0], parts[2]
# 		elif(parts[1].find('sem:hasEndTimeStamp') != -1):
# 			event_period[parts[0]][1].append(parts[2])
# 			# elif(event_period.get(parts[0])[1] != parts[2]):
# 				# print 'Error: event %s already has end time'%parts[0],event_period.get(parts[0])[0]
# 	else:
# 		event_period[parts[0]] = [[],[]]
# 		if(parts[1].find('sem:hasBeginTimeStamp') != -1):
# 			event_period[parts[0]][0].append(parts[2])
# 		elif(parts[1].find('sem:hasEndTimeStamp') != -1):
# 			event_period[parts[0]][1].append(parts[2])

# for k in event_period:
# 	for t in event_period[k][0]:
# 		output.write('START\t' + k + '\t' + t + '\n')
# 	for t in event_period[k][1]:
# 		output.write('END\t' + k + '\t' + t + '\n')


# output = open('preprocess_data/roleType','w')
# rt = set()
# for line in open('output/relations_other.nq'):
# 	if(line.find('sem:roleType') != -1):
# 		parts = line.split(' ')
# 		rt.add(parts[2])

#######
# # output.write(parts[2] + '\n')
# for r in rt:
# 	output.write(r + '\n')


#######
# output = open('./preprocess_data/event_nextEvent','w')
# for line in open('output/relations_base.nq'):
# 	if(line.find('<event') != -1 and line.find('nextEvent') != -1):
# 		output.write(line)


#######
# output = open('preprocess_data/roleType_pick','w')
# rt = {}
# for line in open('preprocess_data/wiki_role'):
# 	parts = line.split('\t')
# 	output.write(parts[1] + '\t' + parts[0] + '\n')
# 	k = 'wdt:' + parts[1]
# 	rt[k] = parts[0]

##########
# output = open('preprocess_data/roleType_wiki_pick','w')
# output2 = open('preprocess_data/excep_wiki','w')
# for line in open('preprocess_data/roleType'):
	# if(rt.has_key(line.strip())):
		# output.write(line.strip() + '\t' + rt[line.strip()] + '\n')
	# if(line.find('wdt:') == -1):
	# 	output2.write(line)


#####
# output = open('preprocess_data/wdt_count','w')
# cnt = {}
# for line in open('output/relations_other.nq'):
# 	if(line.find('sem:roleType') != -1 and line.find('wdt') != -1):
# 		parts = line.split(' ')
# 		if(cnt.has_key(parts[2])):
# 			cnt[parts[2]] += 1
# 		else:
# 			cnt[parts[2]] = 1
# # for k in cnt:
# # 	output.write(k + '\t' + str(cnt[k]) + '\n')

# l = sorted(cnt.items(), key = lambda cnt:cnt[1], reverse = True)
# for ll in l:
# 	output.write(ll[0] + '\t' + str(ll[1]) +'\n')
# print(type(l[0]))



#####
# output = open('preprocess_data/wdt_cnt_name','w')
# wiki_property = {}
# for line in open('preprocess_data/wiki_property'):
# 	parts = line.split('\t')
# 	wiki_property[parts[0]] = parts[1]
# for line in open('preprocess_data/wdt_count'):
# 	parts = line.split('\t')
# 	output.write(parts[0] + '\t' + wiki_property[parts[0]] + '\t' + parts[1]) 



##########
# output = open('preprocess_data/relation_important_event','w')

# r = []
# dec_r = {}
# for line in open('preprocess_data/roleType_wiki_pick'):
# 	r.append(line.split('\t')[0])
# 	dec_r[line.split('\t')[0]] = line.split('\t')[1]

# cnt = 0
# m = ['E1','E2','R']
# for line in open('output/relations_other.nq'):
# 	if(line.find('eventkg_relation_') == -1):
# 		continue
# 	cnt += 1
# 	if(cnt % 4 == 1):
# 		m[0] = 'E1'
# 		m[1] = 'E2'
# 		m[2] = 'R'
# 	elif(cnt % 4 == 2):
# 		m[0] = line.split(' ')[2]
# 	elif(cnt % 4 == 3):
# 		m[1] = line.split(' ')[2]
# 	else:
# 		# print line
# 		m[2] = line.split(' ')[2]
# 		if(m[2] in r):
# 			output.write(m[0] + '\t' + m[1] + '\t' + m[2] + '\t' + dec_r[m[2]]+ '\n')



#####
# import pickle 
# import json
# class Event_Info:
# 	subject_name = ''
# 	object_name = ''
# 	role_type = ''
# 	role_type_descrip = ''
# 	start = []
# 	end = []

# 	def __init__(self,parts, start, end):
# 		self.subject_name = parts[0]
# 		self.object_name = parts[1]
# 		self.role_type = parts[2]
# 		self.role_type_descrip = parts[3]
# 		for st in start:
# 			start.append(st)
# 		for et in end:
# 			end.append(st)





# output = open('preprocess_data/event_beginToend','w')
event_period = {}
for line in open('preprocess_data/event_beginend'):
	parts = line.split(' ')
	if(event_period.has_key(parts[0])):
		if(parts[1].find('sem:hasBeginTimeStamp') != -1):
			event_period[parts[0]][0].append(parts[2])
			# elif(event_period.get(parts[0])[0] != parts[2]):
				# print 'Error: event %s already has begin time'%parts[0],event_period.get(parts[0])[0], parts[2]
		elif(parts[1].find('sem:hasEndTimeStamp') != -1):
			event_period[parts[0]][1].append(parts[2])
			# elif(event_period.get(parts[0])[1] != parts[2]):
				# print 'Error: event %s already has end time'%parts[0],event_period.get(parts[0])[0]
	else:
		event_period[parts[0]] = [[],[]]
		if(parts[1].find('sem:hasBeginTimeStamp') != -1):
			event_period[parts[0]][0].append(parts[2])
		elif(parts[1].find('sem:hasEndTimeStamp') != -1):
			event_period[parts[0]][1].append(parts[2])
print 'Step 1 Finish'

val_info = []
cnt = 0 
for line in open('preprocess_data/relation_important_event'):
	parts = line.split('\t')
	if(event_period.has_key(parts[1])):
		cnt += 1
		print 'Cnt is ',cnt
		event_info = Event_Info(parts, event_period[parts[1]][0], event_period[parts[1]][1])
		# val_info.append(event_info)
		# ans = json.dumps(event_info)
		# output.write(ans + '\n')






# for k in event_period:
# 	for t in event_period[k][0]:
# 		output.write('START\t' + k + '\t' + t + '\n')
# 	for t in event_period[k][1]:
# 		output.write('END\t' + k + '\t' + t + '\n')
