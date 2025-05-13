from Bio import PDB
import os

parser = PDB.PDBParser(QUIET=True)
io = PDB.PDBIO()

# List only .pdb files
pdb_files = [f for f in os.listdir() if f.endswith('.pdb')]

for pdb_file in pdb_files:
    structure = parser.get_structure(pdb_file, pdb_file)
    model = structure[0]

    # Try to get chain A
    if 'A' in model:
        chain = model['A']
    else:
        # Use the first chain if A doesn't exist
        chain = list(model.get_chains())[0]

    # Save only this chain
    new_structure = PDB.Structure.Structure(pdb_file)
    new_model = PDB.Model.Model(0)
    new_model.add(chain)
    new_structure.add(new_model)

    io.set_structure(new_structure)
    io.save(f"single_{pdb_file}")
