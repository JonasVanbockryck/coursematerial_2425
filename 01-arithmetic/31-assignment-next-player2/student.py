# write your code here

def next_player2(player, player_count): 
    final_result = (player +1) % player_count

    return final_result if final_result > 0 else 1
