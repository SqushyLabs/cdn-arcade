import re
import subprocess
from pathlib import Path


def format_data_json(project, version, json_file):
    print(f"Updating {json_file} for {project} @ {version}")
    with open(json_file, 'r') as file:
        data = file.read()

    PROJECT = "AXO_ESCAPE"
    VERSION = "67bb8ab689d3eecbd8ec84ff979ab5c4a05b9fca"
    if "cdn-squshy-arcade" in data:
        return

    sub_folders = ["images", "media", "fonts"]
    for folder in sub_folders:
        data = re.sub(fr'"{folder}/(.*?)"', fr'"https://cdn.jsdelivr.net/gh/SqushyLabs/cdn-squshy-arcade@{VERSION}/{PROJECT}/images/\1"', data)

    with open(json_file, "w") as text_file:
        text_file.write(data)


if __name__ == '__main__':
    version = subprocess.check_output("git rev-parse HEAD").decode("utf-8")
    data_jsons = [x for x in Path("./").resolve().rglob("*data.json")]
    for data_file in data_jsons:
        format_data_json(data_file.parent.stem, version, data_file)

