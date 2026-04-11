import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

STOCKHOLM = ZoneInfo("Europe/Stockholm")

SCHEDULE = [
    # Round 1
    ("Mexiko - Sydafrika (A)",                  datetime(2026, 6, 11, 21,  0, tzinfo=STOCKHOLM)),
    ("Sydkorea - Tjeckien (A)",                 datetime(2026, 6, 12,  4,  0, tzinfo=STOCKHOLM)),
    ("Kanada - Bosnien (B)",                    datetime(2026, 6, 12, 21,  0, tzinfo=STOCKHOLM)),
    ("USA - Paraguay (D)",                      datetime(2026, 6, 13,  3,  0, tzinfo=STOCKHOLM)),
    ("Qatar - Schweiz (B)",                     datetime(2026, 6, 13, 21,  0, tzinfo=STOCKHOLM)),
    ("Brasilien - Marocko (C)",                 datetime(2026, 6, 14,  0,  0, tzinfo=STOCKHOLM)),
    ("Haiti - Skottland (C)",                   datetime(2026, 6, 14,  3,  0, tzinfo=STOCKHOLM)),
    ("Australien - Turkiet (D)",                datetime(2026, 6, 14,  6,  0, tzinfo=STOCKHOLM)),
    ("Tyskland - Curaçao (E)",                  datetime(2026, 6, 14, 19,  0, tzinfo=STOCKHOLM)),
    ("Nederländerna - Japan (F)",               datetime(2026, 6, 14, 22,  0, tzinfo=STOCKHOLM)),
    ("Elfenbenskusten - Ecuador (E)",           datetime(2026, 6, 15,  1,  0, tzinfo=STOCKHOLM)),
    ("Sverige - Tunisien (F)",                  datetime(2026, 6, 15,  4,  0, tzinfo=STOCKHOLM)),
    ("Spanien - Kap Verde (H)",                 datetime(2026, 6, 15, 18,  0, tzinfo=STOCKHOLM)),
    ("Belgien - Egypten (G)",                   datetime(2026, 6, 15, 21,  0, tzinfo=STOCKHOLM)),
    ("Saudiarabien - Uruguay (H)",              datetime(2026, 6, 16,  0,  0, tzinfo=STOCKHOLM)),
    ("Iran - Nya Zeeland (G)",                  datetime(2026, 6, 16,  3,  0, tzinfo=STOCKHOLM)),
    ("Frankrike - Senegal (I)",                 datetime(2026, 6, 16, 21,  0, tzinfo=STOCKHOLM)),
    ("Irak - Norge (I)",                        datetime(2026, 6, 17,  0,  0, tzinfo=STOCKHOLM)),
    ("Argentina - Algeriet (J)",                datetime(2026, 6, 17,  3,  0, tzinfo=STOCKHOLM)),
    ("Österrike - Jordanien (J)",               datetime(2026, 6, 17,  6,  0, tzinfo=STOCKHOLM)),
    ("Portugal - DR Kongo (K)",                 datetime(2026, 6, 17, 19,  0, tzinfo=STOCKHOLM)),
    ("England - Kroatien (L)",                  datetime(2026, 6, 17, 22,  0, tzinfo=STOCKHOLM)),
    ("Ghana - Panama (L)",                      datetime(2026, 6, 18,  1,  0, tzinfo=STOCKHOLM)),
    ("Uzbekistan - Colombia (K)",               datetime(2026, 6, 18,  4,  0, tzinfo=STOCKHOLM)),
    # Round 2
    ("Tjeckien - Sydafrika (A)",                datetime(2026, 6, 18, 18,  0, tzinfo=STOCKHOLM)),
    ("Schweiz - Bosnien och Herzegovina (B)",   datetime(2026, 6, 18, 21,  0, tzinfo=STOCKHOLM)),
    ("Kanada - Qatar (B)",                      datetime(2026, 6, 19,  0,  0, tzinfo=STOCKHOLM)),
    ("Mexiko - Sydkorea (A)",                   datetime(2026, 6, 19,  3,  0, tzinfo=STOCKHOLM)),
    ("USA - Australien (D)",                    datetime(2026, 6, 19, 21,  0, tzinfo=STOCKHOLM)),
    ("Skottland - Marocko (C)",                 datetime(2026, 6, 20,  0,  0, tzinfo=STOCKHOLM)),
    ("Brasilien - Haiti (C)",                   datetime(2026, 6, 20,  2, 30, tzinfo=STOCKHOLM)),
    ("Turkiet - Paraguay (D)",                  datetime(2026, 6, 20,  5,  0, tzinfo=STOCKHOLM)),
    ("Nederländerna - Sverige (F)",             datetime(2026, 6, 20, 19,  0, tzinfo=STOCKHOLM)),
    ("Tyskland - Elfenbenskusten (E)",          datetime(2026, 6, 20, 22,  0, tzinfo=STOCKHOLM)),
    ("Ecuador - Curaçao (E)",                   datetime(2026, 6, 21,  2,  0, tzinfo=STOCKHOLM)),
    ("Tunisien - Japan (F)",                    datetime(2026, 6, 21,  6,  0, tzinfo=STOCKHOLM)),
    ("Spanien - Saudiarabien (H)",              datetime(2026, 6, 21, 18,  0, tzinfo=STOCKHOLM)),
    ("Belgien - Iran (G)",                      datetime(2026, 6, 21, 21,  0, tzinfo=STOCKHOLM)),
    ("Uruguay - Kap Verde (H)",                 datetime(2026, 6, 22,  0,  0, tzinfo=STOCKHOLM)),
    ("Nya Zeeland - Egypten (G)",               datetime(2026, 6, 22,  3,  0, tzinfo=STOCKHOLM)),
    ("Argentina - Österrike (J)",               datetime(2026, 6, 22, 19,  0, tzinfo=STOCKHOLM)),
    ("Frankrike - Irak (I)",                    datetime(2026, 6, 22, 23,  0, tzinfo=STOCKHOLM)),
    ("Norge - Senegal (I)",                     datetime(2026, 6, 23,  2,  0, tzinfo=STOCKHOLM)),
    ("Jordanien - Algeriet (J)",                datetime(2026, 6, 23,  5,  0, tzinfo=STOCKHOLM)),
    ("Portugal - Uzbekistan (K)",               datetime(2026, 6, 23, 19,  0, tzinfo=STOCKHOLM)),
    ("England - Ghana (L)",                     datetime(2026, 6, 23, 22,  0, tzinfo=STOCKHOLM)),
    ("Panama - Kroatien (L)",                   datetime(2026, 6, 24,  1,  0, tzinfo=STOCKHOLM)),
    ("Colombia - DR Kongo (K)",                 datetime(2026, 6, 24,  4,  0, tzinfo=STOCKHOLM)),
    # Round 3
    ("Schweiz - Kanada (B)",                    datetime(2026, 6, 24, 21,  0, tzinfo=STOCKHOLM)),
    ("Bosnien - Qatar (B)",                     datetime(2026, 6, 24, 21,  0, tzinfo=STOCKHOLM)),
    ("Marocko - Haiti (C)",                     datetime(2026, 6, 25,  0,  0, tzinfo=STOCKHOLM)),
    ("Skottland - Brasilien (C)",               datetime(2026, 6, 25,  0,  0, tzinfo=STOCKHOLM)),
    ("Sydafrika - Sydkorea (A)",                datetime(2026, 6, 25,  3,  0, tzinfo=STOCKHOLM)),
    ("Tjeckien - Mexiko (A)",                   datetime(2026, 6, 25,  3,  0, tzinfo=STOCKHOLM)),
    ("Curaçao - Elfenbenskusten (E)",           datetime(2026, 6, 25, 22,  0, tzinfo=STOCKHOLM)),
    ("Ecuador - Tyskland (E)",                  datetime(2026, 6, 25, 22,  0, tzinfo=STOCKHOLM)),
    ("Tunisien - Nederländerna (F)",            datetime(2026, 6, 26,  1,  0, tzinfo=STOCKHOLM)),
    ("Japan - Sverige (F)",                     datetime(2026, 6, 26,  1,  0, tzinfo=STOCKHOLM)),
    ("Turkiet - USA (D)",                       datetime(2026, 6, 26,  4,  0, tzinfo=STOCKHOLM)),
    ("Paraguay - Australien (D)",               datetime(2026, 6, 26,  4,  0, tzinfo=STOCKHOLM)),
    ("Norge - Frankrike (I)",                   datetime(2026, 6, 26, 21,  0, tzinfo=STOCKHOLM)),
    ("Senegal - Irak (I)",                      datetime(2026, 6, 26, 21,  0, tzinfo=STOCKHOLM)),
    ("Kap Verde - Saudiarabien (H)",            datetime(2026, 6, 27,  2,  0, tzinfo=STOCKHOLM)),
    ("Uruguay - Spanien (H)",                   datetime(2026, 6, 27,  2,  0, tzinfo=STOCKHOLM)),
    ("Nya Zeeland - Belgien (G)",               datetime(2026, 6, 27,  5,  0, tzinfo=STOCKHOLM)),
    ("Egypten - Iran (G)",                      datetime(2026, 6, 27,  5,  0, tzinfo=STOCKHOLM)),
    ("Panama - England (L)",                    datetime(2026, 6, 27, 23,  0, tzinfo=STOCKHOLM)),
    ("Kroatien - Ghana (L)",                    datetime(2026, 6, 27, 23,  0, tzinfo=STOCKHOLM)),
    ("Colombia - Portugal (K)",                 datetime(2026, 6, 28,  1, 30, tzinfo=STOCKHOLM)),
    ("DR Kongo - Uzbekistan (K)",               datetime(2026, 6, 28,  1, 30, tzinfo=STOCKHOLM)),
    ("Algeriet - Österrike (J)",                datetime(2026, 6, 28,  4,  0, tzinfo=STOCKHOLM)),
    ("Jordanien - Argentina (J)",               datetime(2026, 6, 28,  4,  0, tzinfo=STOCKHOLM)),
]

