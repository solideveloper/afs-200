def stringEval (string) :
     lower = 0
     upper = 0
     for i in range(len(string)) :
          if(string[i]>='a' and string[i]<='z'):
               lower += 1
          elif(string[i]>='A' and string[i]<='Z'):
               upper += 1
     print ("Printed String:", string)
     print('Lower case letters = ' + str(lower))
     print('Upper case letters = ' + str(upper))

stringEval('How Many UPPER and lower Case Letter Are In This String?')