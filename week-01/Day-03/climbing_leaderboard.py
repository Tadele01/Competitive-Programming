def climbingLeaderboard(ranked, player):
    unique_stack = []
    for score in ranked:
        if unique_stack:
            top = unique_stack[-1]
            if top == score:
                continue
            else:
                unique_stack.append(score)
        else:
             unique_stack.append(score)
    length = len(unique_stack) + 1
    ranks = []
    for value in player:
        not_found = True
        for i in range(len(unique_stack)):
            top = unique_stack[-1]
            if top <= value:
                unique_stack.pop()
                length -= 1
                continue
            if top > value:
                ranks.append(length)
                not_found = False
                break
            length = len(unique_stack)
        if not_found:
            ranks.append(1)
    return ranks 