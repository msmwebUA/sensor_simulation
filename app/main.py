import sys
from PySide6.QtWidgets import QApplication
from app import App

def main():
  app = QApplication(sys.argv)
  window = App()
  window.show()
  window.raise_() # window on top
  window.activateWindow() # activate window to get focus
  sys.exit(app.exec())

if __name__ == "__main__":
  main()