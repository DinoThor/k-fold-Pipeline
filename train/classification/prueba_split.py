from prueba_class import Classification
import numpy as np
from sklearn.model_selection import train_test_split

class ClassificationSplit():
    def __init__(self) -> None:
        self._classif = Classification()
        self._splitDatasets = []

        for npArray in self._classif._numpyArrays:
            self._splitDatasets.append(train_test_split(npArray, train_size=0.8))
        
        print(type(self._splitDatasets[0][0]))

cs = ClassificationSplit()