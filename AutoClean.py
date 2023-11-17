import os
import time
import datetime
import json

with open("trackUpload.json", "r") as tU:      # read the json file
  variables = json.load(tU)

variables["uploaded"] = False    # change the variable in python

with open("trackUpload.json", "w") as tU:      # write back to the json file
  json.dump(variables, tU)

uploaded = variables["uploaded"]    # To get the value currently stored

video = ""
title = video
description = "variable Description"
keywords = "variablekeywords"
category = "20"

# python3 upload_video.py --file="file"  --title="Summer vacation in California" --description="Had fun surfing in Santa Cruz" --keywords="surfing,Santa Cruz" --category="22" --privacyStatus="private"


def upload_vid():
        os.system("python upload_video.py" + ' --file="%s"' % video + ' --title="%s"' % title + ' --description="%s"' % description +  ' --keywords="%s"' % keywords + ' --category="%s"' % category + ' --privacyStatus="private"')

if __name__ == '__main__':

  while True:
    folder_path = r"Clips\Valorant"  # Replace with the path to your folder

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    #pick video and upload    
    if len(files) > 0:
      oldest_file = min(files, key=lambda f: os.path.getctime(os.path.join(folder_path, f)))
      file_path = os.path.join(folder_path, oldest_file)
    print(f"Uploading {file_path}")
    video = file_path
    title = video
    upload_vid()
    #read outcome of upload sucess
    with open("trackUpload.json", "r") as tU:      # read the json file
        variables = json.load(tU)
    uploaded = variables["uploaded"]    # To get the value currently stored
    

    #delete video
    if uploaded == True:
      files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
      if len(files) > 0:
        oldest_file = min(files, key=lambda f: os.path.getctime(os.path.join(folder_path, f)))
        file_path = os.path.join(folder_path, oldest_file)
        os.remove(file_path)
        print(f"Deleted file: {oldest_file}")
      time.sleep(1)  # wacht  
    #break out of loop if files arent uploading anymore    
    elif uploaded == False:
       print("File isnt uploaded, program will stop now")
       break
    os.system("echo upload is %s" % uploaded)


