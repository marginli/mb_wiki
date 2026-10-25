---
title: MB099C 驅動品系（MB099C split-GAL4）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: low
---

# MB099C 驅動品系（MB099C split-GAL4）


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

**MB099C 是一個 split-GAL4 驅動品系，讓外加基因只在幾型 PPL1 多巴胺神經元（DAN，傳遞懲罰）裡表現，而且不標支配 γ1pedc 的那一型。** split-GAL4 的原理見 [[e-split-gal4]]。依 Hige 2015 方法，它的兩半是 TH-p65ADZp（插在 VK00027）與 73F07-ZpGAL4DBD（插在 attP2）；TH 是合成多巴胺所需酵素的調控序列，73F07 是另一段調控序列的編號。本庫兩篇用它接上紅光活化通道 [[e-cschrimson]]，但**兩篇對它標到幾型 DAN 說法不同**。

## 版本與規模（它標到誰）

| 來源 | 原文怎麼說 |
|---|---|
| Hige 2015 | 「MB099C labels four types of PPL1 DANs: PPL1-γ2α′1, α′2α2, α′3, and α3, but never labels PPL1-γ1pedc」（text.txt 第 292–293 行，影像在補充圖 S1B：？待查） |
| Aso 2016 | 「the combination of PPL1-γ2α′1 and PPL1-α′2α2 (MB099C)」（第 370 行）；並說 MB320C 與 MB099C 合計標「三型」DAN（第 353–355 行）；圖 2A 只畫這兩型 |

兩篇作者有重疊（Aso、Rubin），表現影像都放在補充資料或 Janelia 網站，本庫沒有取得。

## 庫內誰用了它

| 來源 | 用來做什麼 | 得到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 氣味配光活化 MB099C 的 DAN，記錄兩顆 MBON：鄰格的 MBON-γ1pedc（MB099C 不標 γ1pedc 的 DAN，所以這是在看多巴胺會不會影響到別格），以及 α2 格的 MBON-α2sc（看要多少次「氣味＋光」配對才會讓突觸變弱） | γ1pedc 不變（n＝8）；α2sc 用 1 s 協定不變，要 60 s 氣味配 120 下光才變弱 |
| [[s-aso-2016-dan-cell-type-rules]] | 以光代替電擊訓練，比較學習速率、保留時間、更新規則 | 即時記憶中等；10 次間隔訓練後有 1 日與 4 日記憶（圖 2C）；訓練後只讓果蠅聞兩種氣味、不給光，記憶減弱得比 MB320C 等組多（圖 3C） |

數值見 [[numbers]] 與兩個來源頁。

## 已知的問題

- **⚠️ 標記幾型，兩篇不同。** 四型（Hige 2015）還是兩型（Aso 2016），見 [[syn-contradictions]] 1.4，本頁不裁決。差的兩型裡有 PPL1-α3；Aso 2016 的 MB630B 只活化 PPL1-α3，就能在間隔訓練後形成 4 日記憶。※ 推論：若四型的說法對，Aso 2016 中 MB099C 的長期記憶可能部分來自 α3。
- **一個品系不等於一型細胞。** 不論兩型或四型，「活化 MB099C」都是好幾型 DAN 一起放電；Hige 2015 拿它與只標一顆 DAN 的 MB320C（見 [[e-ppl1-gamma1pedc]]）比較 α2 與 γ1 的門檻，活化強度不同是混淆因子。
- **放電證據不完整。** Aso 2016 引 Hige 2015 說這幾型對光的放電相近；Hige 來源頁只提到 PPL1-α′2α2 的放電在補充圖 S2：？待查。
- **73F07 也出現在別的品系。** Felsenberg 2017 的 R73F07-GAL4 只標 PPL1-γ2α′1；Handler 2019 的 73F07-LexA 標「γ2 DAN」（見 [[e-ppl1-gamma2alpha1]]）。同一段序列在不同版本中標到的範圍不一定相同。

## 相關

- 品系：[[e-split-gal4]]、[[e-mb504b]]；細胞：[[e-dopaminergic-neuron]]、[[e-ppl1-gamma2alpha1]]、[[e-ppl1-gamma1pedc]]
- 概念：[[c-mb-compartment]]、[[c-us-substitution]]、[[c-spaced-training]]
- 矛盾：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-aso-2016-dan-cell-type-rules]]
