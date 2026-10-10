import os
import json

static_files = {}

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    for file in files:
        if file in ["generate_config.py", "zipconfig.json"] or file.startswith('.'):
            continue
            
        full_path = os.path.join(root, file)
        relative_path = os.path.relpath(full_path, ".")
        mc_path = relative_path.replace("\\", "/")
        
        static_files[mc_path] = {
            "fetch": f"{mc_path}"
        }

config_data = {
    "static": static_files,
    "dynamic": {}
}

with open("zipconfig.json", "w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=4)

print("zipconfig.json erfolgreich generiert!")