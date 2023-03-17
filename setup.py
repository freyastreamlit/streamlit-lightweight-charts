import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-lightweight-charts",
    version="0.7.2",
    author="Joe Rosa",
    author_email="joe.rosa@itpmngt.co.uk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    description="streamlit-lightweight-charts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/freyastreamlit/streamlit-lightweight-charts",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.62",
    ],
)
