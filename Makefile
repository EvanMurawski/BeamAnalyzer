all: ./beamanalyzer/frontend/guistructure.ui
	pyuic4 ./beamanalyzer/frontend/guistructure.ui > ./beamanalyzer/frontend/guistructure.py
	pyuic4 ./beamanalyzer/frontend/forcemomentprompt.ui > ./beamanalyzer/frontend/forcemomentprompt.py
	pyuic4 ./beamanalyzer/frontend/distforceprompt.ui > ./beamanalyzer/frontend/distforceprompt.py
	pyuic4 ./beamanalyzer/frontend/mainwindow.ui > ./beamanalyzer/frontend/mainwindow.py
	pyuic4 ./beamanalyzer/frontend/settingsdialog.ui > ./beamanalyzer/frontend/settingsdialog.py
