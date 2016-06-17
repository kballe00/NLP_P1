# Filename: modify_gene.py
# Author: Keith Ballew
# Description: Counts the words in gene.train, and replaces words that occur less than
#              five times with "_RARE_"
# Usage: python gene.train
# Date created: 06/16/16
# Last modified: 06/17/16

gene_train_file = open( 'gene.train', 'r' );
modified_gene_train_file = open( 'modified_gene.train', 'w' );

dictionary = dict( );

# Iterate over words and count them
for line in gene_train_file:
    split_line = line.split( );

    # Ignore lines with no text
    if len( split_line ) == 0:
        continue;

    word = split_line[ 0 ];

    if word in dictionary:
        dictionary[ word ] += 1;
    else:
        dictionary[ word ] = 1;
        
# Reset file read position for iterating again
gene_train_file.seek( 0 );

# Iterate again to replace words that occurred less than five times 
for line in gene_train_file:
    split_line = line.split( );

    # Ignore lines with no text
    if len( split_line ) == 0:
        continue;

    word = split_line[ 0 ];

    if dictionary[ word ] < 5:
        split_line[ 0 ] = '_RARE_';

    modified_gene_train_file.write( ' '.join( split_line ) + '\n' );
    
gene_train_file.close( );
modified_gene_train_file.close( );
