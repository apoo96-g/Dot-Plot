# Dot-Plot
Create markers and plot the dot plots to check for linearity of the assembled genome

Create the markers using the 2kb_marker_generation.sh script. It generates markers, blasts the extracted markers against the given genome to be compared. The reference genome taken here is T2T-CHM13v2.0. 

The blast output is then filtered for marker start and subject start.
Eg: Markers <Genome> 
1002000 138449
2002000 1140498
3002000 2235584
4002000 3241579
5002000 4241389
6002000 5241100
7002000 6240279
8002000 7240762
9002000 8241252

The file then can be used to generate plots using the dotplot.py.
