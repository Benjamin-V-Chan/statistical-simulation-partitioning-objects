import json
import statistics

def load_simulation_results(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_results(simulation_results):
    num_groups_list = [res['num_groups'] for res in simulation_results]
    mean_groups = statistics.mean(num_groups_list)
    median_groups = statistics.median(num_groups_list)
    stdev_groups = statistics.stdev(num_groups_list) if len(num_groups_list) > 1 else 0

    all_group_sizes = []
    for res in simulation_results:
        all_group_sizes.extend(res['group_sizes'])
    mean_group_size = statistics.mean(all_group_sizes)
    median_group_size = statistics.median(all_group_sizes)
    stdev_group_size = statistics.stdev(all_group_sizes) if len(all_group_sizes) > 1 else 0

    summary = {
        'total_simulations': len(simulation_results),
        'mean_num_groups': mean_groups,
        'median_num_groups': median_groups,
        'stdev_num_groups': stdev_groups,
        'mean_group_size': mean_group_size,
        'median_group_size': median_group_size,
        'stdev_group_size': stdev_group_size
    }
    return summary

if __name__ == '__main__':
    results = load_simulation_results('../outputs/simulation_results.json')
    analysis = analyze_results(results)
    with open('../outputs/analysis_summary.txt', 'w') as f:
        for key, value in analysis.items():
            f.write(f"{key}: {value}\n")
    print("Analysis completed. Summary saved to outputs/analysis_summary.txt")