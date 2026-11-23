---
title: 傳遞物質預測（neurotransmitter prediction）
created: 2026-11-21
updated: 2026-11-24
tags: [concept, active, cross-domain]
confidence: medium
---

# 傳遞物質預測（neurotransmitter prediction）

**用訓練好的神經網路，從單一突觸的電子顯微鏡影像判斷那個突觸用哪一種神經傳遞物質。它是預測，不是量測；庫內有五篇把它的輸出當成「這顆細胞是興奮性還是抑制性」來用。** 電顯影像本身只看得到形狀，看不到化學物質，所以連結體能給出「誰接到誰」卻給不出「這個連結是加還是減」——傳遞物質預測就是用來補這一格的。

## 怎麼算 / 怎麼判定

做法在庫內各篇是同一套，出自 Eckstein 等人：

1. 以突觸前位點為中心，從電顯體積裡切出一個 3D 小塊（[[s-yamada-2023-second-order-conditioning]] 用邊長 80 體素）。
2. 丟進一個 3D 卷積神經網路（VGG 架構）分類，輸出為**六種傳遞物質之一**：乙醯膽鹼、GABA、麩胺酸、多巴胺、血清素、章魚胺。
3. 一顆細胞有數千個突觸前位點，所以「這顆細胞用什麼」是逐突觸結果的多數決。[[s-yamada-2023-second-order-conditioning]] 的 SMP108 是 2,753 個位點中 2,416 個被判為乙醯膽鹼。

**準確率是逐突觸的，不是逐細胞的。** [[s-ganguly-2024-visual-inputs-to-kc]] 報告在 FAFB 體積上 88%、在 hemibrain 上 79%，並說預測為膽鹼性者的信心分數一般最高（> 0.8）。**由逐突觸準確率推到細胞層級的信心，庫內沒有任何一篇說明怎麼算**：？待查。

**從傳遞物質到正負號，是第二層推論。** 模型裡要的是「興奮」或「抑制」，而這一步各篇的約定不同：[[s-minnick-2026-untrained-connectome]] 把血清素、章魚胺、乙醯膽鹼、多巴胺、酪胺一律記為興奮（+1），GABA 與麩胺酸記為抑制（−1）。果蠅的麩胺酸常是抑制性的，與哺乳類相反。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-ganguly-2024-visual-inputs-to-kc]] | 直接採用 Codex 中已列出的 Eckstein 等人結果，把接到視覺 Kenyon 細胞的每一型上游分到六類（圖 3C） | 直接的視覺投射神經元**全部**被預測為膽鹼性；25 個局部視覺中間神經元（LVIN）中 19 個膽鹼性（76%）、2 個 GABA（8%）、3 個麩胺酸（12%）、1 個未知（4%），即 5 個被預測為抑制性。該頁把「這些是預測值」列為問題與限制第 3 條 |
| [[s-yamada-2023-second-order-conditioning]] | 把 Eckstein 的網路移用到 hemibrain（改成等向性），對 396 型中間神經元做預測，用來在 MBON-α1 到獎賞型 DAN 的兩跳路徑裡挑出「興奮性」的那一條 | 主路 MBON-α1 →（SMP353／SMP354）→ SMP108 → 多型獎賞 DAN，**兩層都被預測為乙醯膽鹼（興奮性）**。SMP108 另有乙醯膽鹼轉移酶染色驗證，**SMP353/354 只有預測**。注意該篇的「連結數最多」是**在膽鹼性細胞裡**的冠軍——圖上有幾型麩胺酸性神經元連得更多，該篇沒有探討 |
| [[s-aso-2023-upwind-neurons]] | 以預測值標示 MBON-α1 與 MBON-α3 下游中間神經元的傳遞物質（圖 3D） | MBON-α1 為麩胺酸、MBON-α3 為乙醯膽鹼，與該篇電生理量到的抑制／興奮符號相符。**這是庫內唯一一次預測值與同篇的生理量測對得上** |
| [[s-li-2020-mb-connectome]] | **預測不是在 hemibrain 上跑的。** 作法是先把每一型典型與非典型 MBON 在 **FAFB**（另一份成蟲全腦電顯體積）裡跨資料集認出對應的神經元，再依特徵性的 T-bar 形態取**至少 100 個**突觸位置，丟給 Eckstein et al. 2020 的模型。作者說明理由：抗體染色或 RNA profiling 需要的專一 GAL4 驅動品系還不存在 | 34 型 MBON 的傳遞物質標註，後續全部的「推拉」「興奮還是抑制」推論都建立在這上面。**14 型非典型 MBON 裡只有 MBON10 是實測（圖 8 的實線外框），其餘 13 型全是預測（虛線）。** 引用時另有兩點：Eckstein et al. 2020 在本篇引用時**還是 bioRxiv 預印本**；圖上的標法各圖不同（圖 7、8 用虛線／實線，圖 17、19、26 用底線或空心圓） |
| [[s-minnick-2026-untrained-connectome]] | 把連結體附帶的自動預測欄當成整個脈衝網路每顆神經元的正負號來源（全腦加腹神經索 172,433 顆） | 嗅葉局部神經元分成麩胺酸性 161、GABA 性 146、膽鹼性 105、血清素性 14、章魚胺性 3。**也製造了該篇最大的一個已知缺陷**：兩顆 [[e-apl-neuron]] 被預測成膽鹼性（興奮性），而真果蠅的 APL 是 GABA 性、正是壓低 Kenyon 細胞編碼密度的抑制回饋。同一份連結體的「已驗證」欄把 APL 列為 GABA，兩欄互相衝突，該篇所有主結果採用預測欄 |

