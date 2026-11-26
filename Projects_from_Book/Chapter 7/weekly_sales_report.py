"""Chapter 7 project: Weekly Sales Report.
Reconstructed from manuscript project description.
"""

def weekly_report():
    branches = ["North", "South", "West"]
    totals = {}
    best = ("", "", float("-inf"))
    for branch in branches:
        total = 0
        for day in range(1, 6):
            sale = float(input(f"{branch}, day {day} sales: $"))
            total += sale
            if sale > best[2]:
                best = (branch, f"Day {day}", sale)
        totals[branch] = total
    print("\nWEEKLY SALES REPORT")
    for branch, total in totals.items():
        print(f"{branch:12} ${total:,.2f}")
    print("Grand total:", f"${sum(totals.values()):,.2f}")
    print("Best sales day:", best)

if __name__ == "__main__":
    weekly_report()
