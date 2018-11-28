# encoding:utf-8
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 输入邮件地址, 口令和POP3服务器地址:
email = 'tianhainingwangyou@163.com'  # input('Email: ')
password = 'taotao521'  # input('Password: ')
pop3_server = 'pop3.163.com'  # input('POP3 server: ')

# -*- encoding: utf-8 -*-

import imaplib
import email
import argparse
import logging


class GetEmail(object):

    def __init__(self):
        self.map4 = None
        self.username = "tianhaining@daokoudai.com"
        self.password = "wangyou521A"

    def process(self):
        self.map4 = imaplib.IMAP4_SSL("imap.exmail.qq.com", 993)
        self.map4.login(self.username, self.password)
        self.map4.select()
        self.filter_data("war package for online from jenkins is ready", True)
        self.map4.close()
        self.map4.logout()

    def filter_data(self, signature, is_mo):
        typ, data = self.map4.search(None, 'Subject', signature)
        print typ, data



get_email = GetEmail()
get_email.process()
