"""
LCD class with font support

CC-BY-SA 2014, Markus Birth <markus@birth-online.de>
"""

from pyb import LCD

class FontLCD(LCD):
    def __init__(self, skin_position):
        super().__init__()
        self.isFontLoaded = False
        self.cursorX = 0
        self.cursorY = 0
        self.cursorLine = 0
        self.font = []
        self.fontWidth  = 3
        self.fontHeight = 4
        self.calculateLines()

    def calculateLines(self, lineSpacing = 1):
        self.displayWidth = 128
        self.displayHeight = 32
        self.lineSpacing = lineSpacing
        self.maxLines = self.displayHeight // ( self.fontHeight + self.lineSpacing )
        self.lines = [""] * self.maxLines
        
    def loadFont(self, fontname):
        fontfile = __import__(fontname)
        self.font = fontfile.fontdata
        self.isFontLoaded = True
        self.write("FONT LOADED.")
        for i in range(1,6):
            self.write("\nThis is line %i" % i)

    def redraw(self):
        self.fill(0)
        self.cursorX = 0
        self.cursorY = 0
        line_temp = list(self.lines)
        for l in range(0, self.maxLines):
            self.lines[l] = ""
        for l in range(0, self.maxLines-1):
            self.cursorX = 0
            self.cursorY = l * (self.fontHeight + self.lineSpacing)
            self.cursorLine = l
            self.write(line_temp[l])
        self.show()

    def newline(self):
        self.cursorX = 0
        self.cursorY = self.cursorY + self.fontHeight + self.lineSpacing
        self.cursorLine = self.cursorLine + 1
        if self.cursorLine >= self.maxLines:
            for i in range(0, self.maxLines - 1):
                self.lines[i] = self.lines[i+1]
            self.lines[self.maxLines - 1] = ""
            self.redraw()
            self.cursorLine = self.maxLines - 1

    def writeLetter(self, charcode, x0, y0):
        letter = self.font[charcode]
        for x in range(0, self.fontWidth):
            for y in range(0, self.fontHeight):
                bit = letter[x] & 2**y
                self.pixel(x0 + x, y0 + y, bit)

    def text(self, text, x, y, colour):
        if not self.isFontLoaded:
            super().text(text, x, y, colour)
        else:
            for i in range(0, len(text)):
                charcode = ord(text[i])
                if charcode >= 32 and charcode <= 127:
                    self.writeLetter(charcode, x, y)
                    x = x + self.fontWidth + 1
            self.show()

    def write(self, text):
        if not self.isFontLoaded:
            # no font loaded - use built-in function
            super().write(text)
        else:
            for i in range(0, len(text)):
                charcode = ord(text[i])
                if charcode >= 32 and charcode <= 127:
                    self.writeLetter(charcode, self.cursorX, self.cursorY)
                    self.cursorX = self.cursorX + self.fontWidth + 1
                    self.lines[self.cursorLine] += chr(charcode)
                    if self.cursorX > self.displayWidth:
                        self.newline()
                elif charcode == 10:
                    self.newline()
            self.show()