數值見 [[numbers]]。

## 引用時的陷阱

1. **「預測」兩個字不能在引用時掉掉，而且掉掉的例子就在原文裡。** 五篇裡只有 [[s-aso-2023-upwind-neurons]] 有同篇的生理量測可以對照，[[s-yamada-2023-second-order-conditioning]] 只有一型（SMP108）有染色。其餘的「這條路是興奮性的」全部是分類器的輸出。**整條機制說法的正負號若來自預測，那條機制的強度就以預測的準確率為上限。**
   ⚠️ **[[s-li-2020-mb-connectome]] 圖 8 的圖說自己就把預測寫成了事實**：圖上 MBON20 的外框是虛線（predicted GABA），而圖說寫的是「The other two, **the GABAergic MBON10 and MBON20**, were described by Aso et al., 2014a」——只有 MBON10 是實線（實測）。這有實質後果：該篇圖 18A 把「非典型 GABA」單獨列成一欄，而那一欄有 37% 的輸出落在側副葉、是「非典型 MBON 直通運動系統」的核心數字；**若 MBON20 的 GABA 身分是預測的，那一欄就不是「兩型實測 GABA」的統計**，而論文沒有討論這個敏感度。本庫的判讀依據是圖 8 右下角的色鍵與各格外框的實虛線，以 300 dpi 整頁渲染確認。
2. **「這篇用哪一份影像做預測」要查清楚。** 同樣是 Eckstein 的模型，[[s-yamada-2023-second-order-conditioning]] 跑在 hemibrain 上（把網路改成等向性），[[s-li-2020-mb-connectome]] 跑在 **FAFB** 上、再把結果對應回 hemibrain 的細胞型。**寫「Li 2020 用 hemibrain 影像預測傳遞物質」是錯的。** 跨資料集這一步本身也會引進誤差：要先在另一份腦裡認出同一型細胞，而那一步靠的是形態比對。
3. **同一份連結體裡可能有兩個互相衝突的欄位，而選哪一欄是作者的決定。** APL 的例子（自動預測欄寫膽鹼性、註記欄寫「已驗證 GABA」）顯示這不是理論上的風險：[[s-minnick-2026-untrained-connectome]] 選了預測欄，結果模型裡的抑制回饋變成興奮回饋。**查一顆細胞的傳遞物質時，先問這個值來自哪一欄。**
4. **逐突觸的準確率不是逐細胞的信心。** 88% 指的是「隨機抽一個突觸，判對的機率」。一顆細胞有數千個突觸，多數決之後的細胞層級準確率通常更高——但高多少，庫內沒有來源說過：？待查。反過來，突觸數很少的細胞（[[s-ganguly-2024-visual-inputs-to-kc]] 的 LVIN 中位數只有 11 個突觸接到視覺 KC）就沒有這份保障。
5. **預測只給傳遞物質，不給受體。** 同一種傳遞物質對不同的下游可以有相反的淨效果：[[s-yamada-2023-second-order-conditioning]] 的 MBON-α1 放麩胺酸，該篇需要它對 SMP353/354 是抑制，而 [[s-ichinose-2015-reward-recurrent-circuit]] 的迴圈需要它對同格的 PAM-α1 是淨興奮。**「這顆細胞是抑制性的」這句話沒有指定下游時，是不完整的。**
6. **六類之外的東西預測不出來。** 共同傳遞物（[[s-aso-2019-nitric-oxide-cotransmitter]] 的一氧化氮）、神經胜肽都不在六類裡，所以預測值說「這顆是膽鹼性」並不排除它同時放別的東西。

## 相關

- 連結體：[[e-hemibrain]]、[[e-fafb]]（Li 2020 的預測在這一份上跑）、[[e-neuprint]]、[[e-catmaid]]
- 細胞：[[e-apl-neuron]]、[[e-mbon]]、[[e-dopaminergic-neuron]]、[[e-kenyon-cell]]
- 概念：[[c-sparse-coding]]、[[c-valence-coding]]
- 來源：[[s-ganguly-2024-visual-inputs-to-kc]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]、[[s-minnick-2026-untrained-connectome]]、[[s-li-2020-mb-connectome]]（預測在 FAFB 上跑）
- 待開頁面：`e-flywire`、`e-codex`（[[e-fafb]]、[[e-neuprint]] 已開頁，移到上面）
