# Dot-Plot
### Marker Generation and Dot Plot Construction

Run the 2kb_marker_generation.sh script to generate 2 kb genomic markers from the reference assembly. The script performs the following steps:

 **Marker Extraction**: Segments the reference genome into 2 kb non-overlapping markers.

  **BLAST Search**: Aligns the extracted markers against the target genome using blastn.

 **Result Filtering**: Filters BLAST hits to retain only those with ≥98% percent identity (pID).

  **Coordinate Extraction**: Parses the BLAST output to extract qstart (marker start) and sstart (subject start) coordinates.

The resulting coordinates can be used as input for generating dot plots using **dotplot.py** to assess synteny and linearity between the reference and target genomes.

Sample input file for use with dotplot.py
<small>

| Marker Start | Genome Chr Start |
|--------------|------------------|
| 1,000,001    | 1,010,236        |
| 2,000,001    | 2,009,870        |
| 3,000,001    | 3,011,723        |
| 4,000,001    | 4,010,301        |
| 5,000,001    | 5,012,672        |
| 6,000,001    | 6,011,133        |
| 7,000,001    | 7,012,311        |

</small>

	

## Version 2:

The script **Dot_plot_v2.ipynb** performs all the aforementioned steps in a streamlined manner. It takes as input a BLAST output file containing alignments between markers and a chromosome-wise reference genome.

## Reference Marker Files:

**t2t_markers.zip**: Contains markers(T2T1Mb) derived from the T2T_CHM13.v2 assembly. Each marker is 2 kb in size and spaced 1 Mb apart across chromosomes.

**hg38_100kb_markers.zip**: Contains markers(hg38100kb) from the hg38 assembly, each 2 kb in size and spaced 100 kb apart across chromosomes.

**Arabidopsis_thaliana_markers.zip**: Contains chromosome-wise markers from _Arabidopsis thaliana_, each 2 kb in size and spaced 100 kb apart.
