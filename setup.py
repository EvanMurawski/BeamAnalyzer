from setuptools import setup, find_packages
try:
	import py2exe
except ImportError:
	pass

setup(
	name='beamanalyzer',
	version='v0.4.0',
	url='https://github.com/EvanMurawski/BeamAnalyzer',
	license='MIT',
	author='Evan Murawski',
	package_dir = {'': 'beamanalyzer'},
	packages=['frontend', 'backend'],
	options = {"py2exe": {"packages": ["beamanalyzer.frontend", "beamanalyzer.backend"]}},
	windows = ["beamanalyzer/guiinterface.py"])