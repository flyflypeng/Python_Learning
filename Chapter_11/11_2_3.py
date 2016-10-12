import sys

line_no = 0
while True:
        line_no = line_no + 1
        line = sys.stdin.readline()
        if line == '':
            break;
        print '#%-10d%s' % (line_no,line)
