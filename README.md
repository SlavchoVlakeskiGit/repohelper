# repohelper

A small Python CLI I built to make it faster to start clean side projects, practice repos, and portfolio projects.

The main idea is simple: when I start a small repo, I usually end up recreating the same folders, starter files, and placeholders. This tool saves that setup time without trying to generate a full app or replace bigger tools.

## What it does

`repohelper` creates small starter repos using a few opinionated profiles.

Current profiles:
- `python-tool`
- `python-app`
- `java-console`

It can:
- list available profiles
- check whether a project name looks valid
- preview what it would create with `--dry-run`
- generate folders and starter files
- avoid overwriting existing folders unless `--force` is used

## Why I built it

I wanted a small utility for my own workflow.

When starting practice projects or portfolio repos, I kept repeating the same setup steps by hand. I did not want a full scaffolding engine. I just wanted something small that gives me a clean starting point.

## Example commands

```bash
python main.py about
python main.py profiles
python main.py check-name expense-tracker
python main.py create expense-tracker --profile python-app --dry-run
python main.py create expense-tracker --profile python-app