import random

def generate_partition(num_objects, alpha=1.0):
    groups = []
    for i in range(num_objects):
        if not groups:
            groups.append([i])
        else:
            weights = [len(group) for group in groups] + [alpha]
            total_weight = sum(weights)
            probabilities = [w / total_weight for w in weights]
            r = random.random()
            cum_prob = 0.0
            for j, p in enumerate(probabilities):
                cum_prob += p
                if r < cum_prob:
                    chosen_index = j
                    break
            if chosen_index < len(groups):
                groups[chosen_index].append(i)
            else:
                groups.append([i])
    return groups