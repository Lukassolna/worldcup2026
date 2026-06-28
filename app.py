import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from streamlit_echarts import st_echarts
from datetime import datetime
from zoneinfo import ZoneInfo

# Hardcoded eventual winner — highlighted in the race view
LEADER = "Ogge"

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

ANSWERS_SHEET = "Answers"
FACIT_SHEET   = "Facit"
GOAL_COL = "Hur många mål görs det totalt under alla 72 matcher i gruppspelet?"

conn = st.connection("gsheets", type=GSheetsConnection)

def load(sheet):
    return conn.read(worksheet=sheet, ttl=60)

def get_match_cols(df):
    cols = list(df.columns)
    try:
        start = cols.index("E-postadress") + 1
        end   = cols.index(GOAL_COL)
        return cols[start:end]
    except ValueError:
        return []

def outcome(score):
    try:
        h, a = map(int, score.split("-"))
        return "H" if h > a else ("A" if a > h else "D")
    except Exception:
        return None

def calc_points(tip, result):
    if not result or not tip:
        return 0
    if tip == result:
        return 3
    if outcome(tip) == outcome(result):
        return 1
    return 0

# Build a normalised match name → kickoff time lookup
SCHEDULE_LOOKUP = {name.replace(" ", "").lower(): dt for name, dt in SCHEDULE}

def kickoff_time(match_col):
    key = match_col.replace(" ", "").lower()
    dt  = SCHEDULE_LOOKUP.get(key)
    return dt.strftime("%d %b %H:%M") if dt else ""

is_admin = "lukas" in st.query_params

if is_admin:
    # =========================================================
    # ADMIN
    # =========================================================
    st.title("🔐 Admin")

    answers_df = load(ANSWERS_SHEET)
    facit_df   = load(FACIT_SHEET)
    match_cols = get_match_cols(answers_df)

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
        timestamp = datetime.now(STOCKHOLM).strftime("%Y-%m-%d %H:%M:%S")
        conn.update(worksheet="LastUpdate", data=pd.DataFrame([[timestamp]]))
        st.success(f"Saved: {selected_match} → {new_result}")
        st.rerun()

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

