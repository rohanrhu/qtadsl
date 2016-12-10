# -*- coding: utf-8 -*-
# QtAdsl easy adsl tool for GNU/Linux
 # Copyright (C) 2008, Oğuzhan Eroğlu <rohanrhu2@gmail.com>
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 
from distutils.core import setup
from os import system

locales = []

translations = ["tr"]
for i in translations:
    locales.append(("share/locale/%s/LC_MESSAGES" % i, ["qtadsl/po/tr/LC_MESSAGES/qtadsl.mo"]))

datas = [("share/applications", ["data/qtadsl.desktop"]), ("share/pixmaps", ["qtadsl/icons/qtadsl.png"])]

datas.extend(locales)

setup(name = "qtadsl",
      version = "0.1.1",
      description = "Network tool for usb modems...",
      author = "Oğuzhan Eroğlu",
      author_email = "oguzhan@oguzhaneroglu.com",
      url = "http://qtadsl.googlecode.com",
      packages = ["qtadsl"],
      data_files = datas,
      scripts = ["data/qtadsl"])