# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
from setuptools import find_packages, setup

req = "requirements.txt"
dev_requirements = [
    "bandit",
    "flake8",
    "isort",
    "pytest",
    "pytest-cov",
    *open(req, "r").read().split("\n"),
]
test_requirements = ["pytest", *open(req, "r").read().split("\n")]
run_requirements = [
    *dev_requirements,
    *open(req, "r").read().split("\n"),
]

with io.open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setup(
    name="sc_ride",
    version="0.0.1",
    author="Lucas Althoff",
    author_email="ls.althoff@gmail.com",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    url="https://github.com/lucas-althoff/smartcity_ride",
    license="COPYRIGHT",
    description="API com modelo para Cidades Inteligentes MMSISB",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
        "dev": dev_requirements,
        "unit": test_requirements},
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=(),
    entry_points={
        "console_scripts": ["src = src.__main__:start"],
    }
    )
