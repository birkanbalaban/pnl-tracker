from setuptools import setup, find_packages

setup(
    name="binance-pnl-tracker",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'openpyxl',
        'plyer',
        'python-binance',
        'configparser',
        'tkinter',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Binance Futures PNL tracking application",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/binance-pnl-tracker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
) 