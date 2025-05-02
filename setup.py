from setuptools import setup, find_packages

setup(
    name="pomodoro",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tkinter",
    ],
    entry_points={
        "console_scripts": [
            "pomodoro=pomodoro.__main__:main",
        ],
    },
    author="Thomas Raes",
    author_email="raes.thomas@gmail.com",
    description="A study timer application built with Python and Tkinter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/traes008/pomodoro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
) 