import hashlib

def crack_sha1_hash(hash,use_salts=False):
  passwordlines=[];
  saltlines=[];
  found =False;
  with open('top-10000-passwords.txt') as file:
      passwordlines = file.readlines();
  with open('known-salts.txt') as saltfile:
      saltlines = saltfile.readlines();    

  if(use_salts == False):    
    for password in passwordlines:
       newhash = hashlib.sha1(password.strip().encode('utf-8'));
    
       if(hash== newhash.hexdigest()):
          found =True;
          return password.strip();
    if(found==False):
     return "PASSWORD NOT IN DATABASE";
   

  else:
    for password in passwordlines:
        for salt in saltlines:
          prependsalt= salt.strip()+password.strip();
          appendsalt=password.strip()+salt.strip();
          prependhash = hashlib.sha1(prependsalt.encode('utf-8'));
          appenddhash = hashlib.sha1(appendsalt.encode('utf-8'));

          if((hash == prependhash.hexdigest()) or (hash == appenddhash.hexdigest())):
            found = True;
            return password.strip();

    if(found==False):
     return "PASSWORD NOT IN DATABASE";        

         
             

    