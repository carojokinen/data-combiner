import os


def alusta_csvtiedostot():
    file = "yhdistetty.csv"
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("file deleted")
    else:
        print("file not found")

    with open("yhdistetty.csv", "w") as file:
        eka_rivi = f"PVM;TIME;CH;E;J;T\n"
        file.write(eka_rivi)
        print("eka ready!")

    vfile = "virhedata.csv"
    if(os.path.exists(vfile) and os.path.isfile(vfile)):
        os.remove(vfile)
        print("file deleted")
    else:
        print("file not found")

    with open("virhedata.csv", "w") as vfile:
        eka_vrivi = f"PVM;TIME;tiedosto virhelen; rivisisalto\n"
        vfile.write(eka_vrivi)
        print("eka ready!")

    

def lue_tiedostot():
    tiedostot = []
    path_of_the_directory= "Percodata"
    print("Files and directories in a specified path:")
    for filename in os.listdir(path_of_the_directory):
        f = os.path.join(path_of_the_directory,filename)
        if os.path.isfile(f):
            tiedostot.append(f)
    return tiedostot
 

def yhdista_tiedosto(tiedoston_nimi):
    txt_data = []
    virhe_data = []
    with open(tiedoston_nimi) as file:
        for rivi in file:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(" ")
            if osat[0] == "MEM" and len(osat) != 17:
                virhe_data.append([tiedoston_nimi, osat])
#                raise ValueError(tiedoston_nimi + ", len = " + str(len(osat)))
            elif osat[0] == "MEM":
                osat[3] = "20"+osat[3]
                lisattava_data =[osat[3], osat[4], osat[8], osat[12], osat[14], osat[16]]
                txt_data.append(lisattava_data)
#        print(txt_data)

    with open("yhdistetty.csv", "a") as csv_file:
        for lista in txt_data:
            rivi = f"{lista[0]};{lista[1]};{lista[2]};{lista[3]};{lista[4]};{lista[5]}\n"
            csv_file.write(rivi)

    with open("virhedata.csv", "a") as virhecsv_file:
        for lista in virhe_data:
            rivi = f"{lista[0]};{lista[1]}\n"
            virhecsv_file.write(rivi)


def main():
    alusta_csvtiedostot()
    txt_tiedostot = lue_tiedostot()
    for tiedosto in txt_tiedostot:
        yhdista_tiedosto(tiedosto)
    print("Ready!")

# yhdista_tiedosto("Percodata/pm2106010103.txt")

main()

