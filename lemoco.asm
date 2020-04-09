section .data
	
	metinaa: db "uc saniye", 10,""
	metinaa_l: equ $-metinaa

	metina: db "iki saniye "
	metina_l: equ $-metina

	forsleep:
		saniye: dd 0
		nanosaniye: dd 0


section .text

	mov dword [saniye], 2
	mov dword [nanosaniye], 0
	mov eax, 162
	mov ebx, forsleep
	mov ecx, 0
	int 80h

	mov eax,4
	mov ebx, 1
	mov ecx, metina
	mov edx, metina_l
	int 80h

	mov dword [saniye], 3
	mov dword [nanosaniye], 0
	mov eax, 162
	mov ebx, forsleep
	mov ecx, 0
	int 80h

	mov eax,4
	mov ebx, 1
	mov ecx, metinaa
	mov edx, metinaa_l
	int 80h

	mov eax, 1
	xor ebx, ebx
	int 80h
