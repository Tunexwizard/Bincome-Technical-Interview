
import os
from dotenv import load_dotenv
import psycopg2
from collections import Counter
import random

# Load environment variables
load_dotenv()

data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

all_colors = []
for day, color_string in data.items():
    colors = [c.strip().upper() for c in color_string.split(",")]
    for i, color in enumerate(colors):
        if color == "BLEW":
            colors[i] = "BLUE"
        elif color == "ARSH":
            colors[i] = "ASH"
    all_colors.extend(colors)

color_counts = Counter(all_colors)

average = sum(color_counts.values()) / len(color_counts)
mean_color = min(color_counts.items(), key=lambda x: abs(x[1] - average))[0]
most_worn = color_counts.most_common(1)[0][0]
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1])
median_color = sorted_colors[len(sorted_colors)//2][0]
variance = sum((x - average) ** 2 for x in color_counts.values()) / len(color_counts)
total_colors = len(all_colors)
red_count = color_counts.get("RED", 0)
prob_red = red_count / total_colors

def save_to_postgres(data_dict):
    db_url = os.getenv("SUPABASE_DB_URL")
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS color_frequencies (
            color TEXT PRIMARY KEY,
            frequency INT
        )
    """)
    for color, freq in data_dict.items():
        cur.execute("""
            INSERT INTO color_frequencies (color, frequency)
            VALUES (%s, %s)
            ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency
        """, (color, freq))
    conn.commit()
    conn.close()

def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

def binary_to_decimal():
    binary = "".join(random.choices(["0", "1"], k=4))
    return binary, int(binary, 2)

def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

if __name__ == "__main__":
    print("Mean color:", mean_color)
    print("Most worn color:", most_worn)
    print("Median color:", median_color)
    print("Variance of colors:", variance)
    print("Probability of Red:", prob_red)
    binary, decimal = binary_to_decimal()
    print("Random 4-digit binary:", binary, "=> Base 10:", decimal)
    print("Sum of first 50 Fibonacci numbers:", fibonacci_sum(50))
    print("Search 7 in list [1,3,5,7,9]:", recursive_search([1,3,5,7,9], 7))
    save_to_postgres(color_counts)
