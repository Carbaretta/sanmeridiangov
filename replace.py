import os

root_dir = r"c:\dev\sanmeridiangov"
files = ["index.html", "taxes.html", "support.html", "press.html", "tourism.html", "economy.html", "spending-2025.html"]

for f in files:
    path = os.path.join(root_dir, f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    content = content.replace(
        '<i class="fas fa-sun text-warning me-2 fs-3"></i>',
        '<img src="country_flag.png" alt="San Meridian Flag" style="height: 32px; width: 48px; object-fit: cover; border-radius: 4px;" class="me-2 shadow-sm border border-light">'
    )
    content = content.replace(
        '<i class="fas fa-sun text-warning me-2"></i>',
        '<img src="country_flag.png" alt="San Meridian Flag" style="height: 24px; width: 36px; object-fit: cover; border-radius: 3px;" class="me-2">'
    )
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

police_files = ["index.html", "most-wanted.html", "wanted-diaz.html", "wanted-rojas.html", "wanted-silva.html", "wanted-mendez.html"]

for f in police_files:
    path = os.path.join(root_dir, "police", f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    content = content.replace(
        '<i class="fas fa-star border border-2 rounded-circle p-2 me-2 border-warning text-warning"></i>\n                Policia Nacional',
        '<img src="../country_flag.png" alt="San Meridian Flag" style="height: 40px; width: 60px; object-fit: cover; border-radius: 4px;" class="me-3 shadow-sm border border-secondary">\n                Policia Nacional'
    )
    content = content.replace(
        '<i class="fas fa-star border border-2 rounded-circle p-2 me-2 border-warning text-warning"></i>Policia Nacional',
        '<img src="../country_flag.png" alt="San Meridian Flag" style="height: 32px; width: 48px; object-fit: cover; border-radius: 4px;" class="me-2 shadow-sm border border-secondary">Policia Nacional'
    )
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
