import random
import re
import time
from enum import Enum, auto
from js import document
from pyodide.ffi import create_proxy
from js import prompt

class HitAndBlowGame:

    class HitBlowResult(Enum):
        HIT = auto()
        BLOW = auto()
        NONE = auto()

    def game_start(self, event=None):
        """ゲームをスタートする時に呼び出し
        """
        self.clear_table()
        self.enable_input_form()
        self.result.innerText = ""
        self.cpu_num = self.cpu_input()
        self.is_game_continue = True
        print(f"自分の数字: {self.player_num}")
        print(f"cpuの数字: {self.cpu_num}")

    def player_input(self):#多分使わない
        """プレイヤーの数字入力
        """
        pattern = r'^\d{3}$'
        while(True):
            #val = input("数字を入力してください: ")
            val = '333'
            if val.isdigit() and len(val) == 3:
                break
            print("３桁の数字を入力してください")
            
        return val

    def cpu_input(self):
        """ランダムに3桁の数字を返す（最初0あり）
        """
        val = ""
        for _ in range(3):
            val += str(random.randint(0, 9))
        return val

    def add_list(self, input_num):
        """入力した数字をリストに格納

        Args:
            input_num (str): 入力した数字
        """
        if self.turn % 2 == 1:
            self.player_input_list.append[input_num]
        else:
            self.cpu_input_list.append[input_num]

    def HB_judge(self, input_num):
        """入力した数字のHとBを返す

        Args:
            input_num (_type_): _description_
        """
        hit = 0
        blow = 0
        split_i_num = [int(num) for num in str(input_num)]
        result = [HitAndBlowGame.HitBlowResult.NONE, HitAndBlowGame.HitBlowResult.NONE, HitAndBlowGame.HitBlowResult.NONE]
        if self.turn % 2 == 0:
            split_p_num = [int(num) for num in str(self.player_num)]
            self.hit(split_i_num, split_p_num, result)
            self.blow(split_i_num, split_p_num, result)
        else:
            split_c_num = [int(num) for num in str(self.cpu_num)]
            self.hit(split_i_num, split_c_num, result)
            self.blow(split_i_num, split_c_num, result)

        for re in result:
            if re == HitAndBlowGame.HitBlowResult.HIT:
                hit += 1
            if re == HitAndBlowGame.HitBlowResult.BLOW:
                blow += 1

        return hit, blow
    
    def game_judge(self, hit):
        """ゲームが終了したかどうかの判定
        """
        if hit == 3:
            self.is_game_continue = False
        self.turn += 1


    def hit(self, split_i_num, split_num, result):
        """ヒットしているかの判定

        Args:
            split_i_num (list): 入力した数字を1文字ごとにリストに格納したもの
            split_num (list): 正解を1文字ごとにリストに格納したもの
            result (list): 結果を格納するリスト
        """
        for i in range(3):
            if split_num[i] == split_i_num[i]:
                result[i] = (HitAndBlowGame.HitBlowResult.HIT)
    
    def blow(self, split_i_num, split_num, result):
        """ブローしているかの判定

        Args:
            split_i_num (list): 入力した数字を1文字ごとにリストに格納したもの
            split_num (list): 正解を1文字ごとにリストに格納したもの
            result (list): 結果を格納するリスト
        """
        for i in range(3):
            if result[i] == HitAndBlowGame.HitBlowResult.HIT:
                continue
            for j in range(i,3):
                if split_num[i] == split_i_num[j]:
                    result[i] = HitAndBlowGame.HitBlowResult.BLOW


    def add_data_from_form(self,event):
        # Prevent form from submitting normally
        event.preventDefault()

        # Retrieve input values
        first_digit = int(document.getElementById('first-digit').value)
        second_digit = int(document.getElementById('second-digit').value)
        third_digit = int(document.getElementById('third-digit').value)
        player_input = first_digit * 100 + second_digit * 10 + third_digit

        # Find table and add new row
        table = document.getElementById('player-table')
        new_row = table.insertRow(-1)
        new_row.insertCell(0).textContent = player_input

        # Clear inputs after adding
        document.getElementById('first-digit').value = ''
        document.getElementById('second-digit').value = ''
        document.getElementById('third-digit').value = ''

        p_hit, p_blow = self.HB_judge(player_input)
        new_row.insertCell(1).textContent = p_hit
        new_row.insertCell(2).textContent = p_blow
        self.game_judge(p_hit)
        if self.is_game_continue == False:
            self.result.innerText = "You Win!"
            self.disable_input_form()

        time.sleep(1)

        cpu_input = self.cpu_input()
        c_hit, c_blow = self.HB_judge(cpu_input)
        table = document.getElementById('cpu-table')
        new_row = table.insertRow(-1)
        new_row.insertCell(0).textContent = cpu_input
        new_row.insertCell(1).textContent = c_hit
        new_row.insertCell(2).textContent = c_blow
        self.game_judge(c_hit)
        if self.is_game_continue == False:
            self.result = document.getElementById('result')
            if(self.result.innerText != "You Win!"):
                self.result.innerText = "Draw!"
                self.disable_input_form()
            elif (self.result.innerText == ""):
                self.result.innerText = "You Lose!"
                self.disable_input_form()



    def __init__(self):
        # Clear inputs after adding
        document.getElementById('first-digit').value = ''
        document.getElementById('second-digit').value = ''
        document.getElementById('third-digit').value = ''

        self.turn = 1
        self.player_num = prompt("3桁の数字を入力してください")
        your_num = document.getElementById('your-number')
        your_num.innerText = "Your Number : " + self.player_num

        self.cpu_num = ""
        self.player_input_list = []
        self.cpu_input_list = []
        self.is_game_continue = True
        self.player_table = document.getElementById('player-table')
        self.cpu_table = document.getElementById('cpu-table')
        self.input_form = document.getElementById('inputForm')
        self.input_form.addEventListener('submit', create_proxy(self.add_data_from_form))
        self.result = document.getElementById('result')
        self.result.innerText = ""
        self.new_game_button = document.getElementById('newGameBtn')
        self.new_game_button.addEventListener('click', create_proxy(self.game_start))

    def clear_table(self):
        table = document.getElementById('player-table')
        row_count = table.rows.length  
        while row_count > 1:  
            table.deleteRow(-1)  
            row_count -= 1
        table = document.getElementById('cpu-table')
        row_count = table.rows.length
        while row_count > 1:  
            table.deleteRow(-1)  
            row_count -= 1

    def disable_input_form(self):
        """
        Disables the form to prevent any more inputs after the game ends or as needed.
        """
        input_form = document.getElementById('inputForm')
        # Disable each input element in the form
        for element in input_form.elements:
            element.disabled = True

    def enable_input_form(self):
        """
        Disables the form to prevent any more inputs after the game ends or as needed.
        """
        input_form = document.getElementById('inputForm')
        # Disable each input element in the form
        for element in input_form.elements:
            element.disabled = False


#TODO:ヒント機能つけたい
#TODO:先頭に０が付くとバグる
#TODO:ユーザー入力にバリデーション張る
#TODO:ターミナル実装
#TODO:デザインこだわる
#TODO:ゲーム続行機能
#TODO:命名規則を統一する