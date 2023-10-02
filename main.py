import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Seleção de Arquivos')

        # Cria um widget central e um layout vertical para ele
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Cria um botão para abrir o diálogo de seleção de diretório
        self.btn_diretorio = QPushButton('Selecionar Diretório', self)
        self.btn_diretorio.clicked.connect(self.abrirDialogoDiretorio)

        # Cria um rótulo para exibir o nome do diretório selecionado
        self.label_diretorio = QLabel('', self)

        # Cria um botão para abrir o diálogo de seleção de arquivo .ui
        self.btn_ui = QPushButton('Selecionar Arquivo .ui', self)
        self.btn_ui.clicked.connect(self.abrirDialogoUI)

        # Cria um rótulo para exibir o nome do arquivo .ui selecionado
        self.label_ui = QLabel('', self)

        # Cria um botão para abrir o diálogo de seleção de arquivo .py
        self.btn_py = QPushButton('Selecionar Arquivo .py', self)
        self.btn_py.clicked.connect(self.abrirDialogoPY)

        # Cria um rótulo para exibir o nome do arquivo .py selecionado
        self.label_py = QLabel('', self)

        # Adiciona os widgets ao layout vertical
        layout.addWidget(self.btn_diretorio)
        layout.addWidget(self.label_diretorio)
        layout.addWidget(self.btn_ui)
        layout.addWidget(self.label_ui)
        layout.addWidget(self.btn_py)
        layout.addWidget(self.label_py)

        self.show()

    def abrirDialogoDiretorio(self):
        # Cria um diálogo de seleção de diretório
        options = QFileDialog.Options()
        diretorio_selecionado = QFileDialog.getExistingDirectory(self, 'Selecione um Diretório', options=options)

        if diretorio_selecionado:
            self.label_diretorio.setText(f'Diretório selecionado: {diretorio_selecionado}')

    def abrirDialogoUI(self):
        # Cria um diálogo de seleção de arquivo .ui
        options = QFileDialog.Options()
        file_filter = 'Arquivos .ui (*.ui);;Todos os Arquivos (*)'
        arquivo_selecionado, _ = QFileDialog.getOpenFileName(self, 'Selecione um Arquivo .ui', '', file_filter, options=options)

        if arquivo_selecionado:
            self.label_ui.setText(f'Arquivo .ui selecionado: {arquivo_selecionado}')

    def abrirDialogoPY(self):
        # Cria um diálogo de seleção de arquivo .py
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
