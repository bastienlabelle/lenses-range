#!/usr/bin/env python
# -*- coding: utf-8 -*-

import exifread
import sys
import os
import os.path
import argparse

parser = argparse.ArgumentParser(description='GETRANGE - This script provides metadata on the usage range of lenses used in photographs.')
parser.add_argument('--directory', '-d', action='store', default='.',help='Directory to process (default current directory)')
parser.add_argument('--ext', '-x', action='store',default='jpg', help = 'Extension to count (default "jpg")')
args = parser.parse_args()

directory = args.directory
extension = "." + args.ext

stats = {}
i = 0

for dirpath, dirnames, filenames in os.walk(directory):
	for filename in [f for f in filenames if f.endswith(extension)]:
		file = open(os.path.join(dirpath, filename),'rb')
		tags = exifread.process_file(file)

		for key,val in tags.items():
			if key == 'EXIF LensModel':
				print('%s: %s' % (os.path.join(dirpath, filename),val))
				i = i + 1
				val = str(val)
				if val in stats.keys():
					stats[val] = stats[val] + 1
				else:
					stats[val] = 0

print('\n\n\n---\n\n\n')
print('')
for key, val in stats.items():
	print("%s: %s (%s%%)" % (key,val,str(round((val/i)*100,2))))


sys.exit()
