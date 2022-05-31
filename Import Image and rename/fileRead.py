import requests
import time
start_time = time.time()

def imgDownloader (initial_dir, final_dir):
    
    with open(initial_dir,'r') as f:
        
        for line in f:
            response = requests.get(line.strip('\n'))
            a = line.split("images/")
            b = a[1].split("/")
            with open(f'{final_dir}/{b[0]}.jpeg', 'wb') as file:
                file.write(response.content)
            
            
print("--- %s seconds ---" % (time.time() - start_time))

imgDownloader('photo-link-Copy.txt',"C:/Users/Admin/Desktop/Shiam/Data Management/Python-Data-management/Import Image and rename/test")