# Explication de l'architecture du dossier `docker`

Le dossier `docker` contient les scripts et configurations spécifiques à Docker.

L'architecture de ce projet semble être conçue pour une application conteneurisée utilisant Docker. Voici les détails de chaque composant :




### Scripts

- `build.sh`: Un script pour construire les images Docker du projet.
- `clean.sh`: Un script pour nettoyer ou supprimer les conteneurs/images Docker.
- `run_nrg.sh`: Script pour exécuter une tâche spécifique, probablement liée au projet (NRG peut être un acronyme ou un nom spécifique).
- `start_int.sh`: Script pour démarrer l'environnement intégré (INT suggère un environnement d'intégration).

### Sous-dossiers Docker

#### `mysql`

Contient les configurations pour un conteneur MySQL.

- `1-SCHEMA.sql`: Script SQL pour créer la structure de la base de données (schéma).
- `2-PRIVILEGES.sql`: Script SQL pour définir les privilèges des utilisateurs de la base de données.
- `Dockerfile`: Le Dockerfile pour créer l'image Docker de MySQL personnalisée.

#### `newman`

Configuration pour Newman, un outil de test d'API Postman.

- `Dockerfile`: Dockerfile pour construire une image exécutant Newman.
- `collections/iterator-test-nrg`: Collection Postman pour des tests spécifiques.
- `environments/int.postman_environment.json`: Fichier de configuration pour l'environnement de test dans Postman.
- `report`: Dossier probablement destiné aux rapports de test.

#### `nginx`

Configuration pour un serveur web/proxy Nginx.

- `int.conf`: Configuration Nginx pour l'environnement d'intégration.

#### `python`

Configuration pour une application backend en Python.

- `Dockerfile`: Dockerfile pour construire une image Python personnalisée.
- `backend/main.py`: Le script principal de l'application backend.
- `backend/test_main.http`: Fichier pour tester l'API backend, probablement utilisé avec des outils comme HTTPie ou VS Code.

## Conclusion

Chaque composant de cette architecture joue un rôle spécifique dans la configuration, le déploiement, et le test de l'application.
