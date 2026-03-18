# Monster Scanner Skill

[![Status: Active](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/OscillateLabsLLC/.github/blob/main/SUPPORT_STATUS.md)

## Upgrading to 2.0

Version 2.0 changes the skill entry point from `skill-monster-scanner.mikejgray` to `skill-monster-scanner.oscillatelabsllc`. This means your saved settings (e.g. the `scary` flag) will not carry over automatically.

To migrate your settings, copy your settings file:

```bash
# Mycroft/OVOS
cp ~/.config/mycroft/skills/skill-monster-scanner.mikejgray/settings.json \
   ~/.config/mycroft/skills/skill-monster-scanner.oscillatelabsllc/settings.json

# Neon
cp ~/.config/neon/skills/skill-monster-scanner.mikejgray/settings.json \
   ~/.config/neon/skills/skill-monster-scanner.oscillatelabsllc/settings.json
```

## About

A skill to help your children feel safe at night by scanning for monsters under the bed.

## Configuration

If you feel like being a monster yourself, you can set `scary` in the config to `true` and the skill will sometimes find a monster.

Under skill settings (`~/.config/mycroft/skills/skill-monster-scanner.oscillatelabsllc/settings.json`):

| Option  | Value   | Description                                                  |
| ------- | ------- | ------------------------------------------------------------ |
| `scary` | `false` | Whether or not to occasionally find a monster under the bed. |

Note: If you are running Neon, the skill settings file will be located at `~/.config/neon/skills/skill-monster-scanner.oscillatelabsllc/settings.json`.

## Examples

- "Are there monsters under my bed?"
- "Is the Boogeyman under the bed?"

## Credits

- Oscillate Labs

## Category

Fun

## Tags

ovos skill neon skill monster scanner kids children fun silly
