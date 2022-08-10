#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class config():
    SERVER = '0.0.0.0'
    PORT_SERVER = 3000
    DEBUG = True

    #
    # MQTT Server
    #
    MQTT_SERVER = 'broker.hivemq.com'
    MQTT_PORT = 1883

    #
    # MySQL Server
    #
    MYSQL = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    DATABASE = 'skill_scheduler'

    #
    # Peerjs Server
    #
    PEER_SERVER = 'peer.vlute.edu.vn'
    PEER_SERVER_PORT = '443'
    PEER_SERVER_PATH = '/peerjs'

    #
    # STUN; TURN Server
    #
    STUN_SERVER = 'stun:stun.l.google.com:19302'
    TURN_SERVER = 'turn:peer.vlute.edu.vn:3478?transport=tcp'
    TURN_USER = 'admin'
    TURN_PASSWORD = 'admin'

    #
    # SocketIO
    #
    IO_SERVER = 'https://peer.vlute.edu.vn'
    IO_SERVER_PORT = '443'