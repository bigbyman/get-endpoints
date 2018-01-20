from setuptools import setup
setup (
	name="get-endpoints",
	version='0.2',
	py_modules=['main'],
	install_requires=[
		'Click',
		'colorama'
	],
	entry_points='''
		[console_scripts]
		getend=main:cli
	''',
)