fname = input('Enter File: ')
if len(fname) < 1 : fname = 'txt.txt'
hand = open(fname)

di = dict()
for lin in hand:
  lin = lin.rstrip()
  # print(lin)
  wds = lin.split()
  # print(wds)
  for w in wds:
    # print(w)
    # if w in di:
    #   di[w] = di[w] + 1
    #   print('**Existing**')
    # else:
    #   di[w] = 1
    #   print('**New**')
    # print(di[w])

    # if the key is not there the count is zero
    # oldcount = di.get(w,0)
    # print(w, 'old', oldcount)
    # newcount = oldcount + 1
    # di[w] = oldcount

    # idom: retrieve/create/update counter
    di[w] = di.get(w,0) + 1 

print(di)


# now we want to find the most common word
largest = -1
theword = None
for k,v in di.items():
  print(k,v)
  if v > largest:
    largest = v
    theword = k # capture/ remember the word that was largest
    
  
print(theword, largest)