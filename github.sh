#!/bin/bash
git init
git add .
git commit -m "注释语句"
git remote add origin https://github.com/hzmaths/algorithm
git pull origin master
git push -u origin master
