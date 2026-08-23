.intel_syntax noprefix
.global _start
.text
_start:
; Manual CALLSTACK Project
lea rsp, [callstack]

lea r15, [rip]
jmp save
jmp dprint

jmp exit

exit:
mov rax, 60
xor rdi, rdi
syscall

print:
mov rax, 1
mov rdi, 1
lea rsi, [text]
lea rdx, [textlen]
syscall

jmp back

dprint:
lea r15, [rip]
jmp save
jmp print

lea r15, [rip]
jmp save
jmp print

jmp back

save:

; rax is last index
mov rax, [callstack]
add rax, 8
mov [callstack], rax

; rbx is return address
mov rbx, r15
add rbx, 4

; exc is last address in stack
lea rcx, [callstack]

add rcx, rax

; write to last address, return pos
mov [rcx], rbx

add r15, 2
jmp r15

back:
lea rbx, [callstack]
mov rax, [callstack]
add rbx, rax ; set rbx to the address of the last address

; save return address and wipes stack
mov rcx, [rbx]
mov rdx, 0x0000000000000000
mov [rbx], rdx
; not necessary to clean it but it
; looks better and could lead to less errors

; move the stack back
sub rax, 8
mov [callstack], rax

jmp rcx

.data
callstack: .skip 1024, 0x00
text: .ascii "Hello, World!\n"
textlen = . - text
