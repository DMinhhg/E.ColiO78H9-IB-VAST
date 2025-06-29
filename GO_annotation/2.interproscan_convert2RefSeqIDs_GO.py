input_file = "interproscan.tsv"
output_withGO_file = "idswithgo.txt"
protein_ids_file = "protein_ids.txt"

with open(input_file) as fin, open(output_withGO_file, "w") as fout, open(protein_ids_file, "w") as fprot:
    for line in fin:
        if line.startswith("#") or not line.strip():
            continue
        fields = line.strip().split("\t")
        protein = fields[0]
        fprot.write(f"{protein}\n")  
        if len(fields) > 13 and fields[13] and fields[13] != "-":
            go_terms = fields[13].split("|")
            for go in go_terms:
                fout.write(f"{protein}\t{go}\n") 
