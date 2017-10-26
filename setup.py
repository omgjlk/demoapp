from setuptools import setup

setup(name='demoapp',
      version='0.1',
      description='A demo webserver app',
      author='Jesse Keating',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['demoapp'],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['demoapp=demoapp:run'],
      }
)
