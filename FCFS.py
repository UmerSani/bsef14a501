
def FCFS():
	
i=0

	n=3

	f=open("read.txt","r")

	distlist=[dict()for i in range (n)]

	i=0

	for i in range(0,3):

		line=f.readline()

		num=line.split(" ")

		distlist[i]={'p_n':num[0],'a_t':int(num[1]),'b_t':int(num[2])}

	s_t=distlist[0]['a_t']

	i=0

	w=[0 for i in range(3)]

	i=0

	for i in range(0,3):

		s_t=s_t+distlist[i]['b_t']

		w[i]=s_t-distlist[i]['a_t']-distlist[i]['b_t']

	i=0

	wt=(w[0]+w[1]+w[2])/3
	
	for i in range(0,3):

		print(distlist[i]['p_n']," waiting time is ",w[i])

	print("Average waiting Time is: ",wt)


FCFS()
