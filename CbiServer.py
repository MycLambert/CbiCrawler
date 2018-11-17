# -*- coding: utf-8 -*-
from flask import Flask
from InstrumentBooking import *



def main():
	session = requests.Session()
	session = sign_in(session)
#创建项目对象
	app = Flask(__name__)


if __name__ == '__main__':
	main()