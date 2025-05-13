from Bio import PDB

# Load the structure
parser = PDB.PDBParser(QUIET=True)
structure = parser.get_structure('1bbo', '1bbo.pdb')

# Extract chain A from the structure
chain_A = structure[0]['A']

# Save the extracted chain A into a new PDB file
io = PDB.PDBIO()
io.set_structure(chain_A)
io.save('1bbo_chainA.pdb')

print("Chain A extracted and saved as 1bbo_chainA.pdb")
