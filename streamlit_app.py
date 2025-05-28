# streamlit_app.py

import streamlit as st
from compiler import tokenize, parse, check_ast, execute

# Session state to hold tables and output
if 'tables' not in st.session_state:
    st.session_state.tables = {}
if 'output' not in st.session_state:
    st.session_state.output = ""

st.set_page_config(page_title="Hinglish SQL Compiler", layout="wide")

# Title
st.title("🧠 Hinglish SQL Compiler")

# Layout: Two columns (Input on left, Table on right)
left, right = st.columns(2)

# --- LEFT SIDE: Command input ---
with left:
    st.subheader("💬 Enter Hinglish SQL Command")
    user_command = st.text_area("Type here:", height=200)
    if st.button("▶️ Run Command"):
        try:
            tokens = tokenize(user_command)
            ast = parse(tokens)
            check_ast(ast)
            output = execute(ast, st.session_state.tables)
            st.session_state.output = f"✅ Output: {output}"
        except Exception as e:
            st.session_state.output = f"❌ Error: {str(e)}"

# --- RIGHT SIDE: Visual table viewer ---
with right:
    st.subheader("📊 Table Viewer")
    if not st.session_state.tables:
        st.info("No tables created yet.")
    else:
        for table_name, rows in st.session_state.tables.items():
            st.markdown(f"**🗃️ Table: `{table_name}`**")
            if rows:
                st.table({"Values": rows})
            else:
                st.write("Table is empty.")

# --- BOTTOM AREA: Output / Errors ---
st.markdown("---")
st.subheader("🧾 Output Log")
st.code(st.session_state.output, language='text')
