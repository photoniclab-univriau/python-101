# buat sebuah fungsi dimana diberikan sebuah nama folder, output: list file yang ada di dalam folder tersebut

import pandas

from analysis import analyse_data, analyse_img
from utils import files_to_analyse

def main():
    csv_files = files_to_analyse("output", "csv")

    for csv_file in csv_files:
        output_xyz = analyse_data(csv_file)
        print(output_xyz)
    
    
    hasil_analsisis_citra = []
    img_files = files_to_analyse("citra", "jpg")
    
    for image_file in img_files:
        img_data = analyse_img(image_file)
        hasil_analsisis_citra.append(img_data)
        print(img_data)
    
    df_hasil_analisis = pandas.DataFrame(hasil_analsisis_citra)
    df_hasil_analisis.to_csv("hasil-analisis-citra.csv", index=False, sep=";"   )


if __name__ == "__main__":
    main()