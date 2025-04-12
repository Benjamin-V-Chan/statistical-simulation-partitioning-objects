import json
import matplotlib.pyplot as plt

def load_simulation_results(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

if __name__ == '__main__':
    results = load_simulation_results('../outputs/simulation_results.json')
    num_groups_list = [res['num_groups'] for res in results]
    all_group_sizes = []
    for res in results:
        all_group_sizes.extend(res['group_sizes'])
    
    plt.figure()
    plt.hist(num_groups_list, bins=20, edgecolor='black')
    plt.title('Histogram of Number of Groups per Simulation')
    plt.xlabel('Number of Groups')
    plt.ylabel('Frequency')
    plt.savefig('../outputs/num_groups_histogram.png')
    plt.close()
    
    plt.figure()
    plt.hist(all_group_sizes, bins=20, edgecolor='black')
    plt.title('Histogram of Group Sizes across Simulations')
    plt.xlabel('Group Size')
    plt.ylabel('Frequency')
    plt.savefig('../outputs/group_sizes_histogram.png')
    plt.close()
    
    print("Visualizations created. Check outputs folder for plots.")