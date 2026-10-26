---
title: MBON-γ5β′2a（M6；γ5 MBON）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-γ5β′2a（M6；γ5 MBON）


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

蘑菇體輸出神經元（[[e-mbon]]）的一型。新名 MBON-γ5β′2a 串了 γ 葉第 5 格（γ5）與 β′ 葉 β′2a 小區兩個位置；舊名 M6（Felsenberg 2018 的寫法）；Handler 2019 與 Cohn 2015 則不用這兩個名字，只用它樹突所在的區室（γ5 格）稱它「γ5 MBON」。依 Felsenberg 2018，它放出麩胺酸（glutamate），活化時讓果蠅「走開」，樹突在 γ5 格，左右腦各一顆（摘要稱「a pair」）。它被 [[e-mbon-gamma1pedc]]（MVP2）以 GABA 抑制。這條連結是 Felsenberg 2018 解釋消退的關鍵：消退後 MVP2 上的舊痕跡（對 CS+ 的反應比 CS− 小）仍在，M6 的樹突卻新出現痕跡，使軸突的 CS+／CS− 差別變得不顯著（見下表與 [[c-memory-extinction]]）。

## 版本與規模（標記它的品系）

| 來源 | 品系 | 稱呼 |
|---|---|---|
| Felsenberg 2018 | R66C08-GAL4（只標 M6）；VT1211-GAL4／-LexA（同時標 M4β′ 與 M6） | M6、MBON-γ5β′2a |
| Handler 2019 | 66C08-Gal4 | γ5 MBON |
| Cohn 2015 | 主文沒寫品系名（？待查） | γ5 MBON |

※ 推論：Handler 的 66C08-Gal4 就是 Felsenberg 2018 的 R66C08-GAL4，標的是同一型（品系名只差前綴 R）；Cohn 的「γ5 MBON」只以區室命名，γ5 格是否只有這一型 MBON，庫內來源沒有說明：？待查。

## 庫內誰用了它

| 來源 | 怎麼用 | 看到什麼 |
|---|---|---|
| [[s-felsenberg-2018-memory-extinction]] | 電擊訓練、消退後的活體鈣成像（樹突與軸突分開量）；離體以 CsChrimson 活化 M4β′／M6、看 PAM；再暴露時以 [[e-shibire-ts]] 阻斷 VT1211；電顯追蹤 | 只訓練：樹突 CS+＝CS−，**軸突** CS+ 較大；消退後：樹突新出現 CS+ < CS−（中位數約 0.20 vs 0.65），軸突差別不顯著；活化 M4β′／M6 使 γ5 PAM ΔF/F0 約 +1.75（5 個腦），γ4 無反應；MVP2 接 M6R 17、M6L 16 個突觸，靠近樹突根部 |
| [[s-handler-2019-dopamine-receptor-timing]] | 離體配對（R58E02-LexA＋P2X2 活化 DAN，量 γ5 MBON 鈣） | 論文說 γ5 也有類似 γ4 的雙向改變；資料在補充圖 S3（？待查，補充資料未取得） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 以 [[e-p2x2]] 活化它本身、看各格 DAN；活體與離體鈣成像 | 活化後 γ2–γ4 DAN 下降、γ5 DAN 小幅上升；活體氣味反應約 0.05，遠小於 γ3 的約 1.05，離體時兩者無差異 |

## 已知的問題

- **樹突沒變不等於輸出沒變。** Felsenberg 2018 的訓練效果只在 M6 軸突看得到、樹突看不到；作者以 MVP2 在樹突根部的抑制解釋，這是從解剖推的功能。
- **「抵消」是「不顯著」。** 消退後軸突的 CS+／CS− 差別不顯著，論文只做組內比較，沒做「組別 × 氣味」交互作用檢定；圖 7 圖說自己寫 partially compensates。樹突的「CS+ < CS−」也分不出是 CS+ 變小還是 CS− 變大。
- **M4β′ 與 M6 分不開。** 離體活化與行為阻斷都用 VT1211，同時標兩者；阻斷實驗另有一個作者稱「unexpectedly」的結果（再聞 CS− 時阻斷，躲避消失），見來源頁 3.2。
- **活體 γ5 DAN 的氣味反應沒量到**（自發振盪，data not shown），「M6 → γ5 PAM」的回饋是離體證據加行為阻斷拼成的（見 [[t-mbon-dan-feedback]]）。
- **「推動走開」是引用。** Handler 引 Aso 2014b，Felsenberg 2018 引 Owald 2015 等。

## 相關

- 細胞：[[e-mbon]]、[[e-mbon-gamma1pedc]]、[[e-mbon-gamma4]]、[[e-dopaminergic-neuron]]、[[e-r58e02]]
- 概念：[[c-memory-extinction]]、[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]
- 主題：[[t-memory-updating]]、[[t-mbon-dan-feedback]]
- 來源：[[s-felsenberg-2018-memory-extinction]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]
