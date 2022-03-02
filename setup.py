import setuptools
import platform

platform_system = platform.system()

setuptools.setup(
    name="testpypi",
    version=1.0,
    author="Matthew Brady",
    author_email="mbrad@synopsys.com",
    description="description",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/matthewb66/test_pyinstaller_multi",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    entry_points={
        'console_scripts': ['testpypi=main:main'],
    },
)
