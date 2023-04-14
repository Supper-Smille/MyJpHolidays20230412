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
vYear : int = 2024

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


####################################################################
# 出力例
#
# 0  2024/1/1(月) 元旦
# 1  2024/1/2(火) 年始休み5
# 2  2024/1/3(水) 年始休み6
# 3  2024/1/8(月) 成人の日
# 4  2024/2/11(日) 建国記念の日
# 5  2024/2/12(月) 振り替え休日
# 6  2024/2/23(金) 令和天皇誕生日
# 7  2024/3/20(水) 春分の日
# 8  2024/4/29(月) 昭和の日
# 9  2024/5/3(金) 憲法記念日
# 10  2024/5/4(土) みどりの日
# 11  2024/5/5(日) こどもの日
# 12  2024/5/6(月) 振り替え休日
# 13  2024/7/15(月) 海の日
# 14  2024/8/11(日) 山の日
# 15  2024/8/12(月) 振り替え休日
# 16  2024/9/16(月) 敬老の日
# 17  2024/9/22(日) 秋分の日
# 18  2024/9/23(月) 振り替え休日
# 19  2024/10/14(月) スポーツの日
# 20  2024/11/3(日) 文化の日
# 21  2024/11/4(月) 振り替え休日
# 22  2024/11/23(土) 勤労感謝の日
# 23  2024/12/29(日) 年末休み1
# 24  2024/12/30(月) 年末休み2
# 25  2024/12/31(火) 年末休み3

