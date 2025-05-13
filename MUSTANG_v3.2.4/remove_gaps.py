from Bio import SeqIO

input_file = "aligned_sequences_realigned.fasta"
output_file = "aligned_sequences_realigned_nogaps.fasta"

with open(output_file, "w") as out_handle:
    for record in SeqIO.parse(input_file, "fasta"):
        # Manually remove '-' from sequence string
        record.seq = record.seq.__class__(str(record.seq).replace("-", ""))
        SeqIO.write(record, out_handle, "fasta")

print(f"Cleaned FASTA written to {output_file}")
