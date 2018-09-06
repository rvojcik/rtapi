from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="racktables-api",
    version="0.2.5",
    packages=["rtapi"],
    license="GPLv2",
    description="Simple racktables API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rvojcik/rtapi",
    author="Robert Vojcik",
    author_email="robert@vojcik.net",
    keywords=['rtapi', 'racktables', 'racktables api', 'racktables-api','racktables cli','racktables-cli'],
    classifiers=[
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Topic :: Database"
    ]
)


