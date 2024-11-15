#include <stdio.h>

void addtwo(int x);

int main() {
  int x = 0;
  addtwo(x);
  printf("%d\n", x);
}

void addtwo(int x) {
  x += 2;
  return;
}
