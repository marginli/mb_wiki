---
title: GCaMP 系鈣感測器（GCaMP calcium indicators）
created: 2026-10-25
updated: 2026-11-13
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
| G-CaMP（版本號未寫） | Mao 2009（引 Yu et al. 2004） | 庫內最早的一篇；原文只寫 G-CaMP，沒有版本號 |
| G-CaMP 1.6 | Tomchik 2009（引 Reiff et al. 2005） | 三篇中最早的版本 |
| GCaMP3／GCaMP3.0 | Dylla 2017（GCaMP3）、Burke 2012（GCaMP3.0） | 兩篇都用它量 DAN：Dylla 量九個區室的 DAN 與 KC，Burke 量 PAM 對外加章魚胺的反應 |
| GCaMP6f | Hige 2015、Felsenberg 2017、Felsenberg 2018、Pribbenow 2022、Eschbach 2021（幼蟲） | — |
| GCaMP6s | Handler 2019、Cohn 2015、Aso 2023 | — |
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
| [[s-huang-2024-dopamine-memory-dynamics]] | jGCaMP7b | PPL1-α′2α2（R82C10-LexA）、PPL1-α3（MB065B） | 頭固定的活果蠅；氣味 5 s 或 10 s 期間相對基線的平均 ΔF/F；只當對照，主實驗用電壓成像 | **與同型細胞的電壓成像對照**（延伸圖 13）：吸引氣味讓 PPL1-α3 放電明顯下降，鈣訊號卻幾乎不變（ACV 與基線無統計差異）；OCT 配電擊時鈣訊號小於兩者分別給的相加，作者歸因於指示劑飽和 |
| [[s-mao-2009-dopaminergic-neuron-types]] | G-CaMP（版本未寫） | [[e-dopaminergic-neuron]]（TH-GAL4） | 活體，頭頂開窗、覆塑膠膜；20× 物鏡、488 nm、每秒 4.4 張；垂直葉四段的 DAN 末梢（α 尖端、α′ 尖端、上段、下段連交界）；ΔF/F＝(刺激中最亮的連續 5 張平均 − 刺激前 5 張平均) ÷ 刺激前 5 張平均 | 四段 DAN 對電擊（定電流 0.0001–0.1 mA）與氣味的反應排序不同；配對前後的 Post/Pre（訓練後 10 分鐘 ÷ 訓練前 5 分鐘 × 100%）。**只看得到上升**（對照 Huang 2024 延伸圖 13） |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | GCaMP3 | [[e-dopaminergic-neuron]]（TH-GAL4，另帶 mb247-DsRed 當地標）；[[e-kenyon-cell]]（[[e-ok107-gal4]]） | 活體，共軛焦 20× 水鏡、每秒 5 張、每回合只拍前 45 秒；九個蕈狀體區室；ΔF/F0 的 F0 取第 3–24 張，再除以「第 2 回合丁醇反應在反應最強那一區的最大值」 | DAN 與 KC 對 CS、電擊的聯結式改變；DAN 電擊反應與流經果蠅電流的對數相關（Spearman ρ：γ1 0.636、γ2 0.330、γ5 0.481、β′2 0.583）；九區空間樣式的夾角 |
| [[s-burke-2012-octopamine-dopamine-reward]] | GCaMP3.0 | [[e-dopaminergic-neuron]]：0104-GAL4 標的約 40 顆 PAM | 剖開頭殼的活體（800 µl 無糖 HL3 類似液）；β′ 葉尖固定 ROI；每秒 3 張；F 取前 24 張（＝前 8 秒）的平均；取施藥後 5 秒內的峰值 | 浴中終濃度 5 mM 章魚胺使 ΔF/F 峰值達約 0.50，先加 2.45 mM mianserin 則只約 0.13（各 n＝11，※ 從圖 4c 判讀）。**注意 30 秒處單純施液也造成約 0.2 的瞬跳，與 mianserin 組對章魚胺的反應同量級** |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | GCaMP6f | [[e-mbon]]：M4/6（MB011B 或 [[e-vt1211]]）、α′3 MBON（MB027B）；[[e-kenyon-cell]]（[[e-ok107-gal4]]、MB369B） | 離體＋TTX：M6 樹突對噴注乙醯膽鹼的鈣峰值；活體：β′2 樹突與 M4 軸突取氣味開始後 3 秒的 AUC、α′3 取峰值。活體每種條件 9–12 個半腦、來自 5–7 隻果蠅（**圖上的 n 是半腦數，不是果蠅數**） | 離體配對前後的峰值比約 1.05–1.06（n＝18）；活體糖訓練前後的 AUC 比約 0.65（n＝9）；α′3 在十次氣味後 MBON 反應由約 0.32 降到約 0.07，同格 KC 不變（約 0.88 → 0.85） |
| [[s-eschbach-2021-learned-innate-valence-integration]] | GCaMP6f | **幼蟲** MBON-m1（SS02163）與 CN-33（SS02108） | 一齡幼蟲夾在微流道晶片（通道寬 300 µm），雙光子 925 nm、25× 水鏡、每秒 35 張、6 層層距 2 µm；量神經突；以 tdTomato 校正，ΔF/F₀ 的基線取刺激前 5 秒 | 氣味經側角活化兩型細胞（KC 以 TNTe 阻斷後仍上升）；光活化全部 KC 時反應雙向，加 PTX（拿掉抑制）後變強烈興奮、加 MCA（拿掉興奮）後消失；嫌惡訓練後 MBON-m1 對 CS+ 的反應降到約三成（9 隻，※ 從圖判讀） |
| [[s-aso-2023-upwind-neurons]] | GCaMP6s | UpWiN（R64A11-LexA） | 離體腦，雙光子；ROI 取**樹突與軸突徑的交界**；光活化 MBON 1 秒、9 次、間隔 30 秒後平均 | 活化 MBON-α3 時 UpWiN 的峰值約 0.43 ΔF/F（n＝5）、同時活化 MBON-α1 時約 0.04（n＝7）；**單獨活化 MBON-α1 在鈣訊號上看不到可偵測的抑制**（n＝11），但它有效抵消了 MBON-α3 的興奮。圖說沒有報告任何統計檢定，「effectively canceled」是目視判斷 |

