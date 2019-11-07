def check(s,l):
  at = s.find('@') #check for '@' to confirm if it's an email or website
  if(at != -1):   #
    i=0
    checker = False
    #the conditions are checking character's ASCII values
    #the actual character can be used as well such as 'if (string[0]<'s'):'
    if (ord(s[0])<58 and ord(s[0])>47):
      return False
    else: 
      checker = True
    for i in range(at):
      if ((ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57) or ord(s[i])==95 or ord(s[i])==46):       
        checker = True 
      else:
        return False
    domain_list = ["gmail","yahoo","hotmail"]  #add your email domains
    suffix_list = ["com","net","org"]          #email suffixes
    dot = s.rfind('.')
    domain = s[at+1 : dot]
    if domain in domain_list:
      checker = True
        
    else:
      return False
        
    suffix = s[dot+1 : len(s)]  
    if suffix in suffix_list:
      checker = True
    else:
      return False

    if(checker==True):
      print("EMAIL",l+1)
      return checker

  else:
    dot1=s.find('.')
    dot2=s.rfind('.')
    for i in range(3):
      if ((ord(s[i])==119)):
        checker = True
      else:
        return False

    for i in range(dot1+1,dot2):
      if ((ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57)):
        checker = True
        
      else:
        return False

    suffix_list = ["com","net","org"] 
    suffix = s[dot2+1 : len(s)]  
    if suffix in suffix_list:
      checker = True
    else:
      return False

    if(checker==True):
      print("WEB",l+1)
      return checker


n=int(input("Enter a number "))
stringlist=[]
for c in range(n):
  print(c+1, end=". ")
  newline=input()
  newline=newline.lower()
  newline=newline.strip()
  stringlist.append(newline)
  #print(stringlist)
for c in range(n):
  check(stringlist[c],int(c))
  #if(check(stringlist[c],int(c))==False):
  #  print("invalid",c+1)
