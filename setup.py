import setuptools

setup(name='AsciiArt',
    version='0.1.dev',
    description='Ascii "art" from images',
    author='clara',
    packages=find_packages(exclude=['tests']),
    install_requires=['pillow'])
