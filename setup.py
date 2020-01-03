from setuptools import setup

with open('c_pyvizio/version.py') as f: exec(f.read())
with open('README.md', 'r') as myfile:
    longdescription=myfile.read()

setup(
    name='c_pyvizio',

    version=__version__,
    description='Python library for interfacing with Vizio SmartCast TVs and Sound Bars (2016+ models)',
    long_description=longdescription,
    long_description_content_type="text/markdown",
    url='https://github.com/cbishop76/c_pyvizio',

    author='Vlad Korniev',
    author_email='vladimir.kornev@gmail.com',

    license='GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],

    keywords='vizio smartcast',

    packages=["c_pyvizio"],

    install_requires=['click', 'requests', 'jsonpickle', 'xmltodict'],
    entry_points={
        'console_scripts': [
            'c_pyvizio=c_pyvizio.cli:cli',
        ],
    },
)
