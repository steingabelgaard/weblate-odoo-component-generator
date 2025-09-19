# -*- coding: utf-8 -*-
# Copyright 2018 ACSONE SA/NV (<http://acsone.eu>)

import contextlib
import subprocess
import tempfile

import giturlparse


@contextlib.contextmanager
def temp_git_clone(repository, branch, use_ssh=False):
    repository_https = repository
    with tempfile.TemporaryDirectory() as repo_dir:
        subprocess.check_call([
            'git',
            'clone',
            repository_https,
            '-b', branch,
            '--depth', '1',
            repo_dir,
        ])
        yield repo_dir
