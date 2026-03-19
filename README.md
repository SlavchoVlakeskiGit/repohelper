# repohelper

A small Python CLI I built to speed up the boring part of starting a new repo.

I made it for the kind of projects I start often: side tools, practice apps, and portfolio repos. Instead of creating the same folders and starter files by hand every time, I can run one command and get a clean starting point.

Small Python CLI for setting up clean starter repos for side projects and portfolio work.

## What it can do

- list the available profiles
- check whether a project name looks valid
- preview output with `--dry-run`
- create folders and starter files
- avoid overwriting existing folders unless `--force` is used

## Profiles

### `python-tool`
A small Python utility or CLI-style repo.

### `python-app`
A simple Python project with `src/` and `tests/`.

### `java-console`
A basic Java console project.

## Why I built it

Most of my small repos start the same way:
- a README
- a `.gitignore`
- a basic folder layout
- a couple of starter files

That setup is not hard, but it is repetitive. I wanted a small tool that handles that part and gets me to the actual project faster.

## Example commands

```bash
python main.py about
python main.py profiles
python main.py check-name expense-tracker
python main.py create expense-tracker --profile python-app --dry-run
python main.py create expense-tracker --profile python-app
```

## Example output

```bash
python main.py create sample-tool --profile python-tool --dry-run
```

This previews the project folder, directories, and files before anything is written.

## Project structure

```text
repohelper/
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── main.py
├── repohelper/
│   ├── __init__.py
│   ├── cli.py
│   ├── constants.py
│   ├── generator.py
│   ├── profiles.py
│   ├── utils.py
│   └── validators.py
└── tests/
    ├── __init__.py
    ├── test_profiles.py
    └── test_validators.py
```

## Notes

This project is meant to stay narrow and useful.

It does not try to support every language, framework, or project type. The goal is just to make small repo setup faster, cleaner, and more consistent.
