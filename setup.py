from setuptools import setup, find_packages
setup(
    name='datavalidator',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Chidimma Ijoma',
    author_email='nevusijoma@gmail.com',
    description='A simple data validation package'
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Data-Epic/data-validator-chidimma-ijoma",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Use the correct classifier
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",  # Specify the license here
)