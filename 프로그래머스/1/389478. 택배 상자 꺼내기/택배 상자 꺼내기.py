def solution(n, w, num):
    # 상자의 좌표 계산
    row = (num - 1) // w
    pos_in_row = (num - 1) % w
    if row % 2 == 0:  # 짝수층 → 방향
        col = pos_in_row
    else:  # 홀수층 ← 방향
        col = w - 1 - pos_in_row

    # 위에 있는 층들 중 해당 col에 상자가 있으면 +1
    count = 1  # 자기 자신
    for r in range(row + 1, (n + w - 1) // w):
        if r % 2 == 0:  # → 방향
            if col < n - r * w:
                count += 1
        else:  # ← 방향
            if w - 1 - col < n - r * w:
                count += 1
    return count