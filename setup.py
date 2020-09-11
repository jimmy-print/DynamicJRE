from setuptools import setup

setup(
    name="DynamicJRE",
    version="0.0",
    author="jimmy-print",
    description="Command line podcast downloader for The JRE",
    author_email="jimmy.wang123@outlook.sg",
    url="https://github.com/jimmy-print/DynamicJRE",
    license="MIT",
    packages=["dynamicjre"],
    entry_points={
        "console_scripts": ['jrep = dynamic_jre.jrep:main']
    },
    install_requires=["requests", "bs4", "lxml"],
)
