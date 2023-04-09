from sys import stdin

def main():
    n, m, k = map(int, input().split())
    rain_infos = [tuple(map(int, input().split())) for _ in range(m)]

    total_rain = [0] * (n + 1)
    collapse_time = -1
    collapse_floor = -1

    for idx, (t, r) in enumerate(rain_infos):
        total_rain[t] += r
        
        while t > 0:
            if total_rain[t] > k:
                if collapse_time == -1 or idx + 1 < collapse_time:
                    collapse_time = idx + 1
                    collapse_floor = t

                break
            
            t -= 1

        if collapse_time != -1:
            break

    if collapse_time != -1:
        print(collapse_time, collapse_floor)
    else:
        print(-1)

main()
