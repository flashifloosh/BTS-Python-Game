import random  # Importiert das Modul random, um zufällige Auswahl zu ermöglichen
from colorama import Fore, Style  # Importiert Fore und Style von colorama, um farbige Ausgabe in der Konsole zu ermöglichen (pip install colorama)

def load_words(filename):  # Definiert eine Funktion, die Wörter aus einer Datei lädt
    with open(filename, 'r', encoding='utf-8') as file:  # Öffnet die Datei im Lese-Modus mit der richtigen Codierung
        words = [word.upper() for word in file.read().splitlines() if word]  # Liest die Datei, teilt sie in Zeilen auf, wandelt die Wörter in Großbuchstaben um und ignoriert leere Wörter
    for word in words:  # Überprüft jedes Wort in der Liste
        if len(word) != 5 or not word.isalpha():  # Wenn das Wort nicht genau 5 Buchstaben lang ist oder nicht nur Buchstaben enthält
            raise ValueError(f"Ungültiges Wort '{word}' in der Wortliste. Alle Wörter müssen genau 5 Buchstaben lang sein und dürfen keine Zahlen enthalten.")  # Löst eine Ausnahme aus
    return words  # Gibt die Liste der Wörter zurück

def restart_menu():
    while True:
        replay = input("Möchtest du noch einmal spielen? (Y/n): ").lower()  # Fordert den Benutzer auf, 'y' oder 'n' einzugeben und wandelt es in Kleinbuchstaben um (Y ist Standardwert)
        if replay == "y" or replay == "":  # Wenn der Benutzer 'y' oder Enter eingibt
            return True
        elif replay == "n":
            return False
        else:
            print("Fehler: Bitte gebe 'y' oder 'n' ein.")  # Gibt eine Fehlermeldung aus, wenn der Benutzer etwas anderes als 'y', Enter oder 'n' eingibt

def play_wordle(words, max_attempts=5):  # Definiert eine Funktion, um das Spiel Wordle zu spielen
    word_to_guess = random.choice(words)  # Wählt ein zufälliges Wort aus der Liste der Wörter
    attempts = 0  # Setzt die Anzahl der Versuche auf 0

    while attempts < max_attempts:  # Führt die Schleife aus, solange die Anzahl der Versuche kleiner ist als die maximale Anzahl der Versuche
        print("\n\nVersuch", attempts + 1, "von", max_attempts)  # Gibt die aktuelle Versuchsnummer aus (beginnend bei 1) (\n\n fügt zwei Leerzeilen hinzu)
        guess = input("Gebe ein Wort mit 5 Zeichen ein: ").upper()  # Fordert den Benutzer auf, ein Wort einzugeben und wandelt es in Großbuchstaben um
        if len(guess) != 5 :  # Überprüft, ob das eingegebene Wort genau 5 Zeichen lang ist
            print("Fehler: Das Wort muss genau 5 Zeichen lang sein.")  # Gibt eine Fehlermeldung aus, wenn das Wort nicht genau 5 Zeichen lang ist
            continue  # Springt zum nächsten Durchlauf der Schleife
        if not guess.isalpha():  # Überprüft, ob das eingegebene Wort nur Buchstaben enthält
            print("Fehler: Das Wort darf nur Buchstaben enthalten.")  # Gibt eine Fehlermeldung aus, wenn das Wort nicht nur Buchstaben enthält
            continue  # Springt zum nächsten Durchlauf der Schleife

        feedback = ''  # Initialisiert die Feedback-Variable als leeren String
        for i in range(len(word_to_guess)):  # Durchläuft jedes Zeichen im zu erratenden Wort
            if guess[i] == word_to_guess[i]:  # Überprüft, ob das Zeichen an der gleichen Position im eingegebenen Wort und im zu erratenden Wort gleich ist
                feedback += Fore.GREEN + guess[i] + Style.RESET_ALL  # Fügt das Zeichen in grüner Farbe zum Feedback hinzu, wenn es an der gleichen Position ist
            elif guess[i] in word_to_guess:  # Überprüft, ob das Zeichen im zu erratenden Wort vorkommt, aber nicht an der gleichen Position
                feedback += Fore.BLUE + guess[i] + Style.RESET_ALL  # Fügt das Zeichen in blauer Farbe zum Feedback hinzu, wenn es im Wort vorkommt, aber nicht an der gleichen Position
            else:  # Wenn das Zeichen weder im Wort vorkommt noch an der gleichen Position ist
                feedback += '\u25A0'  # Fügt ein schwarzes Quadrat zum Feedback hinzu

        print("\n", feedback)  # Gibt das Feedback aus

        if feedback.count(Fore.GREEN) == len(word_to_guess):  # Überprüft, ob die Anzahl der grünen Zeichen gleich der Länge des zu erratenden Wortes ist
            print("\nDu hast gewonnen! Das Wort war:", word_to_guess) # Gibt eine Gewinnnachricht und das zu erratende Wort aus
            if not restart_menu():  # Wenn das Spiel nicht erneut gestartet werden soll
                break  # Beendet die Schleife
            else:  # Wenn das Spiel erneut gestartet werden soll
                word_to_guess = random.choice(words)  # Wählt ein neues zufälliges Wort aus der Liste der Wörter
                attempts = 0  # Setzt die Anzahl der Versuche auf 0
                continue  # Startet die Schleife erneut

        attempts += 1  # Erhöht die Anzahl der Versuche um 1

    if attempts == max_attempts:
        print("\nDu hast verloren. Das Wort war:", word_to_guess)  # Gibt eine Verlustnachricht und das zu erratende Wort aus, wenn die maximale Anzahl der Versuche erreicht ist

    if restart_menu():
        play_wordle(words)  # Startet das Spiel erneut

words = load_words('words.txt')  # Lädt die Wörter aus der Datei 'words.txt'
play_wordle(words)  # Startet das Spiel Wordle mit den geladenen Wörtern