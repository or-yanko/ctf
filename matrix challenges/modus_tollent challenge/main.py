#made by or yanko 04.03.2021



#make mulutal work ------------------------------------------------------
def union_of_list(l1, l2):
    merge = []
    for char in l1:
        if char in l2:
            merge.append(char)
    return merge

#fins si offset and func name -------------------------------------------
def find_si(lines, line_num):
    #find si
    si = 0x0
    line_num += 2
    line = lines[line_num]
    splites_str_si = line.split(' ')
    str_si = splites_str_si[len(splites_str_si)-1]
    try:
        if str_si[2] == 'h':
            final_str_si = str_si[0] + str_si[1]
            si = int(final_str_si, 16)
        else:
            si = int(str_si, 10)
    except:
        si = int(str_si, 10)

    return si
def find_offset(lines, line_num):
    # find offset in input string
    str_offset = ""
    line = lines[line_num]
    str_offset += line[27]
    str_offset += line[28]
    offset = int(str_offset, 16)
    final_offset = 0x90 - offset
    return final_offset
def find_which_func_to_use(lines, line_num):
    line_num += 4
    func = 'f'
    line = lines[line_num]
    func += line[9]
    return func


# f1 --------------------------------------------------------------------
def f1(lst, place, si):
    lst1 = lst[place]
    lst2 = f1_all_posibilities(si)
    lst[place] = union_of_list(lst1, lst2)
def f1Check(di, si):
    num = di // 0x10
    if num & 0xf == si:
        return True
    return False
def f1_all_posibilities(si):
    allposi = []

    for i in range(1, 0xff):
        x = chr(i)
        if f1Check(i, si):
            allposi.append(x)
    return allposi

# f2 --------------------------------------------------------------------
def f2(lst, place, si):
    lst1 = lst[place]
    lst2 = f2_all_posibilities(si)
    lst[place] = union_of_list(lst1, lst2)
def f2Check(di, si):
    if di & 0xf == si:
        return True
    return False
def f2_all_posibilities(si):
    allposi = []
    for i in range(1, 0xff):
        x = chr(i)
        if f2Check(i, si):
            allposi.append(x)
    return allposi

# f3 --------------------------------------------------------------------
def f3(lst, place, si):
    lst1 = lst[place]
    lst2 = f3_all_posibilities(si)
    lst[place] = union_of_list(lst1, lst2)
def f3Check(di, si):
    num = ~ di & 0xff
    num //= 0x10
    if num & 0xf == si:
        return True
    return False
def f3_all_posibilities(si):
    allposi = []

    for i in range(1, 0xff):
        x = chr(i)
        if f3Check(i, si):
            allposi.append(x)
    return allposi


# f4 --------------------------------------------------------------------
def f4(lst, place, si):
    lst1 = lst[place]
    lst2 = f4_all_posibilities(si)
    lst[place] = union_of_list(lst1, lst2)
def f4Check(di, si):
    num = ~ di & 0xff
    if num & 0xf == si:
        return True
    return False
def f4_all_posibilities(si):
    allposi = []

    for i in range(1, 0xff):
        x = chr(i)
        if f4Check(i, si):
            allposi.append(x)
    return allposi


