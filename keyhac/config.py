import sys
import os
import datetime

import pyauto
from keyhac import *

def configure(keymap):

    # --------------------------------------------------------------------
    # config.py編集用のテキストエディタの設定
    keymap.editor = "C:\Program Files\Hidemaru\Hidemaru.exe"

    # --------------------------------------------------------------------
    # 表示のカスタマイズ

    # フォントの設定
    keymap.setFont( "ＭＳ ゴシック", 12 )

    # テーマの設定
    keymap.setTheme("black")

    # --------------------------------------------------------------------
    # どのウインドウにフォーカスがあっても効くキーマップ
    keymap_global = keymap.defineWindowKeymap()

    # クリップボード履歴
    keymap_global[ "C-S-Z"   ] = keymap.command_ClipboardList     # クリップボード履歴表示
    keymap_global[ "C-S-X"   ] = keymap.command_ClipboardRotate   # 直近の履歴を末尾に回す
    keymap_global[ "C-S-A-X" ] = keymap.command_ClipboardRemove   # 直近の履歴を削除

    # カーソル移動
    keymap_global[ "LC-H" ] = "Left"
    keymap_global[ "LC-J" ] = "Down"
    keymap_global[ "LC-K" ] = "Up"
    keymap_global[ "LC-L" ] = "Right"
    keymap_global[ "LC-U" ] = "Home"
    keymap_global[ "LC-O" ] = "End"

    # 文字選択
    keymap_global[ "LC-S-H" ] = "S-Left"
    keymap_global[ "LC-S-J" ] = "S-Down"
    keymap_global[ "LC-S-K" ] = "S-Up"
    keymap_global[ "LC-S-L" ] = "S-Right"
    keymap_global[ "LS-LC-U" ] = "S-Home"
    keymap_global[ "LS-LC-O" ] = "S-End"

    # クリップボード履歴の最大数 (デフォルト:1000)
    keymap.clipboard_history.maxnum = 1000

    # クリップボード履歴として保存する合計最大サイズ (デフォルト:10MB)
    keymap.clipboard_history.quota = 10*1024*1024




