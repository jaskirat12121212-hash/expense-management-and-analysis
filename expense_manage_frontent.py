import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns
import os 

st.title(
   "Expense management "
   #"This expense management is used to manage and analyse the expense "
)
FILE="transaction.csv"
if os.path.exists(FILE):
    df=pd.read_csv(FILE)
else:
    df=pd.DataFrame(columns=["amount","category","transaction_type"])
if "transactions" not in st.session_state:
        if os.path.exists(FILE):
            st.session_state.transactions=pd.read_csv(FILE)
        else:
            st.session_state.transactions=pd.DataFrame(columns=["amount","category","transaction_type"])

with st.sidebar.form("expense form"):
 st.sidebar.header("Enter the parameters for analyses")
 amount=st.sidebar.number_input("Enter amount")

 categories=st.sidebar.selectbox("Select category",["Groceries","Rent","Food","Transport","Shopping","Entertainment","Healthcare","Others"])

 transaction_type=st.sidebar.selectbox("Enter transaction type",["UPI","Cash","Card"])
 submitted=st.form_submit_button("Add expense")
 if submitted:
     new_data=pd.DataFrame([{ "category":categories,"amount":amount,"type":transaction_type}])
     st.session_state.transactions=pd.concat([st.session_state.transactions,new_data],ignore_index=True)
     st.session_state.transactions.to_csv(FILE,index=False)
     st.success("Expense added successfully")

if not st.session_state.transactions.empty:
    st.subheader("Previous expenses")
    st.dataframe(st.session_state.transactions)
else:
    st.info("No previous expense")

if st.button("submit"):
    df=st.session_state.transactions.copy()
    st.subheader("All expenses")
    st.dataframe(df)
    if not df.empty:
        category_total=df.groupby("category")["amount"].sum().sort_values(ascending=False)
        st.subheader("Total spending")
        st.bar_chart(category_total)
    else:
        st.info("Add expense first")
    new_data=pd.DataFrame([{"amount":amount,"category":categories,"transaction_type":transaction_type}])
    st.session_state.transactions=pd.concat([st.session_state.transactions,new_data],ignore_index=True)
    st.session_state.transactions.to_csv(FILE,index=False)
    df=st.session_state.transactions
    previous=df[(df["category"]=="Rent")&(df["transaction_type"]=="UPI")].tail(5)
    if len(previous)==0:
        st.warning("No previous expense")
        st.info("Add past transaction")
    else:
        comparison=pd.DataFrame({"Transaction":[f"Previous {i+1}" for i in range(len(previous))]+["New expense"],"Amount":previous(amount).astype(float).islist()+
                                 [float(amount)]})
        st.subheader(f"{categories}:Previous expense vs new expense")
        st.bar_chart(comparison.set_index("transactions"),y="Amount")
        average=previous[amount].astype(float).mean()
        difference=amount-average
        st.metric("Previous expenses","{average:.2f}",delta=f"{difference} vs average")
        if difference>0:
            st.write(f"The new expense is {difference} greater than previous one")
        elif difference<0:
            st.write(f"The new expense is {difference} below previous one")
        else:
            st.write("The new expense is same as previous expense")



   

