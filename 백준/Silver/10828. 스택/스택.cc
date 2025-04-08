#include <stdio.h>
#include <string.h>

int stack[10000];
int top = -1;

void push (int item){
    stack[++top] = item;
}

int pop(){
    if(top == -1) return -1;
    return stack[top--];
}

int size(){
    return top + 1;
}

int empty(){
    if(top == -1) return 1;
    else return 0;
    //return (top == -1) ? 1 : 0;
}

int peek(){
    if(top == -1) return -1;
    return stack[top];
}

int main() {
    int n, x;
    char command[20];

    setvbuf(stdin, NULL, _IOFBF, 1 << 20);
    setvbuf(stdout, NULL, _IOFBF, 1 << 20);
    
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%s", command);

        if(strcmp(command, "push") == 0){
            scanf("%d", &x);
            push(x);
        }else if(strcmp(command, "pop") == 0){
            printf("%d\n", pop());
        }
        else if(strcmp(command, "size") == 0){
            printf("%d\n", size());
        }
        else if(strcmp(command, "empty") == 0){
            printf("%d\n", empty());
        }
        else if(strcmp(command, "top") == 0){
            printf("%d\n", peek());
        }
    }
    return 0;
}