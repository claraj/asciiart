import setuptools

setup(name='AsciiArt',
    version='1.0.dev',
    description='Ascii "art" from images',
    author='clara',
    classifiers=['Development Status :: 3 - Alpha',
        Programming Language :: Python :: 3.4],
    packages=find_packages(exclude=['tests']),
    install_requires=['pillow'])
