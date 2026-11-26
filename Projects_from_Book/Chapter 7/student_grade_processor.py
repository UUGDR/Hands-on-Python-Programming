"""Chapter 7 project: Student Grade Processor.
Reconstructed from manuscript project descriptions; not a verbatim screenshot transcription.
"""

def main():
    scores = []
    clean = True
    while True:
        name = input("Student name (done to finish): ").strip()
        if name.lower() == "done":
            break
        try:
            score = float(input(f"Score for {name}: "))
        except ValueError:
            print("Invalid score; try again.")
            continue
        if score == -1:
            print("Skipped invalid entry.")
            continue
        if score > 100:
            print("Score above 100; stopping.")
            clean = False
            break
        if score < 0:
            print("Score cannot be negative.")
            continue
        scores.append((name, score))
    else:
        print("Completed normally.")
    if clean:
        print("Data entry finished.")
    if scores:
        values = [score for _, score in scores]
        print("Students:", len(scores), "Average:", round(sum(values)/len(values), 2),
              "Highest:", max(values), "Lowest:", min(values))
    else:
        print("No valid scores.")

if __name__ == "__main__":
    main()
