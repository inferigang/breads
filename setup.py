from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent

setup(
    name='breads-ad',
    version='1.1.1',
    author='oppsec',
    author_email='opps3c@gmail.com',
    description='Breaking Active Directory Security (BREADS) is a tool design to attack Active Directory environments',
    readme='README.md',
    long_description = (this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/inferigang/breads',

    install_requires=[
        'python-ldap >= 3.4.4',
        'rich >= 13.5.3',
        'requests >= 2.31.0'
    ],

    packages=find_packages(),

    entry_points = {
        'console_scripts': [
            'breads-ad = src.main:BreadsPrompt.cmdloop',
        ],
    },

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10.12',
)
