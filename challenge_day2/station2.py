import datetime

def solution_station2(date_str: str) -> str:
    japanese_days = {
        0: "月曜日",  # Monday
        1: "火曜日",  # Tuesday
        2: "水曜日",  # Wednesday
        3: "木曜日",  # Thursday
        4: "金曜日",  # Friday
        5: "土曜日",  # Saturday
        6: "日曜日",  # Sunday
    }

    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    weekday_num = date_obj.weekday()

    return japanese_days[weekday_num]
