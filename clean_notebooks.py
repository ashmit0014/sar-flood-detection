import nbformat
import os

notebooks = ['Indus_flood.ipynb', 'Indus_dry.ipynb']

for filename in notebooks:
    if os.path.exists(filename):
        print(f"Cleaning {filename}...")
        # Read the notebook
        with open(filename, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Surgically remove the broken widget metadata
        if 'widgets' in nb.metadata:
            del nb.metadata['widgets']
            print(" - Removed broken widget metadata.")
            
        # Save the notebook back with all outputs intact
        with open(filename, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(" - Saved successfully.\n")
    else:
        print(f"Could not find {filename}")

print("All done!")