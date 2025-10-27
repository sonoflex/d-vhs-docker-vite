# 🎬 D-VHS – Der digitale Filmclub

> Eine kleine Web-App für unseren privaten Filmclub, um den gemeinsamen DVD-Pool zu verwalten, Wunschlisten zu teilen und doppelte Käufe zu vermeiden.

---

## 🧠 Konzept

Wir (eine kleine Gruppe von Filmfreunden) kaufen DVDs mit Filmen, die man mehr als einmal sehen will – also Klassiker und Lieblingsfilme.  
Über die D-VHS-App wollen wir:

- unseren gemeinsamen **DVD-Pool** sichtbar machen  
- **Wunschlisten** pflegen  
- **Verleihstatus** verfolgen („wer hat gerade welche DVD?“)  
- **Doppelte Käufe vermeiden**  
- und natürlich ein bisschen Nostalgie aufleben lassen 😉

---

## 🧩 Funktionsumfang

### 🎞️ **Filme**
| Feld | Beschreibung |
|------|---------------|
| `tmdb_id` | ID des Films bei der TMDB-API |
| `title` | Filmtitel |
| `year` | Erscheinungsjahr |
| `description` | Kurze Beschreibung |
| `owner_id` | Besitzer der DVD |
| `lent_to_id` | (optional) aktuell ausgeliehen an |
| `lent_since` | (optional) Datum des Verleihs |
| `wishlist_user_ids` | Liste der Nutzer, die den Film auf der Wunschliste haben |
| `poster_url` | Bild (Plakat) vom Film |

### 👤 **Nutzer**
| Feld | Beschreibung |
|------|---------------|
| `id` | Primärschlüssel |
| `username` | Benutzername |
| `email` | E-Mail zum Zurücksetzen |
| `password_hash` | Passwort-Hash (bcrypt) |

---

## 🏗️ Architektur

| Komponente | Technologie | Beschreibung |
|-------------|--------------|---------------|
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) | REST-API zur Verwaltung von Nutzern, Filmen und Verleihstatus |
| **Frontend** | [Vue.js (Vite)](https://vitejs.dev/) | Weboberfläche für Liste, Filter und Detailansicht |
| **Datenbank** | SQLite | Einfacher Start, später leicht auf PostgreSQL erweiterbar |
| **Auth** | bcrypt + JWT / FastAPI Users | Sichere Anmeldung und Sitzungen |
| **API-Integration** | [TMDB API](https://developer.themoviedb.org/) | Automatisches Abrufen von Filmtiteln, Beschreibungen und Postern |
| **Deployment** | Docker & docker-compose | Einheitliche Umgebung für Frontend und Backend |

---

## ⚙️ Projektstruktur

```bash
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes/
│   │   ├── services/
│   │   └── tmdb.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── vite.config.js
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
git 