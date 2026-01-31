import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class Clock(QWidget):
    
    def __init__(self):
        super().__init__()
        self.time_label= QLabel(self)
        self.timer= QTimer()
        self.initUI()

    #Design UI
    def initUI(self):
        
        self.setWindowTitle("Clock")
        self.setGeometry(500, 250, 500, 200)

        #Layout
        vbox= QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        #Center Alignment
        self.time_label.setAlignment(Qt.AlignCenter)

        #Style
        self.time_label.setStyleSheet("font-size: 100px;"
                                      "color: #2bd65e;")
        self.setStyleSheet("background-color: #252626;")
        fontID= QFontDatabase.addApplicationFont("C:/Users/sanje/Downloads/Sanjeevs-Font-Regular.TTF")
        fontFamily= QFontDatabase.applicationFontFamilies(fontID)
        if fontFamily:
            myFont= QFont(fontFamily[0], 150)
            self.time_label.setFont(myFont)

        #Update time in real time
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        
        self.updateTime()

    #Time Updation
    def updateTime(self):
        currentTime= QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(currentTime)






def main():

    app= QApplication(sys.argv)
    clock= Clock()
    #Shows the window
    clock.show()
    #Executes the window 
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

