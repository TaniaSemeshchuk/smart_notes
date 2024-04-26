from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QTextEdit,
                             QLabel,
                             QListWidget,
                             QPushButton, QLineEdit,
                             QHBoxLayout, QVBoxLayout)

app = QApplication([])
notes_win = QWidget()
notes_win.resize(900, 600)
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

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(field_text)

col2 = QVBoxLayout()
col2.addWidget(list_notes_label)
col2.addWidget(list_notes)
row1 = QHBoxLayout()
row1.addWidget(btn_create)
row1.addWidget(btn_del)
row2 = QHBoxLayout()
row2.addWidget(btn_save)
col2.addLayout(row1)
col2.addLayout(row2)

col2.addWidget(list_tag_label)
col2.addWidget(list_tag)
col2.addWidget(field_tag)

row3 = QHBoxLayout()
row3.addWidget(btn_tag_add)
row3.addWidget(btn_tag_del)
row4 = QHBoxLayout()
row4.addWidget(btn_tag_search)
col2.addLayout(row3)
col2.addLayout(row4)

layout_notes.addLayout(col1, stretch = 2)
layout_notes.addLayout(col2, stretch = 1)
notes_win.setLayout(layout_notes)

notes_win.show()
app.exec_()







