import os, time, shutil, zipfile

folders_list = []
files_list = []
working_list = []
iteratii = 0

class Folders:
    folders_total = 0
    def __init__(self, folder, folder_path):
        global folders_list
        self.index = Folders.folders_total
        self.folder = folder
        self.path = folder_path
        folders_list.append(self)
        Folders.folders_total += 1

class Files:
    files_total = 0
    def __init__(self, fisier, file_path):
        global files_list
        self.index = Files.files_total
        self.file = fisier
        self.path = file_path
        files_list.append(self)
        Files.files_total += 1
        self.updated=False

def scriere_log(mesaj):
    LogFile = open("LogFile.txt","a")
    LogFile.write(mesaj+"\n")
    print (mesaj)
    LogFile.close()
    
def Import(cale):
    for (path, folders, files) in os.walk(cale):
        for folder in folders:
            obiect = len(globals())
            globals()[obiect] = Folders(folder,path)
        for file in files:
            obiect = len(globals())
            globals()[obiect] = Files(file,path)
    scriere_log(str(time.ctime())+": Din "+str(cale)+" s-au importat "+str(Folders.folders_total)+" foldere")
    scriere_log(str(time.ctime())+": Din "+str(cale)+" s-au importat "+str(Files.files_total)+" fisiere")


Import ("C:\\Users\\aion\\Desktop\\Games sounds\\Worms sounds\\de procesat")

while True:
    for (path,folders,files) in os.walk("C:\\Users\\aion\\Downloads"):
        for file in files:
            if file[len(file)-4:len(file)] == ".zip":
                try:
                    arhiva = zipfile.ZipFile(os.path.join("C:\\Users\\aion\\Downloads",file))
                    arhiva.extractall("C:\\Users\\aion\\Downloads")
                    arhiva.close()
                    os.remove(os.path.join("C:\\Users\\aion\\Downloads",file))
                    scriere_log(str(time.ctime())+": S-a dezarhivat "+ str(file))
                except Exception as Error:
                    scriere_log(str(time.ctime())+": A aparut eroarea: "+str(Error))
            if file[len(file)-4:len(file)]==".wav":
                scriere_log(str(time.ctime())+": S-a identificat "+ str(file))
                working_list.append(file)
    for element in working_list:
        try:
            shutil.move(os.path.join("C:\\Users\\aion\\Downloads",element),os.path.join("C:\\Users\\aion\\Desktop\\Games sounds\\Worms sounds\\Procesate",element))
        except Exception as Error:
            print (str(time.ctime())+": A aparut eroarea: "+str(Error))            
        try:
            os.remove(os.path.join("C:\\Users\\aion\\Desktop\\Games sounds\\Worms sounds\\de procesat",element))
        except Exception as Error:
            print (str(time.ctime())+": A aparut eroarea: "+str(Error))
        scriere_log (str(time.ctime())+ ": S-a mutat fisierul "+element)
    working_list=[] 
