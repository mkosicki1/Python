# CTRL + ALT + L-> AUTO - FORMATOWANIE
class Warcaby:

# POLE KLASOWE -> SŁOWNIK ZAWIERAJACY 8 SŁOWNIKÓW
    warcaby = {
            8:{1:"_", 2:"O", 3:"_", 4:"O", 5:"_", 6:"O", 7:"_", 8:"O"},
            7:{1:"O", 2:"_", 3:"O", 4:"_", 5:"O", 6:"_", 7:"O", 8:"_"},
            6:{1:"_", 2:"O", 3:"_", 4:"O", 5:"_", 6:"O", 7:"_", 8:"O"},
            5:{1:"_", 2:"_", 3:"_", 4:"_", 5:"_", 6:"_", 7:"_", 8:"_"},
            4:{1:"_", 2:"_", 3:"_", 4:"_", 5:"_", 6:"_", 7:"_", 8:"_"},
            3:{1:"X", 2:"_", 3:"X", 4:"_", 5:"X", 6:"_", 7:"X", 8:"_"},
            2:{1:"_", 2:"X", 3:"_", 4:"X", 5:"_", 6:"X", 7:"_", 8:"X"},
            1:{1:"X", 2:"_", 3:"X", 4:"_", 5:"X", 6:"_", 7:"X", 8:"_"}
}

# METODA KLASOWA WYPISUJĄCA SZACHOWNICĘ

    def printBoard(self):
        # iteracja po sekwencji wierszy
        print("   | %1s | %1s | %1s | %1s | %1s | %1s | %1s | %1s |  " % ("A","B","C","D","E","F","G","H"))
        for row in self.warcaby.keys():
            # iteracja po polach w wierszu
            print(" %1d " % (row), end="")
            for key in self.warcaby[row].keys():
                print("| %1s " % (self.warcaby[row][key]), end= "")
            print("| %1d \n" % (row),end="")
        print("   | %1s | %1s | %1s | %1s | %1s | %1s | %1s | %1s |  " % ("A", "B", "C", "D", "E", "F", "G", "H"))

    #def getPoint(self):
        print(self.warcaby[3][3])

    def checkMoveFromTo(self, rowstart, columnstart, rowstop, columnstop, type):
        #  sprawdzenie czy punkty znajduja sie w kluczach naszych slowników
        if(rowstart in self.warcaby.keys() and columnstart in self.warcaby[rowstart].keys()
            and (self.warcaby[rowstart][columnstart] =="X" or self.warcaby[rowstart][columnstart] == "O")):
        # sprawdzenie poprawności ruchu pionka X
            if(type == "X" and rowstop == (rowstart + 1)
                    and (columnstop == (columnstart + 1) or (columnstop == (columnstart + 1)))
                    and columnstop >=1 and columnstop <=8 and rowstop >=1 and rowstop <=8):
                self.movePoint(rowstart, columnstart, rowstop, columnstop,type) # wywołanie metody klasowej
                #print("ruch poprawny dla pionka x")
        # sprawdzenie poprawności ruchu pionka O
            elif(type == "O" and rowstop == (rowstart - 1)
                    and (columnstop == (columnstart + 1) or (columnstop == (columnstart + 1)))
                    and columnstop >= 1 and columnstop <= 8 and rowstop >= 1 and rowstop <= 8):
                self.movePoint(rowstart, columnstart, rowstop, columnstop, type)
            else:
                print("błędny ruch")
        else:
            print("błędny ruch pionka")


    def movePoint(self, rowstart, columnstart, rowstop, columnstop,type):
        # przesunięcie pionka na nową pozycję
        self.warcaby[rowstop][columnstop] = type
        # aktulizacja pustego miejsca pozostałego po pionku
        self.warcaby[rowstart][columnstart] = "_"
        self.printBoard()
w1 = Warcaby()
w1.printBoard()
#w1.getPoint()
w1.checkMoveFromTo(6,2,5,3, "O")
