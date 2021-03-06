# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from codecs import open  # To use a consistent encoding
from os import path
import sys

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


class PyTest(TestCommand):

    """ Entry point for py.test that allows 'python setup.py test'
    to work correctly
    """

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=long_description,

    # The project's main homepage.
    url='{{ cookiecutter.project_homepage }}',

    # Author details
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',

    # Choose your license
    license='{{ cookiecutter.license }}',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: ',
        'Topic :: Todo :: Todo',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: {{ cookiecutter.license }}',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['tests']),

    include_package_data=True,

    cmdclass={'tests': PyTest},

    platforms='any',

    test_suite='tests.test_{{ cookiecutter.repo_name }}',

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=[
        'future',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [
            'bumpversion',
            'check-manifest',
            'ipython',
            'ipdb',
            'pylama',
            'black',
            'sphinx',
            'sphinx_rtd_theme',
            'wheel',
        ],
        'test': [
            {%if cookiecutter.enable_coverage%}'coverage',{%endif%}
            'pylama',
            'pytest',
            {%if cookiecutter.enable_coverage%}'pytest-cov',{%endif%}
            'pytest-sugar',
            {%if cookiecutter.enable_tox%}'tox',{%endif%}
        ],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here using relative paths:
    package_data={
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # Delete either or both of these if not required (and remove the corresponding imports in the package __init__.py
    entry_points={
        {%if cookiecutter.enable_entry_points%}
        'console_scripts': ['{{ cookiecutter.cli_script_name }} = {{ cookiecutter.repo_name }}:{{ cookiecutter.cli_entry_point_function_name }}',],
        'gui_scripts': ['{{ cookiecutter.gui_script_name }} = {{ cookiecutter.repo_name }}:{{ cookiecutter.gui_entry_point_function_name }}',],
        {%endif%}
    },

    # Is your project zip safe?
    # zip_safe=True,
)