各篇的參數與數值見 [[numbers]]。

## 已知的問題

- **ΔF/F 數值不可跨篇比較。** 版本不同、表現在不同細胞、用不同顯微鏡、讀取的時間窗與基線定義不同。Tomchik 的「15% ΔF/F0」、Hige 的「超過 2.33 SD」、Handler 的「峰值 1.22 → 0.42」不是同一把尺。
- **成像本身會讓訊號變暗。** Hige 2015 的不給光對照組，KC 反應在配對後也一樣小幅下降，作者歸因於雷射反覆照射造成的漂白（螢光蛋白逐漸變暗）與光損傷。沒有這組對照，下降就會被誤讀為 KC 也學到了東西。
- **鈣上升不等於送出更多訊號。** Tomchik 2009 用 KC 軸突的鈣增強推論「突觸前可塑性」，但沒有量 KC 對 MBON 的傳遞（見 [[t-dopamine-to-plasticity]]）；Cohn 2015 的 sytGCaMP 雖然只在末梢發光，量的仍是鈣，不是傳遞物質的釋放量，DAN 末梢的鈣也只是多巴胺釋放的代替指標。
- **正規化後只剩相對值。** Cohn 2015 的 KC 末梢輪廓經正規化，四格的變化相加約為零，一格變亮必然伴隨別格「相對」變暗。
- **同一顆神經元，樹突與軸突的讀數可以不同。** Felsenberg 2018：學習後 M6 的軸突對 CS+ 反應較大、樹突沒有差別。
- **看不到放電「減少」，強刺激時又會飽和。** Huang 2024 延伸圖 13：同一型 PPL1-α3，電壓成像看到吸引氣味讓放電下降，jGCaMP7b 幾乎看不出來；氣味加電擊時鈣訊號又低於相加。所以用 GCaMP 量 DAN 時，「沒看到下降」不能讀成「沒有下降」，「不到相加」也可能只是飽和。限制：兩種成像是不同批果蠅（鈣 14 隻、電壓 16 隻），PPL1-α′2α2 的鈣成像與電壓成像也用不同品系。
- **對小變化不敏感。** Tomchik 來源頁提醒，G-CaMP 1.6 測不到細胞電位的小幅變化，所以「多巴胺不會激發 KC（不引起去極化）」只能讀成「不引起可偵測的鈣上升」。
- **ER-GCaMP 的方向容易讀反。** 變暗代表放鈣。Handler 2019 在順向配對（KC 在前、DAN 在後）時量到一個顯著的小幅變亮，正文沒有提；來源頁的推論是可能代表內質網回收鈣，也可能是感測器假象（見該來源頁 3.5 節）。

