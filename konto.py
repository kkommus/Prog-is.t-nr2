def konto_haldur(algne_saldo, toiming, summa):
    if toiming == 'deposiit':
        uus_saldo = algne_saldo + summa
    elif toiming == 'valjavote':
        if summa > algne_saldo:
            return "Viga: Kontol pole piisavalt raha.", algne_saldo
        uus_saldo = algne_saldo - summa
    else:
        return "Viga: Tundmatu toiming. Kasuta 'deposiit' või 'valjavote'.", algne_saldo
    
    return uus_saldo

# Põhiprogramm
algne_saldo = float(input("Sisesta algne saldo: "))
while True:
    print(f"\nPraegune saldo: {algne_saldo}€")
    toiming = input("Sisesta toiming ('deposiit' või 'valjavote', lõpetamiseks 'lõpeta'): ").strip().lower()
    
    if toiming == "lõpeta":
        print(f"Lõplik saldo: {algne_saldo}€")
        break

    if toiming not in ["deposiit", "valjavote"]:
        print("Viga: Tundmatu toiming! Kasuta 'deposiit' või 'valjavote'.")
        continue

    try:
        summa = float(input("Sisesta summa: "))
        if summa <= 0:
            print("Viga: Sisestatud summa peab olema positiivne!")
            continue
    except ValueError:
        print("Viga: Palun sisesta korrektne numbriline summa!")
        continue

    tulemus = konto_haldur(algne_saldo, toiming, summa)
    if isinstance(tulemus, tuple):
        print(tulemus[0])
    else:
        algne_saldo = tulemus
        print(f"Tehing edukas! Uus saldo: {algne_saldo}€")
