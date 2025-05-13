from Bio.PDB import PDBList

pdb_ids = [
    "1ard", "1bbo", "1paa", "1sp1", "1sp2",
    "1zaa", "1zfd", "1znf", "1znm", "2drp", "3znf", "5znf"
]

# Some entries like 1zaa1, 1zaa2 may refer to specific chains or models,
# so we just download the main entries (PDB handles chains separately)

pdbl = PDBList()
for pdb_id in pdb_ids:
    pdbl.retrieve_pdb_file(pdb_id, file_format="pdb", pdir=".")
