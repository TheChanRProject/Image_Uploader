from os import getcwd, listdir, chdir, system

def github_upload():

    message = input("Create a commit message: ")
    system("git add .")
    system("git commit -m '{}'".format(message))
    system('git push')

img_path = getcwd() + "/images"
img_list = listdir(img_path)
raw_strings = []
for image in img_list:
    raw = f"https://raw.githubusercontent.com/TheChanRProject/Image_Uploader/master/images/{image}"
    raw_strings.append(raw)

with open("urls.txt", "w") as my_file:
    for url in raw_strings:
        my_file.write(url + "\n")
