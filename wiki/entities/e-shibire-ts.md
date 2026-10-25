---
title: 溫度敏感型阻斷工具（shibire^ts1）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-memory-dynamics]
confidence: high
---

# 溫度敏感型阻斷工具（shibire^ts1）


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

一個溫度敏感的突變基因，論文寫作 shibire<sup>ts1</sup>、Shi^ts1 或 shi。用驅動品系（見 [[e-split-gal4]]）讓它只在選定的神經元表現，把果蠅移到高溫，這些神經元就**送不出訊號**；降回低溫又恢復。依 Felsenberg 2017／2018 的說明，高於 29 °C 時它擋住細胞膜回收、因而擋住突觸小泡釋放，低於 25 °C 時恢復；Ichinose 2015 稱它為「溫度敏感的顯性負向 dynamin」（dynamin 是一種蛋白，本庫只用到它的效果）。好處是可以只在某一段時間（訓練、訓練後、再聞氣味、測驗）關掉某群神經元。它回答的是「這個過程少了這群神經元行不行」（必要性），和光遺傳活化（見 [[e-cschrimson]]）回答的「足不足以」相反。

## 版本與規模（溫度與時段）

| 來源 | 限制溫度（阻斷） | 允許溫度（正常） | 典型阻斷時段 |
|---|---|---|---|
| Ichinose 2015 | 32 °C | 24 °C | 只在訓練；訓練後立刻 1 h；訓練後 22 h 起 1 h；只在測驗 |
| Felsenberg 2017 | 正文與各圖 32 °C；Methods 寫 33 °C（⚠️ 單篇不一致） | 23 °C | 再聞氣味前 30 min 起至結束；或再聞後立即／90 min 才升溫 |
| Felsenberg 2018 | 30–33 °C | 23 °C | 再暴露期間（協定圖顯示約 40–45 min）；或只在測驗 |

## 庫內誰用了它

| 來源 | 關掉哪些神經元（品系） | 得到什麼 |
|---|---|---|
| [[s-ichinose-2015-reward-recurrent-circuit]] | PAM-α1（MB299B）、MBON-α1（MB310C、MB323B）、α/β KC（c739、MB008B） | 訓練時或訓練後 1 h 內關掉三者任一，24 小時記憶受損，22 h 後才關則不受損；提取需要 MBON-α1、不需要 PAM-α1（見 [[c-memory-consolidation]]） |
| [[s-felsenberg-2017-re-evaluation]] | PPL1（TH-GAL4、MB504B）、PAM（R58E02）、PPL1-γ2α′1（MB296B、R73F07）、V2 群 MBON（MB052B）、MBON-γ2α′1（MB077C）等 | 獎賞記憶的消退需要 PPL1 與 V2；再鞏固需要 MBON-γ2α′1、PPL1-γ2α′1，以及再聞之後的 PAM（見 [[c-memory-extinction]]） |
| [[s-felsenberg-2018-memory-extinction]] | PAM（R58E02）、PPL1（MB504B）、M4β′／M6（VT1211） | 嫌惡記憶的消退需要 PAM、不需要 PPL1；關掉 M4β′／M6 讓消退變弱 |

品系見 [[e-r58e02]]、[[e-mb504b]]、[[e-th-gal4]]、[[e-c739-gal4]]。

## 已知的問題

- **只證明「必要」。** 關掉就擋住，不表示這群神經元在正常果蠅身上真的做了作者說的事（Felsenberg 2017 來源頁的限制 1）。
- **時間解析度是數十分鐘。** 升溫要提前開始，所以「再聞氣味期間需要」其實涵蓋前後一段。Felsenberg 2018 正文說阻斷限於再暴露期間，協定圖與圖 S2B 顯示約 40–45 分鐘；PAM 那組沒有「升溫但不再暴露」的對照（見該來源頁 3.1 ⚠️）。
- **關掉的是全部輸出。** Ichinose 2015 的圖題寫「MBON-α1 的回饋」，但 shi 擋的是 MBON-α1 送往所有下游的訊號；「需要的是送回 PAM-α1 那一支」是推論。
- **阻斷可能有與研究問題無關的副作用。** Felsenberg 2018 關掉 M4β′／M6 時再聞 CS−，躲避完全消失（論文只說「unexpectedly」），使「消退變弱」的解讀打折（見該來源頁 3.2）。
- **對照的設計要看齊。** 每個實驗都要 GAL4/+、UAS-shi/+ 兩組對照，以及全程允許溫度的對照；Felsenberg 2018 的 PPL1 實驗找不到允許溫度對照（該來源頁 3.1 ⚠️）。
- 阻斷是否完全，三篇都沒有直接驗證：？待查。

## 相關

- 概念：[[c-memory-extinction]]、[[c-memory-consolidation]]
- 工具：[[e-split-gal4]]、[[e-cschrimson]]、[[e-t-maze]]
- 主題：[[t-memory-updating]]、[[t-mbon-dan-feedback]]
- 來源：[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
