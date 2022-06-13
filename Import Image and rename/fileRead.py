import requests
import time
start_time = time.time()


def img_downloader (initial_dir, final_dir, start_pos):
    count = 1
    with open(initial_dir,'r') as f:
        for i in range (int(start_pos)-1):
            f.readline()
            count +=1
        start_posn = count
        for line in f:
            response = requests.get(line.strip('\n'))
            a = line.split("images/")
            b = a[1].split("/")
            print(count, b[0])
            with open(f'{final_dir}/{count} {b[0]}.jpeg', 'wb') as file:
                file.write(response.content)
            count += 1
        end_posn = count - 1

        print(f'start image: \t {start_posn}\nend Image: \t {end_posn}')


print("--- %s seconds ---" % (time.time() - start_time))

st_pos = input("Enter Starting Position: ")

img_downloader('photo-link.txt', "C:/Users/Admin/Desktop/Shiam/Data Management/Python-Data-management/Import Image and rename/test", st_pos)