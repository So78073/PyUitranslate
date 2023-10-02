import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Seleção de Arquivos')

 
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

 
        self.btn_diretorio = QPushButton('Selecionar Diretório', self)
        self.btn_diretorio.clicked.connect(self.abrirDialogoDiretorio)


        self.label_diretorio = QLabel('', self)


        self.btn_ui = QPushButton('Selecionar Arquivo .ui', self)
        self.btn_ui.clicked.connect(self.abrirDialogoUI)


        self.label_ui = QLabel('', self)


        self.btn_py = QPushButton('Selecionar Arquivo .py', self)
        self.btn_py.clicked.connect(self.abrirDialogoPY)

  
        self.label_py = QLabel('', self)

  
        layout.addWidget(self.btn_diretorio)
        layout.addWidget(self.label_diretorio)
        layout.addWidget(self.btn_ui)
        layout.addWidget(self.label_ui)
        layout.addWidget(self.btn_py)
        layout.addWidget(self.label_py)

        self.show()

    def abrirDialogoDiretorio(self):

        options = QFileDialog.Options()
        diretorio_selecionado = QFileDialog.getExistingDirectory(self, 'Selecione um Diretório', options=options)

        if diretorio_selecionado:
            self.label_diretorio.setText(f'Diretório selecionado: {diretorio_selecionado}')

    def abrirDialogoUI(self):

        options = QFileDialog.Options()
        file_filter = 'Arquivos .ui (*.ui);;Todos os Arquivos (*)'
        arquivo_selecionado, _ = QFileDialog.getOpenFileName(self, 'Selecione um Arquivo .ui', '', file_filter, options=options)

        if arquivo_selecionado:
            self.label_ui.setText(f'Arquivo .ui selecionado: {arquivo_selecionado}')

    def abrirDialogoPY(self):

        options = QFileDialog.Options()
        file_filter = 'Arquivos .py (*.py);;Todos os Arquivos (*)'
        arquivo_selecionado, _ = QFileDialog.getOpenFileName(self, 'Selecione um Arquivo .py', '', file_filter, options=options)

        if arquivo_selecionado:
            self.label_py.setText(f'Arquivo .py selecionado: {arquivo_selecionado}')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
