def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
    
    return merged
def input_intervals():
    intervals = []
    try:
        num_intervals = int(input("Enter the number of intervals: "))
        for i in range(num_intervals):
            start = int(input(f"Enter the start of interval {i+1}: "))
            end = int(input(f"Enter the end of interval {i+1}: "))
            intervals.append([start, end])
    except ValueError:
        print("Invalid inpu.")
    return intervals

if __name__ == "__main__":
    intervals = input_intervals()
    merged_intervals = merge_intervals(intervals)
    print("Merged intervals:", merged_intervals)
