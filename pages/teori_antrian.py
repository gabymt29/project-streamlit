import streamlit as st
import numpy as np

def mm1_queue(lam, mu, c):
    rho = lam / (c * mu)
    Lq = rho / (1 - rho)
    Wq = Lq / lam
    L = lam * Wq
    W = Wq + (1 / mu)
    return Lq, Wq, L, W

def main():
    st.title("Model Antrian M/M/1")
    st.write("Masukkan parameter antrian di bawah ini:")

    lam = st.number_input("Intensitas kedatangan (λ)", min_value=0.0, value=0.0)
    mu = st.number_input("Intensitas pelayanan (μ)", min_value=0.0, value=0.0)
    c = st.number_input("Jumlah server (c)", min_value=1, step=1, value=1)

    if st.button("Hitung"):
        if lam >= c * mu:
            st.error("Sistem tidak stabil (λ >= c * μ)")
        else:
            Lq, Wq, L, W = mm1_queue(lam, mu, c)
            st.success(f"Jumlah rata-rata pelanggan dalam antrian (Lq): {Lq:.4f}")
            st.success(f"Waktu rata-rata menunggu dalam antrian (Wq): {Wq:.4f}")
            st.success(f"Jumlah rata-rata pelanggan dalam sistem (L): {L:.4f}")
            st.success(f"Waktu rata-rata dalam sistem (W): {W:.4f}")

if __name__ == "__main__":
    main()
