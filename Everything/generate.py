
x=range(280)

x[0]=1

for i in range(280):
	if i != 0:
		x[i]=0
		for j in range(i):
			x[i]+=x[j]*x[i-j-1]

		if i%2==0 and i>2:
			y=(x[i-2])
			if i%3==0:
				y+=(x[(i/3)-1]*i*2)/3
			y+=(i*3*x[(i/2)-1])/2
			y/=(2*i)
			print y

		if i%2==1 and i>2:
			y=(x[i-2])
			if i%3==0:
				y+=(x[(i/3)-1]*i*2)/3
			y+=(i*x[(i-3)/2])
			y/=(2*i)
			print y