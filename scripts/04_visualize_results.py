#   1. Import json for reading simulation results and matplotlib for plotting.
#   2. Define load_simulation_results(filepath) to load JSON simulation data.
#   3. In the main block:
#         a. Load the simulation results from "../outputs/simulation_results.json".
#         b. Extract the number of groups from each simulation into a list.
#         c. Also build a flat list of all group sizes.
#         d. Create a histogram for the number of groups:
#               - Set title, labels, and save the plot to "../outputs/num_groups_histogram.png".
#         e. Create a histogram for the group sizes:
#               - Set title, labels, and save the plot to "../outputs/group_sizes_histogram.png".