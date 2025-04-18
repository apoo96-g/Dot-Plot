import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
import os

#All the genome names to be compared
genome_names=['Africa','Ash1','Bengali' ,'Gujarat','Han1', 'hg38', 'KIn2_final'  ,'PJL_ITU', 'PJL_pat' ,'PR1', 'ITU']

#The number of chromosomes to be compared
chromosomes= [str(i) for i in range (1,23)] + ['X','Y']



for chr_name in chromosomes:
    
    combined_df = None
    
    for genome in genome_names:
        # Construct the file path for the blast output filtered for 2 columns with marker start and the subject start. The headers will be named headers (Markers and <Genome Name>). File to be given chromosome wise for each genome to be compared.
        file_path = f'<file_path>/{genome}/{genome}_chr{chr_name}_t2t_plot.txt'
         
        # Check if the file exists before reading
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}. Skipping {genome} for chr{chr_name}")
            continue
        
        # Read the file for the current genome and chromosome
        chr_df = pd.read_csv(file_path, sep='\t', names=['Markers', genome])
        
        # Print first few rows of the file for debugging
        print(f"File {file_path} loaded successfully. First rows of data for {genome}:\n", chr_df.head())
             
        # Merge the current genome data into the combined DataFrame
        if combined_df is None:
            combined_df = chr_df
        else:
            combined_df = pd.merge(combined_df, chr_df, on='Markers', how='outer')
    
    # Save the combined data for the current chromosome
    combined_file_path = f'<file_path>/Combined_plots/all_genome_chr{chr_name}.txt'
    combined_df.to_csv(combined_file_path, sep='\t', index=False)

    print(f"Combined file saved at: {combined_file_path}")
    
    # Read the combined file
    combined_df = pd.read_csv(combined_file_path, sep='\t')

    # Iteratively add 2M, 4M, 6M, etc. to columns from 2nd to 11th
    for i in range(1, len(genome_names)+1):  # Adjusting for zero-based index (1 means second column, 10 means 11th column)
        combined_df.iloc[:, i] += i * 5_000_000  # Add 2M, 4M, 6M, etc.
    
    

    # Write the modified DataFrame back to the same file
    combined_df.to_csv(combined_file_path, sep='\t', index=False)

    print(f"Updated file saved at: {combined_file_path}")

    # Plot a dot plot for the chromosome
    plt.figure(figsize=(12, 7))  # Adjust figure size as needed
    
    
    for genome in genome_names:
            if genome == 'KIn2_final':
                # Plot 'KIn2_final' with larger size and diamond shape
                plt.scatter(combined_df['Markers'], combined_df[genome], label=genome, s=30, alpha=0.7, marker='D', color='deeppink')
            else:
                # Plot other genomes with smaller size and default circle shape
                plt.scatter(combined_df['Markers'], combined_df[genome], label=genome, s=10, alpha=0.7)


    # Labels and title
    plt.xlabel('Markers', fontsize='12')
    plt.ylabel('Genomes', fontsize='12')
    plt.title (f'Chromosome{chr_name}', fontsize='12')

    # Add grid lines for better visibility
    plt.grid(True)

    # Set x and y axis limits (if needed)
    plt.xlim([combined_df['Markers'].min(), combined_df['Markers'].max()])
    plt.ylim([combined_df[genome_names].min().min(), combined_df[genome_names].max().max()])

    # Optional: Add legend
    # Get legend handles and labels
    handles, labels = plt.gca().get_legend_handles_labels()

    # Reverse the handles and labels if needed
    handles, labels = reversed(handles), reversed(labels)

    # Rename the labels as desired
    custom_labels = ['ITU1', 'PR1', 'PJL1.v1', 'PJL1.v2', 'KIn1.v2', 'Hg38' ,'Han1', 'GIH1', 'BIB1', 'Ash1' ,'GWD1' ]
    plt.legend(handles,custom_labels, loc='lower right',markerscale=1.5,fontsize='8')
    

    # Show plot
    plt.show()
