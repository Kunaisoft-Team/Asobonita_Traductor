import polib
import os
from deep_translator import GoogleTranslator

# Configuration
pot_file = "cmsmasters-elementor.pot"  # Input .pot file
output_dir = "translated_pot_files"  # Directory for split & translated files
entries_per_file = 100  # Number of entries per split file

# Load the .pot file
po = polib.pofile(pot_file)

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Initialize translator
translator = GoogleTranslator(source="en", target="es")

# Split and translate
for i in range(0, len(po), entries_per_file):
    chunk = po[i : i + entries_per_file]  # Get a slice of entries
    new_po = polib.POFile()
    new_po.metadata = po.metadata  # Copy metadata

    # Translate and add entries
    for entry in chunk:
        if entry.msgid and not entry.msgstr:  # Only translate empty msgstr
            entry.msgstr = translator.translate(entry.msgid)
        new_po.append(entry)

    # Save translated .pot file
    output_path = os.path.join(output_dir, f"part_{i // entries_per_file + 1}_es.pot")
    new_po.save(output_path)
    print(f"Translated and saved: {output_path}")

print("Splitting & translation complete! 🚀")
