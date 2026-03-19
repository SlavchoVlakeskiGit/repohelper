# repohelper

A small Python CLI I built to make it faster to start clean side projects, practice repos, and portfolio projects.

The goal is simple: when I start a small repo, I usually end up recreating the same folders and starter files. This tool helps with that without trying to generate a full application.

## Current status

Early version. The CLI structure is in place and the basic commands are being built step by step.

## Planned v1 scope

- list available profiles
- check whether a project name looks valid
- create small repo starter structures
- support dry-run mode
- avoid overwriting existing folders by default

## Planned profiles

- `python-tool`
- `python-app`
- `java-console`

## Example commands

```bash
python main.py about
python main.py profiles
python main.py check-name my-project
python main.py create my-project --profile python-tool

### File: `requirements.txt`
```text