import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
#importing QtCore to use Qurl
from PyQt5.QtCore import *

defaultBrowser = "http://google.com"

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        icons = [
          'SP_ArrowBack',
          'SP_ArrowForward',
          'SP_BrowserReload',
          'SP_TitleBarUnshadeButton'
        ]

        #---------------------adding browser-------------------
        self.browser = QWebEngineView()
        #Place to set default web browser URL
        self.browser.setUrl(QUrl(defaultBrowser))
        #to display google search engine on our browser
        self.setCentralWidget(self.browser)
        # Opens in full screen. Change later to make an option
        self.showMaximized()

        #----------------------navbar-------------------------
        navbar = QToolBar()
        self.addToolBar(navbar)

        #-----------------prev Button-----------------
        # prevBtn = QAction('Prev',self)
        prevBtn = QAction("", self)
        prevBtn.setIcon(self.style().standardIcon(getattr(QStyle, icons[0])))
        #when triggered set connection
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)

        #-----------------next Button---------------
        nextBtn = QAction("", self)
        nextBtn.setIcon(self.style().standardIcon(getattr(QStyle, icons[1])))
        #when triggered set connection
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        #-----------refresh Button--------------------
        refreshBtn = QAction("", self)
        refreshBtn.setIcon(self.style().standardIcon(getattr(QStyle, icons[2])))
        #when triggered set connection
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        #-----------home button----------------------
        homeBtn = QAction('Home',self)
        #when triggered call home method
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)

        #---------------------search bar---------------------------------
        self.searchBar = QLineEdit()
        #when someone presses return(enter) call loadUrl method
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)

        #if url in the searchBar is changed then call updateUrl method
        self.browser.urlChanged.connect(self.updateUrl)

        #---------------------Options Menu-------------------------------
        # self.optionsMenu = QComboBox()
        # self.optionsMenu.setItemIcon(self.style().standardIcon(getattr(QStyle, icons[3])))

        # navbar.addWidget(self.optionsMenu)
        #---------------------Options/Functionality----------------------
        # self.optionsMenu.add("E")
        # self.optionsMenu.add("E")
        # self.optionsMenu.add("E")
        # self.optionsMenu.add("E")

    #method to navigate back to home page
    def home(self):
        self.browser.setUrl(QUrl(defaultBrowser))

    #method to load the required url
    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))

    #method to update the url
    def updateUrl(self, url):
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Web Browser')
window = Window()
MyApp.exec_()
