import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypackage", 
    version="0.0.1",
    author="Yin-Ting Chou",
    author_email="yintingchou@gmail.com",
    description="A simple example arithmetic python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.0'
    ]
)