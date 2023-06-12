import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment

def assignment_problem(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    assignment = np.column_stack((row_ind, col_ind))
    total_cost = cost_matrix[row_ind, col_ind].sum()
    return assignment, total_cost

def main():
    st.title("Persoalan Penugasan")
    st.write("Masukkan data penugasan di bawah ini:")

    num_workers = st.number_input("Jumlah Pekerja", min_value=1, step=1, value=1)
    num_jobs = st.number_input("Jumlah Pekerjaan", min_value=1, step=1, value=1)

    cost_matrix = []
    for i in range(num_workers):
        row = []
        for j in range(num_jobs):
            cost = st.number_input(f"Biaya Pekerja {i+1} untuk Pekerjaan {j+1}", value=0.0)
            row.append(cost)
        cost_matrix.append(row)

    cost_matrix = np.array(cost_matrix)

    if st.button("Hitung"):
        assignment, total_cost = assignment_problem(cost_matrix)
        st.success(f"Solusi Penugasan: \n{assignment}")
        st.success(f"Biaya Total Minimum: {total_cost}")

if __name__ == "__main__":
    main()
