# statistical-simulation-partitioning-objects

## Project Overview

This project simulates the random partitioning of $n$ indistinguishable objects into distinguishable non-empty groups using a process inspired by the **Chinese Restaurant Process (CRP)**. It is particularly useful in statistical clustering, nonparametric Bayesian inference, and combinatorial stochastic processes.

Each object chooses to either join an existing group or form a new group based on probabilistic rules influenced by a concentration parameter $\alpha > 0$. The process generates a distribution over all possible partitions of the set $\{1, 2, ..., n\}$.

### Mathematical Foundations

Let:
- $n$ = total number of objects (customers)
- $\alpha$ = concentration parameter
- $k$ = number of groups (tables) formed after $n$ objects are placed
- $C_i$ = the group assignment of object $i$

At step $i$, the probability of joining an existing group $j$ of size $n_j$ is:

$$P(C_i = j) = \frac{n_j}{\alpha + i - 1}$$

The probability of forming a new group is:

$$P(C_i = \text{new}) = \frac{\alpha}{\alpha + i - 1}$$

This defines a probability distribution over partitions known as the **Ewens sampling formula**:

$$P(n_1, ..., n_k) = \frac{\alpha^k}{\alpha^{(n)}} \prod_{j=1}^{k} (n_j - 1)!$$

where $n_j$ is the size of the $j$-th group, $k$ is the total number of groups, and $\alpha^{(n)} = \alpha (\alpha + 1) ... (\alpha + n - 1)$ is the rising factorial.

As $\alpha$ increases, the model prefers more groups. As $\alpha \to 0$, the process becomes deterministic and produces fewer partitions.

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

## Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 2. Generate a single partition (demonstration):
```bash
python scripts/01_generate_partitions.py
```

### 3. Run full simulation and save results:
```bash
python scripts/02_run_simulation.py
```

### 4. Analyze simulation results:
```bash
python scripts/03_analyze_results.py
```

### 5. Visualize simulation output:
```bash
python scripts/04_visualize_results.py
```

## Requirements

The project requires the following Python libraries:
- Python >= 3.8
- matplotlib
- statistics (built-in)
- json (built-in)
- random (built-in)

You can install all necessary packages with:
```bash
pip install -r requirements.txt
```