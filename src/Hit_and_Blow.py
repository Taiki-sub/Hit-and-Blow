import random
from enum import Enum, auto
class HitAndBlowGame:

    class HitBlowResult(Enum):
        HIT = auto()
        BLOW = auto()
        NONE = auto()


    def __init__(self):
        self.turn = 1
        self.player_num = ""
        self.cpu_num = ""
        self.player_input_list = []
        self.cpu_input_list = []
        self.is_game_continue = False

    def game_start(self):
        """ゲームをスタートする時に呼び出し
        """
        self.player_num = self.player_input()
        self.cpu_num = self.cpu_input()
        self.is_game_continue = True
        print(f"自分の数字: {self.player_num}")
        print(f"cpuの数字: {self.cpu_num}")

    def player_input(self):
        val = input("数字を入力してください: ")

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
        if hit == 3:
            self.is_game_continue = False
        self.turn += 1


    def hit(self, split_i_num, split_num, result):
        for i in range(3):
            if split_num[i] == split_i_num[i]:
                result[i] = (HitAndBlowGame.HitBlowResult.HIT)
                continue
    
    def blow(self, split_i_num, split_num, result):
        for i in range(3):
            if result[i] == HitAndBlowGame.HitBlowResult.HIT:
                continue
            for j in range(3):
                if split_num[i] == split_i_num[j]:
                    result[i] == HitAndBlowGame.HitBlowResult.BLOW