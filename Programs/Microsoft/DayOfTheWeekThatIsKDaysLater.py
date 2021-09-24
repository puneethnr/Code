'''
Given current day as day of the week and an integer K, the task is to find the day of the week after K days.
'''

def day_of_week(day: str, k: int) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]
    index = 0
    for i in range(len(days)):
        if days[i] == day:
            index = i
    return days[(index + k) % 7]

if __name__ == '__main__':
    day = input()
    k = int(input())
    res = day_of_week(day, k)
    print(res)