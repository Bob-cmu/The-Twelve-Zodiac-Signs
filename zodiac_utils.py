
import datetime
import json

# 载入星座数据
with open("data/zodiac_data.json", "r") as f:
    xingzuo_biao = json.load(f)

def riqi_zai_qujian(date_str, kaishi, jieshu):
    yue, ri = map(int, date_str.split("-"))
    start_month, start_day = map(int, kaishi.split("-"))
    end_month, end_day = map(int, jieshu.split("-"))
    d = datetime.date(2000, yue, ri)
    d_start = datetime.date(2000, start_month, start_day)
    d_end = datetime.date(2000, end_month, end_day)
    if start_month > end_month:
        # 跨年星座（如摩羯座）
        return d >= d_start or d <= d_end
    else:
        return d_start <= d <= d_end

def panduan_xingzuo(shengri):
    for x in xingzuo_biao:
        if riqi_zai_qujian(shengri, x["start_date"], x["end_date"]):
            return x
    return None

def tianjia_xingbie(xingzuo_dict, xingbie):
    if xingbie == "male":
        xingzuo_dict["personality"] = xingzuo_dict["male_personality"]
    elif xingbie == "female":
        xingzuo_dict["personality"] = xingzuo_dict["female_personality"]
    return {
        "zodiac": xingzuo_dict["name"],
        "personality": xingzuo_dict["personality"],
        "best_match": xingzuo_dict["match"],
        "match_reason": xingzuo_dict["match_reason"]
    }

def pipei(shengri, xingbie):
    jieguo = panduan_xingzuo(shengri)
    if jieguo:
        return tianjia_xingbie(jieguo, xingbie)
    else:
        return {"error": "cannot determine zodiac"}
