from os import getcwd, listdir, chdir, system

def github_upload():

    message = input("Create a commit message: ")
    system("git add .")
    system("git commit -m '{}'".format(message))
    system('git push')


def image_move(name):
    system(f"mv ~/Downloads/{name} ./images/")
