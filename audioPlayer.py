from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import *
from ui_audioPlayer import Ui_audioWindow
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtMultimedia import *
import os

class AudioMainWindow(QtWidgets.QMainWindow, Ui_audioWindow):

	def __init__(self, *args, **kwargs):
		super(AudioMainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.setLightPalette()
		self.show()
		self.delated_index = 0
		# Action connectings
		self.actionAbout.triggered.connect(self.aboutEvent)
		self.actionQuit.triggered.connect(self.close)
		self.actionLight.triggered.connect(self.setLightPalette)
		self.actionDark.triggered.connect(self.setDarkPalette)
		self.actionOpen_File.triggered.connect(self.remove_item_file)
		self.actionAdd_file_2.triggered.connect(self.save_file)
		self.actionHelp.triggered.connect(self.action_help)
		# Buttons connections
		self.volumeSlider.sliderMoved.connect(self.set_vol)
		self.volumeBtn.clicked.connect(self.switch_vol)
		self.playBtn.clicked.connect(self.player.play)
		self.pauseBtn.clicked.connect(self.player.pause)
		self.prevBtn.clicked.connect(self.playlist.previous)
		self.nextBtn.clicked.connect(self.playlist.next)
		self.replayBtn.clicked.connect(self.replay)
		self.durationSlider.sliderMoved.connect(self.set_pos)
		self.volumeSlider.sliderMoved.connect(self.set_vol)
		# Player connection
		self.player.durationChanged.connect(self.duration_changed)
		self.player.positionChanged.connect(self.position_changed)

		self.playlistView.clicked.connect(self.item_click)

		self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
		self.playlist.currentMediaChanged.connect(self.song_changed)
		selection_model = self.playlistView.selectionModel()
		selection_model.selectionChanged.connect(self.playlist_selection_changed)
	# Functions
	def song_changed(self, media):
		if not media.isNull():
			self.audioLabelName.setText(str(media.canonicalUrl().fileName()))

	def remove_item_file(self):
		self.playlist.removeMedia(self.delated_index)
		self.model.removeRow(self.delated_index)
		if self.playlist.mediaCount() == 0:
			self.audioLabelName.setText('')

	def item_click(self, index):
		self.delated_index = index.row()
	# Special time function
	def hhmmss(self, ms):
		# s = 1000
		# m = 60000
		# h = 360000
		h, r = divmod(ms, 360000)
		m, r = divmod(r, 60000)
		s, _ = divmod(r, 1000)
		return ("%02d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))
	# About program function
	def aboutEvent(self, event):
		''' About function event for about menu or Ctrl+I'''
		about = QtWidgets.QMessageBox.about(self, 'About', "This my audio player that I created using PyQt5")

	# Function that create new window with help text

	def create_help_label(self):
		self.helpLabelText = QtWidgets.QLabel()
		self.helpLabelText.setText('<h1>How to use </h1>\n'
		'<h3>1. Light theme </h3>\n'
		'It\'s set by default. Click view in the upper menubar and in menu select' + '<br>' 
		'Light theme or click Ctrl+L\n'
		'<h3>2. Dark Theme </h3>'
		'Click view in the upper menubar and in menu select Dark theme or click Ctrl+D\n\n'
		'<h3>3. Quick Commands </h3>'
		'Click Ctrl+Q to close the app\n' + '<br>'
		'Click Ctrl+I to see information about the app\n' + '<br>'
		'Click Ctrl+H to see HELP window the app\n' + '<br>'
		'<h3>4. Open and Remove Files </h3>'
		'In order to delete audio select file then click File in upper menu and select Delete file' + '<br>'
		'In order to save file to playlist click File in upper menu and select Add file' + '<br>'
		'<h3>5. About the app </h3>'
		'To get information about the app CLICK Ctrl+I or click App in upper' + '<br>' +  'menu and select About')
		self.helpLabelText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
		helpFont = QFont('Times', 12)
		self.helpLabelText.setFont(helpFont)
		return self.helpLabelText

	def action_help(self):
		helpDialog = QtWidgets.QDialog()
		helpDialog.setModal(True)
		helpDialog.setWindowIcon(QIcon("images/help.png"))
		helpDialog.setMinimumSize(720, 480)
		helpDialog.setWindowTitle('Help')

		Help_Label = self.create_help_label()

		scroll = QtWidgets.QScrollArea()
		scroll.setStyleSheet('padding: 10px')
		scroll.setWidgetResizable(True)
		scroll.setFixedHeight(400)
		scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		scroll.setWidget(Help_Label)

		helpVBoxLayout = QtWidgets.QHBoxLayout()
		helpVBoxLayout.addWidget(scroll)

		helpDialog.setLayout(helpVBoxLayout)
		helpDialog.exec()
		return helpDialog
	# Volume sliding
	def set_vol(self, vol):
		self.player.setVolume(vol)
		self.volumeLabel.setText(str(vol))
		if vol == 100:
			self.volumeBtn.setIcon(QIcon("images/volume100.png"))
		elif vol == 0:
			self.volumeBtn.setIcon(QIcon("images/no_volume.png"))
		else:
			self.volumeBtn.setIcon(QIcon('images/volume.png'))

	# Mute and unmute the video
	def switch_vol(self):
		if self.player.volume() == 0:
			self.set_vol(50)
			self.volumeSlider.setValue(50)
			self.volumeLabel.setText(str(50))
		elif self.player.volume() != 0:
			self.set_vol(0)
			self.volumeSlider.setValue(0)
			self.volumeLabel.setText(str(0))
	# Open file function
	def save_file(self):
		path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "", "mp3 Audio (*.mp3);")
		if path:
			self.playlist.addMedia(
				QMediaContent(
					QUrl.fromLocalFile(path)
				)
			)
		self.model.layoutChanged.emit()
	def replay(self):
		self.set_pos(0)
		self.player.play()
	# Change duration of the audio slider
	def duration_changed(self, duration):
		self.durationSlider.setMaximum(duration)
		if duration >= 0:
			self.video_time.setText(self.hhmmss(duration)) 
	# Change position of the slider
	def position_changed(self, position):
		self.durationSlider.setValue(position)
		if position >= 0:
			self.time.setText(self.hhmmss(position))
	# Set position for slider and audio
	def set_pos(self, pos):
		self.player.setPosition(pos)

	def playlist_position_changed(self, i):
		if i > -1:
			ix = self.model.index(i)
			self.playlistView.setCurrentIndex(ix)

	def playlist_selection_changed(self, ix):
		i = ix.indexes()[0].row()
		self.playlist.setCurrentIndex(i)
	# Set dark theme for app
	def setDarkPalette(self):
		palette = QPalette()
		palette.setColor(QPalette.Window, QColor(53, 53, 53))
		palette.setColor(QPalette.WindowText, Qt.white)
		palette.setColor(QPalette.Base, QColor(25, 25, 25))
		palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		palette.setColor(QPalette.ToolTipBase, Qt.white)
		palette.setColor(QPalette.ToolTipText, Qt.black)
		palette.setColor(QPalette.Text, Qt.white)
		palette.setColor(QPalette.Button, QColor(53, 53, 53))
		palette.setColor(QPalette.ButtonText, Qt.white)
		palette.setColor(QPalette.BrightText, Qt.white)
		palette.setColor(QPalette.Link, QColor(42, 130, 218))
		palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
		palette.setColor(QPalette.HighlightedText, Qt.black)
		self.volumeLabel.setStyleSheet("color: #ffffff")
		self.time.setStyleSheet("color: #ffffff")
		self.audioLabelName.setStyleSheet('color: #ffffff')
		self.video_time.setStyleSheet("color: #ffffff")
		self.playlistView.setStyleSheet('background-color: #000000; color: #ffffff')
		self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }\n"
		"QMenuBar { background-color: #353535; color: #ffffff; border-bottom: 1px solid #BBBBBB; font-size: 16px; }\n"
		"QMenuBar::item:selected { background-color: #0E91EA; color: #ffffff; } \n")
		self.setPalette(palette)
	# set Light thme for app
	def setLightPalette(self):
		palette = QPalette()
		palette.setColor(QPalette.Window, QColor(243, 243, 243))
		palette.setColor(QPalette.WindowText, Qt.black)
		palette.setColor(QPalette.Button, QColor(243, 243, 243))
		palette.setColor(QPalette.ButtonText, Qt.black)
		palette.setColor(QPalette.Base, QColor(0, 0, 0))
		palette.setColor(QPalette.AlternateBase, QColor(243, 243, 243))
		self.volumeLabel.setStyleSheet("color: #000000")
		self.time.setStyleSheet("color: #000000")
		self.audioLabelName.setStyleSheet('color: #000000')
		self.video_time.setStyleSheet("color: #000000")
		self.playlistView.setStyleSheet('background-color: #ffffff; color: #000000')
		self.setStyleSheet("QToolTip { color: #000000; background-color: #f3f3f3; border: 1px solid #000000; }\n"
		"QMenuBar { background-color: #f3f3f3; color: #000000;border-bottom: 1px solid #191919; font-size: 16px; }\n")
		self.setPalette(palette)