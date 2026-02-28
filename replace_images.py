import os

replacements = {
    # index.html
    "https://placehold.co/1920x600/e2e8f0/475569?text=San+Meridian+Landscape": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&q=80&w=1920&h=600",
    "https://placehold.co/600x400/e2e8f0/475569?text=Government+Building": "https://images.unsplash.com/photo-1523292562811-8fa7962ba53a?auto=format&fit=crop&q=80&w=600&h=400",
    
    # tourism.html
    "https://placehold.co/1920x800/10b981/0f172a?text=Lush+Rainforests+&+Beaches": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&q=80&w=1920&h=800",
    "https://placehold.co/1920x800/10b981/0f172a?text=Lush+Rainforests+%26+Beaches": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&q=80&w=1920&h=800",
    "https://placehold.co/600x400/0ea5e9/ffffff?text=Coral+Coast": "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&q=80&w=600&h=400",
    "https://placehold.co/600x400/1e293b/ffffff?text=Capital+City": "https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&q=80&w=600&h=400",
    "https://placehold.co/600x400/166534/ffffff?text=Emerald+Highlands": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=600&h=400",
    "https://placehold.co/600x600/f8fafc/94a3b8?text=Passport+Stamps": "https://images.unsplash.com/photo-1544644181-1484b3f8c5b3?auto=format&fit=crop&q=80&w=600&h=600",
    
    # police/index.html
    "https://placehold.co/1920x800/1e293b/0f172a?text=Police+Headquarters": "https://images.unsplash.com/photo-1555820585-c5ae44394b79?auto=format&fit=crop&q=80&w=1920&h=800",
    
    # police/careers.html
    "https://placehold.co/1920x600/1e293b/0f172a?text=Police+Lineup": "https://images.unsplash.com/photo-1453873531674-2151bcd01707?auto=format&fit=crop&q=80&w=1920&h=600"
}

files_to_check = [
    r"c:\dev\sanmeridiangov\index.html",
    r"c:\dev\sanmeridiangov\tourism.html",
    r"c:\dev\sanmeridiangov\police\index.html",
    r"c:\dev\sanmeridiangov\police\careers.html"
]

for filepath in files_to_check:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        for search, replace in replacements.items():
            content = content.replace(search, replace)
            
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"No changes in {filepath}")
