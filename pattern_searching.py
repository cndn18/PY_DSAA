value=input("Enter the value or string to search for: ")
count = 0    
with open("C:\\Users\\HP\\Desktop\\search.txt", 'r') as f:
    for word in f.readlines():
        words = word.lower().split()
        if value in words:
            count += 1
    print(count)
