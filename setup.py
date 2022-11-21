from setuptools import find_packages, setup

setup(
    name='Tyclonie Logger',
    packages=find_packages(),
    version='1.0',
    description='A library designed to make logging easy. Well formatted and a lovely replacement to just print.',
    author='Tyclonie',
    license='MIT',
    setup_requires=["colorama==0.4.6"]
)
