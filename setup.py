import setuptools

setuptools.setup(
    name="dump_xml",
    version="0.1.0",
    url="https://github.com/intouch-smartwater/dump_xml",

    author="James Cheese",
    author_email="james.cheese@intouch-ltd.com",

    description="A simple dictionary to XML converter that "Just Works".",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
