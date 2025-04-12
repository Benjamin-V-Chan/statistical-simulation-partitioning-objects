from partition_utils import generate_partition

if __name__ == '__main__':
    num_objects = 20
    alpha = 1.0
    partition = generate_partition(num_objects, alpha)
    print("Generated Partition:")
    for idx, group in enumerate(partition):
        print(f"Group {idx+1}: {group}")