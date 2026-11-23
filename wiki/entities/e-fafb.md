---
title: FAFB 全腦電顯影像體積（FAFB）
created: 2026-11-24
updated: 2026-11-24
tags: [entity, active, cross-domain]
confidence: medium
---

# FAFB 全腦電顯影像體積（FAFB）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **FAFB（Full Adult Fly Brain）**：一顆成年雌果蠅**全腦**的連續切片穿透式電子顯微鏡影像（Zheng et al. 2018）。
- **影像體積 vs 連結體**：前者是一堆對齊好的電顯切片，誰是誰還沒標；後者是已經把神經元切分出來、突觸也標好的接線圖。FAFB 是前者。
- **CATMAID**：多人協作、在影像體積上人工追蹤神經元的網頁軟體。見 [[e-catmaid]]。
- **FlyWire**：以 FAFB 這份影像為底做出的全腦自動分段與連結體，查詢介面為 Codex。
- **T-bar**：果蠅突觸前位點在電顯下的特徵結構，傳遞物質預測以它定位取樣。
- **標記**：`※ 推論`＝本庫推得、原文沒明說；`？待查`＝要靠其他資料確認。

## 是什麼

**FAFB 是一份影像，不是一份連結體。** 它涵蓋一整顆成年雌果蠅的腦（含兩側視葉），但影像本身不告訴你哪一團像素是哪顆神經元——要用就得先追蹤。庫內四篇用到它，而**四篇用的是三個完全不同的層次**：直接在原始影像上人工追蹤幾顆神經元（[[s-felsenberg-2018-memory-extinction]]）、拿它當 [[e-hemibrain]] 查不到的東西的跨資料集對照（[[s-li-2020-mb-connectome]]）、以及把它當成某個演算法的訓練或套用體積（[[s-yamada-2023-second-order-conditioning]]、[[s-ganguly-2024-visual-inputs-to-kc]]）。

**對本庫而言，FAFB 最重要的身分是「hemibrain 的補丁」。** hemibrain 只有半邊中央腦，沒有重建視葉的髓質，食道下區（SEZ）也不在體積內；這兩塊的缺口都由 FAFB 補（見下表 [[s-li-2020-mb-connectome]] 一列）。

FAFB 的體素大小、影像張數與全腦神經元數，庫內沒有任何來源頁寫出：`？待查`。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-felsenberg-2018-memory-extinction]] | 在 FAFB 原始影像上以 [[e-catmaid]] 人工追蹤 MVP2、M4β′、M6 三顆細胞，**至少兩位各有超過 500 小時追蹤經驗的審核者校對** | MVP2 的突觸前位點多半落在 bouton 狀結構上；突觸計數、樹狀圖與「突觸到樹突根部的沿枝距離」 |
| [[s-li-2020-mb-connectome]] | 三處：(1) **傳遞物質預測在 FAFB 上跑，不是 hemibrain**——先把每一型典型與非典型 MBON 在 FAFB 裡跨資料集認出來，依 T-bar 形態取 **≥100 個**突觸位置，丟給 Eckstein et al. 2020 的模型；(2) 髓質（ME）不在 hemibrain 體積內，髓質視覺投射神經元的身分靠 FAFB 或光學影像比對確定；(3) SEZ 輸出神經元的樹突形態去 FAFB 補（該篇圖 35E）。比對工具是 Fiji 的 `ColorMIP_Mask_Search` | 34 型 MBON 的傳遞物質標註（圖 7、圖 8 以虛線外框表示預測、實線表示實測）；髓質 VPN 的來源腦區標註 |
| [[s-yamada-2023-second-order-conditioning]] | 沿用 Eckstein et al. 2020 **在 FAFB 上訓練**的 3D VGG 網路，因兩份體積解析度不同而改成等向性（四層降採樣、池化一律 2 × 2 × 2、輸入為以突觸為中心邊長 80 體素的小塊），再套到 hemibrain | 396 型中間神經元的傳遞物質預測；SMP108 的 2,753 個突觸前位點中 2,416 個被判為乙醯膽鹼 |
| [[s-ganguly-2024-visual-inputs-to-kc]] | FAFB 是本篇主資料集 FlyWire 所依據的原始影像；該篇直接採用 Codex 中已列出的 Eckstein 等人預測結果 | 傳遞物質預測的逐突觸準確率：**FAFB 88%、hemibrain 79%** |

各篇引用的數字見 [[numbers]]。

## 引用時的陷阱

1. **「在 FAFB 上做的」至少有三種意思，寫清楚是哪一種。** [[s-felsenberg-2018-memory-extinction]] 是人手追三顆細胞；[[s-ganguly-2024-visual-inputs-to-kc]] 的 FlyWire 是同一份影像的全腦自動分段；[[s-li-2020-mb-connectome]] 只是去認幾顆對應的神經元。**三者的錯誤來源完全不同**，混用等於把人工校對過的少數細胞與自動分段的全腦擺在同一個信心水準上。
2. **跨資料集比對的成功率沒有統一報法。** [[s-li-2020-mb-connectome]] 只寫「在許多情況下」能確定標註髓質 VPN，**沒有給比例**；[[s-ganguly-2024-visual-inputs-to-kc]] 用 NBLAST 報 66%，而該數字與它自己的圖 7A 對不上（見該頁問題與限制第 8 條）。引用「跨資料集確認過」時，先問確認了幾顆、用什麼判準。
3. **訓練體積與套用體積不同，準確率就不同。** 同一個傳遞物質預測模型在 FAFB 上 88%、在 hemibrain 上 79%；[[s-yamada-2023-second-order-conditioning]] 要把它移到 hemibrain 還得改成等向性。**「這個模型準確率 88%」這句話沒有指定體積時是不完整的**（見 [[c-neurotransmitter-prediction]]）。
4. **FAFB 補得了身分與形態，補不了突觸數。** [[s-li-2020-mb-connectome]] 用它確認髓質 VPN 是誰、SEZ 神經元長什麼樣，但該篇所有突觸計數仍然來自 hemibrain。**不要把「身分在 FAFB 確認過」讀成「連結在 FAFB 驗證過」。**
5. **同一段原文有兩面，只取一半會過度樂觀。** [[s-li-2020-mb-connectome]] 寫「在許多情況下我們能夠確定地標註髓質 VPN」，但同段緊接著寫 **"we have little definitive insight into the type of visual information conveyed by their VPN inputs"**——**來源腦區確認了，編碼內容沒有。**

## 相關

- 另一份體積與它的介面：[[e-hemibrain]]、[[e-neuprint]]
- 追蹤與比對工具：[[e-catmaid]]、[[e-nblast]]、[[e-mcfo]]
- 方法：[[c-neurotransmitter-prediction]]
- 細胞與構造：[[e-visual-projection-neuron]]、[[e-accessory-calyx]]、[[e-mbon]]
- 來源：[[s-felsenberg-2018-memory-extinction]]、[[s-li-2020-mb-connectome]]、[[s-yamada-2023-second-order-conditioning]]、[[s-ganguly-2024-visual-inputs-to-kc]]
- 待開頁面：`e-flywire`（以 FAFB 為底的全腦連結體）、`e-codex`（FlyWire 的查詢介面）、`e-optic-lobe`（視葉四神經氈）
