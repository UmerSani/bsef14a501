
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

	j=0
	
	end[3]
	k=0
	for i in range(0,3):
		first=distlist[i]['a_t']
		for j in range(1,3):
			if(distlist[j]['a_t']<distlist[j-1]['a_t']):
				first=distlist[j-1]['a_t']
				sec=distlist[j-1]['b_t']
				distlist[j-1]['a_t']=distlist[j]['a_t']
				distlist[j-1]['b_t']=distlist[j]['b_t']
				distlist[j]['a_t']=first
				distlist[j]['a_t']=sec
	st=distlist[0]['a_t']
	n=3
	for l in range(0,3)
		AQ[l][p_n]=NULL
		AQ[l][a_t]=NULL
		AQ[l][b_t]=NULL
	for i in range (0,n):
		while(AQ[i][p_n]!=NULL & st>=AQ[i][a_t])
			for k in range(0,2):
				while(AQ[i][b_t]!=0):
					AQ[j]['b_t']=AQ[j]['b_t']-1
					st=st+1
			AQ[i][a_t]=AQ[i][a_t]+5
		if(st>=distlist[i][a_t]):
			if(distlist[i][p_n]%2==0)
				for k in range(0,2):
					while(distlist[i][b_t]!=0):
						distlist[j]['b_t']=distlist[j]['b_t']-1
						st=st+1
			else
				for k in range(0,3):
					while(distlist[i][b_t]!=0):
						distlist[j]['b_t']=distlist[j]['b_t']-1
						st=st+1
			if(distlist[i][b_t]>0)
				if(distlist[i][p_n]%2==0)
					AQ[i][p_n]=distlist[i][p_n]
					AQ[i][a_t]=distlist[i][a_t]
					AQ[i][b_t]=distlist[i][b_t]
				distlist[n][p_n]=distlist[i][p_n]
				distlist[n][a_t]=distlist[i][a_t]
				distlist[n][b_t]=distlist[i][b_t]
			else
				end[k++]=st
	print(distlist[0][p_n]" Waiting time is "end[0]-distlist[0][a_t])

	print(distlist[1][p_n]" Waiting time is "end[1]-distlist[1][a_t])

	print(distlist[2][p_n]" Waiting time is "end[2]-distlist[2][a_t]
VRR()
