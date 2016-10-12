import fileinput

def process(string):
    print 'Processing: %s' % string

for line in fileinput.input('somefile.txt'):
    process(line)