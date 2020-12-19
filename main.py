import sys 
from PyQt5.QtWidgets import QApplication
from audioPlayer import AudioMainWindow

APP = QApplication(sys.argv)

audioplayer = AudioMainWindow()

sys.exit(APP.exec_())