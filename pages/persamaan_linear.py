import streamlit as st
import numpy as np

def solve_linear_program(c, A, b):
    m, n = A.shape
    c = np.array(c)
    A = np.array(A)
    b = np.array(b)

    # Menggunakan metode Simplex untuk menyelesaikan pemrograman linier
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:m, :n] = A
    tableau[:m, n:] = np.eye(m)
    tableau[m, :n] = c
    tableau[m, n:] = np.zeros(m)

    pivot_col = np.argmax(tableau[m, :n])
    while pivot_col != -1:
        pivot_row = np.argmin(tableau[:m, -1] / tableau[:m, pivot_col])
        pivot_val = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_val
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]
        pivot_col = np.argmax(tableau[m, :n])

    # Menghitung solusi dan dualitas
    primal_solution = tableau[:m, -1]
    dual_solution = tableau[m, :n]

    return primal_solution, dual_solution

def main():
    st.title("Dualitas dan Sensitivitas")
    st.write("Masukkan data pemrograman linier di bawah ini:")

    num_variables = st.number_input("Jumlah Variabel", min_value=1, step=1, value=1)
    num_constraints = st.number_input("Jumlah Kendala", min_value=1, step=1, value=1)

    c = []
    for j in range(num_variables):
        coefficient = st.number_input(f"Koefisien Fungsi Tujuan untuk Variabel {j+1}", value=0.0)
        c.append(coefficient)

    A = []
    for i in range(num_constraints):
        row = []
        for j in range(num_variables):
            coefficient = st.number_input(f"Koefisien Kendala {i+1} untuk Variabel {j+1}", value=0.0)
            row.append(coefficient)
        A.append(row)

    b = []
    for i in range(num_constraints):
        constraint_value = st.number_input(f"Nilai Kendala {i+1}", value=0.0)
        b.append(constraint_value)

    c = np.array(c)
    A = np.array(A)
    b = np.array(b)

    if st.button("Hitung"):
        primal_solution, dual_solution = solve_linear_program(c, A, b)
        st.success(f"Solusi Primal: {primal_solution}")
        st.success(f"Solusi Dual: {dual_solution}")

if __name__ == "__main__":
    main()
