import requests
import time
start_time = time.time()


with open('photo-link.txt','r') as f:
    
    sum = 0
    for line in f:
        response = requests.get(line.strip('\n'))
        a = line.split("images/")
        b = a[1].split("/")
        with open(f'C:/Users/Admin/Desktop/Shiam/Practice/file Read/photos/{b[0]}.jpeg', 'wb') as file:
            file.write(response.content)
            
            
print("--- %s seconds ---" % (time.time() - start_time))

