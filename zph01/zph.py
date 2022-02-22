#!/usr/local/bin/python3
# coding: utf-8

# ZPH01 - zph.py
# 2/22/22 19:10
#

__author__ = "Benny 55<benny.think@gmail.com>"

import serial
import re


class ZPH01:
    def __init__(self, port='/dev/serial1', debug=False):
        self.ser = serial.Serial(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)
        self.voc_map = {
            "00": "Good",
            "01": "Fair",
            "02": "Moderate",
            "03": "Poor"
        }
        # EU regulation https://en.wikipedia.org/wiki/Particulates#European_Union
        self.pm_25_range = {
            "0-10": "Good",
            "10-20": "Fair",
            "20-25": "Moderate",
            "25-50": "Poor",
            "50-75": "Very Poor",
            "75-800": "Extremely Poor",
            "800-100000": "Hazardous"
        }
        self.debug = debug

    def read_data(self):
        raw_data = self.ser.read(10).hex()
        data = re.findall("..", raw_data)
        if self.debug:
            print(data)
        pm_25 = int(data[3], 16) + int(data[4], 16) / 100
        voc = data[7]
        return pm_25, self.voc_map[voc]

    def output(self):
        pm, voc = self.read_data()
        result = {
            "VOC status": voc,
            "PM 2.5 percent": round(pm, 4),
            "PM 2.5 count": round(pm * 600, 4),
            "PM 2.5 level": round(pm * 20, 4)

        }
        pm25_status = "N/A"
        for r, value in self.pm_25_range.items():
            low, high = [int(i) for i in r.split("-")]
            if low <= pm * 20 < high:
                pm25_status = value
                break

        result["PM 2.5 status"] = pm25_status
        return result

    def __del__(self):
        self.ser.close()


if __name__ == '__main__':
    zph = ZPH01()
    print(zph.output())
