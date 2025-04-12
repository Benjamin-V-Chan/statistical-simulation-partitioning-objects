# This module contains the utility function to generate a random partition
#
# FUNCTION generate_partition(num_objects, alpha):
#   Input:
#       - num_objects: Total number of objects to partition.
#       - alpha: Concentration parameter controlling the chance to start a new group.
#
#   Process:
#       1. Initialize an empty list "groups" to hold the partition.
#       2. Iterate over each object (by index):
#           a. If no groups exist yet, create the first group with the object.
#           b. If groups already exist:
#               i. For each group, assign a weight equal to its current size.
#              ii. Include an additional weight (alpha) for the possibility to start a new group.
#             iii. Compute the normalized probabilities from these weights.
#              iv. Draw a random number; based on the cumulative probabilities:
#                  - If an existing group is chosen, append the object to that group.
#                  - Otherwise, create a new group with the object.
#       3. Return the list "groups" representing the partition.
# END FUNCTION
