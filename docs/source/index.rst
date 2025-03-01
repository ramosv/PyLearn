.. PyLearn-AI documentation master file

Welcome to the PyLearn-AI Documentation
====================================

PyLearn-AI is a pure-Python machine learning and deep learning framework built entirely with the Python standard library.
No external dependencies required.

Features
--------
- No dependencies (NO NumPy, SciPy, or Pandas) — just Python 3.10
- Supports basic machine learning and deep learning models
- Includes custom matrix and tensor operations
- Educational and easy to understand, encouraging users to learn the underlying functionality

.. note::
   The dependencies in ``requirements.txt`` are only for documentation, testing, and publishing.

Novelty
-------
PyLearn-AI does not use NumPy or any other external libraries.
At its core, the ``UnitFrame`` data structure assists with common matrix operations.

Usage
-----
.. code-block:: python

    from pylearn.core.unitframe import UnitFrame

    uf = UnitFrame([[1, 2], [3, 4]])
    print(uf)

Project Structure
-----------------
.. code-block:: text

    PyLearn-AI/
    ├── core/           # Core algorithms, structures, and tensor class
    ├── neural/         # Deep learning models (MLP, CNN, GNN)
    ├── reinforcement/  # Reinforcement learning (Q-learning, policy optimization)
    ├── supervised/     # Supervised learning (regression, classification)
    ├── unsupervised/   # Clustering, dimensionality reduction
    ├── utils/          # Activations, losses, metrics, and preprocessing

License
-------
This project is licensed under the MIT License. See :doc:`../../LICENSE`.
