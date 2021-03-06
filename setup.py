from setuptools import setup

setup(name='cosub',
      version='0.1',
      description='A tool for managing external HITs on Mechanical Turk',
      author='Long Ouyang',
      author_email='long.ouyang@gmail.com',
      url='http://www.github.com/longouyang/cosub',
      packages=['cosub'],
      install_requires = ['boto >= 2.33.0','pytimeparse >= 1.1.2'],
      entry_points = {
        'console_scripts': [
          'cosub = cosub.runner:go'
        ]
      }
)
