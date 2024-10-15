# Sample test code
import numpy as np
import pandas as pd

from bcsl.bcsl import BCSL


# Sample test code
if __name__ == '__main__':
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

