class DisplayImage():
	@staticmethod
	def display(Image, plot_type):
		data = Image.data
		if Image.system == 'polar':
			x, y = DisplayImage.polar_to_cartesian(data[0], data[1])
			data = np.stack([x, y])
		if plot_type=='intensity':
			plt.imshow(data, cmap='gray')
		elif plot_type=='heatmap':
			plt.imshow(data, cmap='hot')
		else:
			raise Error("invalid plot type")
		plt.show()

	@staticmethod
	def polar_to_cartesian(r, theta):
		x = r * np.cos(theta)
		y = r * np.sin(theta)
		return x, y
