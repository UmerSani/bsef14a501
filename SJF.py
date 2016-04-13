
def SJF():	
	i=0
	n=3
	f=open("read.txt","r")
	
	arry=[for i in range (n)]
	
	k=[0 for i in range(3)]
	
	for i in range(0,3):
		
		file=f.readline()
	
		num=file.split(" ")
		
		arry[i]={'p_n':num[0],'a_t':int(num[1]),'b_t':int(num[2])}
		
		k[i]=i
	s_t=arry[0]['a_t']
	
	i=1
	
	temp=0
	temppp=0
	
	total=0
	
	w_t=[0 for i in range(3)]
	
	for i in range(1,3) :
	
		if(arry[i-1]['b_t'] > arry[i]['b_t']):
			
			temp=arry[i-1]['b_t']
	    
					arry[i-1]['b_t']=arry[i]['b_t']
	                arry[i]['b_t']=temp
		    
				temppp=k[i-1]
		        
				k[i-1]=k[i]
		        
				k[i]=temppp
            
	print("\nWaiting time for Job ",k[0]+1,": 0 units")
	i=1
	for i in range(1,3):
	        
			w_t[i]=arry[i-1]['b_t']+w_t[i-1]
	        
			print("\nWaiting time for Job ",k[i]+1," : ",w_t[i],"units \t")
	        
			total = total + w_t[i]
	
	print("\n\nThe total waiting time : ",total,"\t")
    	
		avg= total/n
    	
		print("\n\nAverage waiting time : ",avg,"\t\n\n")
   

SJF()
