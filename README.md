# MyJpHolidays20230412
a Python Library, you can get a combined list for Japan-Holidays



以下をcopyして、適当なファイル名で保存して実行してみて下さい

#################################################################
# 日本の１年間の祝日を調べます（デモ）
#  
# 使い方
# 
# このlibraryは、簡単使用を意識して作りました
# ただし、スピードはそれなりです（開発の余地ありです）
#
# 同じディレクトリに保存されている"configCTJH.ini"を直接、word、等で開いて編集することで
# ご自分に合ったオリジナルの休みを設定出来ます、初期設定では12/29-1/3になっております
# 尚、一度このlibraryを実行すると無い場合は自動的にiniファイルが作成されます、それを編集して下さい
#
# 変数名 : object = MyJpHolidays.YearToHolidays(vYear)
#       vYear 年の祝日の一覧が複合配列にされて返ってきます
#       オリジナルの休みも含みます
#       通し番号、日付、曜日、祝日名の複合配列です
#       要素の数は、len(変数名) で求められます
#       複合配列内の日付は、strです、datetimeではありません
#       アクセスの仕方はこのデモを参考にして下さい
#
# 変数名 : object = MyJpHolidays.YearToHolidays(vYear, True)
#       vYear 年の祝日の一覧が複合配列にされて返ってきます
#       月、日にちが一桁の場合に前に０が付きます
#
# 秋分の日と春分の日の計算    対応期間： 1980-2150年
#
#################################################################

import MyJpHolidays


# 調べたい年を設定します
vYear : int = 2023

# １年間の日本の祝日を調べて複合配列（通し番号・日付・曜日・祝日名）にして返してきます
# オリジナル休み（初期値：12/29 - 1/3）も含みます、これは後で自由に変えられます
# 表示される名前の優先順位は、オリジナル休み　< 祝日・振替休日
vHoliday : object = MyJpHolidays.YearToHolidays(vYear)

# データにアクセスするには…

# 配列の個数
vMax : int = len(vHoliday) 

# 作成されたデータの一覧を表示します
i : int
for i in range(vMax):
    vTemp_1 : int = vHoliday["tNum"][i]               # 通し番号 : 0 ～ 
                                                      # vMax = 21 ならば　0,1,2,3,4, . . . ,19,20
                                                      #       例:   11
    vTemp_2 : str = vHoliday["tDate"][i]              # 日付（但し、strで保存されている、datetimeではありません）
                                                      #       例：　2023/5/5
    vTemp_3 : str = vHoliday["tYOUBI"][i]             # 曜日  月、火、水、木、金、土、日
                                                      #       例:   金
    vTemp_4 : str = vHoliday["tSYUKUJITSU_Name"][i]   # 祝日名、振替休日、オリジナルの休み
                                                      #       例:   こどもの日
    
    print( str(vTemp_1) + "  " + vTemp_2 + "(" + vTemp_3 + ") " + vTemp_4)
