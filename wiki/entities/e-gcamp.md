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

本庫用到的版本如下表。各版本的靈敏度與反應速度，Tomchik、Hige、Handler 三篇原文都沒有介紹或比較（已搜 fast、slow、kinetic、sensitiv），本頁不依記憶補：？待查。

| 版本 | 來源 | 特別之處 |
|---|---|---|
| G-CaMP 1.6 | Tomchik 2009（引 Reiff et al. 2005） | 三篇中最早的版本 |
| GCaMP6f | Hige 2015、Felsenberg 2017、Felsenberg 2018 | — |
| GCaMP6s | Handler 2019、Cohn 2015 | — |
| GCaMP6m | Felsenberg 2017（PAM 成像）、Felsenberg 2018 | — |
| sytGCaMP | Cohn 2015 **自製**：GCaMP6s 接在突觸小泡蛋白 synaptotagmin 1 上 | 只待在突觸前末梢，量的是末梢的鈣，不是整個細胞質的鈣（見 [[c-presynaptic-calcium]]） |
| ER-GCaMP6-210 | Handler 2019 **自製**的轉基因果蠅（感測器設計引 de Juan-Sanz et al. 2017） | 低親和力版本（對鈣結合較弱，依來源頁說法適合內質網內的高鈣濃度），前端接一段把蛋白送進內質網的訊號序列、尾端接留在內質網的序列，所以量的是**內質網（細胞內儲存鈣的小倉庫）裡面**的鈣。**變暗＝內質網放出鈣**，方向與一般 GCaMP 相反 |

## 庫內誰用了它

| 來源 | 版本 | 表現在哪裡（驅動品系） | 量哪裡、怎麼讀 | 用它算出什麼 |
|---|---|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | G-CaMP 1.6 | [[e-kenyon-cell]]（238Y） | 離體腦，共軛焦；α、α′ 葉與萼部；ΔF/F0（%） | 多巴胺、章魚胺本身幾乎不引起 KC 鈣上升；提高 cAMP 後，KC 對乙醯膽鹼的鈣反應變大 |
| [[s-hige-2015-heterosynaptic-plasticity]] | GCaMP6f | 全部 KC（R13F02-LexA） | 活體，雙光子 920 nm；KC **細胞體**；某顆細胞「有反應」＝峰值超過基線 2.33 個標準差 | 配對前後 KC 對氣味的反應沒有配對專屬的改變；KC 對氣味的稀疏反應與兩種氣味的重疊比例 |
| [[s-handler-2019-dopamine-receptor-timing]] | GCaMP6s | [[e-mbon]]：γ4（離體 VT026001-Gal4、在體 R53C03-LexA）、γ2、γ5；[[e-dopaminergic-neuron]]：基因型表標為「γ4–5 DANs」的 R58E02-LexA（Felsenberg 2017 說同一品系標 13 型 PAM，見 [[e-r58e02]]、[[syn-contradictions]] 1.5） | 雙光子 920 nm；MBON 樹突在區室內的鈣；KC 刺激後 2 s 內的峰值 | KC→MBON 突觸變強或變弱；DAN 活動在順向、逆向配對時是否相同 |
| 同上 | ER-GCaMP6-210 | KC 軸突（OK107-Gal4），γ4/γ5 區室 | KC 刺激後 1 s 平均，以前 2–4 s 標準化 | 只在多巴胺先到時，內質網才放鈣（DopR2 那條路徑） |
| [[s-cohn-2015-coordinated-neuromodulation]] | sytGCaMP；GCaMP6s | sytGCaMP：γ KC 末梢、各格 DAN 末梢（TH＋DDC 啟動子）；GCaMP6s：成對的 γ MBON | 活體與離體，雙光子；γ 葉 12–18 層體積成像；KC 末梢以正規化強度輪廓呈現（相對值） | 同一條 KC 軸突在不同格的末梢鈣不同；DAN 群體的相反樣式；MBON 增強與減弱 |
| [[s-felsenberg-2017-re-evaluation]] | GCaMP6f／6m | PPL1 DAN 細胞體（MB504B 等）、PAM 的 γ5 區（R58E02-LexA，6m）；γ2α′1 MBON、V2 MBON | 離體 910 nm；活體以 5 s 氣味的 AUC 除以同一隻對新氣味的 AUC | MBON 活化後 DAN 的反應；訓練後 γ2α′1 MBON 對 CS− 反應變大 |
| [[s-felsenberg-2018-memory-extinction]] | GCaMP6f／6m | PAM 末梢（R48B04）；MVP2、M4β′、M6 的樹突與軸突 | 同 Felsenberg 2017 的讀法 | γ5 PAM 被 M4β′／M6 活化；消退前後新舊記憶的鈣痕跡 |

各篇的參數與數值見 [[numbers]]。

## 已知的問題

- **ΔF/F 數值不可跨篇比較。** 版本不同、表現在不同細胞、用不同顯微鏡、讀取的時間窗與基線定義不同。Tomchik 的「15% ΔF/F0」、Hige 的「超過 2.33 SD」、Handler 的「峰值 1.22 → 0.42」不是同一把尺。
- **成像本身會讓訊號變暗。** Hige 2015 的不給光對照組，KC 反應在配對後也一樣小幅下降，作者歸因於雷射反覆照射造成的漂白（螢光蛋白逐漸變暗）與光損傷。沒有這組對照，下降就會被誤讀為 KC 也學到了東西。
- **鈣上升不等於送出更多訊號。** Tomchik 2009 用 KC 軸突的鈣增強推論「突觸前可塑性」，但沒有量 KC 對 MBON 的傳遞（見 [[t-dopamine-to-plasticity]]）；Cohn 2015 的 sytGCaMP 雖然只在末梢發光，量的仍是鈣，不是傳遞物質的釋放量，DAN 末梢的鈣也只是多巴胺釋放的代替指標。
- **正規化後只剩相對值。** Cohn 2015 的 KC 末梢輪廓經正規化，四格的變化相加約為零，一格變亮必然伴隨別格「相對」變暗。
- **同一顆神經元，樹突與軸突的讀數可以不同。** Felsenberg 2018：學習後 M6 的軸突對 CS+ 反應較大、樹突沒有差別。
- **對小變化不敏感。** Tomchik 來源頁提醒，G-CaMP 1.6 測不到細胞電位的小幅變化，所以「多巴胺不會激發 KC（不引起去極化）」只能讀成「不引起可偵測的鈣上升」。
- **ER-GCaMP 的方向容易讀反。** 變暗代表放鈣。Handler 2019 在順向配對（KC 在前、DAN 在後）時量到一個顯著的小幅變亮，正文沒有提；來源頁的推論是可能代表內質網回收鈣，也可能是感測器假象（見該來源頁 3.5 節）。

## 相關

- 其他感測器：[[e-epac-camp-sensor]]
- 細胞：[[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]
- 製備：[[c-ex-vivo-explant]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-camp-signaling]]、[[c-presynaptic-calcium]]
- 主題：[[t-dopamine-to-plasticity]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
