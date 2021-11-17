from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QDoubleSpinBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


class Window(QWidget):
    """
    Window
    Atributos:    
        data:
            Diccionario con la información de la flor.    
    Metodos:
        deepLeerning:
            Abre y procesa el .csv necesario para entrenar a la aplicación.
        predict:
            Actualiza los datos en la variable data con la nueva información de la interfaz y la utiliza para predecir el tipo de flor que es.
        startWidgets:
            Inicializa los componentes UI de los Labels y los Entrys.
        startLabels:
            Crea los Labels para mostrar al lado de cada Entry y la salida con el resultado de predict.
        startEntrys:
            Crea los Entrys para la entrada de datos. Cada Entry se enlazaría con el metodo predict. Cada vez que cambia el valor, se lanzaría dicho método.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplicación PyQt5')
        self.setFixedSize(600, 350)
        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.data = {
            'SepalLengthCm': 0,
            'SepalWidthCm': 0,
            'PetalLengthCm': 0,
            'PetalWidthCm': 0,
        }
        self.styleFont = QtGui.QFont('Times', 20)
        self.deepLeerning()
        self.startWidgets()

    def deepLeerning(self):
        """
        Abre y procesa el .csv necesario para entrenar a la aplicación.
        """
        df = pd.read_csv('~/Atom/Tkinter/IrisSpecies.csv')
        X = df.drop(['Id', 'Species'], axis=1)
        y = df['Species']

        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            random_state=0,
                                                            test_size=0.01)

        self.clf = DecisionTreeClassifier()
        self.clf.fit(X_train, y_train)

    def predict(self):
        """
        Actualiza los datos en la variable data con la nueva información de la interfaz y la utiliza para predecir el tipo de flor que es.
        """
        newData = self.data.copy()
        for k, v in newData.items():
            newData[k] = [round(self.data[k].value(), 2)]

        dfNew = pd.DataFrame(newData)
        predict = self.clf.predict(dfNew)
        self.lPrediction.setText(predict[0])

    def startWidgets(self):
        """
        Inicializa los componentes UI de los Labels y los Entrys.
        """
        self.startLabels()
        self.startEntrys()

    def startLabels(self):
        """
        Crea los Labels para mostrar al lado de cada Entry y la salida con el resultado de predict.
        """
        namesLabel = ['Sepal Length (cm)', 'Sepal Width (cm)',
                      'Petal Length (cm)', 'Petal Width (cm)']
        row = 0
        for key in self.data:
            newLabel = QLabel(self)
            newLabel.setText(namesLabel[row])
            newLabel.setFont(self.styleFont)
            self.gridLayout.addWidget(newLabel, row, 0)
            row += 1

        self.lPrediction = QLabel(self)
        self.lPrediction.setText('')
        self.lPrediction.setFont(self.styleFont)
        self.lPrediction.setStyleSheet(
            'QLabel {color: #61005f;}')
        self.lPrediction.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.lPrediction, 6, 0, 2, 2)

    def startEntrys(self):
        """
        Crea los Entrys para la entrada de datos. Cada Entry se enlazaría con el metodo predict. Cada vez que cambia el valor, se lanzaría dicho método.
        """
        row = 0
        for k, v in self.data.items():
            newEntry = QDoubleSpinBox(self)
            newEntry.setDecimals(2)
            newEntry.setMinimum(0.0)
            newEntry.setSingleStep(0.1)
            newEntry.setFont(self.styleFont)
            newEntry.valueChanged.connect(self.predict)
            self.gridLayout.addWidget(newEntry, row, 1)
            self.data[k] = newEntry
            row += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Window()
    windows.show()
    sys.exit(app.exec_())
