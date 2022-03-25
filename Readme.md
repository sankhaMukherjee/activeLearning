# activeLearning

This package contains routines for active learning. This package is expected to be library
agnostic and easy to use. It will contain several algorithms and will be upgraded as
necessary.

## Prerequisites

You will need to have a valid Python installation on your system. This has been tested with Python 3.6 - 3.9. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development 
and testing purposes. Detailed documentation is present [here](https://sankhamukherjee.github.io/activeLearning/).

### Package Installation

This is the repository is meant to be used for installing the activeLearning package. 
A wheel dstribution of this package is present in the [`dist`](../master/dist) folder and may be 
installed within your virtual enviroonment. Just download this directly into your folder and install 
like any other pip package as:

`pip3 install activeLearning-<version>-py3-none-any.whl`

Git alternatively allows you to install packages directly from Github. Consider doing the following:

`pip3 install git+https://github.com/sankhaMukherjee/activeLearning.git`

This has been built upon a Unix system. If you use this for other systems, you 
may wish to consider building this library from source.  If this is a 
provate repo, or you use ssh, remember to use the following instead:

`pip3 install git+ssh://git@github.com/sankhaMukherjee/activeLearning.git`

### Package Building

You may wish to make customize this package for your own use. For that, you need to build the system:

 - Clone this repo to your computer
 - Install a virtual enviromnent, and istall the required packages
 - Buid the system

 A `Makefile` has been provided for aiding with this process. The following commands should allow you do do the following

  - `make grantPermission`: grants execute permission to all shell scripts in the [`bin`](../master/bin) folder
  - `make clean`: clean unwanted and temporary files that are generated
  - `make build`: This will allow you to build Wheel packages for your system

## Contributing

Please make any changes/updates in a new branch, and then send in a pull request. When you incorporate new
changes to the repo, please consider updating the documentation including creating some examples and some
tutorials that will allow users to properly use this repo.

Furthermore, it is very useful to create unit tests for your package. This is going to allow you to generate
high-quality packages that will have lower failure-rates in the real world.

There is a Makefile that will aid you in the process.

  - `make docs`: automatically generate the documentation after making changes to it. 
  - `make tests`: will allow you to run unit tests

Additionally, if `tox` is properly installed on your system, you can use it to test across multiple
Python installed versions just by issuing the `tox` command. 

## Authors

Sankha S. Mukherjee - Initial work (2022)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

 - Hat tip to anyone who's code was used
 - Inspiration
 - etc.
 