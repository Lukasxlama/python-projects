def oktal_zu_dezimal(oktal):
    ergebnis = 0
    for zeichen in oktal:
        if zeichen.isdigit():
            if int(zeichen) >= 8:
                print(f"Ungültige Zahl im Oktalsystem: {oktal}")
                return
            ergebnis = (ergebnis + int(zeichen)) * 8
        else:
            print(f"Ungültige Zahl im Oktalsystem: {oktal}")
            return
    return ergebnis // 8


oktal_ = input("Bitte gib eine Zahl im Oktalsystem ein: ")
dezimal = oktal_zu_dezimal(oktal_)

if dezimal is not None:
    print(f"{oktal_} im Oktalsystem entspricht {dezimal} im Dezimalsystem.")