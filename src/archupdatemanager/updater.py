import subprocess
import shutil

def run_yay_updates():
    if shutil.which("yay") is None:
        raise SystemExit("Error: AUR helper 'yay' not found. ArchSecure currently requires yay to check for updates.")

    result = subprocess.run(["yay", "-Qu"], capture_output=True, text=True)
    return result.stdout

def run_yay_upgrade(noconfirm=False):
    if shutil.which("yay") is None:
        raise SystemExit("Error: AUR helper 'yay' not found. ArchSecure currently requires yay to upgrade.")

    cmd = ["yay", "-Syu"]
    if noconfirm:
        cmd.append("--noconfirm")

    try:
        subprocess.run(cmd, check=True)
        print("\n✅ Upgrade completed successfully!")
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"Upgrade failed with error: {e}")