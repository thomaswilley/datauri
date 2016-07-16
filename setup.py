from setuptools import setup

version = __import__('django').get_version()


setup(
    name='datauri',
    version='0.1.0',
    url='https://github.com/thomaswilley/datauri',
    author='@thomaswilley',
    description=('Convert a file into a Data URI in python3 w/no other dependencies.'),
    license='MIT',
    scripts=['datauri.py'],
    entry_points={'console_scripts': [
        'datauri = datauri:main',
    ]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
