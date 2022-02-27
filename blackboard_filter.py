import cv2
import numpy as np

class BlackBoard(object):

	def __init__(self):
		pass

	def resize(self,image,window_height = 1000):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	
		
	def render(self,image):
		# Create sharpening kernel
		kernel = np.array([[1,-1,0], [-1,4,-1], [-1,0,-1]])

		# applying the sharpening kernel to the input image & displaying it.
		drawing = cv2.filter2D(image, -1, kernel)

		# Noise reduction
		drawing = cv2.bilateralFilter(drawing, 9, 75, 75) 
		return drawing

	def start(self, img_path):
		image = cv2.imread(img_path)
		tmp_canvas = BlackBoard()
		image = tmp_canvas.resize(image, 1000)
		res = tmp_canvas.render(image)
		cv2.imwrite('BlackBoard_image.jpg', res)
		cv2.imshow('BlackBoard image',res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("Image saved as 'BlackWhite_image.jpg'")
