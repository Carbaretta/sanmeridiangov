import os

files_to_update = [
    r"c:\dev\sanmeridiangov\support.html",
    r"c:\dev\sanmeridiangov\tourism.html",
    r"c:\dev\sanmeridiangov\taxes.html",
    r"c:\dev\sanmeridiangov\press.html"
]

old_link = '''<a class="navbar-brand d-flex align-items-center" href="index.html">
                <img src="country_flag.png" alt="San Meridian Flag" style="height: 32px; width: 48px; object-fit: cover; border-radius: 4px;" class="me-2 shadow-sm border border-light">
                <span class="d-none d-sm-inline">Government of San Meridian</span>
                <span class="d-sm-none">San Meridian Gov</span>
            </a>'''
            
old_link2 = '''<a class="navbar-brand d-flex align-items-center" href="index.html">
                <img src="country_flag.png" alt="San Meridian Flag" style="height: 32px; width: 48px; object-fit: cover; border-radius: 4px;" class="me-2 shadow-sm border border-light">Government of San Meridian
            </a>'''

new_link = '''<a class="navbar-brand d-flex align-items-center" href="index.html">
                <img src="country_flag.png" alt="San Meridian Flag"
                    style="height: 32px; width: 48px; object-fit: cover; border-radius: 4px;"
                    class="me-2 shadow-sm border border-light">
                <span class="d-none d-sm-inline">Government of San Meridian</span>
                <span class="d-sm-none">San Meridian Gov</span>
            </a>'''


for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        if old_link in content:
            content = content.replace(old_link, new_link)
        if old_link2 in content:
            content = content.replace(old_link2, new_link)
            
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"No changes in {filepath}")
