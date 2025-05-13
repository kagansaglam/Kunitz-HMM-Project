import requests


uniprot_ids = [
    "P11111", "P22222", "P12345", "P33333",
    "P54321", "P44444", "P99999", "P55555"
]


output_file = "all_proteins.fasta"


base_url = "https://rest.uniprot.org/uniprotkb/{}.fasta"


with open(output_file, "w") as out_f:
    for uid in uniprot_ids:
        response = requests.get(base_url.format(uid))
        if response.status_code == 200:
            out_f.write(response.text)
            print(f"✅ Retrieved {uid}")
        else:
            print(f"❌ Failed to retrieve {uid} (Status {response.status_code})")

print(f"\n🔁 All sequences saved to: {output_file}")
