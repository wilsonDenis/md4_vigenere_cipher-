
📝 Cours du 2 décembre 2025 — Notes restructurées
🎓 MIT Licence & Open Source
* La MIT License est une licence open source très permissive.
* Elle permet à quiconque d’utiliser, copier, modifier et redistribuer le code, même à des fins commerciales.
* La seule obligation : garder la notice de copyright et la licence MIT dans toute redistribution.
❓ Projet Open Source ?
Un projet open source est un projet dont :
* le code source est accessible,
* l'utilisateur peut le lire, le modifier et le redistribuer,
* selon les conditions de la licence choisie.

🔍 Différences entre Apache, GPL et nuance générale
🟦 Licence Apache (Apache 2.0)
* Très permissive (comme MIT, mais plus longue).
* Autorise la modification, redistribution, usage commercial.
* Autorise le code propriétaire : tu peux intégrer du code Apache dans un projet fermé.
* Inclut une protection contre les brevets (patent grant).
🟥 Licence GPL (GNU GPL v3 par ex.)
* Copyleft fort.
* Toute redistribution d’un logiciel contenant du code GPL doit être :
    * aussi sous GPL,
    * avec le code source accessible.
* Impossible d’intégrer du code GPL dans un projet privé/fermé.
🟨 Nuance Apache vs GPL
Critère	Apache	GPL
Permissivité	Très permissive	Copyleft fort
Usage commercial	✔️	✔️ (mais avec obligation de publier le code)
Projet fermé (propriétaire)	✔️ autorisé	❌ interdit
Clause de brevet	✔️ oui	✔️ oui
Obligation de partager les modifications	❌	✔️ obligatoire
→ Apache = liberté maximale → GPL = partage obligatoire du code modifié

🔐 md4_vigenere_cipher
Le chiffrement de Vigenère nécessite :
* un message (plaintext)
* une clé (key)
Principe : Chaque lettre du message est décalée selon la lettre équivalente de la clé (répétée).

📁 Commandes Git — Rappel
🔽 Cloner un projet
git clone <url>
📊 Vérifier l’état du dépôt
git status
→ Montre les fichiers modifiés, ajoutés, supprimés…
➕ Ajouter un fichier suivi
git add <script.py>
💬 Commit : enregistrer une version
git commit -m "<tag>: description"
Tags conseillés :
* feature → ajout de fonctionnalité
* doc → documentation
* bug_fix → correction
* refactor → amélioration interne du code
⏪ Revenir à un commit précédent
git checkout <id_commit>

 Principes de développement
✔️ KISS
Keep It Simple and Stupid → Faire simple. Pas de complexité inutile.
✔️ DRY
Don’t Repeat Yourself → Ne pas dupliquer du code. Factoriser.
✔️ Dette technique
Accumulation de mauvaises pratiques, de shortcuts, de code compliqué ou mal architecturé → rend le projet plus difficile à maintenir.
✔️ Convention
Toutes vos variables, fonctions et noms de fichiers doivent être en anglais.


