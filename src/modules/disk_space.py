import os
from string import ascii_uppercase
import matplotlib.pyplot as plt
import numpy as np
from shutil import disk_usage
import logging
from functools import lru_cache

logging.basicConfig(level=logging.DEBUG,
                    filename=f"{__name__}.log",
                    filemode='a',
                    format="%(filename)s - %(asctime)s - %(funcName)s - %(levelname)s: %(message)s"
                    )
logging.getLogger('matplotlib.font_manager').disabled = True  # To suppress log-trash from matplotlib
logging.getLogger('matplotlib.pyplot').disabled = True


@lru_cache
def scan_disks():
    logging.debug(f"\"scan_disks\": module launched")
    directory = []
    for index, _ in enumerate(ascii_uppercase):
        if os.path.exists(f"{ascii_uppercase[index]}:"):
            directory.append(f"{ascii_uppercase[index]}:/")
    logging.info(directory)
    return directory


@lru_cache
def storage_info(path: str) -> list[float]:
    total, used, free = disk_usage(path)
    logging.info(f'{path} -> Total: {"%.1f" % (total / 10 ** 9)},'
                 f' Used: {"%.1f" % (used / 10 ** 9)}, Free: {"%.1f" % (free / 10 ** 9)}')
    return [total / 10 ** 9, used / 10 ** 9, free / 10 ** 9]


def space_on_disks_graph(full_path_to_save_image, image_name):  # save info about using storage in png
    logging.debug(f"\"space_on_disks_graph\": module launched")
    disks = scan_disks()
    storages = tuple(i[:2] for i in disks)
    lst_used = []
    lst_free = []
    for disk in disks:
        area = storage_info(disk)
        lst_used.append(area[1])
        lst_free.append(area[2])
    storage_area = {
        'Used': np.array(lst_used),
        'Free': np.array(lst_free),
    }
    width = 0.75  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()
    bottom = np.zeros(len(storages))

    for _, area in storage_area.items():
        p = ax.bar(storages, area, width, label=_, bottom=bottom, edgecolor="black")
        bottom += area

        ax.bar_label(p)

    ax.set_title("Disk space usage")
    ax.legend()

    # labels name
    plt.ylabel("Gigabytes")
    plt.xlabel("Disks")

    # save as png
    try:
        plt.savefig(f"{full_path_to_save_image}/{image_name}.png")
        logging.debug(f"png file has been saved to: {full_path_to_save_image}")
    except FileNotFoundError:
        logging.error("The function accepted a non-existent path")


# space_on_disks_graph("W:/trash_snake_project/updates", "MyMemory")
