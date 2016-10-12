import sys

# read from stdin
text = sys.stdin.read()
words = text.split()

wordcount = len(words)
print 'worldcount: ', wordcount
