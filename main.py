from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from random import randint, random
import copy
import json
import os
import base64


class GameBlock(QLabel):
    def __init__(self, x, y):
        super(GameBlock, self).__init__()
        self.setFixedSize(60, 60)
        self.val = 0
        self.setFont(QFont(u"Segoe UI", 14))
        self.normal_style = u"QWidget {background-color: rgb(220, 220, 220);} "
        self.style_2 = u"QWidget {background-color: rgb(246, 255, 164);}"
        self.style_4 = u"QWidget {background-color: rgb(254, 255, 120);}"
        self.style_8 = u"QWidget {background-color: rgb(255, 237, 89);}"
        self.style_16 = u"QWidget {background-color: rgb(255, 218, 78);}"
        self.style_32 = u"QWidget {background-color: rgb(255, 199, 84);}"
        self.style_64 = u"QWidget {background-color: rgb(255, 170, 67);}"
        self.style_128 = u"QWidget {background-color: rgb(255, 149, 41);}"
        self.style_256 = u"QWidget {background-color: rgb(255, 136, 35);}"
        self.style_512 = u"QWidget {background-color: rgb(255, 110, 45);}"
        self.style_1024 = u"QWidget {background-color: rgb(255, 91, 30);}"
        self.style_2048 = u"QWidget {background-color: rgb(255, 30, 10);}"
        self.style_4096 = u"QWidget {background-color: rgb(255, 25, 5);}"
        self.style_8192 = u"QWidget {background-color: rgb(255, 15, 0);}"
        self.style_16384 = u"QWidget {background-color: rgb(255, 0, 0);}"
        self.style_32768 = u"QWidget {background-color: rgb(255, 0, 0);}"
        self.style_65536 = u"QWidget {background-color: rgb(255, 0, 0);}"
        self.style_131072 = u"QWidget {background-color: rgb(255, 0, 0);}"
        self.setAlignment(Qt.AlignCenter)
        self.x = x
        self.y = y
        self.style_choose()

    def style_choose(self):
        if self.val == 0:
            self.setStyleSheet(self.normal_style)
            self.setText('')
        elif self.val == 2:
            self.setStyleSheet(self.style_2)
            self.setText('2')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 4:
            self.setStyleSheet(self.style_4)
            self.setText('4')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 8:
            self.setStyleSheet(self.style_8)
            self.setText('8')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 16:
            self.setStyleSheet(self.style_16)
            self.setText('16')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 32:
            self.setStyleSheet(self.style_32)
            self.setText('32')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 64:
            self.setStyleSheet(self.style_64)
            self.setText('64')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 128:
            self.setStyleSheet(self.style_128)
            self.setText('128')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 256:
            self.setStyleSheet(self.style_256)
            self.setText('256')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 512:
            self.setStyleSheet(self.style_512)
            self.setText('512')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 1024:
            self.setStyleSheet(self.style_1024)
            self.setText('1024')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 2048:
            self.setStyleSheet(self.style_2048)
            self.setText('2048')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 4096:
            self.setStyleSheet(self.style_4096)
            self.setText('4096')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 8192:
            self.setStyleSheet(self.style_8192)
            self.setText('8192')
            self.setFont(QFont(u"Segoe UI", 14))
        elif self.val == 16384:
            self.setStyleSheet(self.style_16384)
            self.setText('16384')
            self.setFont(QFont(u"Segoe UI", 11))
        elif self.val == 32768:
            self.setStyleSheet(self.style_32768)
            self.setText('32768')
            self.setFont(QFont(u"Segoe UI", 11))
        elif self.val == 65536:
            self.setStyleSheet(self.style_65536)
            self.setText('65536')
            self.setFont(QFont(u"Segoe UI", 11))
        elif self.val == 131072:
            self.setStyleSheet(self.style_131072)
            self.setText('131072')
            self.setFont(QFont(u"Segoe UI", 11))

    def update(self):
        self.style_choose()


