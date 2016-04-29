#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>

int sum=0;
pthread_mutex_t mut= PTHREAD_MUTEX_INITIALIZER;

void fun1(int *a)
{
for(int i=0;i<100;i++)
{
	a[i]=i;
}

}
void fun2(int *a)
{
for(int i=0;i<100;i++)
{
	if (a[i]%2!=0)
	{pthread_mutex_lock(&mut);

		sum=sum+a[i]*2;
		pthread_mutex_unlock(&mut);

	}
}
}
void fun3(int *a)
{
for(int i=0;i<100;i++)
{
	if(i%2==1)
		{pthread_mutex_lock(&mut);
			sum-a[i];
			pthread_mutex_unlock(&mut);
		}
}
}
void fun4(int *a)
{
	printf("Answer is\n ",sum);
}
int main()
{
pthread_t t1,t2,t3,t4;
int a[100];
pthread_create(&t1,NULL,fun1,a);
pthread_join(t1,NULL);
pthread_create(&t2,NULL,fun2,a);

pthread_create(&t3,NULL,fun3,a);
pthread_join(&t2,NULL);
pthread_join(&t3,NULL);
pthread_create(&t4,NULL,fun4,a);
pthread_join(&t4,NULL);

return 0;
}
