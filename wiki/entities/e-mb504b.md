---
title: MB504B 驅動品系（MB504B split-GAL4）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# MB504B 驅動品系（MB504B split-GAL4）


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

**MB504B 是一個 split-GAL4 驅動品系，讓外加基因只在 PPL1 群（傳遞懲罰的那群多巴胺神經元，DAN）中的幾型表現。** split-GAL4 把開啟基因的 GAL4 拆成兩半，各由一段調控序列控制，兩半都在的細胞才有作用（見 [[e-split-gal4]]）。依 Handler 2019 的基因型表，MB504B 的兩半是 52H03-p65.AD 與 TH-Gal4.DBD（TH 是合成多巴胺所需酵素的調控序列）。本庫三篇用它：一篇用來活化 PPL1、兩篇用來阻斷。

## 版本與規模（它標到誰）

| 來源 | 怎麼描述 |
|---|---|
| Handler 2019 | 「支配蘑菇體六個區室的一部分 PPL 神經元」（text.txt 第 196–197 行）；沒列是哪六個 |
| Felsenberg 2017 | 延伸圖 6c：四型 PPL1——PPL1-γ1pedc（MB-MP1）、PPL1-γ2α′1（MB-MV1）、PPL1-α′2α2（MB-V1）、PPL1-α3 |
| Felsenberg 2018 | 「獲得嫌惡記憶所必需」的 PPL1 群；沒列型別 |

※ 推論：Felsenberg 2017 的四型，名稱裡的區室恰好是 γ1pedc、γ2、α′1、α′2、α2、α3 六個，可能就是 Handler 說的「六個區室」；但兩篇都沒有這樣對照，而且 γ1pedc 算一格還是兩格（γ1 與 pedc），來源之間也不一致（見 [[s-aso-2016-dan-cell-type-rules]] 對區室計數的討論）。

## 庫內誰用了它

| 來源 | 接上什麼 | 用來做什麼 |
|---|---|---|
| [[s-handler-2019-dopamine-receptor-timing]] | CsChrimson | 行為：以光活化 PPL，與氣味依不同時間差配對，量果蠅之後追氣味的變化 |
| [[s-felsenberg-2017-re-evaluation]] | shi^ts1 | 糖獎賞記憶再聞 CS+ 時阻斷：消退被部分擋住（PI 約 0.13，見該來源頁 3.1 節）；再聞 CS− 時阻斷：記憶喪失 |
| [[s-felsenberg-2018-memory-extinction]] | Shi^ts1 | 嫌惡記憶再暴露期間阻斷：消退照常（圖 1D） |

數值見各來源頁與 [[numbers]]。

## 已知的問題

- **一個品系＝四型 DAN 一起動。** 讀到「阻斷 MB504B」時要記得是四型 PPL1 同時被關；Felsenberg 2017 逐一阻斷單一型時，消退都不受影響。
- **PPL 與 PPL1 是不是同一群。** Handler 寫 PPL、Felsenberg 兩篇寫 PPL1，但三篇用的是同一個品系名，這讓「指同一群」的說法有了品系上的依據；見 [[syn-contradictions]] 4.4（部分解決）。Felsenberg 2017 延伸圖 6b 另列支配蘑菇體的 PPL1 共六型（多了 PPL1-γ1 與 PPL1-α′3），MB504B 沒標這兩型。
- **兩個記憶方向、兩種結果。** 同一個品系，阻斷時對獎賞記憶的消退有影響（Felsenberg 2017），對嫌惡記憶的消退沒有影響（Felsenberg 2018）。這是不同實驗的不同結論，不是矛盾；兩篇的記憶種類、訓練與時間點都不同。
- **Felsenberg 2018 的 PPL1 實驗缺允許溫度對照**（該來源頁 3.1 第 4 點）。

## 相關

- 品系：[[e-split-gal4]]、[[e-r58e02]]、[[e-mb099c]]
- 細胞：[[e-dopaminergic-neuron]]、[[e-ppl1-gamma1pedc]]、[[e-ppl1-gamma2alpha1]]
- 工具：[[e-shibire-ts]]、[[e-cschrimson]]
- 概念與主題：[[c-memory-extinction]]、[[t-memory-updating]]、[[t-timing-rules]]；矛盾：[[syn-contradictions]]
- 來源：[[s-handler-2019-dopamine-receptor-timing]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
