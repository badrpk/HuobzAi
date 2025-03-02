.section .data
message:    .asciz "Hello from Huobz AI (ARM64 Assembly)\n"

.section .text
.global _start

_start:
    mov x0, 1              // File descriptor (stdout)
    ldr x1, =message       // Load address of message
    mov x2, 38             // Length of message
    mov x8, 64             // syscall: write
    svc 0

    mov x8, 93             // syscall: exit
    mov x0, 0
    svc 0