#main -------------------------------------------------------------------
def main():
    filled_list = []
    full_list = []
    assemblytext = """movzx   eax, byte ptr [rbp-70h]
movsx   eax, al
mov     esi, 0Fh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1D92
movzx   eax, byte ptr [rbp-75h]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1D98
movzx   eax, byte ptr [rbp-85h]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1D9E
movzx   eax, byte ptr [rbp-8Ah]
movsx   eax, al
mov     esi, 0Dh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1DA4
movzx   eax, byte ptr [rbp-71h]
movsx   eax, al
mov     esi, 2
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1DAA
movzx   eax, byte ptr [rbp-7Dh]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1DB0
movzx   eax, byte ptr [rbp-67h]
movsx   eax, al
mov     esi, 0
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1DB6
movzx   eax, byte ptr [rbp-80h]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1DBC
movzx   eax, byte ptr [rbp-78h]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1DC2
movzx   eax, byte ptr [rbp-66h]
movsx   eax, al
mov     esi, 0Fh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1DC8
movzx   eax, byte ptr [rbp-86h]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1DCE
movzx   eax, byte ptr [rbp-6Fh]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1DD4
movzx   eax, byte ptr [rbp-86h]
movsx   eax, al
mov     esi, 0Dh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1DDA
movzx   eax, byte ptr [rbp-7Bh]
movsx   eax, al
mov     esi, 0Bh
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1DE0
movzx   eax, byte ptr [rbp-74h]
movsx   eax, al
mov     esi, 7
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1DE6
movzx   eax, byte ptr [rbp-85h]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1DEC
movzx   eax, byte ptr [rbp-6Eh]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1DF2
movzx   eax, byte ptr [rbp-80h]
movsx   eax, al
mov     esi, 0Bh
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1DF8
movzx   eax, byte ptr [rbp-71h]
movsx   eax, al
mov     esi, 4
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1DFE
movzx   eax, byte ptr [rbp-8Bh]
movsx   eax, al
mov     esi, 0Fh
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1E04
movzx   eax, byte ptr [rbp-7Fh]
movsx   eax, al
mov     esi, 4
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E0A
movzx   eax, byte ptr [rbp-7Dh]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1E10
movzx   eax, byte ptr [rbp-6Dh]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1E16
movzx   eax, byte ptr [rbp-8Bh]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E1C
movzx   eax, byte ptr [rbp-65h]
movsx   eax, al
mov     esi, 0Dh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E22
movzx   eax, byte ptr [rbp-77h]
movsx   eax, al
mov     esi, 8
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E28
movzx   eax, byte ptr [rbp-72h]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1E2E
movzx   eax, byte ptr [rbp-75h]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E34
movzx   eax, byte ptr [rbp-7Ah]
movsx   eax, al
mov     esi, 0Eh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E3A
movzx   eax, byte ptr [rbp-73h]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1E40
movzx   eax, byte ptr [rbp-73h]
movsx   eax, al
mov     esi, 0Fh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E46
movzx   eax, byte ptr [rbp-8Ah]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E4C
movzx   eax, byte ptr [rbp-81h]
movsx   eax, al
mov     esi, 4
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E52
movzx   eax, byte ptr [rbp-8Dh]
movsx   eax, al
mov     esi, 0Bh
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E58
movzx   eax, byte ptr [rbp-69h]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1E5E
movzx   eax, byte ptr [rbp-87h]
movsx   eax, al
mov     esi, 1
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E64
movzx   eax, byte ptr [rbp-8Fh]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1E6A
movzx   eax, byte ptr [rbp-66h]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E70
movzx   eax, byte ptr [rbp-8Ch]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1E76
movzx   eax, byte ptr [rbp-8Dh]
movsx   eax, al
mov     esi, 8
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E7C
movzx   eax, byte ptr [rbp-87h]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E82
movzx   eax, byte ptr [rbp-6Ah]
movsx   eax, al
mov     esi, 7
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1E88
movzx   eax, byte ptr [rbp-7Eh]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E8E
movzx   eax, byte ptr [rbp-84h]
movsx   eax, al
mov     esi, 0Ah
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1E94
movzx   eax, byte ptr [rbp-6Ch]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1E9A
movzx   eax, byte ptr [rbp-83h]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1E9D
movzx   eax, byte ptr [rbp-72h]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1EA0
movzx   eax, byte ptr [rbp-83h]
movsx   eax, al
mov     esi, 0
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EA3
movzx   eax, byte ptr [rbp-69h]
movsx   eax, al
mov     esi, 0
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EA6
movzx   eax, byte ptr [rbp-7Ch]
movsx   eax, al
mov     esi, 0
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EA9
movzx   eax, byte ptr [rbp-82h]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1EAC
movzx   eax, byte ptr [rbp-81h]
movsx   eax, al
mov     esi, 8
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1EAF
movzx   eax, byte ptr [rbp-70h]
movsx   eax, al
mov     esi, 0Ah
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1EB2
movzx   eax, byte ptr [rbp-76h]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1EB5
movzx   eax, byte ptr [rbp-65h]
movsx   eax, al
mov     esi, 7
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1EB8
movzx   eax, byte ptr [rbp-6Fh]
movsx   eax, al
mov     esi, 0Ah
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EBB
movzx   eax, byte ptr [rbp-6Bh]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1EBE
movzx   eax, byte ptr [rbp-7Fh]
movsx   eax, al
mov     esi, 8
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1EC1
movzx   eax, byte ptr [rbp-76h]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1EC4
movzx   eax, byte ptr [rbp-89h]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1EC7
movzx   eax, byte ptr [rbp-6Ah]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1ECA
movzx   eax, byte ptr [rbp-68h]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1ECD
movzx   eax, byte ptr [rbp-8Eh]
movsx   eax, al
mov     esi, 0Bh
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1ED0
movzx   eax, byte ptr [rbp-6Dh]
movsx   eax, al
mov     esi, 0
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1ED3
movzx   eax, byte ptr [rbp-7Ah]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1ED6
movzx   eax, byte ptr [rbp-79h]
movsx   eax, al
mov     esi, 0Bh
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1ED9
movzx   eax, byte ptr [rbp-7Eh]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EDC
movzx   eax, byte ptr [rbp-74h]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EDF
movzx   eax, byte ptr [rbp-77h]
movsx   eax, al
mov     esi, 6
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EE2
movzx   eax, byte ptr [rbp-6Bh]
movsx   eax, al
mov     esi, 8
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EE5
movzx   eax, byte ptr [rbp-8Fh]
movsx   eax, al
mov     esi, 4
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1EE8
movzx   eax, byte ptr [rbp-8Ch]
movsx   eax, al
mov     esi, 0Ah
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1EEB
movzx   eax, byte ptr [rbp-82h]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EEE
movzx   eax, byte ptr [rbp-7Ch]
movsx   eax, al
mov     esi, 0Ah
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1EF1
movzx   eax, byte ptr [rbp-88h]
movsx   eax, al
mov     esi, 0Ah
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1EF4
movzx   eax, byte ptr [rbp-89h]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1EF7
movzx   eax, byte ptr [rbp-68h]
movsx   eax, al
mov     esi, 1
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EFA
movzx   eax, byte ptr [rbp-90h]
movsx   eax, al
mov     esi, 2
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1EFD
movzx   eax, byte ptr [rbp-78h]
movsx   eax, al
mov     esi, 9
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1F00
movzx   eax, byte ptr [rbp-67h]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1F03
movzx   eax, byte ptr [rbp-6Ch]
movsx   eax, al
mov     esi, 5
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1F06
movzx   eax, byte ptr [rbp-7Bh]
movsx   eax, al
mov     esi, 1
mov     edi, eax
call    f2
test    eax, eax
jnz     loc_1F09
movzx   eax, byte ptr [rbp-8Eh]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1F0C
movzx   eax, byte ptr [rbp-79h]
movsx   eax, al
mov     esi, 3
mov     edi, eax
call    f1
test    eax, eax
jnz     loc_1F0F
movzx   eax, byte ptr [rbp-88h]
movsx   eax, al
mov     esi, 0Bh
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1F12
movzx   eax, byte ptr [rbp-90h]
movsx   eax, al
mov     esi, 0Bh
mov     edi, eax
call    f3
test    eax, eax
jnz     loc_1F15
movzx   eax, byte ptr [rbp-84h]
movsx   eax, al
mov     esi, 0Ch
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1F18
movzx   eax, byte ptr [rbp-6Eh]
movsx   eax, al
mov     esi, 1
mov     edi, eax
call    f4
test    eax, eax
jnz     loc_1F1B
lea     rdi, aSucess    ; "Sucess!"
call    sub_10D0
mov     eax, 0
jmp     loc_1F2D"""
    lines = assemblytext.split('\n')
    #fill the main array of arrays
    for i in range(0x20, 0xff):
        filled_list.append(chr(i))
    for i in range(1, 0x30):
        full_list.append(filled_list)
    #loop of every command that we use to the string
    for first_line_num in range(0, 616, 7):
        #read the command
        line_num = first_line_num
        offset = find_offset(lines, line_num)
        si = find_si(lines, line_num)
        func = find_which_func_to_use(lines, line_num)

#        print('si=', si, '\toffset=', offset, '\tfunc=', func)

        #use the command
        if func == 'f1':
            f1(full_list, offset, si)
        elif func == 'f2':
            f2(full_list, offset, si)
        elif func == 'f3':
            f3(full_list, offset, si)
        elif func == 'f4':
            f4(full_list, offset, si)
        else:
            exit('error')


        #delete
        #for i in full_list:
        #    print(i)

    #make the list of list a string
    final_str = ""
    for lst in full_list:
        try:
            final_str += lst[0]
        except:
            final_str += chr(0x7)

    print(final_str)

main()
