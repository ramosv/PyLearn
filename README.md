# PyLearnLite  

**PyLearnLite** is a pure-Python machine learning and deep learning framework built entirely with the Python standard library. No external dependencies required.  

## Features  
- No dependencies—just Python  
- Supports basic machine learning and deep learning models  
- Includes custom matrix and tensor operations  
- Educational and easy to understand
  
Note: requirements.txt related dependencies are for documentation, testing and package publishing.

## Installation  
```bash
pip install pylearnlite
```

## Usage  
```python
from pylearnlite.core.unitframe import UnitFrame

# simple matrix example
uf = UnitFrame([[1, 2], [3, 4]])
print(uf)
```

## Project Structure  
```plaintext
pylearnlite/
├── core/           # Core algorithms, structures, and tensor class
├── neural/         # Deep learning models (MLP, CNN, GNN)
├── reinforcement/  # Reinforcement learning (Q-learning, policy optimization)
├── supervised/     # Supervised learning (regression, classification)
├── unsupervised/   # Clustering, dimensionality reduction
├── utils/          # Activations, losses, metrics, and preprocessing
```

## License  
[MIT License](/LICENSE)  
