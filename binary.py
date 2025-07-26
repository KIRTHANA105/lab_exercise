import streamlit as st
import time
import random
import matplotlib.pyplot as plt

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def measure_search_times(start=1000, stop=10001, step=1000):
    times = []
    sizes = list(range(start, stop, step))
    for n in sizes:
        arr = sorted(random.sample(range(1, 10 * n), n))
        target = random.choice(arr)

        start_time = time.time()
        binary_search_recursive(arr, target, 0, n - 1)
        end_time = time.time()

        times.append((end_time - start_time) * 1000) 
    return sizes, times

st.set_page_config(page_title="Binary Search Analyzer", layout="centered")
st.title(" Recursive Binary Search - Time Complexity")
st.write("This app measures and visualizes the time taken by **recursive binary search** for various list sizes.")


start = st.slider("Start size (n)", 100, 5000, 1000, step=100)
stop = st.slider("End size (n)", start + 1000, 20000, 10000, step=1000)
step = st.slider("Step size", 100, 5000, 1000, step=100)

if st.button("Run Experiment"):
    with st.spinner("Running binary search tests..."):
        sizes, times = measure_search_times(start, stop + 1, step)

    st.write(" Results Table")
    st.dataframe({"Input Size (n)": sizes, "Time Taken (ms)": times})


    st.write(" Time vs Input Size")
    fig, ax = plt.subplots()
    ax.plot(sizes, times, marker='o', color='blue', linestyle='--')
    ax.set_xlabel("Input Size (n)")
    ax.set_ylabel("Time Taken (ms)")
    ax.set_title("Recursive Binary Search Time Analysis")
    st.pyplot(fig)


