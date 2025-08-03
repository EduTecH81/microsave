import json
import os
import datetime
import random

FITXER_DADES = "dades.json"

FRASES_MOTIVADORES = [
    "Cada euro compta! 💪",
    "Estalviar avui és invertir en tu mateix.",
    "No cal ser ric per començar, cal començar per ser ric.",
    "Els petits hàbits fan grans canvis. 👊",
    "1 € avui val més que 0 € sempre."
]

# Si no existeix l'arxiu, el crea
def carregar_dades():
    if not os.path.exists(FITXER_DADES):
        with open(FITXER_DADES, 'w') as f:
            json.dump([], f)
    with open(FITXER_DADES, 'r') as f:
        return json.load(f)

def guardar_dades(dades):
    with open(FITXER_DADES, 'w') as f:
        json.dump(dades, f, indent=4)

def afegir_estalvi():
    try:
        quantitat = float(input("Introdueix la quantitat a estalviar (€): "))
        if quantitat <= 0:
            print("⚠️ La quantitat ha de ser positiva.")
            return
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        entrada = {"data": data, "quantitat": quantitat}
        dades = carregar_dades()
        dades.append(entrada)
        guardar_dades(dades)
        print(f"✅ Has afegit {quantitat:.2f} € a l'estalvi.")
        print("💡", random.choice(FRASES_MOTIVADORES))
    except ValueError:
        print("⚠️ Introdueix un número vàlid.")

def veure_total():
    dades = carregar_dades()
    total = sum(item["quantitat"] for item in dades)
    print(f"\n📊 Total estalviat: {total:.2f} €")

def veure_historial():
    dades = carregar_dades()
    if not dades:
        print("Encara no hi ha registres d'estalvi.")
        return
    print("\n🗂️ Historial d'estalvi:")
    for item in dades:
        print(f" - {item['data']} -> {item['quantitat']:.2f} €")

def menu():
    while True:
        print("\n====== MicroSave 💰 ======")
        print("1. Afegir estalvi")
        print("2. Veure total estalviat")
        print("3. Veure historial")
        print("4. Sortir")
        opcio = input("Selecciona una opció: ")
        if opcio == "1":
            afegir_estalvi()
        elif opcio == "2":
            veure_total()
        elif opcio == "3":
            veure_historial()
        elif opcio == "4":
            print("Fins aviat! 👋")
            break
        else:
            print("Opció no vàlida.")

if __name__ == "__main__":
    menu()
