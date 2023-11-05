# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 11:37:44 2022

@author: Justin
"""

class Rotor (object):
    def __init__(self, wires):
        self.position = 0
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ."
        self.wiring = {}
        self.originalWiring = {}
        self.rotation = []
        self.setupWiring(wires)
        
    def rotate(self):
        count = 0
        rotating = list(self.wiring.keys())
        while count < 28:
            plug = rotating[count]
            if count == 27:
                plug2 = rotating[-1]
            else:
                plug2 = rotating[count + 1]
            self.wiring[plug] = self.wiring[plug2]
            count += 1

        
    def setupWiring(self, wires):
        count = 0
        insert = []
        while count < 28:
            self.wiring[wires[count][0]] = wires[count][1]
            self.originalWiring[wires[count][0]] = wires[count][1]
            insert.append(wires[count][0])
            insert.append(wires[count][1])
            self.rotation.append(insert)
            insert = []
            count += 1
            
    def switch(self, inlet):
        outlet = self.wiring[inlet]
        return outlet
    
    def reset(self):
        count = 0
        while count < 28:
            self.wiring[self.alphabet[count]] = self.originalWiring[self.alphabet[count]]
        
class Enigma (object):
    def __init__(self):
        self.rotor1 = Rotor((("A", "."), (".", "A"), ("B", " "), (" ", "B"), ("C", "Z"), ("Z", "C"), ("D", "Y"), ("Y", "D"), ("E", "X"), ("X", "E"), ("F", "W"), ("W", "F"), ("G", "V"), ("V", "G"), ("H", "U"), ("U", "H"), ("I", "T"), ("T", "I"), ("J", "S"), ("S", "J"), ("K", "R"), ("R", "K"), ("L" ,"Q"), ("Q", "L"), ("M", "P"), ("P", "M"), ("N", "O"), ("O", "N")))
        self.rotor2 = Rotor((("A", "B"), ("B", "A"), ("C", "D"), ("D", "C"), ("E", "F"), ("F", "E"), ("G", "H"), ("H", "G"), ("I", "J"), ("J", "I"), ("K", "L"), ("L", "K"), ("M", "N"), ("N", "M"), ("O", "P"), ("P", "O"), ("Q", "R"), ("R", "Q"), ("S", "T"), ("T", "S"), ("U", "V"), ("V", "U"), ("W", "X"), ("X", "W"), ("Y", "Z"), ("Z", "Y"), (" ", "."), (" ", ".")))
        self.rotor3 = Rotor((("A", "C"), ("C", "A"), ("B", "D"), ("D", "B"), ("E", "G"), ("G", "E"), ("F", "H"), ("H", "F"), ("I", "K"), ("K", "I"), ("J", "L"), ("L", "J"), ("M", "O"), ("O", "M"), ("N", "P"), ("P", "N"), ("Q", "S"), ("S", "Q"), ("R", "T"), ("T", "R"), ("U", "W"), ("W", "U"), ("V", "X"), ("X", "V"), ("Y", " "), (" ", "Y"), ("Z", "."), (".", "Z")))
        self.rotor4 = Rotor((("A", "D"), ("D", "A"), ("B", "E"), ("E", "B"), ("C", "F"), ("F", "C"), ("G", "I"), ("I", "G"), ("H", "J"), ("J", "H"), ("K", "M"), ("M", "K"), ("L", "N"), ("N", "L"), ("O", "Q"), ("Q", "O"), ("P", "R"), ("R", "P"), ("S", "U"), ("U", "S"), ("T", "V"), ("V", "T"), ("W", "Y"), ("Y", "W"), ("X", "."), (".", "X"), ("Z", " "), (" ", "Z")))
        self.rotor5 = Rotor((("A", "Q"), ("Q", "A"), ("B", "Z"), ("Z", "B"), ("C", "."), (".", "C"), ("D", "X"), ("X", "D"), ("E", "M"), ("M", "E"), ("F", "Y"), ("Y", "F"), ("G", "N"), ("N", "G"), ("H", " "), (" ", "H"), ("I", "T"), ("T", "I"), ("J", "O"), ("O", "J"), ("K", "R"), ("R", "K"), ("L", "S"), ("S", "L"), ("P", "U"), ("U", "P"), ("W", "V"), ("V", "W")))
        #self.rotor6 = Rotor(())
        #self.rotor7 = Rotor(())
        #self.rotor8 = Rotor(())
        #self.rotor9 = Rotor(())
        #self.rotor10 = Rotor(())
        self.plugboard = {}
        
    def setupRotors(self):
        rotors = []
        print("Select five rotors")
        while len(rotors) < 5:
            rotor = input("Select a rotor you want to use. There are 10 rotors. Enter a number between 1 and 10.")
            rotors.append(rotor)
        return rotors
            
                
    def setupPlugboard(self, inchar, outchar):
        self.plugboard[inchar] = outchar
        
    def code(self, inmess):
        outmes = ""
        char = ""
        count = 0
        count2 = 0
        change = input("How many letters do you want to change with the plugboard: ")
        while count < change:
            inchar = input("Enter the letter you want changed: ")
            outchar = input("Enter the letter you want it to become: ")
            self.setupPlugboard(inchar, outchar)
            count += 1
        count = 0
        rotors = self.setupRotors()
        for c in inmess:
            char = self.plugboard[c]
            char = self.rotor1.switch(char)
            self.rotor1.rotate()
            char = self.rotor2.switch(char)
            self.rotor2.rotate()
            char = self.rotor3.switch(char)
            self.rotor3.rotate()
            char = self.rotor4.switch(char)
            self.rotor4.rotate()
            char = self.rotor5.switch(char)
            self.rotor5.rotate()
            char = self.rotor5.switch(char)
            self.rotor5.rotate()
            char = self.rotor4.switch(char)
            self.rotor4.rotate()
            char = self.rotor3.switch(char)
            self.rotor3.rotate()
            char = self.rotor2.switch(char)
            self.rotor2.rotate()
            char = self.rotor1.switch(char)
            self.rotor1.rotate()
            outmes += char
            count += 1
            if count%2 == 0:
                if count2%2 == 0:
                    self.rotor1.rotate()
                    self.rotor3.rotate()
                    self.rotor5.rotate()
                else:
                    self.rotor2.rotate()
                    self.rotor4.rotate()
                count2 += 1
                count += 1
        self.rotor1.reset()
        self.rotor2.reset()
        self.rotor3.reset()
        self.rotor4.reset()
        self.rotor5.reset()
        return outmes
        
machine = Enigma()
encoded = machine.code("XXXXXXXXXX")
print(encoded)
print(machine.code(encoded))