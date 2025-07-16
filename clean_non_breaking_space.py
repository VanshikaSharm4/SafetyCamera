# clean_non_breaking_space.py

file_path = "model/__init__.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace non-breaking spaces with regular space
cleaned_content = content.replace('\u00A0', ' ')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(cleaned_content)

print("✅ Cleaned non-breaking spaces from model/__init__.py")
