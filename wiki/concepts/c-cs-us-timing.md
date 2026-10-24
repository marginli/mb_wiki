---
title: 制約刺激與非制約刺激的時序（CS–US timing）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, mb-learning]
confidence: high
---

# 制約刺激與非制約刺激的時序（CS–US timing）

**聯想學習（associative learning）裡，制約刺激（conditioned stimulus, CS；本庫指氣味）與非制約刺激（unconditioned stimulus, US；電擊、獎賞，或代替它們的多巴胺訊號）誰先誰後、隔多久，決定動物學不學得到、學到什麼方向。** 順向配對（forward pairing）＝CS 先、US 後；逆向配對（backward pairing）＝US 先、CS 後；痕跡制約（trace conditioning）＝CS 結束後空白一段時間才給 US。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蘑菇體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **MBON**：蘑菇體輸出神經元（MB output neuron），接收 KC 的訊號，推動果蠅靠近或走開。
- **區室**：葉沿長度切成的一格，以 γ1pedc、γ2、γ4、α2 等編號命名；細胞也以所在區室命名，例如 MBON-γ1pedc、PPL1-γ1pedc。詳見 [[c-mb-compartment]]。
- **乙醯膽鹼**（acetylcholine）：嗅覺訊號傳給 KC 時用的化學物質；在取出的腦上噴它，等於「假裝聞到氣味」。
- **光**：指光遺傳活化 DAN，即讓 DAN 帶上照紅光就放電的蛋白，用光代替真的懲罰或獎賞（見 [[c-us-substitution]]）。
- **離體、在體、閉迴路**：離體＝取出的腦泡在養液裡；在體＝活果蠅頭部固定、打開腦殼；閉迴路＝頭部固定的果蠅踩在球上走，送氣管隨牠的轉向轉動，可同時記錄行為與腦。
- **協同**：兩個刺激配對時的反應，大於兩者分別單獨給的反應相加（見 [[c-coincidence-detection]]）。
- **價性**（valence）：氣味被學成「好」（吸引）或「壞」（迴避）。
- **DopR1、DopR2、內質網鈣**：KC 上兩種多巴胺受體。DopR1 接上製造 cAMP 的路徑；DopR2 接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑，所以量內質網鈣就是在看 DopR2 路徑有沒有啟動。

## 怎麼算 / 怎麼判定

時間差＝US 的某個時點減 CS 的某個時點，正值＝順向、負值＝逆向。**本頁最該記住的一件事：三篇的「某個時點」不一樣。**

| 來源 | 從哪裡算到哪裡 | 測了哪些時間差 |
|---|---|---|
| Tomchik 2009 行為 | 氣味**結束** → 電擊開始（氣味、電擊各 60 s） | 同時、倒序、trace 0／15／30／45 s |
| Tomchik 2009 成像 | 乙醯膽鹼（模擬氣味）噴射**開始** → 多巴胺噴射開始 | −15、+1、+15、+30 s |
| Hige 2015 | 氣味開始 → 第一下光。光共四下、每 0.5 s 一下（跨 1.5 s）。順向：第一下在氣味開始後 0.2 s；逆向寫成「最後一下光後 0.5 s 給氣味」，換算第一下光在氣味前 2.0 s | 只有順向、逆向各一點 |
| Handler 2019 | 多巴胺神經元（DAN）開始 − 氣味／KC 開始，稱刺激間隔（inter-stimulus interval, ISI）；**只看起點，不計持續時間** | 行為 −6、−2、0、+1、+6 s；離體 −6、−1.2、−0.6、0、+0.5、+6 s；閉迴路 +9、−2 s |

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 比較 KC 內 cAMP 協同的時間窗與行為 trace 制約的時間窗 | 成像：+1、+15 s 有協同，+30 s 與多巴胺先到 15 s 沒有；行為：表現指數（學習分數，見 [[c-performance-index]]）隨 trace 間隔遞減，倒序幾乎學不到 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 測 MBON-γ1pedc 的突觸減弱是否依賴先後 | 順向：配對氣味的放電降約八成；逆向：無變化 |
| [[s-handler-2019-dopamine-receptor-timing]] | 同一套 ISI 並排量行為、γ4 突觸、cAMP 與內質網鈣 | 離體 −1.2 s 時 KC→MBON 突觸增強，0 與 +0.5 s 減弱，±6 s 幾乎不變；行為也隨順序在吸引與迴避之間翻轉 |

> 各點數值見 [[numbers]]。

## 引用時的陷阱

1. **起算點不同，數字不能跨篇或跨實驗直接比。** Tomchik 2009 說行為與成像的時間窗「相近」；但來源頁把兩者都改成從 CS 開始算之後，行為在 60–75 s（60 s 氣味＋trace 0 或 15 s）仍學得到，成像在 30 s 就沒有協同，差 2–3 倍（來源頁的計算）。Handler 2019 閉迴路順向是 +9 s 卻照樣有效，因為氣味持續 10 s，多巴胺到時氣味還在。
2. **Hige 2015 的「順向」含一半痕跡配對**：四下光在氣味開始後 0.2、0.7、1.2、1.7 s，氣味只有 1 s，所以後兩下落在氣味結束之後。
3. **「逆向」的結果三篇不同**：Tomchik 2009 沒有顯著協同（配對只比相加多約 0.8 個百分點，p＝0.14），Hige 2015 無效，Handler 2019 是突觸增強與價性反轉。三篇的逆向時間差也不同（約 −15 s、−2.0 s、−1.2 s）。不在本頁裁決，見 [[syn-contradictions]] 1.1。
4. **取樣稀疏**：Hige 2015 只有兩點；Handler 2019 行為的相鄰取樣點最近也差 1 s，Handler 2019 正文「只移動幾百毫秒就翻轉」的說法只有離體資料支持。

## 相關

- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]
- 概念：[[c-coincidence-detection]]、[[c-us-substitution]]、[[c-performance-index]]、[[c-kc-mbon-plasticity]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]
