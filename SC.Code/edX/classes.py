"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
*********************
* Created on Sat Aug  7 22:24:26 2021
*********************
* fechas.py
*********************
* Version: 001
*********************
* @authors: SCelis
*********************
* Copyright (c) 2021 SCelis
* All Rights Reserved.
*********************
* Pruebas con fechas
*********************
* ChangeLog:
*
*   iSCelis@rev 001: Create
*
**********
* TODO: ??
**********
* Description: Pruebas con fechas
****
*
"""
class Car:
    speed = 0
    started = False
 
    def start(self):
        self.started = True
        print("Car started, let's ride!")
 
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")
 
    def stop(self):
        self.speed = 0
        print('Halting')