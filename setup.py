from setuptools import setup
from setuptools import find_packages
from os import path
from sphinx.setup_command import BuildDoc

name = 'pylecroy'
version = '0.1.1'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name=name,
      version=version,
      cmdclass={'build_sphinx': BuildDoc},
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'source_dir': ('setup.py', 'docs/source')
          }
      },
      description='Lecroy oscilloscope driver',
      long_description=long_description,
      long_description_content_type='text/markdown',

      classifiers=[
        'License :: OSI Approved ::  Massachusetts Institute of Technology (MIT)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Device driver',
        'Intended Audience :: Developers',
      ],

      entry_points={
          'console_scripts': ['lecroy_info = bin.lecroy_info:main'],
      },

      keywords='lecroy',
      
      url='https://git.ul-ts.com/ims-se/hardware-team/pybench/pylecroy',
      author='Laurent Bonnet',
      author_email='laurent.bonnet@ul.com',
      python_requires='>=3.6',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy', 'pywin32==300', 'matplotlib'],
      zip_safe=False)
