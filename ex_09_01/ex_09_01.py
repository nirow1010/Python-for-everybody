ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for name in names:
 # if name not in counts:
  #  counts[name] = 1
  #else:
   # counts[name] = counts[name] + 1
#print(counts)


#if name in counts:
 # x = counts[name]
#else: 
 # x = 0 


#x = counts.get(name, 0)

for name in names:
  counts[name] = counts.get(name, 0) + 1
print(counts)


counts = { 'chunk': 1, 'fred': 42, 'jan': 100 }

for aaa,bbb in counts.items():
  print(aaa, bbb)