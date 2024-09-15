Introduction
============

``Image Transform Library`` is a library for performing transforms and inverse transforms to/from images within Python.

The goal of this library is to provide a modular and easily expandable codebase for computing transforms and inverse transforms for 3D data sets, specifically images.

Currently, the library has support for cartesian coordinate images (X & Y), polar coordinate images (R & theta), Zernike polynomial transforms, and discrete Fourier transforms.

Installation
============

The dependencies for this project can be installed by running ``pip install -r requirements.txt``.

All the library modules and classes are available under ``src``. To use, simply download and extract the files to your desired directory.

No driver code is supplied with this library, the documentation for all the modules and classes are available under the further Sphinx documentation.

Documentation
=============

This library comes with further documentation of the included modules and classes using the Sphinx extension. To generate html documentation, run ``docs\make html``, and open the generated file ``docs\_build\html\index.html``.
