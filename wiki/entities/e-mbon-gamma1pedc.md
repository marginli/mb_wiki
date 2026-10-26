---
title: MBON-γ1pedc（MVP2）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-γ1pedc（MVP2）


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

蘑菇體輸出神經元（[[e-mbon]]）的一型，樹突（收訊號的分枝）在 γ1pedc 區室，也就是 γ 葉最靠近根部的那一格（區室見 [[c-mb-compartment]]；字尾 pedc 的意思，庫內來源都沒有解釋：？待查）。舊名 MB-MVP2（Hige 2015 的寫法）或 MVP2；Felsenberg 2017 寫成 MBON-γ1pedc>α/β，「>α/β」表示它的軸突再伸到 α/β 葉。依 Felsenberg 2017／2018，它放出 GABA（一種抑制性傳遞物質），活化時讓果蠅偏向「靠近」；它的軸突接到其他 MBON（M4β′、M6，見 [[e-mbon-gamma5beta2a]]）身上抑制它們，這叫前饋抑制（feedforward inhibition）。同一格的多巴胺神經元是傳遞懲罰的 [[e-ppl1-gamma1pedc]]。

## 版本與規模（標記它的品系）

| 來源 | 品系 | 用途 |
|---|---|---|
| Hige 2015 | R12G04-LexA（讓它帶 GFP，方便電極對準） | 活體全細胞記錄 |
| Felsenberg 2017 | MB112C（Methods、延伸圖 4a）；延伸圖 6i 寫 MB122C | 行為阻斷 |
| Felsenberg 2018 | MB112C-GAL4 | 活體鈣成像、解剖 |

⚠️ Felsenberg 2017 的品系名前後不一（MB112C vs MB122C，單篇自身不一致）。細胞數：Felsenberg 2018 的電顯追蹤分出左右腦各一顆（MVP2(L)、MVP2(R)）。

## 庫內誰用了它

| 來源 | 怎麼用 | 看到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 全細胞膜片鉗（[[c-whole-cell-patch-clamp]]），氣味配一顆 PPL1-γ1pedc 的光活化 | 配對氣味的放電降 80% ± 5.7%、突觸電荷降 90% ± 3.7%，至少 40 分鐘；逆向配對無效；MBON 不放電也會發生（見 [[c-kc-mbon-plasticity]]） |
| [[s-felsenberg-2017-re-evaluation]] | 在糖記憶再活化期間以 [[e-shibire-ts]] 阻斷 | 不影響消退與再鞏固；作者用它確認消退需要的是 V2 群 MBON（α、α′ 葉上的一群 MBON），不是與它相鄰的 MVP2 |
| [[s-felsenberg-2018-memory-extinction]] | 電擊訓練後活體雙光子鈣成像樹突；FAFB 電顯追蹤 | 訓練後對 CS+ 的反應比 CS− 小，消退後**仍然**比較小（中位數約 0.2 vs 0.4，從圖判讀）；接到 M6R 17 個、M6L 16 個、M4β′ 47 個突觸，接 M6 的點靠近樹突根部 |

> [[s-aso-2016-dan-cell-type-rules]] 只在圖 5B 示意圖畫出它的 GABA 前饋連結，用來解釋同時活化兩型 DAN 時的結果，沒有操作或量它，所以不列入表。

## 已知的問題

- **兩種讀法不能直接並列。** Hige 用電極量放電與電荷，誘發學習的是光活化單一顆 DAN；Felsenberg 2018 用鈣成像、真電擊、訓練後 60 分鐘量。兩者方向一致（配對氣味的反應變小），幅度不能比。
- **「推動靠近」是引用，不是本庫來源自己測的。** Hige 引 Aso 2014b；Felsenberg 2018 引 Perisse 2016 說明它抑制 M4β′／M6。
- **它的痕跡沒消，不等於下游沒變。** Felsenberg 2018 顯示，訓練留下的痕跡（MVP2 對 CS+ 的反應比 CS− 小）在消退後仍在，但下游 M6 的軸突反應被消退抵銷；只看這顆 MBON 會以為消退沒發生。
- ⚠️ Felsenberg 2018 的方法表寫 MVP2→M6L 16 個突觸，圖 S4B 只畫 15 個（單篇自身不一致）。

## 相關

- 細胞：[[e-mbon]]、[[e-ppl1-gamma1pedc]]、[[e-mbon-gamma5beta2a]]、[[e-mbon-gamma2alpha1]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-memory-extinction]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-memory-updating]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
