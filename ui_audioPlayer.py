# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *


class PlaylistModel(QAbstractListModel):
	def __init__(self, playlist, *args, **kwargs):
		super(PlaylistModel, self).__init__(*args, **kwargs)
		self.playlist = playlist
	def data(self, index, role):
		if role == Qt.DisplayRole:
			media = self.playlist.media(index.row())
			return media.canonicalUrl().fileName()
	def rowCount(self, index):
		return self.playlist.mediaCount()
class Ui_audioWindow(object):
    def setupUi(self, audioWindow):
        audioWindow.setObjectName("audioWindow")
        audioWindow.setMinimumSize(720, 480)
        audioWindow.setWindowIcon(QtGui.QIcon('images/audio.png'))
        audioWindow.setStyleSheet("")
        # Action font
        action_font = QtGui.QFont()
        action_font.setFamily("Arial")
        action_font.setPointSize(12)

        self.playlistView = QtWidgets.QListView()
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")

        # Label font
        label_font = QtGui.QFont()
        label_font.setFamily("MS Sans Serif")
        label_font.setPointSize(14)
        # Central widget
        self.centralwidget = QtWidgets.QWidget(audioWindow)
        self.centralwidget.setObjectName("centralwidget")
        audioWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(audioWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        # App menu selection
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        self.menuQuit.setCursor(QCursor(Qt.PointingHandCursor))
        # File menu selection
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setCursor(QCursor(Qt.PointingHandCursor))
        # View menu selection
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuView.setCursor(QCursor(Qt.PointingHandCursor))
        # menu setting
        audioWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(audioWindow)
        self.statusbar.setObjectName("statusbar")
        audioWindow.setStatusBar(self.statusbar)
        # Quit menu
        self.actionQuit = QtWidgets.QAction(audioWindow)
        self.actionQuit.setIcon(QIcon('images/quit.png'))
        self.actionQuit.setFont(action_font)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut('Ctrl+Q')
        # About menu
        self.actionAbout = QtWidgets.QAction(audioWindow)
        self.actionAbout.setIcon(QIcon('images/about.png'))
        self.actionAbout.setFont(action_font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setShortcut('Ctrl+I')
        # Help menu
        self.actionHelp = QtWidgets.QAction(audioWindow)
        self.actionHelp.setIcon(QIcon('images/help.png'))
        self.actionHelp.setFont(action_font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setShortcut('Ctrl+H')
        # Light theme for app
        self.actionLight = QtWidgets.QAction(audioWindow)
        self.actionLight.setFont(action_font)
        self.actionLight.setObjectName("actionLight")
        self.actionLight.setShortcut('Ctrl+L')
        # Dark theme for app
        self.actionDark = QtWidgets.QAction(audioWindow)
        self.actionDark.setFont(action_font)
        self.actionDark.setObjectName("actionDark")
        self.actionDark.setShortcut('Ctrl+D')
        # Menus adding
        self.actionAdd_file_2 = QtWidgets.QAction(audioWindow)
        self.actionAdd_file_2.setObjectName("actionAdd_file_2")
        self.actionAdd_file_2.setIcon(QIcon("images/files.png"))
        self.actionAdd_file_2.setFont(action_font)

        self.actionOpen_File = QtWidgets.QAction(audioWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.setIcon(QIcon("images/delete.png"))
        self.actionOpen_File.setFont(action_font)
        self.menuQuit.addAction(self.actionAbout)
        self.menuQuit.addAction(self.actionHelp)
        self.menuQuit.addAction(self.actionQuit)
        self.menuView.addAction(self.actionLight)
        self.menuView.addAction(self.actionDark)
        self.menuFile.addAction(self.actionAdd_file_2)
        self.menuFile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        # Audio player init
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlistView.setFont(label_font)
        # Audip player init ends

        # Buttons slider and everything else
        # Play button
        self.playBtn = QtWidgets.QPushButton()
        self.playBtn.setIcon(QIcon('images/play.png'))
        self.playBtn.setIconSize(QSize(50,50))
        self.playBtn.setFixedSize(50, 50)
        self.playBtn.setStyleSheet("background-color: transparent")
        self.playBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # Pause button
        self.pauseBtn = QtWidgets.QPushButton()
        self.pauseBtn.setIcon(QIcon('images/pause.png'))
        self.pauseBtn.setIconSize(QSize(50,50))
        self.pauseBtn.setFixedSize(50, 50)
        self.pauseBtn.setStyleSheet("background-color: transparent")
        self.pauseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # Replay button
        self.replayBtn = QtWidgets.QPushButton()
        self.replayBtn.setIcon(QIcon('images/replay.png'))
        self.replayBtn.setIconSize(QSize(50,50))
        self.replayBtn.setFixedSize(50, 50)
        self.replayBtn.setStyleSheet("background-color: transparent")
        self.replayBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # Previous button
        self.prevBtn = QtWidgets.QPushButton()
        self.prevBtn.setIcon(QIcon('images/prev.png'))
        self.prevBtn.setIconSize(QSize(50,50))
        self.prevBtn.setFixedSize(50, 50)
        self.prevBtn.setStyleSheet("background-color: transparent")
        self.prevBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # Next button
        self.nextBtn = QtWidgets.QPushButton()
        self.nextBtn.setIcon(QIcon('images/next.png'))
        self.nextBtn.setIconSize(QSize(50,50))
        self.nextBtn.setFixedSize(50, 50)
        self.nextBtn.setStyleSheet("background-color: transparent")
        self.nextBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # Volume button
        self.volumeBtn = QtWidgets.QPushButton()
        self.volumeBtn.setIcon(QIcon('images/volume.png'))
        self.volumeBtn.setIconSize(QSize(50,50))
        self.volumeBtn.setFixedSize(50, 50)
        self.volumeBtn.setStyleSheet("background-color: transparent")
        self.volumeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # Volume slider
        self.volumeSlider = QtWidgets.QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 0)
        self.volumeSlider.setFocusPolicy(Qt.StrongFocus)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.volumeSlider.setSingleStep(10)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(50)
        # Volume Label
        self.volumeLabel = QtWidgets.QLabel()
        self.volumeLabel.setText('50')
        self.volumeLabel.setFont(label_font)
        # Horizontal box layout
        self.hboxLayout = QtWidgets.QHBoxLayout()
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)

        # Time label and slider
        self.time = QtWidgets.QLabel()
        self.time.setText('00:00')
        self.time.setFont(label_font)

        self.durationSlider = QtWidgets.QSlider(Qt.Horizontal)
        self.durationSlider.setRange(0, 0)
        self.durationSlider.setMinimum(0)
        self.durationSlider.setMaximum(100)

        self.video_time = QtWidgets.QLabel()
        self.video_time.setText('00:00')
        self.video_time.setFont(label_font)

        self.audioLabelName = QtWidgets.QLabel()
        self.audioLabelName.setFont(label_font)
        # Upper layout for time slider

        self.hboxLayout_time = QtWidgets.QHBoxLayout()
        self.hboxLayout_time.setContentsMargins(0, 0, 0, 10)
        self.hboxLayout_time.addWidget(self.audioLabelName)
        self.hboxLayout_time.addWidget(self.time)
        self.hboxLayout_time.addWidget(self.durationSlider)
        self.hboxLayout_time.addWidget(self.video_time)
        # Lower layout for buttons and labels and slider
        self.hboxLayout.addWidget(self.replayBtn)
        self.hboxLayout.addWidget(self.prevBtn)
        self.hboxLayout.addWidget(self.playBtn)
        self.hboxLayout.addWidget(self.pauseBtn)
        self.hboxLayout.addWidget(self.nextBtn)
        self.hboxLayout.addWidget(self.volumeBtn)
        self.hboxLayout.addWidget(self.volumeSlider)
        self.hboxLayout.addWidget(self.volumeLabel)

        # Vertical widget for all media
        self.vboxLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vboxLayout.addWidget(self.playlistView)
        self.vboxLayout.addLayout(self.hboxLayout_time)
        self.vboxLayout.addLayout(self.hboxLayout)

        self.retranslateUi(audioWindow)
        QtCore.QMetaObject.connectSlotsByName(audioWindow)

    def retranslateUi(self, audioWindow):
        _translate = QtCore.QCoreApplication.translate
        audioWindow.setWindowTitle(_translate("audioWindow", "AudioPlayer"))
        self.menuQuit.setTitle(_translate("audioWindow", "App"))
        self.menuFile.setTitle(_translate("audioWindow", "File"))
        self.menuView.setTitle(_translate("audioWindow", "View"))
        self.actionHelp.setText(_translate("audioWindow", "Help"))
        self.actionQuit.setText(_translate("audioWindow", "Quit"))

        self.actionLight.setText(_translate("audioWindow", "Light"))
        self.actionDark.setText(_translate("audioWindow", "Dark"))

        self.actionAbout.setText(_translate("audioWindow", "About"))
        self.actionAdd_file_2.setText(_translate("audioWindow", "Add File"))
        self.actionOpen_File.setText(_translate("audioWindow", "Delete file"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    audioWindow = QtWidgets.QMainWindow()
    ui = Ui_audioWindow()
    ui.setupUi(audioWindow)
    audioWindow.show()
    sys.exit(app.exec_())
