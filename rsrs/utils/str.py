#!/usr/bin/env python
# coding: utf-8


def custom_replace(s: str):
    z_digit = "　１２３４５６７８９０ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    h_digit = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    s = s.translate(str.maketrans(z_digit, h_digit))
    target_char = " ・〜?"
    for char in target_char:
        s = s.replace(char, "")
    return s