else:
    # =========================================================
    # MAIN PAGE (scrollable)
    # =========================================================
    answers_df = load(ANSWERS_SHEET)
    facit_df   = load(FACIT_SHEET)

    def facit_for(match):
        if facit_df is not None and not facit_df.empty and match in facit_df.columns:
            vals = facit_df[match].dropna()
            if not vals.empty:
                return str(vals.iloc[0]).strip()
        return ""

    match_cols = get_match_cols(answers_df) if answers_df is not None and not answers_df.empty else []
    facit_row  = facit_df.iloc[0] if facit_df is not None and not facit_df.empty else {}

    # ---- Header ----
    st.title("🏆 Thanks for playing!")
    st.subheader(f"The winner is {LEADER} 🥇")

    if answers_df is None or answers_df.empty:
        st.info("No results yet.")
        st.stop()

    names = sorted(answers_df["Namn"].dropna().unique().tolist())
    player_rows = {name: answers_df[answers_df["Namn"] == name].iloc[0] for name in names}

    # ---- Final standings ----
    standings = []
    for name in names:
        pr = player_rows[name]
        pts = sum(
            calc_points(str(pr.get(m, "")).strip(), str(facit_row.get(m, "")).strip())
            for m in match_cols if m in facit_row
        )
        standings.append({"Name": name, "Points": int(pts)})
    df_lb = pd.DataFrame(standings).sort_values("Points", ascending=False).reset_index(drop=True)
    medals = {0: "🥇", 1: "🥈", 2: "🥉"}
    df_lb.insert(0, "Pos", [medals.get(i, str(i + 1)) for i in df_lb.index])

    # ---- Final standings (top) ----
    st.subheader("Final Standings")
    st.dataframe(df_lb, use_container_width=True, hide_index=True)

    # ---- Match-by-match race ----
    st.write("---")
    st.subheader("Race")

    # Matches with a result + known kickoff, in chronological order
    records = []  # (kickoff, match, result)
    for m in match_cols:
        result = facit_for(m)
        if not result or result == "nan":
            continue
        dt = SCHEDULE_LOOKUP.get(m.replace(" ", "").lower())
        if dt is None:
            continue
        records.append((dt, m, result))
    records.sort(key=lambda x: x[0])

    if not records:
        st.info("No results entered yet — the race will appear once results come in.")
    else:
        default_idx = names.index(LEADER) if LEADER in names else 0
        highlight = st.selectbox("Highlight player and press Play ▶", names, index=default_idx)

        # Cumulative standings snapshot after each match
        running = {name: 0 for name in names}
        steps = []  # (label, state)
        for dt, m, result in records:
            for name in names:
                tip = str(player_rows[name].get(m, "")).strip()
                running[name] += calc_points(tip, result)
            steps.append((f"{m}  →  {result}", dict(running)))

        max_pts = max(max(s.values()) for _, s in steps)

        # ECharts bar race: realtimeSort slides bars past each other smoothly.
        # yAxis keeps the fixed name order; realtimeSort reorders the bars (and
        # their axis labels) by value each step.
        BLUE, GOLD = "#4C8BF5", "#FFD700"

        def data_for(state):
            return [
                {"value": state[n],
                 "itemStyle": {"color": GOLD if n == highlight else BLUE}}
                for n in names
            ]

        base_option = {
            "timeline": {
                "data": [str(i + 1) for i in range(len(steps))],
                "axisType": "category",
                "autoPlay": False,
                "loop": False,
                "playInterval": 900,
                "top": 8, "left": "12%", "right": "12%",
                "symbol": "none",
                "controlPosition": "left",
                "label": {"formatter": "{value}", "interval": max(1, len(steps) // 12)},
                "controlStyle": {
                    "showPlayBtn": True, "showPrevBtn": True, "showNextBtn": True,
                    "itemSize": 30, "itemGap": 16,
                    "color": "#4C8BF5", "borderColor": "#4C8BF5", "borderWidth": 2,
                },
                "checkpointStyle": {"color": "#FFD700", "borderColor": "#FFD700"},
            },
            "grid": {"top": 95, "bottom": 30, "left": 90, "right": 70},
            "xAxis": {
                "type": "value",
                "max": round(max_pts * 1.15) + 1,
                "splitLine": {"lineStyle": {"type": "dashed"}},
            },
            "yAxis": {
                "type": "category",
                "data": names,
                "inverse": True,
                "animationDuration": 300,
                "animationDurationUpdate": 300,
            },
            "animationDuration": 0,
            "animationDurationUpdate": 800,
            "animationEasing": "linear",
            "animationEasingUpdate": "cubicOut",
            "series": [],
        }

        options = [
            {
                "title": {"text": label, "left": "center", "top": 50, "textStyle": {"fontSize": 15}},
                "series": [{
                    "type": "bar",
                    "realtimeSort": True,
                    "data": data_for(state),
                    "label": {"show": True, "position": "right",
                              "valueAnimation": True, "fontWeight": "bold"},
                }],
            }
            for label, state in steps
        ]

        st_echarts(
            options={"baseOption": base_option, "options": options},
            height=f"{max(360, 26 * len(names) + 130)}px",
        )

    # ---- Full tips matrix ----
    st.write("---")
    st.title("🔍 Tips")

    if True:  # Full tips matrix
        names = sorted(answers_df["Namn"].dropna().unique().tolist())

        matrix_css = """
        <style>
        .matrix-table { border-collapse: collapse; font-size: 9px; white-space: nowrap; }
        .matrix-table th { background: #444; color: #fff; padding: 3px 5px; text-align: center; position: sticky; top: 0; z-index: 4; }
        .matrix-table td { padding: 2px 4px; border-bottom: 1px solid #e0e0e0; text-align: center; }
        .matrix-table tr:hover td { background: rgba(100,100,100,0.08); }
        .matrix-table tr:hover td.pin1, .matrix-table tr:hover td.pin2, .matrix-table tr:hover td.pin3 { background: #1a1d23; }
        .pin-base { position: sticky; z-index: 2; background: #0e1117; color: #fafafa; }
        .matrix-table th.pin1, .matrix-table th.pin2, .matrix-table th.pin3 { position: sticky; z-index: 5; background: #444; color: #fff; text-align: left; }
        .matrix-table td.pin1, .matrix-table td.pin2, .matrix-table td.pin3 { position: sticky; z-index: 2; background: #0e1117; color: #fafafa; text-align: left; }
        .matrix-table th.pin1, .matrix-table td.pin1 { left: 0px; min-width: 110px; max-width: 110px; overflow: hidden; text-overflow: ellipsis; }
        .matrix-table th.pin2, .matrix-table td.pin2 { left: 110px; min-width: 45px; max-width: 45px; }
        .matrix-table th.pin3, .matrix-table td.pin3 { left: 155px; min-width: 35px; max-width: 35px; border-right: 1px solid #333; }
        .c3 { background: #4CAF50; color: #222; font-weight: bold; border-radius: 3px; padding: 1px 5px; }
        .c0 { background: #e53935; color: #222; border-radius: 3px; padding: 1px 5px; }
        .c1 { background: #CDDC39; color: #222; border-radius: 3px; padding: 1px 5px; }
        </style>
        """

        header_cells = '<th class="pin1">Match</th><th class="pin2">Kickoff</th><th class="pin3">Result</th>'
        for name in names:
            header_cells += f"<th>{name}</th>"

        rows_html = ""
        for match in match_cols:
            result = facit_for(match)
            has_result = result and result != "nan"
            result_td = f'<td class="pin3"><b>{result}</b></td>' if has_result else '<td class="pin3">–</td>'
            row_html = f'<td class="pin1">{match}</td><td class="pin2" style="color:#888">{kickoff_time(match)}</td>{result_td}'
            for name in names:
                person_row = answers_df[answers_df["Namn"] == name]
                tip = str(person_row.iloc[0].get(match, "")).strip() if not person_row.empty else ""
                if has_result:
                    pts = calc_points(tip, result)
                    css = "c3" if pts == 3 else ("c1" if pts == 1 else "c0")
                    cell = f'<td><span class="{css}">{tip or "–"}</span></td>'
                else:
                    cell = f"<td>{tip or '–'}</td>"
                row_html += cell
            rows_html += f"<tr>{row_html}</tr>"

        html = matrix_css + f'<div style="overflow:auto; max-height:75vh"><table class="matrix-table"><thead><tr>{header_cells}</tr></thead><tbody>{rows_html}</tbody></table></div>'
        st.markdown(html, unsafe_allow_html=True)
