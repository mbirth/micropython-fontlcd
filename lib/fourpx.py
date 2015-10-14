#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GLCD FontName : FourPx3x4
# GLCD FontSize : 3 x 4
# Based on http://www.dafont.com/four-pixel-caps.font

fontdata = [
    [], [], [], [], [], [], [], [],
    [], [], [], [], [], [], [], [],
    [], [], [], [], [], [], [], [],
    [], [], [], [], [], [], [], [],
    [ 0x00, 0x00, 0x00 ],                      # Code for char  
    [ 0x00, 0x0B, 0x00 ],                      # Code for char !
    [ 0x03, 0x00, 0x03 ],                      # Code for char "
    [ 0x00, 0x00, 0x00 ],                      # Code for char #
    [ 0x0A, 0x0F, 0x05 ],                      # Code for char $
    [ 0x0D, 0x00, 0x0B ],                      # Code for char %
    [ 0x00, 0x00, 0x00 ],                      # Code for char &
    [ 0x00, 0x03, 0x00 ],                      # Code for char '
    [ 0x00, 0x06, 0x09 ],                      # Code for char (
    [ 0x09, 0x06, 0x00 ],                      # Code for char )
    [ 0x0A, 0x04, 0x0A ],                      # Code for char *
    [ 0x04, 0x0E, 0x04 ],                      # Code for char +
    [ 0x08, 0x0C, 0x00 ],                      # Code for char ,
    [ 0x04, 0x04, 0x04 ],                      # Code for char -
    [ 0x00, 0x08, 0x00 ],                      # Code for char .
    [ 0x08, 0x06, 0x01 ],                      # Code for char /
    [ 0x0F, 0x09, 0x0F ],                      # Code for char 0
    [ 0x02, 0x0F, 0x00 ],                      # Code for char 1
    [ 0x0D, 0x0F, 0x0B ],                      # Code for char 2
    [ 0x09, 0x0B, 0x0C ],                      # Code for char 3
    [ 0x07, 0x04, 0x0F ],                      # Code for char 4
    [ 0x0B, 0x0D, 0x01 ],                      # Code for char 5
    [ 0x07, 0x0A, 0x04 ],                      # Code for char 6
    [ 0x01, 0x0D, 0x03 ],                      # Code for char 7
    [ 0x0F, 0x0A, 0x0F ],                      # Code for char 8
    [ 0x02, 0x05, 0x0E ],                      # Code for char 9
    [ 0x00, 0x0A, 0x00 ],                      # Code for char :
    [ 0x08, 0x0A, 0x00 ],                      # Code for char ;
    [ 0x00, 0x04, 0x0A ],                      # Code for char <
    [ 0x0A, 0x0A, 0x0A ],                      # Code for char =
    [ 0x0A, 0x04, 0x00 ],                      # Code for char >
    [ 0x01, 0x0D, 0x02 ],                      # Code for char ?
    [ 0x00, 0x00, 0x00 ],                      # Code for char @
    [ 0x0E, 0x05, 0x0F ],                      # Code for char A
    [ 0x0F, 0x0B, 0x0E ],                      # Code for char B
    [ 0x0E, 0x09, 0x09 ],                      # Code for char C
    [ 0x0F, 0x09, 0x06 ],                      # Code for char D
    [ 0x0C, 0x0B, 0x09 ],                      # Code for char E
    [ 0x0E, 0x05, 0x01 ],                      # Code for char F
    [ 0x07, 0x09, 0x0D ],                      # Code for char G
    [ 0x0F, 0x02, 0x0F ],                      # Code for char H
    [ 0x00, 0x0F, 0x00 ],                      # Code for char I
    [ 0x08, 0x09, 0x07 ],                      # Code for char J
    [ 0x0F, 0x04, 0x0A ],                      # Code for char K
    [ 0x07, 0x08, 0x08 ],                      # Code for char L
    [ 0x0F, 0x07, 0x0E ],                      # Code for char M
    [ 0x0F, 0x01, 0x0E ],                      # Code for char N
    [ 0x07, 0x09, 0x0E ],                      # Code for char O
    [ 0x0F, 0x05, 0x06 ],                      # Code for char P
    [ 0x07, 0x0D, 0x07 ],                      # Code for char Q
    [ 0x0E, 0x05, 0x0B ],                      # Code for char R
    [ 0x0B, 0x0B, 0x0D ],                      # Code for char S
    [ 0x01, 0x0F, 0x01 ],                      # Code for char T
    [ 0x07, 0x08, 0x0F ],                      # Code for char U
    [ 0x0F, 0x04, 0x03 ],                      # Code for char V
    [ 0x0F, 0x0E, 0x07 ],                      # Code for char W
    [ 0x0D, 0x06, 0x0B ],                      # Code for char X
    [ 0x03, 0x0C, 0x03 ],                      # Code for char Y
    [ 0x0D, 0x0B, 0x09 ],                      # Code for char Z
    [ 0x00, 0x0F, 0x09 ],                      # Code for char [
    [ 0x01, 0x06, 0x08 ],                      # Code for char BackSlash
    [ 0x09, 0x0F, 0x00 ],                      # Code for char ]
    [ 0x02, 0x01, 0x02 ],                      # Code for char ^
    [ 0x08, 0x08, 0x08 ],                      # Code for char _
    [ 0x00, 0x01, 0x02 ],                      # Code for char `
    [ 0x0C, 0x06, 0x0C ],                      # Code for char a
    [ 0x0F, 0x0A, 0x04 ],                      # Code for char b
    [ 0x04, 0x0A, 0x0A ],                      # Code for char c
    [ 0x04, 0x0A, 0x0F ],                      # Code for char d
    [ 0x0C, 0x0E, 0x0A ],                      # Code for char e
    [ 0x04, 0x0F, 0x05 ],                      # Code for char f
    [ 0x0A, 0x0D, 0x0E ],                      # Code for char g
    [ 0x0E, 0x04, 0x08 ],                      # Code for char h
    [ 0x00, 0x0D, 0x00 ],                      # Code for char i
    [ 0x08, 0x0A, 0x06 ],                      # Code for char j
    [ 0x0E, 0x04, 0x0A ],                      # Code for char k
    [ 0x00, 0x0E, 0x08 ],                      # Code for char l
    [ 0x0E, 0x06, 0x0C ],                      # Code for char m
    [ 0x0E, 0x02, 0x0C ],                      # Code for char n
    [ 0x04, 0x0A, 0x04 ],                      # Code for char o
    [ 0x0E, 0x05, 0x02 ],                      # Code for char p
    [ 0x06, 0x05, 0x0E ],                      # Code for char q
    [ 0x00, 0x0C, 0x02 ],                      # Code for char r
    [ 0x08, 0x0E, 0x02 ],                      # Code for char s
    [ 0x02, 0x07, 0x0A ],                      # Code for char t
    [ 0x06, 0x08, 0x0E ],                      # Code for char u
    [ 0x0E, 0x04, 0x02 ],                      # Code for char v
    [ 0x0E, 0x0C, 0x06 ],                      # Code for char w
    [ 0x0A, 0x04, 0x0A ],                      # Code for char x
    [ 0x06, 0x0C, 0x06 ],                      # Code for char y
    [ 0x02, 0x0E, 0x08 ],                      # Code for char z
    [ 0x04, 0x06, 0x09 ],                      # Code for char {
    [ 0x00, 0x0F, 0x00 ],                      # Code for char |
    [ 0x09, 0x06, 0x04 ],                      # Code for char }
    [ 0x04, 0x06, 0x02 ],                      # Code for char ~
    [ 0x0E, 0x0A, 0x0E ]                       # Code for char
]
