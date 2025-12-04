import subprocess

def run_yay_updates():
    result = subprocess.run(["yay", "-Qu"], capture_output=True, text=True)
    data = result.stdout
    print(data)
    parse_updates(data)

def parse_updates(text):
    pkgs = []
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue  # pula linha vazia

        parts = line.split()
        if len(parts) != 4 or parts[2] != "->":
            print(f"Formato inesperado, ignorando: {line}")
            continue

        pkg, old, arrow, new = parts
        pkgs.append({
            "pkg": pkg,
            "old": old,
            "new": new
        })

    print(pkgs)



run_yay_updates()
