# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Thu Oct 20 13:38:51 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(893, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        MainWindow.setToolTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 881, 501))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Input_Dock = QtGui.QDockWidget(self.layoutWidget)
        self.Input_Dock.setEnabled(True)
        self.Input_Dock.setMaximumSize(QtCore.QSize(230, 524287))
        self.Input_Dock.setAutoFillBackground(False)
        self.Input_Dock.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Input_Dock.setFloating(False)
        self.Input_Dock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.Input_Dock.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.Input_Dock.setObjectName("Input_Dock")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.layoutWidget1 = QtGui.QWidget(self.dockWidgetContents_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 310, 221, 159))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_Source = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_Source.setChecked(True)
        self.radioButton_Source.setObjectName("radioButton_Source")
        self.horizontalLayout_2.addWidget(self.radioButton_Source)
        self.radioButton_Sink = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_Sink.setObjectName("radioButton_Sink")
        self.horizontalLayout_2.addWidget(self.radioButton_Sink)
        self.radioButton_Doublet = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_Doublet.setObjectName("radioButton_Doublet")
        self.horizontalLayout_2.addWidget(self.radioButton_Doublet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_Vortex = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_Vortex.setObjectName("radioButton_Vortex")
        self.horizontalLayout_3.addWidget(self.radioButton_Vortex)
        self.radioButton_Unifoem = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_Unifoem.setObjectName("radioButton_Unifoem")
        self.horizontalLayout_3.addWidget(self.radioButton_Unifoem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_X = QtGui.QLabel(self.layoutWidget1)
        self.label_X.setObjectName("label_X")
        self.horizontalLayout_8.addWidget(self.label_X)
        self.doubleSpinBox_X = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_X.setMinimum(-1000.0)
        self.doubleSpinBox_X.setMaximum(1000.0)
        self.doubleSpinBox_X.setSingleStep(0.1)
        self.doubleSpinBox_X.setObjectName("doubleSpinBox_X")
        self.horizontalLayout_8.addWidget(self.doubleSpinBox_X)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_Y = QtGui.QLabel(self.layoutWidget1)
        self.label_Y.setObjectName("label_Y")
        self.horizontalLayout_9.addWidget(self.label_Y)
        self.doubleSpinBox_Y = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_Y.setMinimum(-1000.0)
        self.doubleSpinBox_Y.setMaximum(1000.0)
        self.doubleSpinBox_Y.setSingleStep(0.1)
        self.doubleSpinBox_Y.setObjectName("doubleSpinBox_Y")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_Y)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Strength = QtGui.QLabel(self.layoutWidget1)
        self.label_Strength.setObjectName("label_Strength")
        self.horizontalLayout_10.addWidget(self.label_Strength)
        self.doubleSpinBox_Strength = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_Strength.setMinimum(-10000.0)
        self.doubleSpinBox_Strength.setMaximum(10000.0)
        self.doubleSpinBox_Strength.setSingleStep(0.1)
        self.doubleSpinBox_Strength.setObjectName("doubleSpinBox_Strength")
        self.horizontalLayout_10.addWidget(self.doubleSpinBox_Strength)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_12.addWidget(self.pushButton_5)
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_12.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.layoutWidget2 = QtGui.QWidget(self.dockWidgetContents_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 271, 301))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_potentialShow = QtGui.QTableWidget(self.layoutWidget2)
        self.tableWidget_potentialShow.setMinimumSize(QtCore.QSize(221, 0))
        self.tableWidget_potentialShow.setObjectName("tableWidget_potentialShow")
        self.tableWidget_potentialShow.setColumnCount(4)
        self.tableWidget_potentialShow.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_potentialShow.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_potentialShow.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_potentialShow.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_potentialShow.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget_potentialShow)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_RemoveEntry = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_RemoveEntry.setEnabled(False)
        self.pushButton_RemoveEntry.setObjectName("pushButton_RemoveEntry")
        self.horizontalLayout_11.addWidget(self.pushButton_RemoveEntry)
        self.pushButton_ChangeEntry = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_ChangeEntry.setEnabled(False)
        self.pushButton_ChangeEntry.setObjectName("pushButton_ChangeEntry")
        self.horizontalLayout_11.addWidget(self.pushButton_ChangeEntry)
        self.pushButton_PotentialRun = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_PotentialRun.setObjectName("pushButton_PotentialRun")
        self.horizontalLayout_11.addWidget(self.pushButton_PotentialRun)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        spacerItem1 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Input_Dock.setWidget(self.dockWidgetContents_3)
        self.horizontalLayout.addWidget(self.Input_Dock)
        self.graphicsView_Main = QtGui.QGraphicsView(self.layoutWidget)
        self.graphicsView_Main.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.graphicsView_Main.setObjectName("graphicsView_Main")
        self.horizontalLayout.addWidget(self.graphicsView_Main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Window = QtGui.QMenu(self.menubar)
        self.menu_Window.setObjectName("menu_Window")
        self.menu_Aerodynamics = QtGui.QMenu(self.menubar)
        self.menu_Aerodynamics.setObjectName("menu_Aerodynamics")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_Icons = QtGui.QToolBar(MainWindow)
        self.toolBar_Icons.setObjectName("toolBar_Icons")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar_Icons)
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Tools = QtGui.QAction(MainWindow)
        self.action_Tools.setObjectName("action_Tools")
        self.action_Potential_Flows = QtGui.QAction(MainWindow)
        self.action_Potential_Flows.setObjectName("action_Potential_Flows")
        self.actionPanel_Methods = QtGui.QAction(MainWindow)
        self.actionPanel_Methods.setObjectName("actionPanel_Methods")
        self.actionCFD = QtGui.QAction(MainWindow)
        self.actionCFD.setObjectName("actionCFD")
        self.action_Clear_all = QtGui.QAction(MainWindow)
        self.action_Clear_all.setObjectName("action_Clear_all")
        self.action_Clear_All = QtGui.QAction(MainWindow)
        self.action_Clear_All.setObjectName("action_Clear_All")
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Window.addAction(self.action_Clear_All)
        self.menu_Aerodynamics.addAction(self.action_Potential_Flows)
        self.menu_Aerodynamics.addAction(self.actionPanel_Methods)
        self.menu_Aerodynamics.addAction(self.actionCFD)
        self.menu_Aerodynamics.addSeparator()
        self.menu_Aerodynamics.addAction(self.action_Clear_all)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Aerodynamics.menuAction())
        self.menubar.addAction(self.menu_Window.menuAction())
        self.label_Strength.setBuddy(self.doubleSpinBox_Strength)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(self.actionCFD, QtCore.SIGNAL("activated()"), self.Input_Dock.show)
        QtCore.QObject.connect(self.actionCFD, QtCore.SIGNAL("activated()"), self.Input_Dock.setFocus)
        QtCore.QObject.connect(self.action_Potential_Flows, QtCore.SIGNAL("activated()"), self.Input_Dock.show)
        QtCore.QObject.connect(self.action_Potential_Flows, QtCore.SIGNAL("activated()"), self.Input_Dock.setFocus)
        QtCore.QObject.connect(self.actionPanel_Methods, QtCore.SIGNAL("activated()"), self.Input_Dock.show)
        QtCore.QObject.connect(self.actionPanel_Methods, QtCore.SIGNAL("activated()"), self.Input_Dock.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "EduAeroSpace", None, QtGui.QApplication.UnicodeUTF8))
        self.Input_Dock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_Source.setText(QtGui.QApplication.translate("MainWindow", "&Source", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_Sink.setText(QtGui.QApplication.translate("MainWindow", "S&ink", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_Doublet.setText(QtGui.QApplication.translate("MainWindow", "&Doublet", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_Vortex.setText(QtGui.QApplication.translate("MainWindow", "&Vortex", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_Unifoem.setText(QtGui.QApplication.translate("MainWindow", "&Uniform flow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_X.setText(QtGui.QApplication.translate("MainWindow", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Y.setText(QtGui.QApplication.translate("MainWindow", "Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Strength.setText(QtGui.QApplication.translate("MainWindow", "Strength", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "&Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_potentialShow.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_potentialShow.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_potentialShow.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_potentialShow.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Strength", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_RemoveEntry.setText(QtGui.QApplication.translate("MainWindow", "&Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ChangeEntry.setText(QtGui.QApplication.translate("MainWindow", "&Change", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_PotentialRun.setText(QtGui.QApplication.translate("MainWindow", "&Simulate", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Window.setTitle(QtGui.QApplication.translate("MainWindow", "&Window", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Aerodynamics.setTitle(QtGui.QApplication.translate("MainWindow", "&Aerodynamics", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Icons.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Tools.setText(QtGui.QApplication.translate("MainWindow", "&Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Potential_Flows.setText(QtGui.QApplication.translate("MainWindow", "&Potential Flows", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPanel_Methods.setText(QtGui.QApplication.translate("MainWindow", "Panel Methods", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCFD.setText(QtGui.QApplication.translate("MainWindow", "CFD", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Clear_all.setText(QtGui.QApplication.translate("MainWindow", "&Clear all", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Clear_All.setText(QtGui.QApplication.translate("MainWindow", "&Clear All", None, QtGui.QApplication.UnicodeUTF8))

