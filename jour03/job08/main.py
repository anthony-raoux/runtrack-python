def fonc_owo(type, saison):
    if (type == "fruits" and saison == "hiver"):
        print("orange, mandarine, kiwi")
    if (type == "fruits" and saison == "été"):
        print("Poire, fraise, cassis")
    if (type == "légumes" and saison == "hiver"):
        print("carotte, topinambour, endive")
    if (type == "légumes" and saison == "été"):
        print("artichaut, aubergine, navet")

fonc_owo("fruits", "hiver")
fonc_owo("fruits", "été")
fonc_owo("légumes", "hiver")
fonc_owo("légumes", "été")