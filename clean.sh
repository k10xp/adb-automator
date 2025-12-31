#!/bin/bash
python3 -m ruff format #TODO: use black
rm -rf .ruff_cache */__pycache__ node_modules */.pytest_cache