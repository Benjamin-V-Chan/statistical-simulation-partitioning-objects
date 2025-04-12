#   1. Import necessary modules: json for file handling, statistics for computations.
#   2. Define load_simulation_results(filepath) to:
#         a. Open and load JSON simulation data.
#         b. Return the simulation data.
#   3. Define analyze_results(simulation_results) to:
#         a. Extract the number of groups from each simulation.
#         b. Compute statistical measures (mean, median, standard deviation) for:
#              i. The number of groups.
#             ii. The group sizes (after flattening all group sizes).
#         c. Package these measures in a summary dictionary.
#         d. Return the summary dictionary.
#   4. In the main block:
#         a. Load simulation results from the "../outputs/simulation_results.json" file.
#         b. Analyze the results.
#         c. Write the analysis summary to "../outputs/analysis_summary.txt".