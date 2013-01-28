import sys

for filename in sys.argv[1:]:
    print filename, ":", len(open(filename).readlines())
    print "%s: %d" % (filename, len(open(filename).readlines()))
