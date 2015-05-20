import os
from setuptools import setup
from distutils import sysconfig

site_packages_path = sysconfig.get_python_lib()

setup(
    name='pbs-python',
    packages=['pbs'],
    version='4.4.1',
    author='Radik Fattakhov',
    author_email='radikft@gmail.com',
    description='openpbs/torque python interface',
    keywords=['pbs'],
    data_files=[(site_packages_path, ['pbs.pth']), (os.path.join(site_packages_path, 'pbs'), ['_pbs.so'])],
    url='http://github.com/radik/pbs-python',
    license='LGPLv3',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Other',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'
    ],
    long_description='''\
This is pip-package of pbs_python 4.4.1 (http://oss.trac.surfsara.nl/pbs_python)
by  Bas van der Vlies (bas.vandervlies@surfsara.nl).
Native extensions from this package compiled on CentOS 6.5 with PBS Torque 5
installed on it and probably not compatible with other versions.
'''
)