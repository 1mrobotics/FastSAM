# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from pkg_resources import parse_requirements
from setuptools import find_packages, setup
from pathlib import Path

setup(
    name="fastsam",
    version="0.1.1",
    install_requires=list(map(str, parse_requirements((Path(__file__).parent / 'requirements.txt').read_text()))),
    packages = ['fastsam'],
    url="https://github.com/CASIA-IVA-Lab/FastSAM",
)
