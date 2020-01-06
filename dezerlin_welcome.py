# coding=utf-8
__author__ = 'yangtao'
__version__ = '0.1'


dezerlin_show = " _______   _______  ________   _______ .______       __       __  .__   __. \n"
dezerlin_show += "|       \ |   ____||       /  |   ____||   _  \     |  |     |  | |  \ |  | \n"
dezerlin_show += "|  .--.  ||  |__   `---/  /   |  |__   |  |_)  |    |  |     |  | |   \|  | \n"
dezerlin_show += "|  |  |  ||   __|     /  /    |   __|  |      /     |  |     |  | |  . `  | \n"
dezerlin_show += "|  '--'  ||  |____   /  /----.|  |____ |  |\  \----.|  `----.|  | |  |\   | \n"
dezerlin_show += "|_______/ |_______| /________||_______|| _| `._____||_______||__| |__| \__|"

def show(author=None, version=None):
    print(dezerlin_show)
    if author:
        print("author: %s"%author)
    if version:
        print("version: %s"%version)
    print("enjoy it!")
    print('')