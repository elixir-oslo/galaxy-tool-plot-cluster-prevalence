import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def parse_events(events_str: str) -> dict:
    parts = events_str.split(",")
    dict_event = {}
    for i in range(0, len(parts) - 1, 2):
        event_id = parts[i]
        start_date = parts[i + 1]

        if not start_date.isdigit():
            raise ValueError(f"Invalid start_date: {start_date}. It must be a string of an integer.")

        dict_event[event_id] = {"start_date": start_date}
    return dict_event


def main(input_file: str, timepoints: str):

    dict_event = parse_events(args.timepoints)
    print(dict_event)


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

    # Concatenate timepoints to the prevalence dataframe by row name
    for row in prevalence_df.index:
        if row in dict_event:
            prevalence_df.loc[row, 'timepoint'] = dict_event[row]['start_date']

    # Sort the dataframe by timepoints
    prevalence_df = prevalence_df.sort_values(by='timepoint')


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
    parser.add_argument("-t", "--timepoints", help="String of timepoints separated by comma")


    args = parser.parse_args()
    print(args)
    main(args.input_file, args.timepoints)
