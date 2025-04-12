#   1. Import generate_partition from partition_utils.py.
#   2. Define a function run_simulation(num_simulations, num_objects, alpha) that:
#         a. Initializes an empty list "results".
#         b. For each simulation iteration:
#              i. Generate a partition.
#             ii. Count the number of groups.
#            iii. Record the sizes of each group.
#             iv. Save the simulation data (e.g., simulation number, number of groups, group sizes) into the results list.
#         c. Return the complete results list.
#   3. In the main block:
#         a. Set parameters (num_simulations, num_objects, alpha).
#         b. Run the simulation.
#         c. Save the results as a JSON file to the "../outputs/" folder.