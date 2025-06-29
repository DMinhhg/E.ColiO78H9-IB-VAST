import pandas as pd

# Load UniProt mapping
uniprot_df = pd.read_excel('idmapping_uniprot.xlsx', engine='openpyxl')
# Use only the main gene symbol
uniprot_df['Gene Symbol'] = uniprot_df['Gene Names'].str.split().str[0]
uniprot_map = dict(zip(uniprot_df['From'], uniprot_df['Gene Symbol']))

# Prepare output set to avoid duplicates
output = set()

# Parse InterProScan TSV
with open('interproscan.tsv') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        fields = line.strip().split('\t')
        prot_id = fields[0]
        go_terms = fields[13] if len(fields) > 13 else ''
        gene_symbol = uniprot_map.get(prot_id)
        if gene_symbol and go_terms and go_terms != '-':
            for go in go_terms.split('|'):
                output.add(f"{gene_symbol}\t{go}")

# Write to file
with open('genesymbol_GO_APECO78.txt', 'w') as out:
    for line in sorted(output):
        out.write(line + '\n')

print("genesymbol_GO_APECO78.txt created for goatools.")
