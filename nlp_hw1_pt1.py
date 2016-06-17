gene_counts = file( 'gene.counts', 'r' );
# TODO: file to write to

wordtags_dict = dict( );

# Iterate over words in file, and associate wordtags
for line in gene_counts:
    split_line = line.split( );
    
    if split_line[ 1 ] == 'WORDTAG':
        