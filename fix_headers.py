import os

files_to_update = [
    r"c:\dev\sanmeridiangov\economy.html",
    r"c:\dev\sanmeridiangov\spending-2025.html"
]

old_link_start = '<a class="navbar-brand d-flex align-items-center" href="index.html"><i class="fas fa-landmark text-warning me-2"></i>'
new_link = '''<a class="navbar-brand d-flex align-items-center" href="index.html">
                <img src="country_flag.png" alt="San Meridian Flag"
                    style="height: 32px; width: 48px; object-fit: cover; border-radius: 4px;"
                    class="me-2 shadow-sm border border-light">
                <span class="d-none d-sm-inline">Government of San Meridian</span>
                <span class="d-sm-none">San Meridian Gov</span>
            </a>'''
            
old_link2 = '<a class="navbar-brand d-flex align-items-center" href="index.html">\n                <img src="country_flag.png" alt="San Meridian Flag" style="height: 32px; width: 48px; object-fit: cover; border-radius: 4px;" class="me-2 shadow-sm border border-light">San Meridian\n            </a>'


for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        if old_link2 in content:
            content = content.replace(old_link2, new_link)
            
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"No changes in {filepath}")
