---
title: MBON-α3（α3 輸出神經元）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-α3（α3 輸出神經元）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」；α3 在 α 葉的尖端。細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **α3 與 α′3 不同。** α 與 α′ 是兩條不同的葉；α′3 是 α′ 葉尖端的一格，那裡的輸出神經元是 MBON-α′3ap、MBON-α′3m（Pribbenow 2022 稱「α′3 MBON」），都不是本頁的細胞。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、把結果送出蕈狀體；學習改變的是 KC→MBON 突觸的強弱（見 [[e-mbon]]）。
- **DAN、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PPL1 群多傳遞懲罰。PPL1-α3 是送多巴胺進 α3 的那一型（[[e-ppl1-alpha3]]）。
- **CS+／CS−、bias**：訓練時配了電擊的氣味（CS+）與沒配的對照氣味（CS−）。Huang 2024 的 bias＝（CS+ 引起的放電改變 − CS− 引起的放電改變）減去訓練前的同一值，單位每秒放電次數。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。「弱標」＝也標到另一型，但表現量低。
- **工具**：CsChrimson／Chrimson88 照紅光讓神經元放電（[[e-cschrimson]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]）；TnT（破傷風毒素輕鏈）讓神經元從發育期起就無法釋放傳遞物質（`e-tnt`）；電壓成像＝用會隨膜電壓變亮變暗的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看每一次放電。
- **連結體、hemibrain**：用電子顯微鏡重建的全腦接線圖；hemibrain 是其中一份（[[e-hemibrain]]）。
- **UpWiN**：Aso 2023 命名的一群「迎風神經元」，活化時果蠅轉向上風。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「該頁」指表格同一列的來源頁。

## 是什麼

**MBON-α3 是樹突在蕈狀體 α3 區室的輸出神經元，用乙醯膽鹼（acetylcholine）傳訊，每側腦 2 顆。** 短名 MBON-14（Aso 2014b 表 1；Aso 2023 寫 MBON14），屬於 V3/V4 群（乙醯膽鹼；與 MBON-γ2α′1、MBON-α′2 同群，Aso 2014b）。同一格的 DAN 是 [[e-ppl1-alpha3]]。在本庫它是「懲罰的長期記憶在哪裡讀出」的主角：Huang 2024 量到電擊訓練讓它對 CS+ 的放電下降並維持到 24 小時；Aso 2023 則發現它與 [[e-mbon-alpha1]] 的末梢匯聚在同一群迎風神經元上，一興奮、一抑制。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 說明 |
|---|---|---|
| MB082C（split-GAL4） | Aso 2014b 圖 2C、7、10、11；Aso 2023 圖 2A、4A | 標 MBON-α3，**也弱標 MBON-α′2**；Aso 2023 型別欄寫「MBON13, 14」 |
| MB093C（split-GAL4） | Aso 2014b；Huang 2024 延伸圖 7d–e | 同上，也弱標 MBON-α′2 |
| G0239-GAL4 | Aso 2014a 表 1、圖 20K（引 Chiang 2011）；Aso 2014b（Plaçais 2013 用過）；Aso 2023 圖 4C | 非 Janelia 品系 |

