import subprocess
import time 

# Délai en secondes (30 minutes).
INTERVAL = 30
def Git_Push():
    try:
        # Ajoute tous les changements.
        subprocess.run(["git", "add", "."], check=True)

        # Commit avec un message de automatique.
        commit_message = "Sauvegarde automatique"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Pousse vers le dépot github.
        subprocess.run(["git", "push"], check=True)

        print("Changement éffecté et poussé sur Git")
    except subprocess.CalledProcessError as e:
        print("Erreur lors de la sauvegarde sur Git:", e)


if __name__ == "__main__":
    print("Script de Sauvegarde automatique démarré...")
    while True:
        Git_Push()
        time.sleep(INTERVAL)
