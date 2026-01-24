# Invoke is broken on Python 3.11
# https://github.com/pyinvoke/invoke/issues/833#issuecomment-1293148106
import inspect
import os
import re
import sys
from typing import Optional

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import invoke  # pylint: disable=wrong-import-position
from invoke import task  # pylint: disable=wrong-import-position

# Specifying encoding because Windows crashes otherwise when running Invoke
# tasks below:
# UnicodeEncodeError: 'charmap' codec can't encode character '\ufffd'
# in position 16: character maps to <undefined>
# People say, it might also be possible to export PYTHONIOENCODING=utf8 but this
# seems to work.
# FIXME: If you are a Windows user and expert, please advise on how to do this
# properly.
sys.stdout = open(  # pylint: disable=consider-using-with
    1, "w", encoding="utf-8", closefd=False, buffering=1
)


def run_invoke(
    context,
    cmd,
    environment: Optional[dict] = None,
    warn: bool = False,
) -> invoke.runners.Result:
    def one_line_command(string):
        return re.sub("\\s+", " ", string).strip()

    return context.run(
        one_line_command(cmd),
        env=environment,
        hide=False,
        warn=warn,
        pty=False,
        echo=True,
    )


REPLACEMENTS = {
    '‘': "'", '’': "'",  # single quotes
    '“': '"', '”': '"',  # double quotes
    '–': '-', '—': '-',  # dashes
    '…': '...',  # ellipsis
    '•': '*',  # bullet
    '′': "'", '″': '"',  # prime marks
    '‹': '<', '›': '>',  # single angle quotes
    '«': '<<', '»': '>>',  # double angle quotes
}

pattern = re.compile(
    "|".join(map(re.escape, REPLACEMENTS.keys())))


def replace(match):
    char = match.group(0)
    return REPLACEMENTS.get(char, '###')  # replace or remove non-ASCII


def normalize_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    normalized_content = pattern.sub(replace, content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(normalized_content)


@task(default=True)
def list_tasks(context):
    clean_command = """
        invoke --list
    """
    run_invoke(context, clean_command)


@task
def lint_toc(context):
    run_invoke(context, "doctoc README.md")


@task
def lint_format(context):
    run_invoke(context, "prettier --write --print-width 80 --prose-wrap always README.md")
    normalize_file("README.md", "README.md")


@task(aliases=["l"])
def lint(context):
    lint_format(context)
    lint_toc(context)
