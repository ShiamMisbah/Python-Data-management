import urllib.request
import csv
import time
import threading
import os

file = open('Applicant_Rolls_8_16_22.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
isjpg = True
isjpeg , ispng = False, False
isJPG, isJPEG, isPNG = False, False, False

error_applicant_images, error_signature_images = set(), set()

def download_applicant_image(applicant_code, applicant_id, image_format):

    image_url = "http://pwd.teletalk.com.bd/images/"+applicant_code+"/applicant_image."+image_format

    save_image = "applicant_image/"+applicant_code+".jpg"
    save_image_id = "applicant_image/applicant_image_id/"+applicant_id+".jpg"
    try:
        urllib.request.urlretrieve(image_url, save_image)
        urllib.request.urlretrieve(image_url, save_image_id)
    except:
        error_applicant_images.add(applicant_code)
        print("error for", error_applicant_images)
        #download_applicant_image(applicant_code, applicant_id, "JPG")
        #download_applicant_image(applicant_code, applicant_id, "PNG")
    print("Done Image")


def download_applicant_signature(applicant_code, applicant_id, image_format):

    image_url = "http://pwd.teletalk.com.bd/images/" + applicant_code + "/applicant_signature."+image_format
    save_image = "applicant_signature/"+applicant_code+".jpg"
    save_image_id = "applicant_signature/applicant_signature_id/"+applicant_id+".jpg"

    try:
        urllib.request.urlretrieve(image_url, save_image)
        urllib.request.urlretrieve(image_url, save_image_id)
    except:
        error_signature_images.add(applicant_code)
        print("error for", error_signature_images)
        #download_applicant_signature(applicant_code, applicant_id, "JPG")
    print("Done Signature")

def download_both(applicant_code,applicant_id, image_format):
    if os.path.isfile("applicant_image/"+applicant_code+".jpg") and os.path.isfile("applicant_image/applicant_image_id/"+applicant_id+".jpg") and os.path.isfile("applicant_signature/"+applicant_code+".jpg") and os.path.isfile("applicant_signature/applicant_signature_id/"+applicant_id+".jpg"):
        print(applicant_code, "and", applicant_id, "already exists.")
    else:
        #threading
        t1 = threading.Thread(download_applicant_image(applicant_code, applicant_id, image_format))
        t2 = threading.Thread(download_applicant_signature(applicant_code, applicant_id, image_format))
        # download_applicant_image(applicant_code, applicant_id, image_format)
        # download_applicant_signature(applicant_code, applicant_id, image_format)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Done Downloading for", i, applicant_code,applicant_id)


tic = time.process_time()
rows = []
for row in csvreader:
    rows.append(row)
print(len(rows))
for i in range(0, len(rows)):
    applicant_code = rows[i][1]
    applicant_id = rows[i][3]
    print("Start Downloading for", i, applicant_code)
    download_both(applicant_code, applicant_id, "jpg")

toc = time.process_time()

print(error_applicant_images)
print("total applicant numbers:", len(error_applicant_images))
print(error_signature_images)
print("total signature number:", len(error_signature_images))
error_images = error_applicant_images.union(error_signature_images)
print(error_images)
print("total number:", len(error_images))
print("Time Elapsed:", toc-tic)
