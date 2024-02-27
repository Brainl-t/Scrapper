import sys
from design.design import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
from pynput.keyboard import Key, Listener
from buttons_positions import buttons_positions
import pyautogui
import threading
import time

INPUT_MODE = False
IS_WORKING = False
SUCCESS_COLOR = (114, 141, 69)
BUTTON_POSITION = buttons_positions["compost"]["button"]
INPUT_FIELD_POSITION = buttons_positions["compost"]["field"]
START_KEY = Key.f2
MAX_SOLD = 99


class MainWindow(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_input)
        self.checked_btn = self.radioButton

        self.radioButton.clicked.connect(lambda: self.trade_selected("compost"))
        self.radioButton_2.clicked.connect(lambda: self.trade_selected("stone_to_tree"))
        self.radioButton_3.clicked.connect(lambda: self.trade_selected("cloth"))
        self.radioButton_4.clicked.connect(lambda: self.trade_selected("mhq"))
        self.radioButton_5.clicked.connect(lambda: self.trade_selected("iron"))
        self.radioButton_6.clicked.connect(lambda: self.trade_selected("corn"))
        self.radioButton_7.clicked.connect(lambda: self.trade_selected("smoke"))
        self.radioButton_8.clicked.connect(lambda: self.trade_selected("green_card"))
        self.radioButton_9.clicked.connect(lambda: self.trade_selected("fish"))

    def trade_selected(self, n):
        global BUTTON_POSITION, INPUT_FIELD_POSITION
        BUTTON_POSITION = buttons_positions[n]["button"]
        INPUT_FIELD_POSITION = buttons_positions[n]["field"]

    def change_key(self, key):
        self.pushButton.setText(key)

    def start_input(self):
        global INPUT_MODE
        INPUT_MODE = True
        self.pushButton.setText("...")


def listen_keys():
    print("start listening")
    with Listener(on_press=show) as listener:
        listener.join()


def show(key):
    global IS_WORKING, INPUT_MODE, START_KEY
    if INPUT_MODE:
            START_KEY = key
            INPUT_MODE = False
            demo.change_key(str(key).replace("'", "").replace("Key.", "").upper())

    elif key == START_KEY:
        IS_WORKING = not IS_WORKING


def sell():
    while True:
        if IS_WORKING:
            pixel = pyautogui.screenshot().getpixel((BUTTON_POSITION.x, BUTTON_POSITION.y))
            if pixel == SUCCESS_COLOR:
                pyautogui.click(INPUT_FIELD_POSITION)
                pyautogui.moveTo(INPUT_FIELD_POSITION)
                pyautogui.typewrite(str(MAX_SOLD))
                pyautogui.click(BUTTON_POSITION)
                pyautogui.click(BUTTON_POSITION.x - 100, BUTTON_POSITION.y)
                time.sleep(4)


if __name__ == '__main__':
    t1 = threading.Thread(target=listen_keys)
    t2 = threading.Thread(target=sell)
    t1.start()
    t2.start()
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
