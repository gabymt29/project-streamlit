import streamlit as st
import numpy as np
from scipy.optimize import linprog

def transport_problem(cost_matrix, supply_vector, demand_vector):
    num_supply = len(supply_vector)
    num_demand = len(demand_vector)

    # Mengubah persoalan transportasi menjadi bentuk standar
    # dengan menambahkan dummy supply atau demand jika perlu
    if num_supply < num_demand:
        supply_vector = np.append(supply_vector, np.sum(demand_vector) - np.sum(supply_vector))
        cost_matrix = np.vstack([cost_matrix, np.zeros(num_demand)])
    elif num_demand < num_supply:
        demand_vector = np.append(demand_vector, np.sum(supply_vector) - np.sum(demand_vector))
        cost_matrix = np.hstack([cost_matrix, np.zeros((num_supply, 1))])

    # Menggunakan metode linprog untuk menyelesaikan persoalan transportasi
    c = cost_matrix.flatten()
    A_eq = np.zeros((num_supply + num_demand, num_supply * num_demand))
    b_eq = np.concatenate([supply_vector, demand_vector])
    for i in range(num_supply):
        A_eq[i, i * num_demand: (i + 1) * num_demand] = 1
    for j in range(num_demand):
        A_eq[num_supply + j, j: num_supply * num_demand: num_demand] = 1
    bounds = [(0, None)] * (num_supply * num_demand)

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    # Mengembalikan hasil alokasi dan biaya total minimum
    allocation = np.round(result.x.reshape((num_supply, num_demand)), 2)
    total_cost = round(result.fun, 2)

    return allocation, total_cost

def main():
    st.title("Persoalan Transportasi")
    st.write("Masukkan data transportasi di bawah ini:")

    num_supply = st.number_input("Jumlah Sumber", min_value=1, step=1, value=1)
    num_demand = st.number_input("Jumlah Tujuan", min_value=1, step=1, value=1)

    cost_matrix = []
    for i in range(num_supply):
        row = []
        for j in range(num_demand):
            cost = st.number_input(f"Biaya dari Sumber {i+1} ke Tujuan {j+1}", value=0.0)
            row.append(cost)
        cost_matrix.append(row)

    supply_vector = []
    demand_vector = []
    for i in range(num_supply):
        supply = st.number_input(f"Kapasitas Sumber {i+1}", min_value=0.0, value=0.0)
        supply_vector.append(supply)
    for j in range(num_demand):
        demand = st.number_input(f"Permintaan Tujuan {j+1}", min_value=0.0, value=0.0)
        demand_vector.append(demand)

    cost_matrix = np.array(cost_matrix)
    supply_vector = np.array(supply_vector)
    demand_vector = np.array(demand_vector)

    if st.button("Hitung"):
        allocation, total_cost = transport_problem(cost_matrix, supply_vector, demand_vector)
        st.success(f"Solusi Alokasi: \n{allocation}")
        st.success(f"Biaya Total Minimum: {total_cost}")

if __name__ == "__main__":
    main()
