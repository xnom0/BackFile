# BackFile

### BackFile est un outil qui permet de scanner un serveur web afin de trouver des fichiers / archives de sauvegarde.

🔍 Les fichiers .swp ou ~ sont générés automatiquement par des éditeurs de texte comme Vim (.swp) ou Emacs/Gedit (~) lors de la modification de fichiers. 

Leur présence sur un serveur web peut permettre à un attaquant de :
✅ Lire des variables sensibles (clés API, mots de passe)
✅ Étudier votre logique applicative pour préparer une attaque
✅ Exploiter d'anciennes versions de votre code

BackFile permet de trouver des fichiers caché (.swp , ~) ou des archives de sauvegarde oublié sur un serveur.

![Screenshot_20240501_153854](https://github.com/xnom0/BackFile/blob/main/1747036201086.jpeg)

Il permet de créer un log lorsque :
* trouver des fichiers ouvert / mal fermer par un editeur de texte en CLI (Vim,Vi,Nano)
* trouver des fichiers archive .zip, .tar, .tar.gz .... 

Afin d'éxécuter le script il vous faut python3

`python3 backfile.py [URL] [FILE]`

Example :

`python3 backfile.py [http://site.com] [index]`

Backfile permet également de chercher des fichiers / archive de configuration.

`python3 backfile.py [http://site.com] [--auto]`
