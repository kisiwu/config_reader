import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="settings-novice",
    version="0.0.2",
    author="Kisiwu",
    author_email="sdemingongo@gmail.com",
    description="Small functions to read/add default settings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kisiwu/novice_config",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)