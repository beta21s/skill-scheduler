#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, jsonify, current_app

class ToolsModel():
    @staticmethod
    def response(message, status=200):
        return jsonify(message=message, status=status)

    @staticmethod
    def getConfig(key):
        return current_app.config[key]

