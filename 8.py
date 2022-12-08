from pyodide.http import open_url

with open_url("8.txt") as f:
    lines = f.readlines()
    g = []
    for line in lines:
        g.append(list(line.strip()))
    w = len(g[0])
    h = len(g)
    # outer trees
    total = w * 2 + h * 2 - 4

    # inner w,h
    iw = w - 2
    ih = h - 2
    for r in range(1, iw + 1):
        for c in range(1, ih + 1):
            tree = g[r][c]
            left = max(g[r][0:c])
            right = max(g[r][c + 1 :])
            col = []
            for i in range(0, h):
                col.append(g[i][c])
            top = max(col[0:r])
            bottom = max(col[r + 1 :])
            if left < tree:
                total += 1
            elif top < tree:
                total += 1
            elif right < tree:
                total += 1
            elif bottom < tree:
                total += 1
    print(total)

    scenic_score = 0
    for r in range(1, iw + 1):
        for c in range(1, ih + 1):
            tree = g[r][c]
            left = g[r][0:c]
            left.reverse()
            right = g[r][c + 1 :]
            col = []
            for i in range(0, h):
                col.append(g[i][c])
            top = col[0:r]
            top.reverse()
            bottom = col[r + 1 :]
            left_score = 0
            for i in left:
                if tree > i:
                    left_score += 1
                if tree <= i:
                    left_score += 1
                    break
            right_score = 0
            for i in right:
                if tree > i:
                    right_score += 1
                if tree <= i:
                    right_score += 1
                    break
            top_score = 0
            for i in top:
                if tree > i:
                    top_score += 1
                if tree <= i:
                    top_score += 1
                    break
            bottom_score = 0
            for i in bottom:
                if tree > i:
                    bottom_score += 1
                if tree <= i:
                    bottom_score += 1
                    break
            score = left_score * right_score * top_score * bottom_score
            if scenic_score < score:
                scenic_score = score

    print(scenic_score)
