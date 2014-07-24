all: guistructure.ui
	pyuic4 guistructure.ui > guistructure.py
	pyuic4 forcemomentprompt.ui > forcemomentprompt.py
	pyuic4 distforceprompt.ui > distforceprompt.py
