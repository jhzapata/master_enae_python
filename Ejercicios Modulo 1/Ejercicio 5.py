#Para practicar con la depuración del código: Repara el programa subido al aula
#virtual. exercice_debug_1.p

#MODIFY EACH STEP IN ORDER TO RUN COMPLETLY THE PROGRAM
print('STEP 1')

for i in range(0,11):
    x = i

print(f'x should be 10:{x}')

if x == 10:
    print('SUCCESS! IN STEP 1')

print('STEP 2')
x = False

for i in range(0,11):
    x = x and True
    if x and  i == 5:
        break 
    

print(f'x should be True:{x}')
print(f'i should be 5:{i}')
if i == 5 and x:
    print('SUCCESS! IN STEP 2')

