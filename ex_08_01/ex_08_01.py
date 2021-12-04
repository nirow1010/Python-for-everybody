han = open('mbox-short.txt')

for line in han:
  line = line.rstrip()
  # print("Line", line)
  wds = line.split()
  # guardian
  if (len(wds) < 1) or wds[0] != 'sad':
    continue
  print(wds)