def calculate_carbon_footprint(food_items):
    # 각 식품별 탄소 발자국 데이터 (kg CO2 equivalent per kg)
    carbon_footprints = {
        "쌀": 1.5,
        "소고기": 27,
        "닭고기": 6.9,
        "돼지고기": 12.1,
        "달걀": 4.8,
        "우유": 1.9,
        "채소": 0.4,
        "과일": 0.9,
        "생선": 6.1
    }

    total_footprint = 0
    for item, quantity in food_items.items():
        if item in carbon_footprints:
            total_footprint += carbon_footprints[item] * quantity
        else:
            print(f"{item}에 대한 탄소 발자국 데이터가 없습니다.")

    return total_footprint

def main():
    print("식품의 종류와 양을 입력하세요. 입력을 마치려면 '끝'을 입력하세요.")

    food_items = {}
    while True:
        food = input("식품 종류: ")
        if food == "끝":
            break
        quantity = float(input("양 (kg 또는 개수): "))
        food_items[food] = quantity

    total_footprint = calculate_carbon_footprint(food_items)
    print(f"입력하신 식품들의 총 탄소 발자국은 {total_footprint:.2f} kg CO2 equivalent입니다.")
main()