class GameField(QMainWindow):
    def __init__(self, x, y, cont_game):
        super(GameField, self).__init__()
        self.action = QAction(self)
        self.action1 = QAction(self)
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menu = QMenu(self.menubar)
        self.menu1 = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu1.menuAction())
        self.menu.addAction(self.action)
        self.menu1.addAction(self.action1)
        self.setWindowTitle('2048')
        self.action.setText('Перезапуск')
        self.action1.setText('Cтатистика')
        self.action.triggered.connect(self.restart)
        self.action1.triggered.connect(self.statistics)
        self.menu.setTitle('Игра')
        self.menu1.setTitle('Статистика')
        self.grid = QGridLayout(self.centralwidget)
        self.grid.setSpacing(3)
        self.size_x = x
        self.size_y = y
        self.score = 0
        self.saved_game = []
        self.save_trig = False
        self.cont_game = cont_game
        self.highscore = {'4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}
        self.load_game()
        self.setFixedSize(self.minimumSize())
        self.cnt_trig = False   # триггер продолжения

    def load_game(self):
        if os.path.exists('SavedGame.2048'):
            with open('SavedGame.2048', 'rb') as jf:
                b_rsave = jf.read()
                rsave = base64.standard_b64decode(b_rsave).decode()
                sg = json.loads(rsave)
            self.highscore = sg['HighScore']
        self.init_map()
        if self.cont_game:
            self.score = sg['LastScore']
            game = sg['SavedGame']
            if self.size_x != len(game):
                self.start_game()
                return
            for x in range(0, self.size_x):
                for y in range(0, self.size_y):
                    self.grid.itemAtPosition(x, y).widget().val = game[x][y]
            self.cnt_trig = True
            self.update_map()

    def init_map(self):
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                aw = GameBlock(x, y)
                self.grid.addWidget(aw, x, y)
        if not self.cont_game:
            self.start_game()

    def start_game(self):
        start_pos = set()
        while len(start_pos) < 2:
            start_pos.add((randint(0, self.size_x - 1), randint(0, self.size_y - 1)))
        for xi, yi in start_pos:
            self.grid.itemAtPosition(xi, yi).widget().val = 2
            self.grid.itemAtPosition(xi, yi).widget().update()
        self.save()

    def restart(self):
        self.reset_map()
        self.start_game()

    def save(self):
        if self.save_trig:
            self.saved_game.clear()
        game = []
        for x in range(0, self.size_x):
            lst = []
            for y in range(0, self.size_y):
                lst.append(self.grid.itemAtPosition(x, y).widget().val)
            game.append(lst)
        if len(self.saved_game) < 6:
            self.saved_game.append(game)
        else:
            self.saved_game.pop(0)
            self.saved_game.append(game)

    def save_after_exit(self, cmd):
        # если пидор никуда не сходил
        if not self.saved_game:
            game = []
            for x in range(0, self.size_x):
                lst = []
                for y in range(0, self.size_y):
                    lst.append(self.grid.itemAtPosition(x, y).widget().val)
                game.append(lst)
            self.saved_game.append(game)

        if self.score > self.highscore[str(self.size_x)]:
            self.highscore[str(self.size_x)] = self.score
        sg = {'HighScore': self.highscore}
        if cmd:
            sg['Continue'] = True
            sg['LastScore'] = self.score
            sg['SavedGame'] = self.saved_game[-1]
        else:
            sg['Continue'] = False
        with open('SavedGame.2048', 'wb') as jf:
            save = json.dumps(sg)
            b_save = base64.standard_b64encode(save.encode())
            jf.write(b_save)

    def closeEvent(self, event:QCloseEvent):
        msgBox = QMessageBox(QMessageBox.Question, "2048", f"Сохранить игру перед выходом?",
                             QMessageBox.NoButton, self)
        msgBox.addButton("Да", QMessageBox.AcceptRole)
        msgBox.addButton("Нет", QMessageBox.RejectRole)
        msgBox.addButton("Отмена", QMessageBox.RejectRole)
        ans = msgBox.exec_()
        if ans == 0:
            self.save_after_exit(True)
            event.accept()
        elif ans == 1:
            self.save_after_exit(False)
            event.accept()
        elif ans == 2:
            event.ignore()

    def restore(self):
        if not self.save_trig:
            self.saved_game.remove(self.saved_game[len(self.saved_game)-1])
        if len(self.saved_game) > 0:
            game = self.saved_game[len(self.saved_game)-1]
            self.saved_game.remove(self.saved_game[len(self.saved_game)-1])
            for x in range(0, self.size_x):
                for y in range(0, self.size_y):
                    self.grid.itemAtPosition(x, y).widget().val = game[x][y]
            self.update_map()

    def statistics(self):
        msg = f'Статистика:\n' \
              f'Лучший счет 4x4: {self.highscore["4"]}\n' \
              f'Лучший счет 5x5: {self.highscore["5"]}\n' \
              f'Лучший счет 6x6: {self.highscore["6"]}\n' \
              f'Лучший счет 7x7: {self.highscore["7"]}\n' \
              f'Лучший счет 8x8: {self.highscore["8"]}\n' \
              f'Лучший счет 9x9: {self.highscore["9"]}\n' \
              f'Лучший счет 10x10: {self.highscore["10"]}\n'
        QMessageBox.information(self, "2048", msg)

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == 16777234:
            mb = self.move_blocks('left', False)
            if not mb:
                self.add_next()
                self.save()
                self.save_trig = False
            else:
                self.check_loose()
        elif event.key() == 16777235:
            mb = self.move_blocks('up', False)
            if not mb:
                self.add_next()
                self.save()
                self.save_trig = False
            else:
                self.check_loose()
        elif event.key() == 16777236:
            mb = self.move_blocks('right', False)
            if not mb:
                self.add_next()
                self.save()
                self.save_trig = False
            else:
                self.check_loose()
        elif event.key() == 16777237:
            mb = self.move_blocks('down', False)
            if not mb:
                self.add_next()
                self.save()
                self.save_trig = False
            else:
                self.check_loose()
        elif event.key() == 16777223:
            self.restore()
            self.save_trig = True

    def add_next(self):
        empty = []
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                if self.grid.itemAtPosition(x, y).widget().val == 0:
                    empty.append((x, y))
        if len(empty) > 0:
            next_val = 2
            if random() < 0.2:
                next_val = 4
            xi, yi = empty[randint(0, len(empty)-1)]
            self.grid.itemAtPosition(xi, yi).widget().val = next_val
            self.grid.itemAtPosition(xi, yi).widget().update()
        else:
            self.check_loose()

    def check_loose(self):
        if self.move_blocks('left', True) and self.move_blocks('up', True) and self.move_blocks('right', True) and \
                self.move_blocks('down', True):
            QMessageBox.information(self, "2048", f"Вы проиграли!\n Счет: {self.score}")
            if self.score > self.highscore[str(self.size_x)]:
                self.highscore[str(self.size_x)] = self.score
            self.reset_map()
            self.start_game()

    def won(self):
        msgBox = QMessageBox(QMessageBox.Question, "2048", f"Вы выиграли!\n Счет: {self.score}\nПродолжить?",
                             QMessageBox.NoButton, self)
        msgBox.addButton("Да", QMessageBox.AcceptRole)
        msgBox.addButton("Нет", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.RejectRole:
            self.reset_map()
            self.start_game()
            self.cnt_trig = False
        else:
            self.cnt_trig = True

    def update_map(self):
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                self.grid.itemAtPosition(x, y).widget().update()

    def reset_map(self):
        self.score = 0
        self.cnt_trig = False   # не уверен
        self.statusbar.showMessage(f'Счет: {self.score}')
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                self.grid.itemAtPosition(x, y).widget().val = 0
                self.grid.itemAtPosition(x, y).widget().update()

    def move_blocks(self, way, test_mode):
        won = False
        x_list = []
        for x in range(0, self.size_x):
            lst = []
            for y in range(0, self.size_y):
                if way in ['left', 'right']:
                    lst.append(self.grid.itemAtPosition(x, y).widget().val)
                elif way in ['up', 'down']:
                    lst.append(self.grid.itemAtPosition(y, x).widget().val)
            x_list.append(lst)
        tst1 = copy.deepcopy(x_list)
        # обработка
        for line in x_list:
            if way in ['right', 'down']:
                line.reverse()
            if line != [0 for _ in range(self.size_x)]:
                while 0 in line:
                    line.remove(0)
                if len(line) == len(set(line)):
                    while len(line) < self.size_x:
                        line.append(0)
                else:
                    for i in range(0, len(line)-1):
                        if line[i] == line[i+1]:
                            line[i] = line[i]*2
                            if not test_mode:
                                self.score += line[i]
                                self.statusbar.showMessage(f'Счет: {self.score}')
                            line[i+1] = 0
                    while 0 in line:
                        line.remove(0)
                    while len(line) < self.size_x:
                        line.append(0)
            if way in ['right', 'down']:
                line.reverse()
            if 2048 in line and not self.cnt_trig:
                won = True
        tst2 = copy.deepcopy(x_list)
        # возврат
        if not test_mode:
            for x in range(0, self.size_x):
                for y in range(0, self.size_y):
                    if way in ['left', 'right']:
                        self.grid.itemAtPosition(x, y).widget().val = x_list[x][y]
                    elif way in ['up', 'down']:
                        self.grid.itemAtPosition(y, x).widget().val = x_list[x][y]
            self.update_map()
        if won and not self.cont_game:
            self.won()
        return tst1 == tst2


class StartWindow(QWidget):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.setWindowTitle('2048')
        self.resize(250, 130)
        self.setFixedSize(self.size())
        self.gridLayout_3 = QGridLayout(self)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.spinBox = QSpinBox(self)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(4)
        self.spinBox.setMaximum(10)
        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.spinBox_2 = QSpinBox(self)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy1)
        self.spinBox_2.setMinimum(4)
        self.spinBox_2.setMaximum(10)
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setRowMinimumHeight(1, 15)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)
        self.setWindowTitle(QCoreApplication.translate("Form", u"2048", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0445", None))
        self.label.setText(
            QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u043e\u043b\u044f:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.connect(self.pushButton, SIGNAL('clicked()'), self, SLOT('start_2048()'))

    def start_2048(self):
        x = self.spinBox.value()
        y = self.spinBox_2.value()
        if x != y:
            self.spinBox_2.setValue(x)
            QMessageBox.information(self, "2048", "Только квадратное поле!")
            return
        global gf
        gf = GameField(x, y, False)
        gf.show()
        self.hide()

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == 16777220:
            self.start_2048()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    if os.path.exists('SavedGame.2048'):
        with open('SavedGame.2048', 'rb') as jf:
            b_rsave = jf.read()
            rsave = base64.standard_b64decode(b_rsave).decode()
            sg = json.loads(rsave)
            if sg['Continue']:
                msgBox = QMessageBox(QMessageBox.Question, "2048", f"Продолжить сохраненную игру?",
                                     QMessageBox.NoButton)
                msgBox.addButton("Да", QMessageBox.AcceptRole)
                msgBox.addButton("Нет", QMessageBox.RejectRole)
                if msgBox.exec_() == msgBox.AcceptRole:
                    xy = len(sg['SavedGame'])
                    w = GameField(xy, xy, True)
                else:
                    w = StartWindow()
            else:
                w = StartWindow()
    else:
        w = StartWindow()
    w.show()
    app.exec_()
