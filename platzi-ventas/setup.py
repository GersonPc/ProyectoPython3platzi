from setuptools import setup

setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)