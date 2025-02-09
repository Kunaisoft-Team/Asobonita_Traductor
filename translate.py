from deep_translator import GoogleTranslator
import polib

# Cargar el archivo .pot
pot_path = "cmsmasters-elementor.pot"
po_path = "cmsmasters-elementor-es_DO.po"

po = polib.pofile(pot_path)

# Traducir cada entrada
translator = GoogleTranslator(source="en", target="es")
for entry in po:
    if entry.msgid and not entry.msgstr:
        entry.msgstr = translator.translate(entry.msgid)

# Guardar el archivo traducido
po.save(po_path)
po.save_as_mofile("cmsmasters-elementor-es_DO.mo")

print(f"Archivo traducido guardado como: {po_path}")
