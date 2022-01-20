#!/usr/bin/env bash

function format {

    # import sorter options to make it compatible with black
    isort --line-length=120 --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses -n $1

    # PEP8 compliant formatter
    black --skip-string-normalization --line-length 120 $1

    # Code style checker to checking if code is compliant with PEP8, and also check the programming error
    flake8 --max-line-length=120 --ignore=E203,E266,E402,E501,W503 $1

}
