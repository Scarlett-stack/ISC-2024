<s>plans within plans</s>
files within files

jk 
Ideea e ca la dastea trb binwalk sa vezi ce contin (cred ca mere si cu cryptool dar nu l-am mai folosit demult)
binwalk <file>
vedem ca la offset 33519 avem 7zip archive 
Cred ca in alte timpuri tot cu binwalk o extrageam dar nu mi-am notat nicaieri si a trb sa fac cu dd (si asta e misto tho)

dd if=06-Idea.jpg of=archive.7z bs=1 skip=33519

if = numele filesului original
of numele out file
bs = block size = 1 byte pt acuratete
skip sare
7z e archive.7z -> extractie