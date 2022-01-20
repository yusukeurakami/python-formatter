import glob
import os
import tqdm
import random
import shutil


import argparse
def main(args):
    target_folder = args.target_folder
    source_folder = args.source_folder
    makedir_list = ["/depth", "/image", "/instance", "/poses"]
    extention_list = [".png", ".png", ".png", ".txt"]

    image_src_path = source_folder + "/image"
    source_selected = [x.split(".")[0] for x in os.listdir(image_src_path)]
    source_list = sorted(source_selected, key=lambda x: int(x))
    source_n = len(source_list)
    print("size of source folder: ", source_n)

    for extention_idx, makedir in enumerate(makedir_list):
        dist_path = target_folder + makedir
        src_path = source_folder + makedir
        if not os.path.isdir(dist_path):
            os.makedirs(dist_path)

        for idx in tqdm.tqdm(range(source_n)):
            print(f"Rendering scene {idx:06d} / {source_n - 1:06f}")
            ext = extention_list[extention_idx]
            name = f"{idx:06d}"
            src = src_path + "/" + f"{idx}" + ext
            dist = dist_path + "/" + name + ext
            print(src, dist)
            shutil.copy(src, dist)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="df")
    parser.add_argument(
        "--source_folder",
        type=str,
        default="/home/urakamiy/datasets/roboeye/2020_12_20_issacSim_synthetic/6010018CSV",
        # default="/home/urakamiy/robot/output/6010018CSV_dataset",
        help="",
    )
    parser.add_argument(
        "--target_folder",
        type=str,
        default="/home/urakamiy/datasets/roboeye/2020_12_20_issacSim_synthetic/6010018CSV_re",
        help="",
    )
    parser.add_argument("--sample_n", type=int, default=2000)

    args = parser.parse_args()
    main(args)
