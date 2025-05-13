from Bio.PDB import PDBParser, PDBIO

# Specify the input PDB file and the chain you want to retain
input_pdb = "1ard.pdb"  # Change this to your PDB file
output_pdb = "1ard_chainA.pdb"  # Output file name
chain_to_keep = "A"  # Chain to retain

# Parse the PDB file
parser = PDBParser(QUIET=True)
structure = parser.get_structure("Structure", input_pdb)

# Extract the specified chain
io = PDBIO()
for model in structure:
    for chain in model:
        if chain.get_id() == chain_to_keep:
            io.set_structure(chain)
            io.save(output_pdb)
            print(f"Chain {chain_to_keep} extracted and saved as {output_pdb}")
