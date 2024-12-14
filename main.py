from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout

#список я сам зробив
video_list = [
    "D:\\other\\PythonVideo\\ivanzlo.avi",
    "D:\\other\\PythonVideo\\monster_fimoz1.avi",
    "D:\\other\\PythonVideo\\monster_fimoz2.avi"
]

current_index = 0  # Я хз что это, это чат гпт сделал

def play():
    media.play()

def stop():
    media.stop()

# Эту функцию тоже чат гпт сделал
def next_video():
    global current_index
    if current_index < len(video_list) - 1:
        current_index += 1
    else:
        current_index = 0  # Опять что то не понятное от чат гпт

# Тут что то общими усилиями с чатом гпт накалякали
def nazad_video():
    global current_index
    if current_index > 0:
        current_index -= 1
    else:
        current_index = len(video_list) - 1  # Опять что то не понятное от чат гпт
    update_video()

# Про эту функцию я вообще даже не думал, но ее сюда чат гпт добавил значит она нужна
def update_video():
    media.stop()
    vid = QMediaContent(QUrl.fromLocalFile(video_list[current_index]))
    media.setMedia(vid)
    media.play()

app = QApplication([])
win = QWidget()

video = QVideoWidget()
media = QMediaPlayer()

media.setVideoOutput(video)

# Тут че та устанавливаем
vid = QMediaContent(QUrl.fromLocalFile(video_list[current_index]))
media.setMedia(vid)
media.play()

win_layout = QVBoxLayout()
win_layout.addWidget(video)

# Кнопки я сам сделал
btn_play = QPushButton("Грати")
btn_stop = QPushButton("Стоп")
btn_next = QPushButton("Вперед")
btn_nazad = QPushButton("Назад")

btn_play.clicked.connect(play)
btn_stop.clicked.connect(stop)
btn_next.clicked.connect(next_video)
btn_nazad.clicked.connect(nazad_video)

row = QHBoxLayout()
row.addWidget(btn_nazad)
row.addWidget(btn_play)
row.addWidget(btn_stop)
row.addWidget(btn_next)

win_layout.addLayout(row)

win.setLayout(win_layout)
win.show()
app.exec_()
