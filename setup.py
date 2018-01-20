from setuptools import setup
setup (
	name="endpoints",
	version='0.2',
	py_modules=['main'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		endpoints=main:cli
	''',
)