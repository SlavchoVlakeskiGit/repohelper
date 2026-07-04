# RepoHelper

RepoHelper is a Python CLI I made to speed up the repetitive part of starting new repos.

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

That previews the folders and files before anything is actually created.

## Possible next improvements

- custom templates
- interactive prompts
- optional Git initialization
- optional license selection

It’s one of those small tools that’s not impressive on its own, but saves time every time I start something new.
