#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 20000

typedef int element;
typedef struct{
    element data[MAX_QUEUE_SIZE];
    int front, back;
}Queue;


void push (Queue *q, element item){
    if(q->back == MAX_QUEUE_SIZE-1) return;
    q->data[++(q->back)] = item;
}

int pop(Queue *q){
    if(q->front == q->back) return -1;
    return q->data[++(q->front)];
}

int size(Queue *q){
    return q->back - q->front;
}

int empty(Queue *q){
    return (q -> front == q->back) ? 1 : 0;
}

int front(Queue *q){
    if(q -> front == q->back) return -1;
    return q->data[q->front + 1];
}

int back(Queue *q){
    if(q -> front == q->back) return -1;
    return q->data[q->back];
}

int main() {
    Queue q = {.front = -1, .back = -1};
    int n, x;
    char command[20];

    setvbuf(stdin, NULL, _IOFBF, 1 << 20);
    setvbuf(stdout, NULL, _IOFBF, 1 << 20);

    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%s", command);

        if(strcmp(command, "push") == 0){
            scanf("%d", &x);
            push(&q,x);
        }else if(strcmp(command, "pop") == 0){
            printf("%d\n", pop(&q));
        }
        else if(strcmp(command, "size") == 0){
            printf("%d\n", size(&q));
        }
        else if(strcmp(command, "empty") == 0){
            printf("%d\n", empty(&q));
        }
        else if(strcmp(command, "front") == 0){
            printf("%d\n", front(&q));
        }
        else if(strcmp(command, "back") == 0){
            printf("%d\n", back(&q));
        }
    }
    return 0;
}