st.set_page_config(page_title="World Cup 2026", page_icon="⚽", layout="centered")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

ANSWERS_SHEET  = "Formulärsvar 1"
FACIT_SHEET    = "Facit"
STANDINGS_SHEET = "Standings"
GOAL_COL = "Hur många mål görs det totalt under alla 72 matcher i gruppspelet?"

conn = st.connection("gsheets", type=GSheetsConnection)

def load(sheet):
    return conn.read(worksheet=sheet, ttl=0)

def get_match_cols(df):
    cols = list(df.columns)
    try:
        start = cols.index("E-postadress") + 1
        end   = cols.index(GOAL_COL)
        return cols[start:end]
    except ValueError:
        return []

# --- Sidebar navigation ---
st.sidebar.title("⚽ World Cup 2026")

is_admin = "lukas" in st.query_params

if is_admin:
    page = "🔐 lukasadmin"
else:
    page = st.sidebar.radio("", ["🏆 Standings", "📅 Schedule", "🔍 Tips"])

# =========================================================
# STANDINGS
# =========================================================
if page == "🏆 Standings":
    st.title("🏆 Standings")
    df = load(STANDINGS_SHEET)
    if df is not None and not df.empty:
        st.dataframe(
            df.sort_values(df.columns[0]).reset_index(drop=True),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No standings yet.")

# =========================================================
# SCHEDULE
# =========================================================
elif page == "📅 Schedule":
    st.title("📅 Schedule")

    now = datetime.now(STOCKHOLM)

    upcoming = [(name, dt) for name, dt in SCHEDULE if dt >= now]
    played   = [(name, dt) for name, dt in SCHEDULE if dt < now]

    if upcoming:
        next_name, next_dt = upcoming[0]
        delta = next_dt - now
        days  = delta.days
        hours = delta.seconds // 3600
        if days > 0:
            countdown = f"{days}d {hours}h"
        else:
            mins = (delta.seconds % 3600) // 60
            countdown = f"{hours}h {mins}m" if hours > 0 else f"{mins}m"
        st.info(f"**Next match in {countdown}** — {next_name}  ·  {next_dt.strftime('%a %d %b, %H:%M')}")

    tab_upcoming, tab_all = st.tabs([f"Upcoming ({len(upcoming)})", f"All ({len(SCHEDULE)})"])

    def build_df(matches):
        return pd.DataFrame(
            [{"Date": dt.strftime("%a %d %b"), "Time": dt.strftime("%H:%M"), "Match": name}
             for name, dt in matches]
        )

    with tab_upcoming:
        if upcoming:
            st.dataframe(build_df(upcoming), use_container_width=True, hide_index=True)
        else:
            st.success("All group stage matches have been played!")

    with tab_all:
        df_all = build_df(SCHEDULE)
        df_all.insert(0, "", ["✅" if dt < now else "🔜" for _, dt in SCHEDULE])
        st.dataframe(df_all, use_container_width=True, hide_index=True)

# =========================================================
# TIPS
# =========================================================
elif page == "🔍 Tips":
    st.title("🔍 View Tips")

    answers_df = load(ANSWERS_SHEET)
    facit_df   = load(FACIT_SHEET)

    if answers_df is None or answers_df.empty:
        st.warning("No answers found.")
        st.stop()

    match_cols = get_match_cols(answers_df)

    # Helper: get facit value for a match
    def facit_for(match):
        if facit_df is not None and not facit_df.empty and match in facit_df.columns:
            vals = facit_df[match].dropna()
            if not vals.empty:
                return str(vals.iloc[0]).strip()
        return ""

    view_mode = st.radio("View by", ["Person", "Match"], horizontal=True)

    if view_mode == "Person":
        names = sorted(answers_df["Namn"].dropna().unique().tolist())
        selected = st.selectbox("Select person", names)
        row = answers_df[answers_df["Namn"] == selected].iloc[0]

        st.subheader(f"Tips by {selected}")

        data = []
        for match in match_cols:
            tip       = str(row.get(match, "")).strip()
            result    = facit_for(match)
            entry = {"Match": match, "Tip": tip}
            if result:
                entry["Result"] = result
                entry["✓"] = "✅" if tip == result else "❌"
            data.append(entry)

        st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

        goal_tip = row.get(GOAL_COL, "")
        st.caption(f"Total goals guess: **{goal_tip}**")

    else:  # Match view
        selected_match = st.selectbox("Select match", match_cols)
        st.subheader(f"**{selected_match}**")

        result = facit_for(selected_match)
        if result:
            st.success(f"Result: **{result}**")
        else:
            st.info("Result not entered yet.")

        data = []
        for _, r in answers_df.iterrows():
            tip   = str(r.get(selected_match, "")).strip()
            entry = {"Name": r.get("Namn", ""), "Tip": tip}
            if result:
                entry["✓"] = "✅" if tip == result else "❌"
            data.append(entry)

        st.dataframe(
            pd.DataFrame(data).sort_values("Name").reset_index(drop=True),
            use_container_width=True,
            hide_index=True,
        )

# =========================================================
# ADMIN
# =========================================================
elif page == "🔐 lukasadmin":
    st.title("🔐 Admin")

    answers_df = load(ANSWERS_SHEET)
    facit_df   = load(FACIT_SHEET)
    match_cols = get_match_cols(answers_df)

    # Build current facit as dict
    current_facit = {col: "" for col in match_cols}
    if facit_df is not None and not facit_df.empty:
        row = facit_df.iloc[0]
        for col in match_cols:
            if col in facit_df.columns:
                val = row.get(col, "")
                current_facit[col] = "" if pd.isna(val) else str(val)

    st.subheader("Enter Match Result")

    col1, col2 = st.columns([3, 1])
    with col1:
        selected_match = st.selectbox("Match", match_cols)
    with col2:
        new_result = st.text_input("Result", value=current_facit.get(selected_match, ""))

    if st.button("💾 Save Result", use_container_width=True):
        current_facit[selected_match] = new_result.strip()
        conn.update(worksheet=FACIT_SHEET, data=pd.DataFrame([current_facit]))
        st.success(f"Saved: {selected_match} → {new_result}")
        st.rerun()

    # Summary of entered results
    st.write("---")
    st.subheader("Results entered so far")
    entered = {k: v for k, v in current_facit.items() if v}
    if entered:
        st.dataframe(
            pd.DataFrame(list(entered.items()), columns=["Match", "Result"]),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No results entered yet.")
