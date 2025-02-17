# File: setup.py
# Date: 6-Oct-2018
#
# Update:
#
import re
import glob

from setuptools import find_packages
from setuptools import setup

packages = []
thisPackage = 'wwpdb.apps.ccmodule'

with open('wwpdb/apps/ccmodule/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


setup(
    name=thisPackage,
    version=version,
    description='wwPDB workflow engine utils',
    long_description="See:  README.md",
    author='Ezra Peisach',
    author_email='ezra.peisach@rcsb.org',
    url='https://github.com/rcsb/py-wwpdb_apps_wf_engine_utils',
    #
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': []
    },
    #
    # Also depends on 'openeye.oechem' but cannot install by pypi
    install_requires=['mmcif', 'mmcif.utils >= 0.13', 'wwpdb.utils.config ~= 0.24',
                      'wwpdb.utils.dp >= 0.11', 'rcsb.utils.multiproc',
                      'wwpdb.utils.wf',
                      'wwpdb.utils.session >= 0.2',
                      'mysqlclient',
                      "wwpdb.io >= 0.16.dev1"
                      ],
    packages=find_packages(exclude=['wwpdb.apps.tests_ccmodule']),
    package_data={
        # If any package contains *.md or *.rst ...  files, include them:
        '': ['*.md', '*.rst', '*.txt', '*.cfg']
    },
    #
    # These basic tests require no database services -
    test_suite="wwpdb.apps.tests_ccmodule",
    tests_require=['tox', 'wwpdb.utils.testing'],
    #
    # Not configured ...
    extras_require={
        'consumer': ['wwpdb.utils.oe_util >= 0.2'],
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'server': ['webob'],
    },
    # Added for
    command_options={
        'build_sphinx': {
            'project': ('setup.py', thisPackage),
            'version': ('setup.py', version),
            'release': ('setup.py', version)
        }
    },
    # This setting for namespace package support -
    zip_safe=False,
)
