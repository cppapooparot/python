def read_config():
	with open("../config/config.txt", "r") as file:
		for line in file:
			value = line.split("=")[1]
			return int(value)

interval = read_config()
print(interval)

