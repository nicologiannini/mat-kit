import setuptools

with open("README.md", "r") as d:
    long_description = d.read()

setuptools.setup(
    name="minimat",
    version="0.1.0",
    author="Nicolò Giannini",
    author_email="nicogiannini@yahoo.com",
    description="A tiny matrix library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicologiannini/minimat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6',
)