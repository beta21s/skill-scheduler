#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

from LuanVan import app
from flask import render_template, request, flash, redirect, url_for, session, jsonify
from LuanVan.models.TaiKhoanModel import TaiKhoan
import os, glob
from PIL import Image

path = "/"

@app.route(path + "account")
def trangCaNhan():
    return render_template("profile.html")

@app.route(path + "share-screen")
def getViewShareScreen():
    return render_template("share-screen.html")