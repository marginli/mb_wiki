---
title: GCaMP 系鈣感測器（GCaMP calcium indicators）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: high
---

# GCaMP 系鈣感測器（GCaMP calcium indicators）

## 是什麼

一類用基因工程讓神經元自己製造、遇到鈣離子就變亮的綠色螢光蛋白。神經元被激發時細胞內的鈣會升高，所以螢光變亮可當作「這顆細胞在活動」的間接指標。讀數通常寫成 ΔF/F（或 ΔF/F0）：螢光比刺激前的基線亮了多少比例。它看不到單一次放電，也不直接告訴你突觸送出了多少訊號。

## 版本與規模

本庫三篇用了四個版本。各版本的靈敏度與反應速度，三篇原文都沒有介紹或比較（已搜 fast、slow、kinetic、sensitiv），本頁不依記憶補：？待查。

| 版本 | 來源 | 特別之處 |
|---|---|---|
| G-CaMP 1.6 | Tomchik 2009（引 Reiff et al. 2005） | 三篇中最早的版本 |
| GCaMP6f | Hige 2015 | — |
| GCaMP6s | Handler 2019 | — |
| ER-GCaMP6-210 | Handler 2019 **自製**的轉基因果蠅（感測器設計引 de Juan-Sanz et al. 2017） | 低親和力版本（對鈣結合較弱，依來源頁說法適合內質網內的高鈣濃度），前端接一段把蛋白送進內質網的訊號序列、尾端接留在內質網的序列，所以量的是**內質網（細胞內儲存鈣的小倉庫）裡面**的鈣。**變暗＝內質網放出鈣**，方向與一般 GCaMP 相反 |

## 庫內誰用了它

| 來源 | 版本 | 表現在哪裡（驅動品系） | 量哪裡、怎麼讀 | 用它算出什麼 |
|---|---|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | G-CaMP 1.6 | [[e-kenyon-cell]]（238Y） | 離體腦，共軛焦；α、α′ 葉與萼部；ΔF/F0（%） | 多巴胺、章魚胺本身幾乎不引起 KC 鈣上升；提高 cAMP 後，KC 對乙醯膽鹼的鈣反應變大 |
| [[s-hige-2015-heterosynaptic-plasticity]] | GCaMP6f | 全部 KC（R13F02-LexA） | 活體，雙光子 920 nm；KC **細胞體**；某顆細胞「有反應」＝峰值超過基線 2.33 個標準差 | 配對前後 KC 對氣味的反應沒有配對專屬的改變；KC 對氣味的稀疏反應與兩種氣味的重疊比例 |
| [[s-handler-2019-dopamine-receptor-timing]] | GCaMP6s | [[e-mbon]]：γ4（離體 VT026001-Gal4、在體 R53C03-LexA）、γ2、γ5；[[e-dopaminergic-neuron]]：γ4/γ5 DAN（R58E02-LexA） | 雙光子 920 nm；MBON 樹突在區室內的鈣；KC 刺激後 2 s 內的峰值 | KC→MBON 突觸變強或變弱；DAN 活動在順向、逆向配對時是否相同 |
| 同上 | ER-GCaMP6-210 | KC 軸突（OK107-Gal4），γ4/γ5 區室 | KC 刺激後 1 s 平均，以前 2–4 s 標準化 | 只在多巴胺先到時，內質網才放鈣（DopR2 那條路徑） |

各篇的參數與數值見 [[numbers]]。

## 已知的問題

- **ΔF/F 數值不可跨篇比較。** 版本不同、表現在不同細胞、用不同顯微鏡、讀取的時間窗與基線定義不同。Tomchik 的「15% ΔF/F0」、Hige 的「超過 2.33 SD」、Handler 的「峰值 1.22 → 0.42」不是同一把尺。
- **成像本身會讓訊號變暗。** Hige 2015 的不給光對照組，KC 反應在配對後也一樣小幅下降，作者歸因於雷射反覆照射造成的漂白（螢光蛋白逐漸變暗）與光損傷。沒有這組對照，下降就會被誤讀為 KC 也學到了東西。
- **鈣上升不等於送出更多訊號。** Tomchik 2009 用 KC 軸突的鈣增強推論「突觸前可塑性」，但沒有量 KC 對 MBON 的傳遞（見 [[t-dopamine-to-plasticity]]）。
- **對小變化不敏感。** Tomchik 來源頁提醒，G-CaMP 1.6 測不到細胞電位的小幅變化，所以「多巴胺不會激發 KC（不引起去極化）」只能讀成「不引起可偵測的鈣上升」。
- **ER-GCaMP 的方向容易讀反。** 變暗代表放鈣。Handler 2019 在順向配對（KC 在前、DAN 在後）時量到一個顯著的小幅變亮，正文沒有提；來源頁的推論是可能代表內質網回收鈣，也可能是感測器假象（見該來源頁 3.5 節）。

## 相關

- 其他感測器：[[e-epac-camp-sensor]]
- 細胞：[[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-camp-signaling]]
- 主題：[[t-dopamine-to-plasticity]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]
