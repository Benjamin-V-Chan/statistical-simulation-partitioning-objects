import json
from partition_utils import generate_partition

def run_simulation(num_simulations, num_objects, alpha):
    results = []
    for sim in range(num_simulations):
        partition = generate_partition(num_objects, alpha)
        num_groups = len(partition)
        group_sizes = [len(group) for group in partition]
        results.append({
            'simulation': sim + 1,
            'num_groups': num_groups,
            'group_sizes': group_sizes
        })
    return results

if __name__ == '__main__':
    num_simulations = 1000
    num_objects = 50
    alpha = 1.0
    simulation_results = run_simulation(num_simulations, num_objects, alpha)
    with open('../outputs/simulation_results.json', 'w') as f:
        json.dump(simulation_results, f, indent=4)
    print("Simulation completed. Results saved to outputs/simulation_results.json")