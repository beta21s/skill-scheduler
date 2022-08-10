#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

from LuanVan import app
from flask import render_template, request, flash, redirect, url_for, session, jsonify
from LuanVan.models.TaiKhoanModel import TaiKhoan
import os, glob
from PIL import Image

path = "/login"

@app.route(path + "")
def getViewDN():
    return render_template("login.html")

@app.route(path + "", methods=['POST'])
def postDangNhap():
    tendn = str(request.form.get("tendn")).strip()
    mat_khau = str(request.form.get("matkhau")).strip()

    tk = TaiKhoan()
    tk.ten_dang_nhap = tendn
    tk.mat_khau = mat_khau
    data = tk.dangNhap()
    if data:
        session['isLogin'] = True
        session['id_tai_khoan'] = data['id_tai_khoan']
        return redirect(url_for('trangCaNhan'))
    else:
        session['isLogin'] = None
        flash('Đăng nhập thất bại')
        return redirect(url_for('getViewDN'))