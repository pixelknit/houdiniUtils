import os
import zipfile
import threading

DIRPATH = "/Users/felipepesantez/Downloads/assets/zip_test"

class UnzipUtils:
    def __init__(self, dirpath):
        self.dirpath = dirpath

    def unzipAll(self):
        zipfiles = [file for file in os.listdir(self.dirpath) if file.endswith(".zip")]
        for zipf in zipfiles:
            with zipfile.ZipFile(self.dirpath + "/" + zipf, "r") as zip_ref:
                zip_ref.extractall(self.dirpath)
            print(f"Done extracting {zipf}")
        print("All files unzipped")

    def deleteZipFiles(self):
        zipfiles = [file for file in os.listdir(self.dirpath) if file.endswith(".zip")]
        for zipf in zipfiles:
            os.remove(self.dirpath + "/" + zipf)

if __name__ == "__main__":
    folder1 = UnzipUtils(DIRPATH)

    thread1 = threading.Thread(target=folder1.unzipAll)
    thread2 = threading.Thread(target=folder1.deleteZipFiles)

    thread1.start()
    thread1.join()
    thread2.start()

