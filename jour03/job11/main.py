def time_to_text(x):
    heure = x // 60
    minutes_restante = (x) % 60

    if heure == 1 and minutes_restante == 1:
        print(f"{heure} heure et {minutes_restante} minute")
    else:
        print(f"{heure} heures et {minutes_restante} minutes")

time_to_text(60)
time_to_text(120)
time_to_text(160)
time_to_text(250)
time_to_text(680)
