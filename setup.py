from setuptools import setup, find_packages

setup(
    name='breads-ad',
    version='1.0.3b',
    author='oppsec (inferigang)',
    author_email='opps3c@gmail.com',
    description='Breaking Active Directory Security (BREADS) is a tool design to attack Active Directory environments',
    readme='README.md',
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