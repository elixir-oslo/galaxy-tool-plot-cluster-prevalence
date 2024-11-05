# galaxy-tool-plot-cluster-prevalence

## Overview
`galaxy-tool-plot-cluster-prevalence` is a Python-based tool designed to plot the prevalence of clusters over samples from the TSV output of PyClone-VI. This tool can be integrated into the Galaxy platform using the provided XML configuration.

## Features
- Reads TSV output from PyClone-VI.
- Plots cluster prevalence over samples using `pandas`, `matplotlib`, and `seaborn`.
- Generates area and line plots to visualize the data.
- Can be integrated into the Galaxy platform.

## Requirements
- Python 3.x
- `pandas` (version 1.2.5)
- `matplotlib` (version 3.4.3)
- `seaborn` (version 0.11.2)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/galaxy-tool-plot-cluster-prevalence.git
    cd galaxy-tool-plot-cluster-prevalence
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To run the tool locally, use the following command:
```sh
python plot_clusters_prevalence.py --input_file path/to/your/input_file.tsv
```

## Galaxy Integration
To integrate this tool into the Galaxy platform, use the provided `plot_clusters_prevalence.xml` file. This XML file defines the tool's configuration, including its requirements, inputs, outputs, and command to execute.

### Steps to Integrate:
1. Place the `plot_clusters_prevalence.xml` file in the appropriate tools directory of your Galaxy instance.
2. Ensure the `plot_clusters_prevalence.py` script is accessible to the Galaxy tool configuration.
3. Restart your Galaxy instance to recognize the new tool.

## Example
Here is an example command to run the tool:
```sh
python plot_clusters_prevalence.py --input_file example_data.tsv
```
