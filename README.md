# BCSL Python

Python port of the Bootstrap-based Causal Structure Learning Algorithm. Depends on the causal-learn package for scoring.


## Installation

```bash
pip install bcsl-python causal-learn
```

## Usage

```python
import numpy as np

from bcsl import BCSL

# Generate synthetic data for testing
n_samples = 200

# Independent variables
Var1 = np.random.normal(0, 1, n_samples)
Var2 = np.random.normal(0, 1, n_samples)

# Dependent variables
Var3 = 2 * Var1 + np.random.normal(0, 1, n_samples)  # Var3 depends on Var1
Var4 = 0.5 * Var2 + np.random.normal(0, 1, n_samples)  # Var4 depends on Var2
Var5 = (
        Var3 + Var4 + np.random.normal(0, 1, n_samples)
)  # Var5 depends on Var3 and Var4
data = pd.DataFrame(
    {"Var1": Var1, "Var2": Var2, "Var3": Var3, "Var4": Var4, "Var5": Var5}
)
bcsl = BCSL(data, use_causal_learn=True, num_bootstrap_samples=4)

# Step 1: Learn local skeletons using HITON-PC
local_skeletons = bcsl.learn_local_skeleton()
print("Local Skeletons:", local_skeletons)

# Step 2: Resolve asymmetric edges using bootstrap
global_skeleton = bcsl.resolve_asymmetric_edges()
print("Global Skeleton (resolved):", global_skeleton)

# Step 3: Orient edges using BDeu and hill-climbing
dag = bcsl.orient_edges()
print("Final DAG:", dag)
```

## Reference
G. Xiang, H. Wang, K. Yu, X. Guo, F. Cao and Y. Song, "Bootstrap-Based Layerwise Refining for Causal Structure Learning," in IEEE Transactions on Artificial Intelligence, vol. 5, no. 6, pp. 2708-2722, June 2024, doi: 10.1109/TAI.2023.3329786.