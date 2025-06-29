#ProgressiveMauve on the assembly
./progressiveMauve --output=aligned_MAUVE.xmfa /home/minhhg/Downloads/Research/MSA/*.fasta

#Convert .xmfa to fasta
./convertAlignment.pl -i /home/minhhg/Downloads/Research/MSA/aligned_MAUVE.xmfa -o /home/minhhg/Downloads/Research/MSA/ALIGNEDFASTA_aligned_MAUVE.fasta -c -l -r

#Running with Raxml-ng
./raxml-ng --all --msa-format fasta --msa /home/minhhg/Downloads/Research/MSA/ALIGNEDFASTA_aligned_MAUVE.fasta --model GTR+G --threads 16 

#Besttree imported to ITOL

