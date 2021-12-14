from setuptools import setup, find_packages

setup(
    name='galicsource',
    version='0.1',
    packages=find_packages(include=['src/galicsauce']),
    url='',
    license='MIT',
    author='nov11',
    author_email='',
    description='various code snippets',
    install_requires=[
        'pandas',
        'numpy'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
