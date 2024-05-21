import os
import opendatasets as od


class Downloader():
    def __init__(self) -> None:
        self._fileRepo = "kaggle-repos.txt"

        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)

        with (open(self._fileRepo, "r")) as file:
            self._repo = [(line.split(":", 1)[0], line.split(":", 1)[1]) for line in file.readlines()]

        od.download(self._repo[0][1].strip())

    def download(self):
        for dataset in self._repo:
            od.download(dataset[1].strip())

downloader = Downloader()
downloader.download()