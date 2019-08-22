a, b, c = input().split()
if a == 'A': print(int(b) + int(c))
elif a == '%': print(int(b) % int(c))
elif a == 'S': print(int(b) - int(c))
elif a == '>':
    if (int(b) > int(c)) == False:
      print("0")
    elif (int(b) > int(c)) == True:
      print("1")
elif a == '<':
     if (int(b) < int(c)) == False:
         print("0")
     elif (int(b) < int(c)) == True:
         print("1")
else: print('Invalid operation!')




