class Tracker:
	def __init__(self):
		self.count = 0
	def increment(self):
		self.count += 1
	def reset(self):
		self.count = 0
	def save_to_file(self):
		with open("data.txt", "w") as file:
			file.write(str(self.count))
	def __str__(self):
		return f"Current count: {self.count}"
