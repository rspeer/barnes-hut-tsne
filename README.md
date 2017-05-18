Barnes-Hut t-SNE for Python
===========================

This is a fork of a fork of a fork. I have not looked at most of the code
in this repository, I just use it.

This project, also known as "Python-TSNE", may be the only working Python 3
implementation of Barnes-Hut t-SNE. It's a sadly unloved project, perhaps
because everyone expects it to be superseded by scikit-learn any day now.

But, as of May 2017, scikit-learn's t-SNE has a bug that causes it to get no
benefit from Barnes-Hut; it uses as much space as plain t-SNE, and runs out of
memory on moderately large data. So, given that:

- [osdf](https://github.com/osdf/py_bh_tsne) made a Cython wrapper of the
  original C++ code by L. J. P. van der Maaten.
- [danielfrg](https://github.com/danielfrg/tsne) made it into a Python package
  that could be installed with `pip`, using a GitHub URL.
- [alexisbcook](https://github.com/alexisbcook/tsne) fixed namespace problems
  that were causing danielfrg's package to fail to import in some situations.
- I made alexisbcook's version into a package on PyPI with a coherent version
  number, so that other code can depend on it.

I have no intention of continuing to maintain this project. If something
about it doesn't quite work for you, I suggest you continue the tradition and
make your own fork.


Requirements
------------

* [numpy](numpy.scipy.org) > =1.7.1
* [scipy](http://www.scipy.org/) >= 0.12.0
* [cython](cython.org) >= 0.19.1
* [cblas](http://www.netlib.org/blas/) or [openblas](https://github.com/xianyi/OpenBLAS).

[Anaconda](http://continuum.io/downloads) is one way to get these requirements. (I don't use it myself.)

Installation
------------

The point of this particular fork is to be installable through PyPI:

```
pip install barnes-hut-tsne
```

Usage
-----

Basic usage:

```
from tsne import bh_sne
X_2d = bh_sne(X)
```

I found this docstring:

```
bh_sne(data)
Run Barnes-Hut T-SNE on _data_.

@param data         The data.

@param pca_d        The dimensionality of data is reduced via PCA
                    to this dimensionality.

@param d            The embedding dimensionality. Must be fixed to
                    2.

@param perplexity   The perplexity controls the effective number of
                    neighbors.

@param theta        If set to 0, exact t-SNE is run, which takes
                    very long for dataset > 5000 samples.

@param random_state A numpy RandomState object; if None, use
                    the numpy.random singleton. Init the RandomState
                    with a fixed seed to obtain consistent results
                    from run to run.

@param copy_data    Copy the data to prevent it from being modified
                    by the C code

```

### Examples

* [Iris](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/iris.ipynb)
* [MNIST](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/mnist.ipynb)

More Information
----------------

See *Barnes-Hut-SNE* (2013), L.J.P. van der Maaten. It is available on [arxiv](http://arxiv.org/abs/1301.3342).
