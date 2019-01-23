from setuptools import setup

setup(
    name='openexchangerates3',
    version='0.1.1',
    description='openexchangerates.org Python3 API client',
    long_description=open('README.rst').read(),
    url='https://github.com/lihan/openexchangerates3',
    license='MIT',
    author='Lihan Li',
    author_email='llihan673@gmail.com',
    packages=['openexchangerates'],
    install_requires=[
        'requests',
    ],
    tests_require=[
        'httpretty',
        'mock'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
