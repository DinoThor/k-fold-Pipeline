import os
import pandas as pd

class Classification():
    def __init__(self) -> None:
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        
        self._dataFrames    = []
        self._numpyArrays   = None

        for root, _, files in os.walk("../../data/classification/"):
            for filename in files:
                path = os.path.join(root, filename)
                if os.path.splitext(path)[-1] == ".csv":
                    self._dataFrames.append((filename, pd.read_csv(path)))

        self._numpyArrays = list(map(lambda df: (df[0], df[1].to_numpy()), self._dataFrames))

if __name__ == "__main__":
    classif = Classification()

    for df in classif._dataFrames:
        print(f"DATASET ==> {df[0]:50s} SHAPE ==> {df[1].shape}")

    