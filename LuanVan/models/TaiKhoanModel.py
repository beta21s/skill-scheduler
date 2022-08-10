#!/usr/bin/env python
# -*- coding: utf-8 -*-

from LuanVan.models.DBConnect import DBConnect

class TaiKhoan():
    db = None
    ten_dang_nhap = None
    mat_khau = None

    def __init__(self):
        self.db = DBConnect()

    def dangNhap(self):
        sql = '''SELECT * FROM `tai_khoan` WHERE `ten_dang_nhap` = %s AND `mat_khau` = SHA2(%s, 512)'''
        return self.db.select_one(sql, (self.ten_dang_nhap, self.mat_khau))