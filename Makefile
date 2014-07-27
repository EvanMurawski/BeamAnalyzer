all: guistructure.ui
	pyuic4 guistructure.ui > guistructure.py
	pyuic4 forcemomentprompt.ui > forcemomentprompt.py
	pyuic4 distforceprompt.ui > distforceprompt.py
	pyuic4 mainwindow.ui > mainwindow.py
	pyuic4 settingsdialog.ui > settingsdialog.py