Huang 2024 電壓成像用哪一條品系標它，來源頁沒有逐型列出（？待查）。細胞數：Aso 2014b 表 1 為 2 顆；Aso 2023 在 hemibrain 右腦數到 2 顆。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 以 split-GAL4 與雙色標記做解剖分類（表 1、圖 17、20） | 歸為乙醯膽鹼性；末梢與麩胺酸性 MBON-α1 的末梢在次微米距離內重疊；MBON-β1>α 的軸突終止於 α1–α3；MBON-γ1pedc>α/β 在 α3 的末梢偏表層，正是它樹突所在處 |
| [[s-aso-2014-mbon-valence]] | MB082C、MB093C 驅動 CsChrimson 活化；驅動 shi 阻斷，量四種記憶 | 活化：兩條都不顯著。2 小時氣味—糖：兩條都受損，但單獨阻斷 MBON-α′2（MB018B）也顯著，無法排除效果來自 α′2。24 小時電擊長期記憶（只在測驗時阻斷）：MB082C 受損，MB093C 與 G0239 沒有，作者不把它歸給 MBON-α3。酒精記憶：兩條結果不一致 |
| [[s-huang-2024-dopamine-memory-dynamics]] | 頭固定、腳踩小球的活果蠅上以電壓成像量放電；MB093C 驅動 TnT 阻斷；模型中的 Mα3 | 自發約 16 次／s（※ 從圖判讀）。吸引氣味對訓練後，它對 CS+ 的下降持續超過 1 小時，24 小時 bias 仍為負但不顯著；嫌惡氣味對時 CS+、CS− 起初一起降，24 小時 CS− 回升約 +9、CS+ 約 −4，bias 才顯著（※ 從圖判讀）。訓練後自發放電上升。阻斷後 5 分鐘記憶正常、3 小時記憶消失（每組 10 隻）。模型中拿掉 MBON-γ1pedc>α/β 的回饋，3 小時的 α3 改變少 36–63%；它到 PPL1-α3 的興奮性連線擬合出來近乎 0 |
| [[s-aso-2023-upwind-neurons]] | hemibrain 連結數；MB082C 光活化、全細胞記錄 UpWiN；G0239 光活化、離體鈣成像；單獨活化看迎風 | 2 顆 → SMP354 共 319 個突觸、→ SMP353 共 9 個；活化它讓 11 顆 UpWiN 中 3 顆（7 隻）被興奮，有的強到放電；鈣成像峰值約 0.43（n＝5），與 MBON-α1 同時活化時約 0.04（n＝7），沒有統計檢定（※ 從圖判讀）；MB082C 引發迎風只有未經多重比較校正的星號 |

數值見各來源頁與 [[numbers]]。Ichinose 2015（引 Plaçais 2013：它參與獎賞長期記憶的提取）與 Aso 2019（引 Pai 2013、Wu 2017：訓練後 3 小時它需要蛋白質合成）只轉述前人結果，不列入表。[[s-pribbenow-2022-postsynaptic-plasticity]] 研究的是 α′3 的 MBON（MB027B），不是本頁的細胞；它的 α3 指的是受體次單元 nAChR α3，也與本頁無關。

## 已知的問題

- **常用的兩條品系都漏到 MBON-α′2。** Aso 2014b 因此不把 2 小時獎賞記憶與 24 小時電擊記憶的效果歸給它。Huang 2024 用的 MB093C 正是 Aso 2014b 在長期記憶中陰性的那一條；兩篇的條件也不同（Huang 用 TnT 從發育期起阻斷、測 3 小時、電擊 20 V；Aso 2014b 只在測驗時以 shi 阻斷、測 24 小時、60 V），所以兩個結果不能直接並排（※ 推論）。
- **「長期改變」裡混有非聯結的成分。** Huang 2024 用嫌惡氣味對訓練時，沒配電擊的 CS− 也一起大幅下降，bias 會低估 CS+ 本身的改變；吸引氣味對在 24 小時已不顯著；48 小時只量了 2 隻。
- **Huang 2024 的「長期」只到 24 小時、行為只測到 3 小時**，不是蛋白質合成依賴的長期記憶的直接證據。
- **它與 MBON-α1 在 UpWiN 上「相抵」的證據較弱。** 離體、三組不同基因型的果蠅、無統計；Aso 2023 圖 4A（MB082C）與 4C（G0239）用不同品系活化它。
- **α3 與 α′3 容易混。** Huang 2024 也量了 MBON-α′3m，且該篇正文與圖對 α′3、α′3m 的寫法不一致（⚠️ 單篇自身不一致）；Aso 2014a 圖 16D 曾把「MBON-α′3ap」誤植為「MBON-α3′ap」。引用前先確認是哪一條葉。

## 相關

- 同格 DAN：[[e-ppl1-alpha3]]；末梢交會的另一型：[[e-mbon-alpha1]]；上游回饋：[[e-mbon-gamma1pedc]]；同模型：[[e-mbon-alpha2sc]]
- 細胞：[[e-mbon]]、[[e-dopaminergic-neuron]]
- 品系與工具：[[e-split-gal4]]、`e-tnt`、[[e-shibire-ts]]、[[e-cschrimson]]、[[e-hemibrain]]
- 概念：[[c-memory-consolidation]]、[[c-kc-mbon-plasticity]]、[[c-odor-generalization]]、[[c-valence-coding]]、[[c-memory-extinction]]
- 主題：[[t-mbon-to-action]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]、[[t-innate-learned-integration]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-aso-2023-upwind-neurons]]
- 待開頁面：`e-mb082c`、`e-mb093c`、`e-upwin`
