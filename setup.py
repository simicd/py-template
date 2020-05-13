import setuptools

# Get a long description from the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

# Get dependencies file and convert it to list of strings
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.1.0",
    author="Dejan Simic",
    author_email="Dejan.Simic",
    description="Python Package Template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=required
)
