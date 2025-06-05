# Dot-Plot
Create markers and plot the dot plots to check for linearity of the assembled genome

Create the markers using the 2kb_marker_generation.sh script. It generates markers, blasts the extracted markers against the given genome to be compared. The reference genome taken here is T2T-CHM13v2.0. 

The blast output is then filtered for marker start and subject start.
Eg: Markers <Genome> \n

The file then can be used to generate plots using the dotplot.py.
