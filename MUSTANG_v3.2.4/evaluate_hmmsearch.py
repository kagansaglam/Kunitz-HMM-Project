# Step 2: Define known Kunitz proteins (positive examples)
positive_proteins = {
    "single_1ard.pdb_A",
    "single_1bbo.pdb_A",
    "single_1paa.pdb_A",
    "single_1sp1.pdb_A",
    "single_1sp2.pdb_A",
    "single_1zfd.pdb_A",
    "single_1znf.pdb_A",
    "single_1znm.pdb_A",
    "single_results.pdb_A"
}

# Step 3: Parse HMMER results.tbl
predicted_hits = set()

with open("results.tbl", "r") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue
        fields = line.strip().split()
        seq_id = fields[0]
        predicted_hits.add(seq_id)

# Evaluation
TP = len(predicted_hits & positive_proteins)
FN = len(positive_proteins - predicted_hits)
FP = len(predicted_hits - positive_proteins)
TN = 0  # Only needed if you have a full known negative list

# Metrics
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Print results
print("Evaluation Results:")
print(f"True Positives (TP): {TP}")
print(f"False Negatives (FN): {FN}")
print(f"False Positives (FP): {FP}")
print(f"Precision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
print(f"F1 Score:  {f1_score:.2f}")
