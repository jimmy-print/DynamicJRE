from setuptools import setup

setup(
    name="DynamicJRE",
    version="0.0",
    description="Command line podcast downloader for The JRE",
    author_email="jimmy.wang123@outlook.sg",
    packages=["dynamic_jre"],
    entry_points={
        "console_scripts": ['jrep = dynamic_jre.jrep:main']
    },
    install_requirements=["requests", "bs4"],
)