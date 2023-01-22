def clean(type):
	f = open(f"{type}_list.txt")
	labels = {'backward', 'down', 'forward', 'go', 'left', 'off', 'on', 'right', 'stop', 'up'}
	nf = open(f"{type}_list_cleaned.txt", "a")

	for line in f:
		if not line:
			continue
		name = line.split("/")[0]
		if name not in labels:
			continue
		nf.write(line)
	f.close()
	nf.close()

for type in ['testing', 'validation']:
	clean(type)