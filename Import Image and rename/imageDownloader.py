import urllib.request
import csv
import time

file = open('Applicant_Rolls_8_16_22.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)


def download_applicant_image(applicant_code):
    image_url = "http://pwd.teletalk.com.bd/images/"+applicant_code+"/applicant_image.jpg"
    save_image = "applicant_image/"+applicant_code+".jpg"
    urllib.request.urlretrieve(image_url,save_image)


def download_applicant_signature(applicant_code):
    image_url = "http://pwd.teletalk.com.bd/images/"+applicant_code+"/applicant_signature.jpg"
    save_image = "applicant_signature/"+applicant_code+".jpg"
    urllib.request.urlretrieve(image_url, save_image)


def download_both(applicant_code):
    try:
        download_applicant_image(applicant_code)
        download_applicant_signature(applicant_code)
        print("Done Downloading for", i, applicant_code)
    except:
        print ("error for", i ,applicant_code)
        error_codes.append(applicant_code)


tic = time.process_time()

error_codes = []
rows = []
for row in csvreader:
    rows.append(row)
print(len(rows))
for i in range(0, len(rows)):
    applicant_code = rows[i][1]
    print("Start Downloading for", i, applicant_code)
    download_both(applicant_code)

print (error_codes)
toc = time.process_time()

print("Time Elapsed:", toc-tic)
