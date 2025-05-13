from Bio import PDB

# List of your PDB files
pdb_files = [
    "single_1ard.pdb", "single_1bbo.pdb", "single_1paa.pdb",
    "single_1sp1.pdb", "single_1sp2.pdb", "single_1zfd.pdb",
    "single_1znf.pdb", "single_1znm.pdb", "single_results.pdb"
]

# Open a file to save the sequences
with open("aligned_sequences.fasta", "w") as output_file:
    for pdb_file in pdb_files:
        # Parse the PDB file
        parser = PDB.PDBParser(QUIET=True)
        structure = parser.get_structure(pdb_file, pdb_file)

        # Get the sequence for each model/chain
        for model in structure:
            for chain in model:
                sequence = ""
                for residue in chain:
                    # Only consider amino acids
                    if PDB.is_aa(residue):
                        sequence += residue.get_resname()  # Add the amino acid name
                # Write the sequence to the output file in FASTA format
                output_file.write(f">{pdb_file}_{chain.get_id()}\n{sequence}\n")
