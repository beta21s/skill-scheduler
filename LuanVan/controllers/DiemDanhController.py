#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

from LuanVan import app
from flask import render_template, request, flash, redirect, url_for, session, jsonify
import os, glob
from PIL import Image

path = "/"

@app.route(path + "")
def getViewDiemDanh():
    session['id_tai_khoan'] = 5
    return render_template("diem-danh.html")

@app.route(path + "", methods=['POST'])
def postLuuFileAnh():
    file = request.files['file']
    image = Image.open(file)

    ten_file = str(uuid.uuid1()) + ".png"
    dg_file = os.path.join("LuanVan/static/diem-danh", ten_file)
    image.save(dg_file)

    session['is_diem_danh'] = True
    return ''