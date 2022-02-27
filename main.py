import argparse as arg
import sys

import blackwhite_filter
import cartoon_filter
import blackboard_filter
import sketch_filter
import vintage_filter

bl_wh = blackwhite_filter.BlackWhite()
cartoon = cartoon_filter.Cartoon()
bboard = blackboard_filter.BlackBoard()
sketch = sketch_filter.Sketch()
vintage = vintage_filter.Vintage()

parser = arg.ArgumentParser('Image-Filters')

parser.add_argument("-i", "--image", required = True,  metavar = '', help = "Input Image Path")
args = parser.parse_args()

if __name__ == '__main__':
	print("Please select filter :\n" \
		"1. Black White\n" \
		"2. Cartoon\n" \
		"2. Black board\n" \
		"4. Sketch\n" \
		"5. Vintage\n" \
		"Anything else to exit\n")
	
	filter_num = input("Select filters from 1, 2, 3, 4, 5 : ")
	while(filter_num != 0):
		if(filter_num == "1"):

			bl_wh.start(args.image)
	
		elif(filter_num == "2"):

			cartoon.start(args.image)

		elif(filter_num == "3"):

			bboard.start(args.image)

		elif(filter_num == "4"):

			sketch.start(args.image)

		elif(filter_num == "5"):

			vintage.start(args.image)

		else:

			print("Exit")
			sys.exit()

		filter_num = input("\nSelect filters from 1, 2, 3, 4, 5 : ")
