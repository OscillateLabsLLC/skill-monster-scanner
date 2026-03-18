import json
from os.path import expanduser, isdir, isfile, join
from pprint import pprint
from shutil import copy
from sys import argv

try:
    import tomllib
except ImportError:
    import tomli as tomllib


def get_skill_json(skill_dir: str, lang_code: str = "en-us"):
    print(f"skill_dir={skill_dir}")
    skill_json = join(skill_dir, f"skill_monster_scanner/locale/{lang_code}/skill.json")
    skill_spec = get_skill_data(skill_dir, lang_code)
    pprint(skill_spec)
    try:
        with open(skill_json, encoding="utf-8") as f:
            current = json.load(f)
    except Exception as e:
        print(e)
        current = None
    if current != skill_spec:
        print("Skill updated. Writing skill.json")
        with open(skill_json, "w+", encoding="utf-8") as f:
            json.dump(skill_spec, f, indent=4, ensure_ascii=False)
    else:
        print("No changes to skill.json")


def get_skill_data(skill_dir: str, lang_code: str = "en-us"):
    skill_data = {
        "skill_id": "skill_monster_scanner.oscillatelabsllc",
        "source": "https://github.com/oscillatelabsllc/skill-monster-scanner",
        "package_name": "skill-monster-scanner",
        "pip_spec": "skill-monster-scanner",
        "license": "Apache-2.0",
        "author": ["Oscillate Labs <mike@oscillatelabs.net>"],
        "icon": "",
        "images": [],
        "name": "skill-monster-scanner",
        "description": "An OVOS voice skill that scans for monsters under the bed",
        "examples": [],
        "tags": ["ovos", "neon", "kids", "fun"],
        "version": "",
    }

    skill_dir = expanduser(skill_dir)
    if not isdir(skill_dir):
        raise FileNotFoundError(f"Not a Directory: {skill_dir}")
    pyproject = join(skill_dir, "pyproject.toml")
    if not isfile(pyproject):
        raise FileNotFoundError(f"pyproject.toml not found: {pyproject}")
    with open(pyproject, "rb") as f:
        data = tomllib.load(f)
    project = data.get("project", {})
    skill_data["package_name"] = project.get("name", "Unknown")
    skill_data["name"] = project.get("name", "Unknown")
    skill_data["description"] = project.get("description", "Unknown")
    skill_data["pip_spec"] = project.get("name", "Unknown")
    lic = project.get("license", {})
    skill_data["license"] = lic.get("text", lic.get("file", "Unknown"))
    skill_data["tags"] = project.get("keywords", ["ovos", "neon"])
    skill_data["version"] = project.get("version", "")

    locale_skill_json = join(skill_dir, f"skill_monster_scanner/locale/{lang_code}/skill.json")
    if isfile(locale_skill_json):
        with open(locale_skill_json, encoding="utf-8") as f:
            skill_json = json.load(f)
            skill_data["examples"] = skill_json.get("examples", [])
    return skill_data


if __name__ == "__main__":
    supported_langs = ["en-us"]
    for lang in supported_langs:
        get_skill_json(argv[1], lang_code=lang)
    copy(f"{argv[1]}/skill_monster_scanner/locale/en-us/skill.json", f"{argv[1]}/skill.json")
