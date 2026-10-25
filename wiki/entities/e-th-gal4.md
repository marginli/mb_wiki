---
title: TH-GAL4 與 TH＋DDC 驅動（TH-GAL4 and TH/DDC drivers）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# TH-GAL4 與 TH＋DDC 驅動（TH-GAL4 and TH/DDC drivers）


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

**TH-GAL4** 是一個「廣泛」的驅動品系（驅動品系的原理見 [[e-split-gal4]]）：它借用 TH 基因的調控序列決定在哪些細胞表現。TH 指酪胺酸羥化酶，合成多巴胺所需的酵素，所以 TH-GAL4 大致標到會製造多巴胺的神經元（[[e-dopaminergic-neuron]]，DAN）。DDC（多巴脫羧酶）是合成多巴胺的另一個酵素，DDC 的調控序列與 TH 合用，可以補上 TH 漏掉的 DAN（Cohn 2015 用兩者讓 γ 葉每一格的 DAN 都帶上感測器）。它們的特點是**範圍大、不專一**：一次標到很多型 DAN，也標到蘑菇體以外的 DAN。本庫的 split-GAL4 品系也常把 TH 序列當作其中一半（例：MB320C、MB099C 的一半是 TH；MB504B 的 DBD 是 TH-Gal4.DBD），見 [[e-split-gal4]]。

## 版本與規模（各篇怎麼描述它標到誰）

| 來源 | 寫法 | 標到誰（依該篇） |
|---|---|---|
| Hige 2015 | TH-GAL4 | 多數 PPL1（含 PPL1-γ1pedc）、少數 PAM，以及蘑菇體以外的許多 DAN |
| Felsenberg 2017 | TH-GAL4 | 全腦大範圍的 DAN，含全部六型支配蘑菇體的 PPL1（γ1pedc、γ1、γ2α′1、α′2α2、α3、α′3；延伸圖 6b） |
| Handler 2019 | TH-Gal4（基因型表標「DAN subset」）＋ DDC-Gal4 | 用來在 DAN 表現多巴胺釋放感測器 VMAT-pHluorin |
| Cohn 2015 | 「TH 與 DDC 啟動子」 | γ 葉各區室的 DAN；**主文沒寫品系名**（全文搜 Gal4 只找到 58E02-LexA），是不是 TH-GAL4 與 DDC-GAL4 兩個品系：？待查（補充資料未取得） |

## 庫內誰用了它

| 來源 | 讓 DAN 帶上什麼 | 用來做什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | CsChrimson（[[e-cschrimson]]） | 正對照（已知應該有效、用來確認方法可行的組）：氣味配光後 MBON-γ1pedc 對配對氣味的放電約 98 → 14（n＝5，圖判讀） |
| [[s-felsenberg-2017-re-evaluation]] | shibire<sup>ts1</sup>（[[e-shibire-ts]]） | 再聞 CS+ 時關掉 → 消退只部分發生（PI 0.17，與 MB504B 的 0.13 並列，以「沒有消退」的偏好為 100%，阻斷後約保住 45–57%，本庫以柱高推算）；再聞 CS− 時關掉 → 記憶消失（見 [[c-memory-extinction]]） |
| [[s-handler-2019-dopamine-receptor-timing]] | VMAT-pHluorin（與 DDC-Gal4 合用） | 確認順向與逆向配對時 DAN 放出的多巴胺一樣多 |
| [[s-cohn-2015-coordinated-neuromodulation]] | sytGCaMP（只在突觸前末梢發光的鈣感測器）、PA-GFP | 看吃糖、電擊、掙扎時各格 DAN 的活動；看活化單一 MBON 時各格 DAN 怎麼變（見 [[t-mbon-dan-feedback]]） |

數值見 [[numbers]]。

## 已知的問題

- **一次動很多型。** 「活化或阻斷 TH-GAL4 有效」只說明「這一大群裡有某些是必要或足夠的」，不能定位到哪一型。Felsenberg 2017 正是如此：TH-GAL4 與 MB504B 的阻斷有效，逐一阻斷單一型 PPL1 都無效。
- **含蘑菇體以外的 DAN。** 行為或生理的效果可能來自蘑菇體以外（Hige 2015 的描述）。
- **同一品系、不同讀數，結論可以相反。** Hige 2015 討論指出：Boto et al. 2014 用同一個 TH-GAL4 活化 DAN，量的是 KC 軸突末梢的鈣，看不到變化；Hige 改量 MBON 收到的突觸電流，看到強烈減弱（見 [[e-kenyon-cell]]）。所以「用 TH-GAL4 沒看到效果」可能只是量錯了位置。
- **各篇描述的涵蓋範圍措辭不同**（「多數 PPL1」vs「全部六型 PPL1」），可能只是詳略不同；兩者是否同一個 TH-GAL4 插入品系，本庫沒有比對：？待查。

## 相關

- 品系：[[e-split-gal4]]、[[e-mb504b]]、[[e-r58e02]]
- 細胞：[[e-dopaminergic-neuron]]
- 工具：[[e-cschrimson]]、[[e-shibire-ts]]、[[e-gcamp]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-felsenberg-2017-re-evaluation]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]
