from setuptools import setup
setup (
	name="getend",
	version='0.2',
	py_modules=['main'],
	install_requires=[
		'Click',
		'colorama'
	],
	entry_points='''
		[console_scripts]
		endpoints=main:cli
	''',
)