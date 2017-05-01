//filetransferserver.c
#include <stdio.h>
#include <sys/types.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#define SA struct sockaddr
#define LISTENQ 5
int main(int argc,char**argv)
{
int fd,sockfd,listenfd,connfd;
pid_t childpid;
socklen_t client;
struct sockaddr_in servaddr,cliaddr;
listenfd=socket(AF_INET,SOCK_STREAM,0);
bzero(&servaddr,sizeof(servaddr));
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
servaddr.sin_port=htons(atoi(argv[1]));
bind(listenfd,(SA*)&servaddr,sizeof(servaddr));
listen(listenfd,LISTENQ);
client=sizeof(cliaddr);
connfd=accept(listenfd,(SA*)&cliaddr,&client);
char buffer[100];
FILE *fp;
read(connfd,buffer,100);
fp=fopen("word1.txt","w");
fprintf(fp,"%s",buffer);
printf("the file was received successfully");
printf("the new file created is add1.txt");
}