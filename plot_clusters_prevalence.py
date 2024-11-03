import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main(input_file):
    # Load PyClone-VI results
    df = pd.read_csv(input_file, sep='\t')

    clusters = df['cluster_id'].unique()
    samples = df['sample_id'].unique()
    prevalence = []

    # Move data to a more plot-friendly format
    for sample in samples:
        sample_prevalence = []
        for cluster in clusters:
            prevalence_value = df[(df['sample_id'] == sample) & (df['cluster_id'] == cluster)]['cellular_prevalence'].sum()
            sample_prevalence.append(prevalence_value)
        prevalence.append(sample_prevalence)

    prevalence_df = pd.DataFrame(prevalence, columns=[f'Cluster {c}' for c in clusters], index=samples)

    # Plot the Fish Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    prevalence_df.plot(kind='area', ax=ax, cmap='Spectral', alpha=0.8)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=prevalence_df, markers=True, dashes=False, ax=ax)

    ax.set_title('Cluster Prevalence Over Samples')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Cellular Prevalence')
    plt.xticks(rotation=45)
    plt.legend(title='Clusters')

    # Save plot to output file (ensure it's a png)
    output_file = 'output.png'
    plt.savefig(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot the prevalence of clusters over samples from the TSV output of PyClone-VI.')
    parser.add_argument('--input_file', required=True, help='Path to the input TSV file')

    args = parser.parse_args()
    print(args)
    main(args.input_file)
