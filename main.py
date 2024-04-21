import Hit_and_Blow
def main():
    HB = Hit_and_Blow.HitAndBlowGame()
    HB.game_start()
    
    """
    while True:
        #自分の入力
        p_val = HB.player_input()
        p_hit, p_blow = HB.HB_judge(p_val)
        print(f"hit: {p_hit}, blow: {p_blow}")
        HB.game_judge(p_hit)
        if HB.is_game_continue == False:
            break
        #cpuの入力
        c_val = HB.cpu_input()
        print(f"cpuの入力: {c_val}")
        c_hit, c_blow = HB.HB_judge(c_val)
        print(f"hit: {c_hit}, blow: {c_blow}")
        HB.game_judge(c_hit)
        if HB.is_game_continue == False:
            break
    """
    


if __name__ == "__main__":
    main()
