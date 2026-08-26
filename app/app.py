from database import Database

# import UI
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Qt, QElapsedTimer, QTimer, QDateTime
from ui import Ui_MainWindow

# libs for Raspberry time manipulation
import subprocess

class App(QMainWindow, Ui_MainWindow):
  def __init__(self) -> None:
    super().__init__()
    self.setupUi(self)

    # full screen UI
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    self.showFullScreen()
    # hide cursor
    self.setCursor(Qt.CursorShape.BlankCursor)
    # vars for exit from full screen mode
    self.click_count = 0
    self.click_timer = QElapsedTimer()
    self.click_to_exit = 7
    self.click_timeout = 2000 # ms

    # clock
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.updateClock)
    self.timer.start(1000)

    # set first stackedWidget page
    self.stackedWidget.setCurrentIndex(0)

    # connect slots (methods) to buttons on signals (events)
    self.nextBtn.clicked.connect(self.nextJoke)
    self.showTimeSettingsBtn.clicked.connect(self.showTimeSettings)
    self.cancelBtn.clicked.connect(self.cancelTimeSettings)
    self.okBtn.clicked.connect(self.setTime)

    # make time settings elements invisible on start
    self.okBtn.setVisible(False)
    self.dateTimeEdit.setVisible(False)
    self.cancelBtn.setVisible(False)

    # init database
    self.db = Database()

    # joke icons (emojis)
    self.joke_icons = ['🤣', '😁', '😜', '😆', '😊', '😂', '😎', '😮', '🙃', '😃']
    self.current_icon_index = -1
    
    # set joke on startup
    self.nextJoke()

    # shedule next joke in every 4 hours
    self.nextJokeTimer = QTimer(self)
    self.nextJokeTimer.timeout.connect(self.nextJoke)
    self.nextJokeTimer.start(14400000)
  
  def nextJoke(self) -> None:
    # Set next joke text and icon (emoji) to labels
    self.jokeLabel.setText(self.db.getRandomJoke())
    self.current_icon_index = (self.current_icon_index + 1) % 10
    self.jokeIcon.setText(self.joke_icons[self.current_icon_index])


  def showTimeSettings(self) -> None:
    self.dateTimeEdit.setVisible(True)
    self.okBtn.setVisible(True)
    self.cancelBtn.setVisible(True)
    self.showTimeSettingsBtn.setVisible(False)
    self.dateTimeLabel.setVisible(False)

  def cancelTimeSettings(self) -> None:
    self.dateTimeEdit.setVisible(False)
    self.okBtn.setVisible(False)
    self.cancelBtn.setVisible(False)
    self.showTimeSettingsBtn.setVisible(True)
    self.dateTimeLabel.setVisible(True)

  def setTime(self) -> None:
    qt_datetime = self.dateTimeEdit.dateTime()
    datetime_string = qt_datetime.toString("yyyy-MM-dd HH:mm:ss")
    try:
      # Use timedatectl to set the system time. Format: 'YYYY-MM-DD HH:MI:SS'
      subprocess.run(["sudo", "timedatectl", "set-time", datetime_string], check=True)
    except subprocess.CalledProcessError as e:
      self.showAlert("Error", f"Failed to set time. Error: {e}", "critical")
    except FileNotFoundError:
      self.showAlert("Error", "timedatectl command not found. Are you running on Linux?", "critical")
    self.dateTimeEdit.setVisible(False)
    self.okBtn.setVisible(False)
    self.cancelBtn.setVisible(False)
    self.showTimeSettingsBtn.setVisible(True)
    self.dateTimeLabel.setVisible(True)

  def mousePressEvent(self, event) -> None:
    # Count clicks (reset, if > 2 sec)
    if self.click_count == 0 or self.click_timer.elapsed() > self.click_timeout:
        self.click_count = 1
        self.click_timer.start()
    else:
        self.click_count += 1
    # Check number of clicks
    if self.click_count >= self.click_to_exit:
        self.minimizeToWindow()
        self.click_count = 0 # reset counter
    # Allow the parent class to handle the event
    super().mousePressEvent(event)

  def minimizeToWindow(self) -> None:
    # Show frame and controls
    self.setWindowFlags(Qt.WindowType.Window)
    # Show cursor
    self.unsetCursor() 
    # Show in normal size
    self.showNormal() 
    self.activateWindow()

  def updateClock(self) -> None:
    now = QDateTime.currentDateTime()
    time_text = now.toString("HH:mm:ss")
    date_text = now.toString("dd.MM.yyyy")
    self.dateTimeLabel.setText(f"🗓️ {date_text}  ⏰ {time_text}")
  
  def showAlert(self, title: str, text: str, alert_type: str) -> None:
    alert = QMessageBox(self)
    alert.setWindowTitle(title)
    alert.setText(text)
    if alert_type == "info":
        alert.setIcon(QMessageBox.Icon.Information)
    elif alert_type == "warning":
        alert.setIcon(QMessageBox.Icon.Warning)
    elif alert_type == "critical":
        alert.setIcon(QMessageBox.Icon.Critical)
    else:
        alert.setIcon(QMessageBox.Icon.Information)
    alert.setStandardButtons(QMessageBox.StandardButton.Ok)
    alert.exec()
    # After dialog closes
    self.stackedWidget.setCurrentIndex(0)