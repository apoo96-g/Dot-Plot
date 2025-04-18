#Index the reference chromosome/genome for which the markers need to be generated
samtools faidx chr1_t2t.fa

#Extract the length for the chromosome
chr_length=$(awk '$1=="chr1" {print $2}' chr1_t2t.fa.fai)
echo "$chr_length"

# Creating a BED file with 1M base intervals and 2kb size for each marker
seq 1000001 1000000 $chr_length | awk -v chr_len=$chr_length '{start=$1; end=start+1999; if(end > chr_len) end=chr_len; print "chr1", start, end}' OFS='\t' > chr1_markers_1M_int_2kb_len.bed

# Extracting the FASTA sequence for each interval specified in the .bed file
bedtools getfasta -fi chr1_t2t.fa -bed chr1_markers_1M_int_2kb_len.bed -fo chr1_markers_1M_int_2kb_len.fa

# Creating BLAST database for KIn1.v2 or any other assembly to be compared to T2T
makeblastdb -in KIn1.v2.fasta -dbtype nucl

# Running BLAST search for the 2kb markers against the assembly
blastn -query chr1_markers_1M_int_2kb_len.fa -db KIn1.v2.fasta -out chr1_blast_markers_1M_2kb_len_against_KIn1.v2.out6 -outfmt 6 -max_target_seqs 1 -max_hsps 1 -num_threads 10

# Extracting unique contig IDs that had hits
cut -f2 chr1_blast_markers_1M_2kb_len_against_KIn1.v2.out6 | sort | uniq > chr1_blast_ctg_ids_1M.txt

# Extracting the marker start and subject start after filtering for hits above 98%
awk '$3 >= 98' chr1_blast_markers_1M_2kb_len_against_KIn1.v2.out6 > chr1_KIn1.v2_filtered.out6
cut -f1,9 chr1_KIn1.v2_filtered.out6 | sed 's/:/\t/' | sed 's/-/\t/' | cut -f2,4 > KIn1.v2_chr1_plot.txt

