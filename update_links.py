import os
import re

# Use the absolute path as requested
directory = r"C:\Users\KAVI\.gemini\antigravity\scratch\stitch_project"

# Map of pages for easy reference
pages = {
    "Home": "index.html",
    "Discovery": "discovery.html",
    "Smart Menu": "menu.html",
    "Booking": "table-booking.html",
    "Cart": "group-cart.html",
    "Track Order": "track-order.html",
    "User Profile": "user-profile.html",
    "Merchant": "merchant-dashboard.html",
    "Reviews": "reviews.html",
    "Eco Impact": "eco-impact.html"
}

def update_nav(html_content, current_file):
    # This is a generic replacement to try and fix common navigation patterns
    # Look for common nav links and update them
    
    replacements = [
        (r'href="#"', '#'), # Placeholder
        (r'href="index\.html"', 'index.html'),
        (r'href="discovery\.html"', 'discovery.html'),
        (r'href="menu\.html"', 'menu.html'),
    ]

    # For index.html, discovery.html, menu.html, we've already done some work.
    # We want to ensure ALL files have a consistent nav if possible, 
    # but at minimum ensure they link to each other correctly.
    
    # Let's find any link that looks like a navigation link and fix it.
    # This is rough but should help for a "single project" feel.
    
    for label, target in pages.items():
        # Match case-insensitive label and fix the tag
        # e.g. <a ...>Home</a> -> <a ... href="index.html">Home</a>
        pattern = re.compile(rf'(<a[^>]*?href=)"[^"]*?"([^>]*?>\s*{label}\s*</a>)', re.IGNORECASE)
        html_content = pattern.sub(rf'\1"{target}"\2', html_content)

    return html_content

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content = update_nav(content, filename)
        
        if updated_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated {filename}")
