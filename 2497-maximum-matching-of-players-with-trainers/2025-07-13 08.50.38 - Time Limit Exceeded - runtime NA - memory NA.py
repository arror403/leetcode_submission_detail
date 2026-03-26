class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        Using Counter for cases with many duplicates
        Time: O(n log n + m log m) but with better constants
        """
        player_counts = Counter(players)
        trainer_counts = Counter(trainers)
        res = 0
        
        for trainer_skill in sorted(trainer_counts.keys()):
            trainer_count = trainer_counts[trainer_skill]
            for player_skill in sorted(player_counts.keys()):
                if player_skill <= trainer_skill:
                    assignments = min(player_counts[player_skill], trainer_count)
                    res += assignments
                    player_counts[player_skill] -= assignments
                    trainer_count -= assignments

                    if trainer_count == 0:
                        break
                else:
                    break
        

        return res


        
        # players.sort()
        # trainers.sort()
        # res = 0
        # i, j = 0, 0

        # while i < len(players) and j < len(trainers):
        #     if trainers[j] >= players[i]:
        #         res += 1
        #         i += 1
        #     j += 1


        # return res