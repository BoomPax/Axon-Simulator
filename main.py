#total_simulation_time = int(input("How long do you want the simulation to be(ms): "))#milliseconds?
#injury_damage = #percent?

from neuron import simulate_neuron
import streamlit as st
import plotly.express as px
import pandas as pd 


st.title("Concussed Neuron Model")

concussion_severity = st.slider("Concussion Severity", 0, 10, 0)

fire = st.button("Fire Action Potential")

# Keep the last result so the graph doesn't reset on other interactions
if "data" not in st.session_state:
    st.session_state.data = simulate_neuron(fire=False)

if fire:
    st.session_state.data = simulate_neuron(
        fire=True,
        severity=concussion_severity,
    )

time, voltage, m, h, n = st.session_state.data

# Graph 1: Membrane Potential
fig1 = px.line(
    x=time,
    y=voltage,
    labels={"x": "Time (ms)", "y": "Membrane Potential (mV)"},
    title="Membrane Potential"
)
fig1.update_yaxes(range=[-90, 60])  # fixed range so the axis doesn't jump
st.plotly_chart(fig1, width="stretch")

# Graph 2: Gating Variables
df = pd.DataFrame({
    "Time (ms)": time,
    "m (Sodium Activation)": m,
    "h (Sodium Inactivation)": h,
    "n (Potassium Activation)": n
})

fig2 = px.line(
    df,
    x="Time (ms)",
    y=["m (Sodium Activation)", "h (Sodium Inactivation)", "n (Potassium Activation)"],
    title="Gating Variables"
)
fig2.update_yaxes(range=[0, 1])
st.plotly_chart(fig2, width="stretch")