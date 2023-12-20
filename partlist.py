def partlist(arr):
  res = []
	kc = ''
	zc = ''
	for i in range(0, len(arr)):
    tmp = []
		for k in range(0, i):
			kc += arr[k] + ' '
		tmp.append(kc[0:len(kc)-1])
		kc = ''
		for z in range(i, len(arr)):
			zc += arr[z] + ' '
		tmp.append(zc[0:len(zc)-1])
		zc = ''
		if '' not in tmp:
			res.append(tuple(tmp))
	return res
