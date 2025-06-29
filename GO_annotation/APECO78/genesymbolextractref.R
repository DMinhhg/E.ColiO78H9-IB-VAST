input_file <- "genomic.gbff"
output_file <- "gene_symbols.txt"

# Read the file
lines <- readLines(input_file)

gene_symbols <- c()
in_cds <- FALSE

for (line in lines) {
  # Detect start of a CDS feature
  if (grepl("^ {5}CDS ", line)) {
    in_cds <- TRUE
  }
  # If it hits another feature or end of features, stop looking for gene in this block
  else if (in_cds && grepl("^ {5}\\S", line)) {
    in_cds <- FALSE
  }
  
  # If inside a CDS, look for /gene="..."
  if (in_cds && grepl('/gene="[^"]+"', line)) {
    gene <- sub('.*\\/gene="([^"]+)".*', '\\1', line)
    gene_symbols <- c(gene_symbols, gene)
  }
}

# Remove duplicates and write to file
gene_symbols <- unique(gene_symbols)
writeLines(gene_symbols, output_file)

cat("Extracted", length(gene_symbols), "gene symbols to", output_file, "\n")