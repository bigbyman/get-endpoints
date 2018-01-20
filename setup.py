from setuptools import setuptools
setup (
	name="endpoints",
	version='0.2'
	py_modules=['main.py'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		endpoints=main:cli
	''',
)