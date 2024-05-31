from prueba_class import Classification
import numpy as np
from sklearn.model_selection import train_test_split

class ClassificationSplit():
    def __init__(self) -> None:
        self._classif = Classification()
        self._splitDatasets = {}

        for dataset_name, npArray in self._classif._numpyArrays:
            self._splitDatasets[dataset_name] = train_test_split(npArray[:, :-1], npArray[:, -1], train_size=0.8)

    def printShapes(self):
        for dataset_name, splitData in self._splitDatasets.items():
            print(f"===== {dataset_name} =====")
            print(f"train shape ==> X{np.shape(splitData[0])} Y{np.shape(splitData[2])}")
            print(f"test shape  ==> X{np.shape(splitData[1])} Y{np.shape(splitData[2])}")


cs = ClassificationSplit()
cs.printShapes()