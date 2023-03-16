import setuptools

setuptools.setup(
    name="streamlit-lightweight-charts",
    version="0.7.0",
    author="Joe Rosa",
    author_email="joe.rosa@itpmngt.co.uk",
    description="streamlit-lightweight-charts",
    long_description="Wrapper for TradingView lightweight-charts",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
