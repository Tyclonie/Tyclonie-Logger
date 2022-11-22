from setuptools import find_packages, setup
from pathlib import Path

setup(
    name='TyclonieLogger',
    packages=find_packages(),
    version='1.1',
    description='A library designed to make logging easy. Well formatted and a lovely replacement to just print.',
    author='Tyclonie',
    license='MIT',
    install_requires=["colorama==0.4.6"],
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown"
)
