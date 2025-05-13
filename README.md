# Kunitz Domain HMM Project

## Overview

The Kunitz domain is a protein structure involved in inhibiting proteases. In this project, we built a **Profile Hidden Markov Model (HMM)** for the Kunitz domain using structural information.

![Ribbon structure of Kunitz domain](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Protein_ribbon_structure.png/500px-Protein_ribbon_structure.png)

### Fig. 1. Ribbon structure of a representative Kunitz domain (PDB 1KTH)

The Kunitz domains are approximately 50-60 amino acids long and function as serine protease inhibitor domains.

---

## Methodology

1. **Structure Selection**
   We retrieved Kunitz-domain protein structures from the **PDB** using a script.

2. **Structural Alignment**
   The selected domain chains were aligned using the **MUSTANG** tool.

---

## Repository Structure

- **data/structures/** – Raw PDB files and chain-extracted structures.
- **data/alignments/** – Structural alignment output from MUSTANG.
- **scripts/** – Various scripts used in the project workflow.

---

## Evaluation

The model correctly identified ~90% of true Kunitz domains. The full confusion counts and derived metrics are in `results/evaluation.txt`.

---

## Conclusion

All output files (alignment, model, search table) are included in the repository.
