import time
from tracker import Tracker

def read_config():
	with open("../config/config.txt", "r") as file:
		for line in file:
			value = line.split("=")[1]
			return int(value)

a = 1
interval = read_config()
tracker = Tracker()
while True:
	tracker.increment()
	print(tracker)
	tracker.save_to_file()
	time.sleep(interval)
