def iseven(z):
    if(z%2==0):
        print(z,' Is even')
        return True
        
    else :
          print(z,'Is odd')
          return False          

first=0
second=1
sum=0

while(first<4*10**6) :
                  if  iseven(first) :
                      sum=sum+first
           
                  new=first+second
                  first=second
                  second=new
                 
print(sum,' : Is the summary of even numbers from zero to ',4*10**6)
                 