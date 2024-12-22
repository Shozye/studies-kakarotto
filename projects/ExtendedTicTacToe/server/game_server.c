/****************************
Maciej Gębala (CC BY-NC 4.0)
server ver. 0.1
2023-03-30
****************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <time.h>

#include "board.h"

int main(int argc, char *argv[])
{
  clock_t tic_start = clock();
  clock_t receive_wait_time = 0;
  clock_t send_wait_time = 0;
  clock_t tic;

  int socket_desc, client_sock[2];
  socklen_t client_size;
  struct sockaddr_in server_addr, client_addr1, client_addr2;
  char server_message[16], client_message[16];

  int a, b, first;
  int player, moveNo, sockNo, move, msg, end_msg;
  bool isWin, isLose, correct;

  if( argc!=3 ) {
    printf("Wrong number of arguments\n");
    return -1;
  }

  // Create socket
  socket_desc = socket(AF_INET, SOCK_STREAM, 0);
  if( socket_desc<0 ) {
    printf("Error while creating socket\n");
    return -1;
  }
  printf("Socket created successfully\n");

  // Set port and IP
  server_addr.sin_family = AF_INET;
  server_addr.sin_port = htons(atoi(argv[2]));
  server_addr.sin_addr.s_addr = inet_addr(argv[1]);

  // Bind to the set port and IP
  if( bind(socket_desc, (struct sockaddr*)&server_addr, sizeof(server_addr))<0 ) {
    printf("Couldn't bind to the port\n");
    return -1;
  }
  printf("Done with binding\n");

  if( listen(socket_desc, 1)<0 ) {
    printf("Error while listening\n");
    return -1;
  }
  printf("\nListening for incoming connections.....\n");

  // Accept incoming connection 1
  client_size = sizeof(client_addr1);
  client_sock[0] = accept(socket_desc, (struct sockaddr*)&client_addr1, &client_size);
  if( client_sock[0]<0 ) {
    printf("Can't accept\n");
        return -1;
  }
  printf("Client 1 connected at IP: %s and port: %i\n", inet_ntoa(client_addr1.sin_addr), ntohs(client_addr1.sin_port));

  // Accept incoming connection 2
  client_size = sizeof(client_addr2);
  client_sock[1] = accept(socket_desc, (struct sockaddr*)&client_addr2, &client_size);
  if( client_sock[1]<0 ) {
    printf("Can't accept\n");
    return -1;
  }
  printf("Client 2 connected at IP: %s and port: %i\n", inet_ntoa(client_addr2.sin_addr), ntohs(client_addr2.sin_port));

  clock_t tic_middle = clock();

  // client 1 recognition
  memset(server_message, '\0', sizeof(server_message));
  strcpy(server_message, "700");

  tic = clock();
  if( send(client_sock[0], server_message, strlen(server_message), 0)<0 ) {
    printf("Can't send\n");
    return -1;
  }
  send_wait_time += clock() - tic;


  memset(client_message, '\0', sizeof(client_message));
  tic = clock();
  if( recv(client_sock[0], client_message, sizeof(client_message), 0)<0 ) {
    printf("Couldn't receive\n");
    return -1;
  }
  receive_wait_time += clock() - tic;


  printf("Message from client 1: %s\n", client_message);

  a=atoi(client_message);
  if( a==1 ) first = 0; else first = 1;

  // client 2 recognition
  memset(server_message, '\0', sizeof(server_message));
  strcpy(server_message, "700");
  tic = clock();
  if( send(client_sock[1], server_message, strlen(server_message), 0)<0 ) {
    printf("Can't send\n");
    return -1;
  }
  send_wait_time += clock() - tic;
  memset(client_message, '\0', sizeof(client_message));
  tic = clock();
  if( recv(client_sock[1], client_message, sizeof(client_message), 0)<0 ) {
    printf("Couldn't receive\n");
    return -1;
  }
  receive_wait_time += clock() - tic;
  printf("Message from client 2: %s\n", client_message);

  b=atoi(client_message);
  if( a==b ) {
    printf("No player diversity\n");
    return -1;
  }

  memset(server_message, '\0', sizeof(server_message));
  strcpy(server_message, "600");
  tic = clock();
  if( send(client_sock[first], server_message, strlen(server_message), 0)<0 ) {
     printf("Can't send\n");
     return -1;
  }
  send_wait_time += clock() - tic;


  player = 1;
  moveNo = 0;
  isWin = false;
  isLose = false;
  correct = true;
  sockNo = first;

  setBoard();
  
  while( (moveNo<25) && (!isWin) && (!isLose) && correct ) {
    moveNo++;
    printf("Move no: %d\n", moveNo);
    memset(client_message, '\0', sizeof(client_message));

    tic = clock();
    if( recv(client_sock[sockNo], client_message, sizeof(client_message), 0)<0 ) {
      printf("Couldn't receive\n");
      return -1;
    }
    receive_wait_time += clock() - tic;

    printf("Client message: %s\n", client_message);
    move = atoi(client_message);
    correct = setMove(move, player);

    if( correct ) isWin = winCheck(player);
    if( correct && !isWin ) isLose = loseCheck(player);
    if( !correct ) { msg =400; end_msg = 500; }
    else if( isWin ) { msg = 200+move; end_msg = 100; }
    else if( isLose ) { msg = 100+move; end_msg = 200; }
    else if( moveNo==25 ) { msg = 300+move; end_msg = 300; }
    else msg = move;

    memset(server_message, '\0', sizeof(server_message));
    sprintf(server_message, "%d", msg);
    player = 3-player;
    sockNo = 1-sockNo;

    tic = clock();
    if( send(client_sock[sockNo], server_message, strlen(server_message), 0)<0 ) {
      printf("Can't send\n");
      return -1;
    }
    send_wait_time += clock() - tic;
    printf("Server message: %s\n",server_message);
    printBoard();
  }

  sockNo = 1-sockNo;
  memset(server_message, '\0', sizeof(server_message));
  sprintf(server_message, "%d", end_msg);
  tic = clock();
  if( send(client_sock[sockNo], server_message, strlen(server_message), 0)<0 ) {
    printf("Can't send\n");
    return -1;
  }
  send_wait_time += clock() - tic;

  printf("Server message: %s\n",server_message);

  //printBoard();

  // Closing sockets
  close(client_sock[0]);
  close(client_sock[1]);
  close(socket_desc);

  printf("End.\n");
  clock_t tic_end = clock();
  long elapsed_socketing = tic_middle - tic_start;
  long elapsed_playing = tic_end - tic_middle;
  printf("[TIME_WAITING] %ld %ld\n", receive_wait_time, send_wait_time);
  printf("[TIME] %ld %ld", elapsed_socketing, elapsed_playing);

  return 0;
}
