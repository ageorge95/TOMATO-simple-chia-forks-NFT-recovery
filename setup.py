from setuptools import setup

setup(
    name="TOMATO",
    packages=[],
    entry_points={
        "console_scripts": [
            "tomato = basket.CLI:main"
        ]
    },
    version=open("basket/version.txt", "r").readline()
)