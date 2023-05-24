from setuptools import setup

setup(
    name='makarenko-serializer',
    version='0.1.0',
    packages=['makarenko_serializer'],
    entry_points={
        "console_scripts": [
            "makarenko_serializer = makarenko_serializer.makarenko_serializer:main"
        ]
    },
    author='alyona makarenko',
)
