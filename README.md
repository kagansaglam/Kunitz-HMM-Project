# Kunitz Domain HMM Project

## Overview

The Kunitz domain is a type of protein structure involved in inhibiting proteases. In this project, we built a **Profile Hidden Markov Model (HMM)** for the Kunitz domain using structural information, which we then used to annotate Kunitz domains in protein sequences.

### Fig. 1. Ribbon structure of a representative Kunitz domain (PDB 1KTH)
![Ribbon structure]([https://en.m.wikipedia.org/wiki/File:PDB_1kth_EBI.jpg])
*The ribbon structure of a representative Kunitz domain showing the compact α+β fold stabilized by three disulfide bonds.*

The Kunitz domains are approximately 50-60 amino acids long and function as serine protease inhibitor domains, found in diverse proteins like BPTI (bovine pancreatic trypsin inhibitor).

---

## Methodology

### 1. Structure Selection
We retrieved Kunitz-domain protein structures from the **PDB** (Protein Data Bank), such as **PDB IDs: 1ARD, 1BBO, 1KTH**, using a script to download the files.

### 2. Structural Alignment
The selected domain chains were aligned using the **MUSTANG** tool, producing a multiple sequence alignment (MSA) in FASTA/MSF format.

### 3. Alignment Conversion
The **MUSTANG** alignment was converted to **Stockholm** format using Biopython's **AlignIO**.

### 4. HMM Building
We trained a profile **HMM** using the **HMMER** tool on the structural MSA. This model captures conserved sequence patterns in the Kunitz domain.

### 5. Domain Search
We applied **hmmsearch** to a test set of protein sequences to identify Kunitz domains. The results were stored in a table.

---

## Results

- **Alignment**: The structural alignment is saved as `data/alignments/kunitz.sto`.
- **HMM Model**: The profile HMM model is saved as `data/model/kunitz.hmm`.
- **Performance**: On our test set, the HMM correctly identified ~90% of true Kunitz domains.

---

## Repository Structure

This project is organized as follows:

- **data/structures/** – Raw PDB files and chain-extracted structures.
- **data/alignments/** – Structural alignment output from MUSTANG.
- **data/sequences/** – Test sequence datasets for HMM scanning.
- **model/** – Final HMM profile files.
- **results/** – HMMER output and evaluation results.
- **scripts/** – Various scripts used in the project workflow.

---

## Example Scripts

### `scripts/fetch_structures.sh`
```bash
#!/bin/bash
mkdir -p data/structures
for pdb in 1ARD 1BBO 1KTH; do
  wget -O data/structures/${pdb}.pdb https://files.rcsb.org/download/${pdb}.pdb
done
