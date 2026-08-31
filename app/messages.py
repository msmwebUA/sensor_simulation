from PySide6.QtWidgets import QMessageBox, QWidget

def showAlert(parent: QWidget, title: str, text: str, alert_type: str) -> None:
  # param parent: window or widget where alert will be shown
  alert = QMessageBox(parent)
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

def showConfirmation(parent: QWidget, title: str, text: str) -> bool:
  # param parent: window or widget where alert will be shown
  answer = QMessageBox.question(
    parent,
    title,
    text,
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, # btns
    QMessageBox.StandardButton.No # focus
  )
  if answer == QMessageBox.StandardButton.Yes:
    return True
  else:
    return False

class ConsoleMessage:
  _widget = None

  @classmethod
  def setWidget(cls, widget):
    # link to plain text widget (passed from main window)
    cls._widget = widget

  @classmethod
  def append(cls, message: str):
    if cls._widget:
      cls._widget.appendPlainText(message)
    else:
      print(f"Widget for console messages not set")