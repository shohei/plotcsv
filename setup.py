from setuptools import setup

setup(name='plotcsv',
      version='0.1',
      description='Plot CSV with matplotlib',
      url='http://github.com/shohei/plotcsv',
      author='Shohei Aoki',
      author_email='shoaok@gmail.com',
      scripts=['bin/plotcsv'],
      install_requires=open('requirements.txt').read().splitlines(),
      license='MIT',
      packages=['plotcsv'],
      zip_safe=False)
