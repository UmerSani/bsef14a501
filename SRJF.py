def VRR():

	
i=0


	n=3


	f=open("read.txt","r")


	distlist=[dict()for i in range (n)]


	i=0


	for i in range(0,3):


		line=f.readline()


		num=line.split(" ")


		distlist[i]={'p_n':num[0],'a_t':int(num[1]),'b_t':int(num[2])}
	st=0

	for i in range(0,3):
		j=0 
		for j in range(0,j<i):
			while(distlist[j][a_t]<=st)
				if(distlist[j][p_n]!=NULL)
					temp[p_n]=distlist[i][p_n]
					temp[a_t]=distlist[i][a_t]
					temp[b_t]=distlist[i][b_t]
		
			distlist[i][p_n]=temp[p_n]
			distlist[i][a_t]=temp[a_t]
			distlist[i][b_t]=temp[b_t]
			while(distlist[i][b_t]!=0)
				distlist[i][b_t]=distlist[i][b_t]-1
				st++
			distlist[i][p_n]=NULL

SRJF()
