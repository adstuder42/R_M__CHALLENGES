#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <crypt.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  char pid[16];

  snprintf(pid, sizeof(pid), "%i", getpid());

  char *args[] = {"/bin/bash", pid, 0};

  args[1] = crypt(pid, "$1$awesome");
  execve("/home/stormind/Documents/root-me/cryptanalyse/pid", &args[0], NULL);
  return 0;
}