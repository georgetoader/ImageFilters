import cv2

class BlackWhite(object):

	def __init__(self):
		pass

	def resize(self,image,window_height = 1000):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	
	
	def render(self, img_rgb):
		img_rgb = cv2.imread(img_rgb)
		img_rgb = self.resize(img_rgb, 1000)
		numDownSamples = 2
		numBilateralFilters = 50

		img_color = img_rgb
		for _ in range(numDownSamples):
			img_color = cv2.pyrDown(img_color)

		for _ in range(numBilateralFilters):
			img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

		for _ in range(numDownSamples):
			img_color = cv2.pyrUp(img_color)

		# convert to grayscale and apply median blur
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
		return img_gray

	def start(self, img_path):
		tmp_canvas = BlackWhite()
		file_name = img_path
		res = tmp_canvas.render(file_name)
		cv2.imwrite("BlackWhite_image.jpg", res)
		cv2.imshow("BlackWhite image", res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("Image saved as 'BlackWhite_image.jpg'")
