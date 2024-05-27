import re
import os
import inquirer

package_dir = os.path.dirname(os.path.abspath(__file__))

algorithms = {
    "Classification": ["SVM", "Random Forest", "KNN", "Decision Tree", "Naive Bayes"],
    "Regression": ["Lineal regression"]
}

questions = [inquirer.List('type', message="Select the MLA type", choices=["Classification", "Regression"])]
typeSelected = inquirer.prompt(questions)["type"]

if typeSelected == "Classification":
    package_dir += "/data/classification"
else:
    package_dir += "/data/regression"

data_dir = [fn for fn in os.listdir(package_dir) if os.path.isdir(os.path.join(package_dir, fn))]

questions = [
    inquirer.List('data', message="Select the datset", choices=data_dir),
    inquirer.List('algorithm', message="Select the algorithm", choices=algorithms[typeSelected])
]

answers = inquirer.prompt(questions)


print(answers)