#!/usr/bin/env python3
import sys
import os 

class NotesAutomation:
    extension = ""
    folderName = ""
    fileName = ""
    foundFileEntension = ""
    path = os.getcwd()
    
    notesFolder = '/home/avinash/bin/Notes'

    python = ".py"
    markdown = ".md"
    java = ".java"
    dart = ".dart"
    js = ".js"
    json = ".json"
    yaml = ".yaml"
    text = ".txt"

    extensions = {
        "python" : python,
        ".py" : python,
        "text" : text,
        ".txt" : text,
        "java" : java,
        ".java" : java,
        "dart" : dart,
        "flutter" : dart,
        ".dart" : dart,
        "yaml" : yaml,
        ".yaml" : yaml,
        "json" : json,
        "jason" : json,
        ".json" : json,
        "md" : markdown,
        ".md" : markdown,
        "markdown" : markdown,
    }

    def getArgs(self, ext_num, folder_num) : 
        try: 
            self.extension = self.extensions[sys.argv[ext_num].lower()]
        except Exception :
            self.extension = ".txt"
        try: 
            self.folderName = str(sys.argv[folder_num])
        except Exception:
            self.folderName = "."
        try:
            self.fileName = str(sys.argv[1])
        except Exception:
            print('Can\'t make file without the file name.')
            sys.exit()

    def createNoteAndFolder(self) :
        if os.path.isdir(self.notesFolder) :
            os.chdir(self.notesFolder)
        else : 
            os.mkdir(self.notesFolder)
            os.chdir(self.notesFolder)
        self.fileName = self.fileName + self.extension
        if os.path.isdir('./' + self.folderName) :
            os.chdir('./'+ self.folderName)
        else :
            os.mkdir('./'+self.folderName)
            os.chdir('./'+self.folderName)
        if not os.path.isfile("./"+self.fileName) : 
            open(self.fileName, "a").close()
        command = "code " + self.fileName
        os.system(command)

    def findFileInFolder(self, folder) : 
        if os.path.isdir(self.path + "/" + folder) :
            self.path = self.path + "/" + folder
            self.findFile(self.fileName, "" , self.path)
        else : 
            self.path = self.findFolder(folder, "", self.path)
            self.findFile(self.fileName, "" , self.path)

    def findFile(self, fileToFind, folderToSearch, thepath) : 
        fileExists  = False
        pathToFolder = ""
        for subdir, dirs, files in os.walk(thepath + folderToSearch) :
            for dir_ in dirs:
                if dir_.lower() == self.folderName.lower():
                    pathToFolder = ""
                    pathToFolder = subdir + "/" + self.folderName
            for file_ in files:
                name = ""
                for i in range(len(str(file_))):
                    if len(str(self.fileName)) > i:
                        if str(file_).lower()[i] == str(self.fileName).lower()[i]:
                            name = name + str(file_)[i]
                            if len(name) > len(self.fileName) * 0.8:
                                self.path = os.path.join(subdir, file_)
                                fileExists = True
                                break
        if not fileExists:
            self.path = os.path.join(pathToFolder ,self.fileName + self.extension)
            open(self.path, "a").close()


if __name__ == "__main__":
    notes = NotesAutomation()
    command = str(sys.argv[0])
    if "nfe" in command: 
        notes.getArgs(3,2)
        notes.createNoteAndFolder()
    elif "on" in command :
        notes.getArgs(3, 2)
        try: 
            notes.findFileInFolder(str(sys.argv[3]))
        except Exception:
            notes.findFileInFolder("")
    else :
        notes.getArgs(3, 1)
        notes.findFileInFolder("")
        