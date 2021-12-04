# fname = input('Enter the file name:\n')
# try:
  # fhand = open(fname)
# except:
  # print('File cannot be opened:', fname)
  # quit()
  
# print(fhand)
# stuff = "hi\nhello"
# count = 0
# len(print(stuff))

# for line in fhand:
  # line = line.rstrip()
  # if not line.startswith('o'):
    # print('Line Count:', line, end="")
    # continue
  # print(line)

fh = open('mbox.txt', 'a')
fh.write('hi')

