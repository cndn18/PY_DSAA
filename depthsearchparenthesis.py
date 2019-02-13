#function to define and count the depth of the parenthesis
def matched(str):
  count = 0
  max_count=0
  for i in str:
      if i == "(":
          count += 1
          if count>max_count:
              max_count=count
      elif i == ")":
          count -= 1
          if count==-1:
            return -1
  if count != 0:
      return -1
  if(count==0):
      return max_count
#an example of the function    

f=matched("a)*(?")
print(f)
