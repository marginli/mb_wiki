---
title: 離體全腦製備（ex vivo brain explant）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, cross-domain]
confidence: high
---

# 離體全腦製備（ex vivo brain explant）

**把果蠅的整顆腦取出，泡在持續供氧或灌流的養液裡，在顯微鏡下一邊刺激、一邊記錄神經元。** 好處是能用藥物或外加通道精準控制「氣味訊號」與「多巴胺」各在何時出現；代價是沒有真實的氣味與行為，腦的自發活動也和活果蠅不同。相對的做法是在體（in vivo）：活果蠅頭部固定、打開腦殼記錄。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體、KC、葉、區室**：蘑菇體（mushroom body）是果蠅腦中把氣味和好壞經驗連起來的構造；代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」，每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ4、α1），細胞以所在區室命名（見 [[e-mushroom-body]]、[[c-mb-compartment]]）。
- **常見詞**：PAM／PPL1＝兩群多巴胺神經元（DAN），分別多傳遞獎賞／懲罰；光遺傳＝讓神經元帶上照光就放電的蛋白（[[e-cschrimson]]）；離體＝把腦取出泡在養液裡，活體＝活果蠅固定後看腦；順向配對＝氣味先、多巴胺後，逆向＝多巴胺先；「未配對」＝兩種刺激錯開、不同時出現；cAMP＝多巴胺受體被活化後在細胞內產生的訊號小分子；※ 推論＝本庫推得、原文沒明說，？待查＝要靠其他資料確認。
- **KC、DAN、MBON**：Kenyon 細胞（代表氣味）、多巴胺神經元、蘑菇體輸出神經元（見 [[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]）。
- **乙醯膽鹼**：嗅覺訊號傳給 KC 時用的化學物質；在取出的腦上滴它，等於「假裝聞到氣味」。
- **離子導入**：用電流把藥從玻璃細針推出。
- **P2X2＋ATP、CsChrimson**：讓選定神經元遇 ATP 或紅光就放電的兩種外加通道（見 [[e-p2x2]]、[[e-cschrimson]]）。
- **ΔF/F0、ΔR/R0**：螢光（或兩色比值）相對刺激前的變化比例。

## 怎麼算 / 怎麼判定

不是一個量，而是一種製備；判定一篇是否「用」它，看它的結論是否在取出的腦上量得。本庫有三類用途：(1) 以乙醯膽鹼模擬氣味、以藥物或 P2X2 模擬多巴胺，量 KC 內訊號或 KC→MBON 突觸；(2) 以光或 ATP 活化一群細胞、看另一群有沒有反應，測功能連結；(3) 當對照，看活體中的某個樣式在離體時是否消失。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 整顆腦灌流（1 ml/min），解剖後 1.5 h 內記錄；30 mM 乙醯膽鹼噴萼部、1 mM 多巴胺噴葉部 | KC 軸突 cAMP 的配對協同與時間窗（見 [[c-coincidence-detection]]） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 乙醯膽鹼離子導入萼部；P2X2＋2 mM ATP 活化 58E02 DAN 或單一 MBON；γ4 MBON 膜片鉗 | 離體時各區室 KC 末梢鈣大致均勻（n＝6），作者以此對照活體的分區樣式；離體 DAN 自發活動大幅減少（資料未示）；單獨活化 DAN 使 γ4 突觸增強 |
| [[s-handler-2019-dopamine-receptor-timing]] | 1–4 日齡腦；10 mM 乙醯膽鹼離子導入 500 ms；P2X2＋2 mM ATP，5 × 100 ms | γ4 突觸的時間差曲線（時間差＝DAN 活化開始減 KC 刺激開始，負值＝多巴胺先到：−1.2 s 增強、0 與 +0.5 s 減弱、±6 s 幾乎不變）；cAMP 與內質網鈣 |
| [[s-felsenberg-2017-re-evaluation]] | 腦泡充氧緩衝液；CsChrimson 活化 MBON（630 nm，40 Hz × 10 ms），GCaMP 看 DAN | 活化 γ2α′1 MBON 使 MB-MV1 與 γ5 的 PAM 鈣上升（約 0.03 → 0.72，4 筆；約 0.01 → 0.53，5 筆，從圖判讀）；活化 V2 MBON 使 PPL1 細胞體一升一降一不顯著 |
| [[s-felsenberg-2018-memory-extinction]] | 同上協定；VT1211-LexA 活化 M4β′／M6，R48B04 看 PAM 末梢 | γ5 PAM ΔF/F0 約 +1.75（5 腦，從圖判讀），γ4 無反應，β′2p／β′2m 輕微抑制 |

> 參數見 [[numbers]]。

## 引用時的陷阱

1. **離體腦的狀態與活體不同。** Cohn 2015 指出離體時 DAN 的自發活動大幅減少，正是它用來解釋「分區樣式消失」的理由；所以在離體量到的突觸規則，起點狀態可能與活果蠅不同。
2. **刺激是人工的。** 乙醯膽鹼的劑量與時長不等於真實氣味；Tomchik 2009 依反應調整噴射壓力與位置，各腦劑量不可比。Cohn 2015 主文沒寫 ATP 噴注的時長與壓力（？待查），與 Handler 2019 的 DAN 刺激強度無法比較，見 [[syn-contradictions]] 1.3。
3. **「活化 A，B 有反應」不等於直接相連。** Felsenberg 2017、2018 與 Cohn 2015 的連結實驗都沒有區分單突觸與多突觸，也沒有氣味。
4. **離體 n 常很小**（Felsenberg 2017 為 4、5 筆；Felsenberg 2018 為 5 腦）。
5. **同類製備、不同結果要先比參數。** Cohn 2015 與 Handler 2019 同實驗室、同 γ4 MBON、同 P2X2 製備，對「未配對的多巴胺」得到不同結果：Cohn 2015 相隔 ＞ 45 s 突觸變強，Handler 2019 相隔 6 s 幾乎不變（見 [[syn-contradictions]] 1.3），不在本頁裁決。

## 相關

- 概念：[[c-whole-cell-patch-clamp]]、[[c-presynaptic-calcium]]、[[c-us-substitution]]、[[c-kc-mbon-plasticity]]
- 實體：[[e-p2x2]]、[[e-cschrimson]]、[[e-gcamp]]、[[e-epac-camp-sensor]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-mbon-dan-feedback]]；矛盾：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
