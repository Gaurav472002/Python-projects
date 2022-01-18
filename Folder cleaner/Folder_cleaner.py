import os
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")


if __name__=="__main__":
    files=os.listdir()
    files.remove("main.py")

    create_folder('Music')
    create_folder('Docs')
    create_folder('Pictures')
    create_folder('others')

    imgexts=[".jpg",".jpeg",".png"]

    pictures=[file for file in files if os.path.splitext(file)[1].lower() in imgexts]

    docexts=[".txt",".docx",".pdf"]

    docs=[file for file in files if os.path.splitext(file)[1].lower() in docexts]

    musicext=[".mp3",".mp4",".wav"]

    musics=[file for file in files if os.path.splitext(file)[1].lower() in musicext]

    
    

    others=[]
    for file in files:
        ext=os.path.splitext(file)[1].lower()
        if(ext not in imgexts and ext not in docexts and ext not in musicext) and os.path.isfile(file):
            others.append(file)

    move("Music",musics)
    move("Docs",docs)
    move("Pictures",pictures)
    move("others",others)