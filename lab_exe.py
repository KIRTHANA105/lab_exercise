import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# ---------- Linear Search Function with Comparison Count ----------
def linear_search(arr, key):
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == key:
            return i, comparisons
    return -1, comparisons

# ---------- Lab Question 1: Time Analysis ----------
def time_analysis(n):
    arr = random.sample(range(1, n * 10), n)
    mid = n // 2

    key_best = arr[0]          # element at start
    key_avg = arr[mid]         # element in middle
    key_worst = -1             # not present

    # Best Case
    start = time.time()
    linear_search(arr, key_best)
    t_best = (time.time() - start) * 1000  # in ms

    # Average Case
    start = time.time()
    linear_search(arr, key_avg)
    t_avg = (time.time() - start) * 1000

    # Worst Case
    start = time.time()
    linear_search(arr, key_worst)
    t_worst = (time.time() - start) * 1000

    return t_best, t_avg, t_worst

# ---------- Lab Question 2: Comparison Count ----------
def comparison_analysis(sizes):
    best_list, avg_list, worst_list = [], [], []
    for n in sizes:
        arr = random.sample(range(1, n * 10), n)
        mid = n // 2

        # Best
        arr_best = [0] + arr[1:]
        _, c_best = linear_search(arr_best, 0)

        # Average
        arr_avg = arr[:]
        arr_avg[mid] = -1
        _, c_avg = linear_search(arr_avg, -1)

        # Worst
        _, c_worst = linear_search(arr, -99999)

        best_list.append(c_best)
        avg_list.append(c_avg)
        worst_list.append(c_worst)
    return best_list, avg_list, worst_list

# ---------- Streamlit App UI ----------
st.title("Linear Search Performance Analysis")

# --- Section 1: Time Analysis ---
st.header("Lab Question 1: Time Analysis (Best, Average, Worst Cases)")

n = st.number_input("Enter array size (e.g., 10000):", min_value=10, max_value=100000, value=10000)

if st.button("Run Time Analysis"):
    t_best, t_avg, t_worst = time_analysis(n)

    # Plot
    fig1, ax1 = plt.subplots()
    cases = ['Best (O(1))', 'Average (O(n/2))', 'Worst (O(n))']
    times = [t_best, t_avg, t_worst]
    ax1.bar(cases, times, color=['green', 'orange', 'red'])
    ax1.set_ylabel('Time (ms)')
    ax1.set_title('Time Taken for Linear Search Cases')
    st.pyplot(fig1)

    # Table
    st.subheader("Execution Time (ms)")
    st.write(f"Best Case: {t_best:.3f} ms")
    st.write(f"Average Case: {t_avg:.3f} ms")
    st.write(f"Worst Case: {t_worst:.3f} ms")

    st.markdown("**Observation:** Best case is O(1) as the element is found at the start. "
                "Average is roughly O(n/2), and worst is O(n) since the element is not present.")

# --- Section 2: Comparison Count ---
st.header("Lab Question 2: Comparison Count vs Input Size")

sizes_input = st.text_input("Enter input sizes separated by commas (e.g., 100,500,1000,5000,10000):", "100,500,1000,5000,10000")
if st.button("Show Comparison Graph"):
    try:
        sizes = list(map(int, sizes_input.strip().split(',')))
        best, avg, worst = comparison_analysis(sizes)

        # Plot
        fig2, ax2 = plt.subplots()
        ax2.plot(sizes, best, label='Best Case (O(1))', marker='o', color='green')
        ax2.plot(sizes, avg, label='Average Case (O(n/2))', marker='o', color='orange')
        ax2.plot(sizes, worst, label='Worst Case (O(n))', marker='o', color='red')
        ax2.set_xlabel('Input Size (n)')
        ax2.set_ylabel('Comparisons')
        ax2.set_title('Comparisons vs Input Size in Linear Search')
        ax2.legend()
        st.pyplot(fig2)

        # Table
        st.subheader("Number of Comparisons")
        st.write("| Size | Best | Avg | Worst |")
        st.write("|------|------|-----|-------|")
        for i in range(len(sizes)):
            st.write(f"| {sizes[i]} | {best[i]} | {avg[i]} | {worst[i]} |")

        st.markdown("**Observation:** Comparisons increase linearly with size. "
                    "Best is always 1, average is near n/2, and worst is n. Theoretical complexities match empirical results.")
    except:
        st.error("Please enter sizes correctly as comma-separated numbers (e.g., 100,500,1000)")
