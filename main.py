from examples.easy import compare_easy_dataset
from examples.hard import compare_hard_dataset

if __name__ == "__main__":
    """
    Compare the easy and hard datasets using the BCSL algorithms vs FCI.
    """
    params = {
        "num_bootstrap_samples": 10,
        # KCI too slow for hard dataset or too many bootstrap samples
        "conditional_independence_method": "fisherz",
        "bootstrap_all_edges": True,
        "multiple_comparison_correction": "bonferroni",  # "fdr" or "bonferroni"
    }
    compare_easy_dataset(**params)
    compare_hard_dataset(**params)

    params["num_bootstrap_samples"] = 100
    compare_easy_dataset(**params)
    compare_hard_dataset(**params)

    params["num_bootstrap_samples"] = 10
    params["conditional_independence_method"] = "kci"
    compare_easy_dataset(**params)
