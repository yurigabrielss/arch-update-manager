def parse_updates(text):
    pkgs = []
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

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

    return(pkgs)