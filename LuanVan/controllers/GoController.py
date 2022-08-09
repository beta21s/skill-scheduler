#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from LuanVan import app
from flask import render_template, request, flash, redirect, url_for, session, jsonify
from LuanVan.models.ToolsModel import ToolsModel
from LuanVan.models.Dicom2Png import Dicom2Png
from LuanVan.models.DicomInfo import DicomInfo
import os, glob

path = "/a-b"

def getListFiles(paths):
    res = []
    for path in os.listdir(paths):
        if os.path.isfile(os.path.join(paths, path)):
            res.append(path)
    return res

@app.route(path + "")
def getViewTrangChu():
    return render_template("template.html")

@app.route(path + "/xhn-spark")
def getViewXuatHuyetNaoSpark():
    listFile = getListFiles("LuanVan/static/dicom/xhn")
    return render_template("xuat-huyet-nao-spark.html", data=listFile)

@app.route(path + "/gan-rfcn")
def getViewXuatHuyetNao():
    listFile = getListFiles("LuanVan/static/dicom/gan")
    return render_template("gan-rfcn.html", data=listFile)

@app.route(path + "/ngu-gat")
def getViewNguGat():
    listFile = getListFiles("LuanVan/static/ngugat/")
    return render_template("ngu-gat.html", data=listFile)