#!/usr/bin/python3
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/devbops_blog_microservice/")

def application(environ, start_response):
   from devbops_blog_microservice import app as application
   return application(environ, start_response)