import streamlit as st
import json
from datetime import datetime, date
import time

# ---------------- CONFIG ----------------
BIRTHDAY = datetime(2026, 2, 8, 0, 0, 0)  # 8 Feb 2026 at 00:00
MEMORY_FILE = "memories.json"

st.set_page_config(
    page_title="For You ❤️",
    page_icon="🎂",
    layout="centered"
)

# ---------------- CSS ANIMATIONS ----------------
st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.03); }
    100% { transform: scale(1); }
}

@keyframes glow {
    0% { box-shadow: 0 0 5px #ff9aa2; }
    50% { box-shadow: 0 0 20px #ff9aa2; }
    100% { box-shadow: 0 0 5px #ff9aa2; }
}

.fade-in {
    animation: fadeIn 1.2s ease-in-out;
}

.countdown-box {
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    background: #fff0f3;
    color: #ff4d6d;
    animation: pulse 3s infinite;
    font-size: 20px;
    margin-bottom: 20px;
}

.memory-box {
    padding: 25px;
    border-radius: 20px;
    background: #ffffff;
    color: #333333;
    animation: fadeIn 1.5s ease-in-out, glow 4s infinite;
    font-size: 18px;
    line-height: 1.6;
}

.locked-box {
    padding: 25px;
    border-radius: 20px;
    background: #f2f2f2;
    color: #000000;
    text-align: center;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MEMORIES ----------------
with open(MEMORY_FILE, "r", encoding="utf-8") as f:
    memories = json.load(f)

# ---------------- TIME CALCULATION ----------------
now = datetime.now()
time_left = BIRTHDAY - now

days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

days_key = str(days)

# ---------------- UI ----------------
st.markdown("<h1 class='fade-in'>💖 A Little Journey Just for You</h1>", unsafe_allow_html=True)
st.markdown("<p class='fade-in'>Something special unlocks every day…</p>", unsafe_allow_html=True)
st.divider()

# ---------------- COUNTDOWN ----------------
if time_left.total_seconds() > 0:
    st.markdown(
        f"""
        <div class="countdown-box">
        ⏳ <b>{days}</b> days  
        <b>{hours}</b> hours  
        <b>{minutes}</b> minutes  
        <b>{seconds}</b> seconds left
        </div>
        """,
        unsafe_allow_html=True
    )
elif time_left.total_seconds() <= 0:
    st.markdown(
        """
        <div class="countdown-box">
        🎉 IT'S YOUR DAY 🎉
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- MEMORY SECTION ----------------
# ---------------- MEMORY SECTION ----------------
st.divider()

if days_key in memories:
    memory_text = memories[days_key].replace("\n", "<br>")

    st.markdown(
        f"""
        <div class="memory-box">
        {memory_text}
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div class="locked-box">
        🔒 Today’s memory is locked<br>
        Come back tomorrow, jaan ❤️
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()
st.caption("Made with love — always by your side ❤️")

# ---------------- AUTO REFRESH ----------------
# ---------------- SAFE AUTO REFRESH ----------------
st.markdown(
    """
    <script>
    setTimeout(function() {
        window.location.reload();
    }, 1000);
    </script>
    """,
    unsafe_allow_html=True
)




