# statistical-simulation-partitioning-objects

## Project Overview

This project simulates the random partitioning of $n$ indistinguishable objects into distinguishable non-empty groups using a process inspired by the **Chinese Restaurant Process (CRP)**. It is particularly useful in statistical clustering, nonparametric Bayesian inference, and combinatorial stochastic processes.

Each object chooses to either join an existing group or form a new group based on probabilistic rules influenced by a concentration parameter $\alpha > 0$. The process generates a distribution over all possible partitions of the set $\{1, 2, ..., n\}$.

## Folder Structure

```
project-root/
├── scripts/
│   ├── partition_utils.py           # Core function for generating partitions
│   ├── 01_generate_partitions.py    # Demonstrates one random partition
│   ├── 02_run_simulation.py         # Runs and logs multiple simulations
│   ├── 03_analyze_results.py        # Computes statistics from results
│   └── 04_visualize_results.py      # Plots distribution of partitions
├── outputs/
│   ├── simulation_results.json      # JSON of simulation outputs
│   ├── analysis_summary.txt         # Summary stats
│   ├── num_groups_histogram.png     # Histogram of group counts
│   └── group_sizes_histogram.png    # Histogram of group sizes
└── requirements.txt                 # Dependencies
```
