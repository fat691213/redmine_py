#!/usr/bin/env python

from redminelib import Redmine


redmine=Redmine(URL,username='***',password='***')

PList=redmine.project.all()

