gene_train_file = open( 'gene.train', 'r' );
modified_gene_train_file = open( 'modified_gene.train', 'w' );

dictionary = dict( );

for line in gene_train_file:
    split_line = line.split( );
    if len( split_line ) == 0:
        continue;
    word = split_line[ 0 ];
    if word in dictionary:
        dictionary[ word ] += 1;
    else:
        dictionary[ word ] = 1;
        
# Reset file read position for iterating again
gene_train_file.seek( 0 );

for line in gene_train_file:
    split_line = line.split( );
    if len( split_line ) == 0:
        continue;
    word = split_line[ 0 ];
    if dictionary[ word ] < 5:
        split_line[ 0 ] = '_RARE_';
    modified_gene_train_file.write( ' '.join( split_line ) + '\n' );
    
gene_train_file.close( );
modified_gene_train_file.close( );