- **軌跡會漂，陰性結果要和漂移比。** [[s-dylla-2017-trace-conditioning-dan-plasticity]] 的 ΔF/F0 軌跡在刺激後普遍緩慢漂到基線以下，**訓練前後、配對與不配對兩組都有**（該來源頁第五節第 2 條）。所以任何「低於基線」的訊號都要先和這段漂移比；該篇想找的「預期的電擊沒來時 DAN 下降」正好會被埋在裡面。同一篇的另一個問題同型：不配對組的 CS 反應一路往下掉（作者自承分不出是神經元疲乏、氣味變淡還是漂白），所以「配對組相對較大」也可能是「配對組沒有掉下去」。
- **鈣看不到抑制，卻看得到抑制的後果。** [[s-aso-2023-upwind-neurons]] 圖 4C：單獨光活化抑制性的 MBON-α1 時，UpWiN 的鈣訊號看不到任何可偵測的下降（n＝11），但同時活化 MBON-α1 與 MBON-α3 時，MBON-α3 原本約 0.43 的興奮被壓到約 0.04。**抑制性輸入在鈣上是「看不見的」，只有在它抵消別的興奮時才顯現。** 該篇的電生理（全細胞記錄）才直接看到 17 顆 UpWiN 中有 4 顆被抑制。這條與下面「看不到放電減少」是同一類限制的兩個面向。
- **效果小的時候，比值要看絕對幅度。** [[s-pribbenow-2022-postsynaptic-plasticity]] 離體誘發的增強是後測／前測約 1.05–1.06（約 5–6%，n＝18），而它的陰性對照組（降低 α2）平均約 1.03——兩者差距小，論文沒有做兩組之間的直接比較（該來源頁 3.3 評價）。同篇 FRAP 在 20 分鐘的回復幅度也只有約 8%。
- **ROI 畫在哪裡會換掉問題。** [[s-burke-2012-octopamine-dopamine-reward]] 的 ROI 取在 β′ 葉尖（PAM 的軸突末梢），而它自己的 Brp::GFP 與 GRASP 顯示章魚胺的接觸點在 ampr（PAM 推定的樹突端），論文沒有說明為何選軸突端（※ 推論）。[[s-aso-2023-upwind-neurons]] 則刻意取在樹突與軸突徑的交界。比較兩篇的 ΔF/F 之前，先確認量的是同一段神經突。
- **幼蟲與成蟲的製備差很多。** [[s-eschbach-2021-learned-innate-valence-integration]] 把一齡幼蟲夾在微流道晶片裡、每秒 35 張、以 tdTomato 校正動作；成蟲的實驗多半是開窗固定、每秒 1–5 張。取樣率、動作校正與基線定義都不同，ΔF/F₀ 不可跨階段比較。

## 相關

- 其他感測器：[[e-epac-camp-sensor]]
- 細胞：[[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]、[[e-th-gal4]]、[[e-r58e02]]
- 製備：[[c-ex-vivo-explant]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-camp-signaling]]、[[c-presynaptic-calcium]]
- 主題：[[t-dopamine-to-plasticity]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-burke-2012-octopamine-dopamine-reward]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-aso-2023-upwind-neurons]]
