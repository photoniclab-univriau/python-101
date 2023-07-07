import pandas
import cv2


def analyse_data(path_csv):
    # sum of x, y, z
    # avg of x, y, z

    df_xyz = pandas.read_csv(path_csv)

    return {
        "avg_x": df_xyz["x"].mean(),
        "avg_y": df_xyz["y"].mean(),
        "avg_z": df_xyz["z"].mean(),
        "sum_x": df_xyz["x"].sum(),
        "sum_y": df_xyz["y"].sum(),
        "sum_z": df_xyz["z"].sum(),
    }

def analyse_img(img_path):
    image = cv2.imread(img_path)
    data = {
        "filename": img_path,
        "rgb_mean": image.mean()
    }
    return data
