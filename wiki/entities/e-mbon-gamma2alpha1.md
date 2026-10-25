---
title: MBON-γ2α′1（γ2α′1 輸出神經元）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-γ2α′1（γ2α′1 輸出神經元）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蘑菇體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

蘑菇體輸出神經元（[[e-mbon]]）的一型，名字串了兩個區室：γ2（γ 葉第 2 格）與 α′1（α′ 葉第 1 格）。※ 推論：表示它的樹突同時伸進這兩格（依命名方式；庫內來源沒有說明命名規則）。同一格的多巴胺神經元是 [[e-ppl1-gamma2alpha1]]（舊名 MB-MV1）。它在本庫兩條研究線上都出現：Hige 2015 拿它當「鄰格」，檢查 γ1pedc 的學習會不會越界；Felsenberg 2017 發現它是糖記憶「再鞏固」（被叫出來的記憶重新存好，見 [[c-memory-consolidation]]）所需的 MBON。

## 版本與規模（標記它的品系）

| 來源 | 品系 | 來源怎麼稱呼 |
|---|---|---|
| Hige 2015 | R25D01-LexA | MBON-γ2α′1 |
| Felsenberg 2017 | MB077C-GAL4（阻斷、光活化）、R25D01-LexA（光活化）；延伸圖 6k、6p 說兩者都標 MBON-γ2α′1 | γ2α′1 MBON |
| Handler 2019 | 25D01-Gal4、25D01-LexA | 「γ2 MBON」 |
| Cohn 2015 | 主文沒寫品系名（？待查） | 「γ2 MBON」 |

※ 推論：Handler 2019 的「γ2 MBON」就是 MBON-γ2α′1。依據：三篇都用 25D01 這段調控序列，而 Felsenberg 2017 明說 R25D01-LexA 標 MBON-γ2α′1；不確定之處：GAL4 與 LexA 版本的表現範圍不一定相同，Handler 沒有比對。Cohn 2015 的「γ2 MBON」只以區室命名、品系未知，是否同一型更不確定（？待查）。

## 庫內誰用了它

| 來源 | 怎麼用 | 看到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 在 γ1 區誘發突觸變弱後，用電極記錄鄰格的它 | 放電約 105 → 91（從圖判讀，n＝6），無效果 → 多巴胺作用沒越界（陰性結果的替代解釋見 [[c-mb-compartment]]） |
| [[s-felsenberg-2017-re-evaluation]] | 糖訓練後再聞 CS−（沒配糖的氣味）時以 [[e-shibire-ts]] 阻斷；離體光活化；活體鈣成像 | 阻斷後再鞏固受損（PI 約 0.12，對照約 0.25／0.265）；3 小時測驗時阻斷它，果蠅也表現不出記憶（PI 約 0.045）；離體光活化它，MB-MV1（PPL1-γ2α′1）的 ΔF/F0 由約 0.03 升到約 0.72、γ5 的 PAM 由約 0.01 升到約 0.53；訓練後對 **CS−** 的反應變大（兩種氣味分派方式分別約 +14% 與 +24%，相對假訓練組），CS+ 不變 |
| [[s-handler-2019-dopamine-receptor-timing]] | 離體配對（73F07-LexA 的 γ2 DAN ＋ P2X2）與真電擊實驗 | 論文說 γ2 也有類似 γ4 的雙向改變；資料在補充圖 S3（？待查，補充資料未取得） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 「γ2 MBON」：離體活化 γ2 DAN、活化 58E02 DAN；活體氣味成像；P2X2 活化它本身 | 活化 γ2 DAN 時 ΔF/F0 約 0.5 → 4.8；活化 58E02 DAN 時約 0.8 → 0.6（不顯著）；活體對氣味的反應約 0.9，遠大於 γ4 的約 0.2；活化它會改變各格 DAN（見 [[t-mbon-dan-feedback]]） |

## 已知的問題

- **CS− 反應變大，現有規則沒有涵蓋。** 庫內的突觸規則都只處理「與多巴胺配對的氣味」；Felsenberg 2017 的變大發生在沒配糖的氣味上，來源沒有解釋（見 [[syn-contradictions]] 3.7）。
- **再鞏固與記憶表現分不開。** 它同時是表現記憶所必需，阻斷時果蠅可能根本叫不出記憶（Felsenberg 2017 圖 4b）。
- **光活化在取出的腦裡、沒有氣味時做，n 小**（4、5 筆），只說明「活化它會讓 DAN 鈣上升」，不區分直接或間接連結。
- **「推動靠近」是引用。** Handler 2019 引 Aso 2014b 說 γ2 MBON 推動靠近；庫內沒有來源自己檢驗。
- 跨篇是否同一型細胞，見「版本與規模」的 ※ 推論。

## 相關

- 細胞：[[e-mbon]]、[[e-ppl1-gamma2alpha1]]、[[e-mbon-gamma1pedc]]、[[e-dopaminergic-neuron]]
- 概念：[[c-mb-compartment]]、[[c-memory-consolidation]]、[[c-kc-mbon-plasticity]]
- 主題：[[t-mbon-dan-feedback]]、[[t-memory-updating]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-felsenberg-2017-re-evaluation]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]
