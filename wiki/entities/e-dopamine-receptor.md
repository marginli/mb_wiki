---
title: KC 上的多巴胺受體（dopamine receptors DopR1／DopR2）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# KC 上的多巴胺受體（dopamine receptors DopR1／DopR2）


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

多巴胺神經元（[[e-dopaminergic-neuron]]，DAN）放出的多巴胺，要被細胞表面的「受體」接住，才會在細胞裡引起變化。本庫談的是 [[e-kenyon-cell]]（KC，蘑菇體裡代表氣味的神經元）上的兩種受體：**DopR1** 與 **DopR2**。依 Handler 2019，DopR1 偏好接上刺激 cAMP 生成的路徑（Gαs），DopR2 偏好接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑（Gαq）；該篇引用的文獻與所用抗體把 DopR2 稱為 DAMB，DopR1 的基因名寫作 Dop1R。Ichinose 2015 稱 DopR1 為「D1 類」受體。研究者用兩種方法拿掉受體：**突變**（整隻果蠅的該基因失效，例如 DopR1−/−、*dumb²*）與 **RNAi**（只在選定的細胞裡降低該基因的表現，通常降不到零）。

## 版本與規模（本庫用到的操作）

| 來源 | 操作 | 範圍 |
|---|---|---|
| Cohn 2015 | DopR1、DopR2 突變；DopR1/DopR2 雙突變；另有多巴胺回收轉運子 DAT 突變；只在 γ KC 以 RNAi 降低 DopR2 | 突變為全身；RNAi 限 γ KC |
| Handler 2019 | DopR1−/−、DopR2−/−（基因型表寫 DopR1null、DopR2attP） | 全身 |
| Ichinose 2015 | 以 c739、MB008B 在 α/β KC，或以 MB310C、MB323B 在 MBON-α1 用 RNAi 降低 DopR1；在 *dumb²*（DopR1 失效的突變）背景下以 MB247 在 KC 補回 DopR1（救援） | RNAi 限選定細胞；降低程度未驗證 |

另：Aso 2016 討論中引 Crocker et al. 2016 說 KC 表現四種多巴胺受體，可能在各區室用法不同；本篇沒有操作受體，只是提到。

## 庫內誰用了它

| 來源 | 量什麼 | 得到什麼 |
|---|---|---|
| [[s-cohn-2015-coordinated-neuromodulation]] | γ KC 突觸前末梢的鈣沿 γ 葉的分布（見 [[c-presynaptic-calcium]]） | DopR2 突變讓「γ2/γ3 強、γ4/γ5 弱」的樣式**倒過來**；γ KC 的 DopR2 RNAi 讓它**變平**（正文寫「similarly altered」）；DopR1 突變表型「較細微」、雙突變仍不對稱（補充圖，？待查） |
| [[s-handler-2019-dopamine-receptor-timing]] | 離體 γ4/γ5 的 KC 軸突 cAMP、內質網鈣；γ4 MBON 的突觸變化；行為 | DopR1−/− 的 cAMP 降到野生型約 27%；DopR1−/−（兩份 DopR1 基因都剔除）不再出現順向配對（KC 先、多巴胺後）的減弱，DopR2−/− 不再出現逆向配對（多巴胺先、KC 後）的增強；兩種突變的行為彈性都受損 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 24 小時糖獎賞記憶（LTM，見 [[c-memory-consolidation]]） | 在 α/β KC 降低 DopR1，LTM 約 0.13（c739）與約 0（MB008B），對照約 0.43–0.53；在 MBON-α1 降低則 n.s.；*dumb²* 救援組約 0.40、野生型約 0.57（圖判讀） |

數值見 [[numbers]]。

## 已知的問題

- **「救回」與「回到原水準」不同。** Ichinose 2015 的救援組與野生型「無顯著差異」，但柱高約為野生型七成，且 n＝7、缺「同型合子只帶 MB247」的對照。
- **突變與 RNAi 結果不一定一致。** Cohn 2015 的 DopR2 突變是「倒轉」，RNAi 是「變平」；可能是減量不完全，也可能有 KC 以外的 DopR2 參與（該來源頁的推論，論文未討論）。突變為全身性，不能單獨定位到 KC。
- **量的東西不同，方向不能直接拼。** Cohn 量末梢鈣分布（不是突觸強弱，也不是配對後）；Handler 量配對後的 KC→MBON 突觸；Ichinose 量行為。「DopR2 與變強有關」在 Cohn 是推論（見該來源頁第六節）。
- **Handler 的 DopR1−/− 在順向配對後反成弱增強**，它的模型解釋不了（見該來源頁 3.6）。
- RNAi 是持續性的，Ichinose 2015 無法區分 DopR1 在獲得、鞏固或提取哪一段被需要。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]
- 概念：[[c-camp-signaling]]、[[c-kc-mbon-plasticity]]、[[c-coincidence-detection]]、[[c-presynaptic-calcium]]、[[c-memory-consolidation]]
- 品系：[[e-c739-gal4]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]
- 來源：[[s-cohn-2015-coordinated-neuromodulation]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]
