class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        for winner,loser in matches:
            loss_count[winner] = loss_count.get(winner,0)
            loss_count[loser] = loss_count.get(loser,0) + 1
            
        zero_loss = []
        one_loss = []
        for key in loss_count.keys():
            if loss_count[key] == 0:
                zero_loss.append(key)
            if loss_count[key] == 1:
                one_loss.append(key)
            
        return [sorted(zero_loss),sorted(one_loss)]
        