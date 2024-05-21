import os
import opendatasets as od

class Downloader():
    def __init__(self, dir: str) -> None:
        self._fileRepo  = "kaggle-repos.txt"
        self._dataDir   = dir

        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)

        with (open(self._dataDir + self._fileRepo, "r")) as file:
            self._repo = [(line.split(":", 1)[0], line.split(":", 1)[1]) for line in file.readlines()]

    def download(self, force: bool = False):
        for dataset in self._repo:
            od.download(dataset[1].strip(), self._dataDir, force = force)


if __name__ == "__main__":
    classification_down = Downloader("./data/classification/")
    regression_down     = Downloader("./data/regression/")

    classification_down.download()
    regression_down.download()