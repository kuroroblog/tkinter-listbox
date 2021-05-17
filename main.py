import tkinter as tk

class Application(tk.Frame):
    # listboxに関する情報を格納する変数
    listBox = None

    # 現在選択中の要素index(位置番号)を取得する。
    def getSelect(self):
        # curselection() : 現在選択中の要素index(位置番号)を取得。
        print(self.listBox.curselection())

    # 引数へ要素index(位置番号)を指定して、要素が確認できる位置へ移動する。
    def setSee(self):
        # see() : 引数へ要素index(位置番号)を指定して、要素が確認できる位置へ移動する。
        # see(11) : 11番目の要素index(位置番号)の要素が確認できる位置へ移動する。
        self.listBox.see(11)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # Frameを親要素として、listbox Widget(Frame)を作成する。
        # height : 高さの設定
        self.listBox = tk.Listbox(frame, height=5)
        for month in ("1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"):
            # listboxへ選択肢要素を格納する。
            # insert : listbox内の指定箇所(要素index(位置番号))へ、選択肢要素を格納する。
            # tk.END : 末尾を表す。
            self.listBox.insert(tk.END, month)

        # Frameを親要素とした場合に、listbox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.listBox.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        checkSelectButton = tk.Button(frame, text="選択確認", width=15, command=self.getSelect)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        checkSelectButton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        moveButton = tk.Button(frame, text="移動", width=15, command=self.setSee)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        moveButton.pack(side=tk.LEFT)

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
