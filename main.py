from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QTextEdit,
                             QLabel,
                             QListWidget,
                             QPushButton)

app = QApplication([])
notes_win = QWidget()

notes_win.setWindowTitle("Розумні нотатки")
field_text = QTextEdit()
list_notes_label = QLabel("Список нотаток")
list_notes = QListWidget()
btn_create = QPushButton('Створити нотатку')
btn_del = QPushButton('Видалити нотатку')
btn_save = QPushButton('Зберегти нотатку')

list_tag_label = QLabel('Список тегів')
list_tag = QListWidget()
btn_tag_add = QPushButton("Додати до нотатки")
btn_tag_del = QPushButton("Видалити з нотатки")
btn_tag_search = QPushButton("Шукати нотатку по тегу")
notes_win.show()
app.exec_()




