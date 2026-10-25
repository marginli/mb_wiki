---
title: PPL1-γ2α′1 多巴胺神經元（PPL1-γ2α′1, MB-MV1）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# PPL1-γ2α′1 多巴胺神經元（PPL1-γ2α′1, MB-MV1）


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

**PPL1-γ2α′1 是 PPL1 群（多傳遞懲罰）中的一型多巴胺神經元（DAN），軸突同時伸進蘑菇體的 γ2 與 α′1 兩個區室。** 名字裡串兩段區室名，就表示它跨這兩格；Hige 2015 的描述是「投射到相鄰的 γ2 區室（也投射到 α′1）」。舊名 MB-MV1（Felsenberg 2017）。同一格的輸出神經元是 [[e-mbon-gamma2alpha1]]。區室見 [[c-mb-compartment]]。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 標到什麼 |
|---|---|---|
| MB296B-GAL4、R73F07-GAL4 | Felsenberg 2017 延伸圖 6d–e | 只標 PPL1-γ2α′1 |
| 73F07-LexA | Handler 2019 | 基因型表標「γ2 DANs」 |
| MB099C（TH／73F07 兩半） | Hige 2015、Aso 2016 | 含它在內的兩型或四型 PPL1（見 [[e-mb099c]]） |
| MB504B | Felsenberg 2017 延伸圖 6c | 含它在內的四型 PPL1（見 [[e-mb504b]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-felsenberg-2017-re-evaluation]] | MB296B（另以 R73F07 重做）驅動 shi^ts1 阻斷；離體以光活化 γ2α′1 MBON，量它的鈣 | 再聞 CS− 時阻斷 → 6 h 獎賞記憶消失（再鞏固失敗）；聞完才阻斷、只在提取時阻斷都不顯著；γ2α′1 MBON 活化後 ΔF/F₀ 約 0.03 → 0.72（4 筆，※ 從圖判讀） |
| [[s-handler-2019-dopamine-receptor-timing]] | 73F07-LexA 驅動 P2X2，離體活化「γ2 DAN」並量 γ2 MBON | 補充圖 S3D：？待查（補充資料未取得） |
| [[s-hige-2015-heterosynaptic-plasticity]] | 經 MB099C 與其他型一起活化 | 氣味配光後，鄰格的 MBON-γ1pedc 不變（多巴胺不越界的證據之一） |
| [[s-aso-2016-dan-cell-type-rules]] | 經 MB099C 與 PPL1-α′2α2 一起活化 | 10 次間隔訓練後有 4 日記憶（圖 2C）；作者推測 PPL1-γ2α′1 可能經由促進學習後的睡眠而廣泛幫助記憶鞏固（text.txt 第 374–378 行，未檢驗） |

數值見各來源頁與 [[numbers]]。

## 已知的問題

- **Handler 的「γ2 DAN」是不是這一型。** ※ 推論：Felsenberg 2017 說 R73F07-GAL4 只標 PPL1-γ2α′1，Handler 用 73F07-LexA 標「γ2 DAN」，兩者可能是同一型；但 GAL4 與 LexA 版本標到的範圍不一定相同，兩篇沒有比對：？待查。Cohn 2015 也活化「γ2 DAN」（圖 6C、6E），品系名主文沒寫，是否同一型無從判斷。
- **只有 Felsenberg 2017 單獨操作它。** Hige 2015 與 Aso 2016 都經由 MB099C 和其他型一起活化，結果不能歸給這一型。
- **懲罰型 DAN 為何保住獎賞記憶，Felsenberg 2017 沒有解釋。** 離體連結實驗沒有氣味、n 小，不能說明是直接突觸。
- **MB099C 的組成兩篇不同**，見 [[syn-contradictions]] 1.4。

## 相關

- 同格輸出：[[e-mbon-gamma2alpha1]]；同群其他型：[[e-ppl1-gamma1pedc]]；細胞群：[[e-dopaminergic-neuron]]
- 品系：[[e-mb099c]]、[[e-mb504b]]、[[e-split-gal4]]；工具：[[e-shibire-ts]]、[[e-p2x2]]
- 概念：[[c-memory-consolidation]]、[[c-ex-vivo-explant]]
- 主題：[[t-memory-updating]]、[[t-mbon-dan-feedback]]；矛盾：[[syn-contradictions]]
- 來源：[[s-felsenberg-2017-re-evaluation]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-aso-2016-dan-cell-type-rules]]
