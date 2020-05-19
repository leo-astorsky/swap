from setuptools import setup


setup(
    name='swap',
    version='0.0.2',
    py_modules=['swap'],
    entry_points={
        'console_scripts': ['swap=swap:main'],
    }
)
