from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="goddess",
    version="1.4",
    description="Fully automated offensive security framework for reconnaissance and vulnerability scanning",
    long_description=long_description,
    author="j3ssie",
    author_email="j3ssiejjj@gmail.com",
    url="https://www.twitter.com/j3ssiejjj",
    download_url="https://github.com/cantix/goddes",
    packages=find_packages(),
    include_package_data=True,
    scripts=('goddess.py',),
    entry_points={},
    install_requires=[
        "Flask",
        "Flask-Cors",
        "Flask-Jsonpify",
        "Flask-JWT",
        "Flask-JWT-Extended",
        "Flask-RESTful",
        "requests",
        "ansi2html",
    ],
    extras_require={
        "tests": [
            "pytest",
        ],
    },
    classifiers=[
        "Operating System :: POSIX",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
)
