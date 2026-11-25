# The Battery's Last Text to Its Charger

A [make.fun](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) entry: the phone battery's final one-line text message to the charger it waited for all day.

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/emafajriana/u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/emafajriana/u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

## The entry

> 1%. I'm not dying, I'm quitting. You had me at 100% this morning and still took the other phone to lunch. Good luck with him.

## How it works

`main.py` (standard library only) validates the line against the competition gate — UTF-8, 1–200 characters, a single line, not only whitespace — writes it to `entry.txt` in the output directory, then reads the file back to prove it is byte-for-byte the text it meant to send.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
