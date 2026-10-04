"""FCFS and Non-preemptive SJF CPU Scheduling.

Tie-breaking rule (both algorithms):
  1. Earlier arrival time first
  2. If still tied, smaller Process ID (input order) first
"""
import copy


# ---------- Task 1 & 2: Input with validation ----------
def read_int(prompt, minimum, label):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print(f"  Invalid {label}: '{raw}' is not an integer. Try again.")
            continue
        if value < minimum:
            print(f"  Invalid {label}: must be >= {minimum}. Try again.")
            continue
        return value


def read_processes():
    n = read_int("Enter number of processes: ", 1, "count")
    processes, seen = [], set()
    for i in range(1, n + 1):
        print(f"Process {i}:")
        while True:
            pid = input("  Process ID (e.g. P1): ").strip()
            if not pid:
                print("  Invalid Process ID: cannot be empty. Try again.")
            elif pid in seen:
                print(f"  Invalid Process ID: '{pid}' already used. Try again.")
            else:
                seen.add(pid)
                break
        at = read_int("  Arrival Time (>= 0): ", 0, "Arrival Time")
        bt = read_int("  Burst Time (>= 1): ", 1, "Burst Time")
        processes.append({"pid": pid, "at": at, "bt": bt, "order": i})
    return processes


# ---------- Scheduling core ----------
def fcfs(procs):
    procs = sorted(procs, key=lambda p: (p["at"], p["order"]))  # Task 4
    time, timeline, result = 0, [], []
    for p in procs:
        if time < p["at"]:
            timeline.append(("IDLE", time, p["at"]))  # Task 7
            time = p["at"]
        start, end = time, time + p["bt"]
        timeline.append((p["pid"], start, end))
        result.append(make_row(p, start, end))
        time = end
    return timeline, result


def sjf(procs):
    remaining = list(procs)
    time, timeline, result = 0, [], []
    while remaining:
        ready = [p for p in remaining if p["at"] <= time]
        if not ready:  # Task 7
            next_at = min(p["at"] for p in remaining)
            timeline.append(("IDLE", time, next_at))
            time = next_at
            continue
        # Task 5 & 6: shortest burst, tie -> earlier arrival -> smaller order
        p = min(ready, key=lambda x: (x["bt"], x["at"], x["order"]))
        start, end = time, time + p["bt"]
        timeline.append((p["pid"], start, end))
        result.append(make_row(p, start, end))
        remaining.remove(p)
        time = end
    return timeline, result


def make_row(p, start, end):
    tat = end - p["at"]
    return {"pid": p["pid"], "at": p["at"], "bt": p["bt"],
            "start": start, "end": end, "tat": tat, "wt": tat - p["bt"]}


# ---------- Task 8: Display ----------
def show(title, timeline, result):
    print("\n" + "=" * 62)
    print(f"{title}")
    print("=" * 62)
    print("Execution sequence:")
    print("  " + " -> ".join(f"{n}[{s}-{e}]" for n, s, e in timeline))
    print("\nGantt chart:")
    bar = "|" + "|".join(f" {n} ".center(7) for n, _, _ in timeline) + "|"
    marks = f"{timeline[0][1]:<8}" + "".join(f"{e:<8}" for _, _, e in timeline)
    print("  " + bar)
    print("  " + marks)
    idle = [(s, e) for n, s, e in timeline if n == "IDLE"]
    if idle:
        print("\nCPU idle intervals: " + ", ".join(f"{s}-{e}" for s, e in idle))
    else:
        print("\nCPU idle intervals: None")
    print("\n{:<6}{:>4}{:>4}{:>7}{:>5}{:>5}{:>5}".format(
        "PID", "AT", "BT", "Start", "End", "TAT", "WT"))
    for r in sorted(result, key=lambda r: r["start"]):
        print("{:<6}{:>4}{:>4}{:>7}{:>5}{:>5}{:>5}".format(
            r["pid"], r["at"], r["bt"], r["start"], r["end"], r["tat"], r["wt"]))
    n = len(result)
    print(f"\nAverage TAT = {sum(r['tat'] for r in result) / n:.2f}")
    print(f"Average WT  = {sum(r['wt'] for r in result) / n:.2f}")


def main():
    original = read_processes()
    backup = copy.deepcopy(original)  # Task 3: preserve original data

    print("\nOriginal process data (same dataset used for both algorithms):")
    print("{:<6}{:>4}{:>4}".format("PID", "AT", "BT"))
    for p in original:
        print("{:<6}{:>4}{:>4}".format(p["pid"], p["at"], p["bt"]))

    # Task 9: same dataset passed (as independent copies) to both algorithms
    t1, r1 = fcfs(copy.deepcopy(original))
    t2, r2 = sjf(copy.deepcopy(original))

    show("FCFS Scheduling", t1, r1)
    show("SJF (Non-preemptive) Scheduling", t2, r2)

    print("\nOriginal data preserved:", "YES" if original == backup else "NO")


if __name__ == "__main__":
    main()
