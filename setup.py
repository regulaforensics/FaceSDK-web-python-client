# coding: utf-8
import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="regula.facesdk.webclient",
    version=os.getenv("PACKAGE_VERSION_TO_PUBLISH", "5.1dev"),
    python_requires=">=3.5",
    description="Regula's FaceSDK web python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Regula Forensics, Inc.",
    author_email="support@regulaforensics.com",
    url="https://mobile.regulaforensics.com",
    keywords=["face recognition", "facesdk", "regulaforensics", "regula"],
    install_requires=[
        "certifi==2022.6.15.1",
        "six>=1.10",
        "python-dateutil>=2.5.3",
        "urllib3>=1.15.1"
    ],
    packages=find_packages(exclude=["test", "tests", "example"]),
    include_package_data=True,
)
