from examples.easy import compare_easy_dataset
from examples.hard import compare_hard_dataset

if __name__ == "__main__":
    """
    Compare the easy and hard datasets using the BCSL algorithms vs FCI.
    """
    num_bootstrap_samples = 10
    bootstrap_all_edges = True
    conditional_independence_method = (
        "fisherz"  # KCI too slow for hard dataset or too many bootstrap samples
    )
    compare_easy_dataset(
        num_bootstrap_samples,
        conditional_independence_method,
        bootstrap_all_edges=bootstrap_all_edges,
    )
    num_bootstrap_samples = 100
    conditional_independence_method = (
        "fisherz"  # KCI too slow for hard dataset or too many bootstrap samples
    )
    compare_easy_dataset(
        num_bootstrap_samples,
        conditional_independence_method,
        bootstrap_all_edges=bootstrap_all_edges,
    )
    # num_bootstrap_samples = 10
    # conditional_independence_method = (
    #     "kci"  # KCI too slow for hard dataset or too many bootstrap samples
    # )
    compare_easy_dataset(num_bootstrap_samples, conditional_independence_method)
    exit(1)
    compare_hard_dataset(num_bootstrap_samples, conditional_independence_method)

    num_bootstrap_samples = 10
    conditional_independence_method = "kci"
    compare_easy_dataset(num_bootstrap_samples, conditional_independence_method)
