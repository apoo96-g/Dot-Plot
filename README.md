# Dot-Plot
Create markers and plot the dot plots to check for linearity of the assembled genome

Create the markers using the 2kb_marker_generation.sh script. It generates markers, blasts the extracted markers against the given genome to be compared. The reference genome taken here is T2T-CHM13v2.0. 

The blast output is then filtered for marker start and subject start.
Eg:
Marker_Start	<Genome>_Start
1000001	1010236
2000001	2009870
3000001	3011723
4000001	4010301
5000001	5012672
6000001	6011133
7000001	7012311
	
The file then can be used to generate plots using the dotplot.py.

Dot_plot_v2.pynb does all of the steps above. The input is the blast file of markers vs genome(chr_wise).
