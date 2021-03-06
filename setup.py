#!/usr/bin/env python
# coding=utf-8
"""A module to interact with Cisco devices running IOS-XR."""

# Copyright 2015 Netflix. All rights reserved.
# Copyright 2016 BigWaveIT. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from setuptools import setup, find_packages


with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

version = '0.53'

setup(
    name='pyIOSXR',
    version=version,
    py_modules=['pyIOSXR'],
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    description='Python API to interact with network devices running IOS-XR',
    author='Elisa Jasinska, Mircea Ulinic',
    author_email='elisa@bigwaveit.org, mircea@cloudflare.com',
    url='https://github.com/fooelisa/pyiosxr/',
    download_url='https://github.com/fooelisa/pyiosxr/tarball/%s' % version,
    keywords=['IOS-XR', 'IOSXR', 'Cisco', 'networking'],
    classifiers=[],
)
