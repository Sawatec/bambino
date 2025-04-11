# Bambino - All-in-One Kitamanagement-App

Bambino ist eine umfassende Management-Plattform für Kindertagesstätten. Die App ermöglicht eine effiziente Verwaltung, Kommunikation mit Eltern und das Erstellen von Entwicklungsberichten.

![grafik](https://github.com/user-attachments/assets/f91eea7c-0f6b-4708-908a-cc316ab85f27)

## Funktionen

- **Dashboard**: Übersicht über wichtige Informationen und Neuigkeiten.
- **Kinderverwaltung**: Verwaltung von Kinderprofilen und Entwicklungsnotizen.
- **Benutzerverwaltung**: Verwaltung von Benutzern und Rollen.
- **Nachrichten**: Kommunikation mit Eltern und Mitarbeitern.
- **Responsive Design**: Optimiert für verschiedene Geräte.

---

## Rollen und Funktionen

### **Erzieher**
- Zugriff auf Profile der Kinder in ihrer zugewiesenen Gruppe.
- Hinzufügen und Bearbeiten von Entwicklungsberichten für Kinder.
- Kommunikation mit Eltern über das Nachrichtensystem.
- Einsehen von wichtigen Updates und Informationen im Dashboard.

### **Eltern**
- Zugriff auf das Profil ihres Kindes.
- Einsehen von Entwicklungsberichten und Nachrichten von Erziehern.
- Kommunikation mit der Kindertagesstätte über das Nachrichtensystem.
- Übermitteln von wichtigen Informationen, wie Abwesenheiten oder Anfragen.

### **Admin**
- Verwaltung aller Benutzer (Erzieher, Eltern und andere Admins).
- Zuweisung von Rollen und Freischaltung von Benutzerkonten.
- Verwaltung von Kinderprofilen und Gruppen.
- Zugriff auf alle Entwicklungsberichte und Nachrichten.
- Überwachung und Verwaltung der gesamten Kindertagesstätte.

---

## Screenshots

### **Dashboard**
Das Dashboard bietet eine Übersicht über wichtige Informationen und Neuigkeiten.

![grafik](https://github.com/user-attachments/assets/cae39ea9-d5c8-4cb3-918a-dde8041f83ec)


---

### **Kinderverwaltung**
Verwalten Sie Kinderprofile und fügen Sie Entwicklungsberichte hinzu.

Erzieher:

![grafik](https://github.com/user-attachments/assets/f7bac23e-7be2-454a-b5bf-49e024adf034)
![Screenshot 2025-04-12 011311](https://github.com/user-attachments/assets/d186199a-0be8-4393-8d41-233022ff51c5)

Eltern:

![grafik](https://github.com/user-attachments/assets/2e530aea-20bf-4e05-ad56-d7abbfa7c4cf)



---

### **Benutzerverwaltung**
Admins können Benutzerrollen verwalten und neue Benutzer freischalten.

![grafik](https://github.com/user-attachments/assets/11defec9-7192-43d4-aecd-2aab99322853)


---

### **Nachrichtensystem**
Kommunizieren Sie effizient mit Eltern und Mitarbeitern.

![grafik](https://github.com/user-attachments/assets/a7815807-c44e-4e15-b18a-07e28e702a61)
![grafik](https://github.com/user-attachments/assets/ac8e25d4-503a-4642-9321-e43fa1d6457a)



## Voraussetzungen

- **Python**: Version 3.8 oder höher
- **Django**: Version 4.0 oder höher
- **SQLite**: Für die Datenbank
- **Node.js** (optional): Für die Verarbeitung von CSS/JS-Assets

---

## Installation

1. **Repository klonen**:
   ```bash
   git clone https://github.com/username/bambino.git
   cd bambino

2. **Virtuelle Umgebung erstellen und aktivieren**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Für Linux/Mac
   venv\Scripts\activate     # Für Windows


3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt

4. **Datenbank-Migrationen ausführen**:
   ```bash
   python manage.py migrate

5. **Superuser erstellen**:
   ```bash
   python manage.py createsuperuser

6. **Entwicklungsserver starten**:
   ```bash
   python manage.py runserver

7. **Anwendung aufrufen**:
   Öffnen Sie http://127.0.0.1:8000 in Ihrem Browser.


