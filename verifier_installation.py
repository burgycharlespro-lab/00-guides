"""Vérifie que le poste est prêt pour les 5 projets.

Module produit par Claude Code (Anthropic), modèle Claude Fable 5.2. Créé le 25/11/2026.

Lancer depuis le dossier Portfolios :
    python 00-guides/verifier_installation.py

Le script ne modifie rien et n'installe rien. Il n'utilise que la bibliothèque
standard de Python : il marche avant toute installation.
"""

import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

ADRESSE_OLLAMA = "http://localhost:11434"
PYTHON_MINIMUM = (3, 12)


def ligne(etat: str, nom: str, detail: str = "") -> None:
    """Affiche une ligne de résultat alignée."""
    print(f"[{etat:^8}] {nom:<28} {detail}")


def version_de(commande: list[str]) -> str | None:
    """Renvoie la première ligne affichée par une commande, ou None si elle échoue."""
    try:
        sortie = subprocess.run(commande, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return None
    texte = (sortie.stdout or sortie.stderr).strip()
    return texte.splitlines()[0] if texte else None


def verifier_python() -> bool:
    actuelle = sys.version_info[:3]
    texte = ".".join(str(n) for n in actuelle)
    if actuelle >= PYTHON_MINIMUM:
        ligne("OK", "Python", texte)
        return True
    ligne("MANQUE", "Python", f"{texte} trouvé, il faut 3.12 ou plus")
    return False


def verifier_outil(nom: str, commande: str, obligatoire: bool = True) -> bool:
    """Vérifie qu'une commande existe et affiche sa version."""
    if shutil.which(commande) is None:
        ligne("MANQUE" if obligatoire else "OPTION", nom, "non installé (voir le guide 01)")
        return not obligatoire
    ligne("OK", nom, version_de([commande, "--version"]) or "installé")
    return True


def verifier_serveur_ollama() -> bool:
    """Interroge le serveur Ollama local et liste les modèles téléchargés."""
    try:
        with urllib.request.urlopen(f"{ADRESSE_OLLAMA}/api/tags", timeout=5) as reponse:
            donnees = json.load(reponse)
    except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError):
        ligne("MANQUE", "Serveur Ollama", f"pas de réponse sur {ADRESSE_OLLAMA} (Ollama est-il lancé ?)")
        return False

    modeles = donnees.get("models", [])
    ligne("OK", "Serveur Ollama", f"répond sur {ADRESSE_OLLAMA}")
    if not modeles:
        ligne("MANQUE", "Modèles téléchargés", "aucun (voir le guide 02)")
        return False
    for modele in modeles:
        taille_go = modele.get("size", 0) / 1_000_000_000
        ligne("OK", "Modèle", f"{modele.get('name', '?')}  ({taille_go:.1f} Go)")
    return True


def main() -> int:
    print("Vérification du poste pour les projets du dossier Portfolios\n")
    resultats = [
        verifier_python(),
        verifier_outil("git", "git"),
        verifier_outil("uv", "uv"),
        verifier_outil("Ollama (commande)", "ollama"),
        verifier_serveur_ollama(),
        verifier_outil("Docker (projet 4, option)", "docker", obligatoire=False),
    ]
    print()
    if all(resultats):
        print("Tout est prêt. Suite : 01-etiquettes-vin/COURS.md, séance 0.")
        return 0
    print("Il manque au moins un élément. Reprendre les guides 01 et 02, puis relancer ce script.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
