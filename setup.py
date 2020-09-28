#!/usr/bin/env python

from setuptools import setup

ver_dic = {}
version_file = open("logpyle/version.py")
try:
    version_file_contents = version_file.read()
finally:
    version_file.close()

exec(compile(version_file_contents, "logpyle/version.py", 'exec'), ver_dic)

setup(name="logpyle",
      version=ver_dic["VERSION_TEXT"],
      description="Time series logging for Python",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Other Audience',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          ],

      python_requires='~=3.6',

      install_requires=[
          "six>=1.8.0",
          "pytools>=2011.1"
      ],

      package_data={"logpyle": ["py.typed"]},
      scripts=[
          "bin/logtool",
          "bin/runalyzer-gather",
          "bin/runalyzer",
      ],

      author="Andreas Kloeckner",
      url="http://pypi.python.org/pypi/logpyle",
      author_email="inform@tiker.net",
      license="MIT",
      packages=["logpyle"])
