from setuptools import setup
from setuptools import find_packages

setup(name='pylecroy',
      version='0.1.0',
      
      description='Lecroy oscilloscope driver',
      long_description=open('README.md').read(),
      
      classifiers=[
        'License :: OSI Approved ::  Massachusetts Institute of Technology (MIT)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Device driver',
        'Intended Audience :: Developers',
      ],
      
      keywords='lecroy',
      
      url='https://git.ul-ts.com/ims-se/hardware-team/pybench/pylecroy',
      author='Laurent Bonnet',
      author_email='laurent.bonnet@ul.com',
      python_requires='>=3.6',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy', 'pywin32', 'matplotlib'],
      zip_safe=False)
