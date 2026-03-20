# RepoHelper

RepoHelper is a small Python CLI I made to speed up the repetitive part of starting new repos.

A lot of my smaller projects begin the same way: a README, a `.gitignore`, a basic folder layout, and a couple of starter files. None of that is hard, but doing it over and over gets old fast, so I ended up building a small tool to handle that part instead of repeating it every time.

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

This was mainly a workflow tool for myself. I did not want a big scaffold generator with endless options. I wanted something opinionated and small enough to understand in one sitting.

One thing I liked while building it was adding `--dry-run`, because it made it much easier to check the output before writing anything to disk.

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

## Notes

I kept the scope narrow on purpose. The goal here was not to clone a full template engine. It was just to remove a bit of setup friction when starting small repos.

## Possible next improvements

- custom templates
- interactive prompts
- optional Git initialization
- optional license selection

It’s one of those small tools that’s not impressive on its own, but saves time every time I start something new.
