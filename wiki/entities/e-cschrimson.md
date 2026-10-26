---
title: CsChrimson（紅光活化通道）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: high
---

# CsChrimson（紅光活化通道）

## 是什麼

一種照紅光就打開、讓正離子流進細胞的通道蛋白（光敏感通道，opsin）。用驅動品系讓特定神經元製造它，紅光一照，那群神經元就放電。這種「用光控制神經元」的方法叫光遺傳（optogenetics）。在本庫，它主要用來直接活化 [[e-dopaminergic-neuron]]（DAN），代替電擊或糖水當作懲罰或獎賞（見 [[c-us-substitution]]）；Felsenberg 2017、2018 則用它在取出的腦裡活化輸出神經元（MBON），看 DAN 會不會跟著反應（見 [[t-mbon-dan-feedback]]）。優點是時間精確到毫秒，而且只動被標記的那幾顆 DAN。

它需要視黃醛（retinal）當輔因子，所以果蠅要先吃含全反式視黃醛的飼料、養在暗處。

**ChrimsonR** 是另一種紅光活化的通道，Handler 2019 只在閉迴路實驗用它（果蠅頭固定在顯微鏡下、腳踩泡沫球，球的轉動帶動送氣管，可同時看腦與行為）。兩者的差別本庫各篇都沒有說明：？待查。

## 版本與規模（光參數）

| 項目 | Hige 2015 | Handler 2019 |
|---|---|---|
| 通道 | CsChrimson（引 Klapoetke et al. 2014） | CsChrimson；閉迴路改用 ChrimsonR |
| 光源 | 627 nm LED，直接照在打開的腦上 | 行為小室：627 nm LED；閉迴路：565 nm，經顯微鏡物鏡照射 |
| 光強 | 14.7 mW/mm² | 小室約 18–40 μW/mm²；閉迴路約 150 μW/mm² |
| 生理實驗的光 | 1 ms × 4 下（2 Hz，氣味開始後 0.2 s 起）；單脈衝 1 ms × 1（氣味開始後 0.8 s）；長協定 1 ms × 120 下（2 Hz，配 60 s 氣味） | 離體腦不用光，改用 P2X2＋ATP；閉迴路 1 s 持續照光 |
| 行為實驗的光 | 500 ms × 12（從圖 7J 讀出，其他參數在補充資料：？待查） | 1 s 持續照光 |
| 視黃醛 | 電生理 0.5 mM、暗處 36–72 h；行為實驗在羽化（蛹變為成蟲）前 0.2 mM、之後 0.4 mM | 0.4 mM，1–3 日齡雌蠅轉入後暗養 2–3 天 |

數值出處見 [[numbers]]。

## 庫內誰用了它

| 來源 | 活化哪些 DAN（驅動品系） | 用它做什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **未使用。** 該篇沒有活化 DAN，直接把多巴胺滴進腦裡 | — |
| [[s-hige-2015-heterosynaptic-plasticity]] | PPL1-γ1pedc（MB320C）；多型 PPL1（MB099C；Hige 說四型、Aso 2016 說兩型，見 [[syn-contradictions]] 1.4）；多數 PPL1 加少數 PAM（TH-GAL4） | 一邊記錄 MBON，一邊讓氣味與 DAN 活化配對；另以光代替電擊訓練果蠅 |
| [[s-handler-2019-dopamine-receptor-timing]] | PAM（MB042B）、PPL（MB504B）；閉迴路用 MB042B 驅動 ChrimsonR | 自由行走果蠅的順向／逆向配對與時間差掃描；閉迴路中同時記錄 γ4 MBON 與行為 |
| [[s-aso-2016-dan-cell-type-rules]] | 六組品系（MB320C、MB099C、MB630B、MB043C、MB213B、MB315C＋MB109B），另以 VT045661-LexA 驅動 LexA 版 CsChrimson；行為：627 nm、34.9 µW/mm²，標準訓練 60 s 內 30 下、每下 1 s；視黃醛羽化前 0.2 mM、之後 0.4 mM | 競技場中代替電擊或糖訓練，比較各型 DAN 的學習規則 |
| [[s-felsenberg-2017-re-evaluation]] | **活化的是 MBON 不是 DAN**：V2 群（R71D08-LexA 等）、γ2α′1 MBON（R25D01-LexA、MB077C）；離體腦，630 nm、0.85 mW/mm²，40 Hz × 10 ms 共 500 ms（圖 4d 為 200 ms）；視黃醛 1 mM | 看活化 MBON 後 PPL1 或 PAM 的鈣反應（MBON → DAN 的功能連結） |
| [[s-felsenberg-2018-memory-extinction]] | **活化的是 MBON**：M4β′ 與 M6（VT1211-LexA）；離體腦，參數同 Felsenberg 2017（500 ms） | 活化後 γ5 的 PAM 末梢 ΔF/F0 約 +1.75（5 個腦），γ4 無反應 |

## 已知的問題

- **光強不能跨篇直接比。** Hige 的 14.7 mW/mm² 照在打開的腦上，Handler 的 18–40 μW/mm² 照在小盒裡自由行走的果蠅身上：一個以毫瓦（mW）、一個以微瓦（μW）為單位，光要穿過的組織也不同，到達 DAN 的實際光量無從比較。
- **同一篇裡，生理與行為的光協定也不同。** Hige 生理用 1 ms 短脈衝、行為用 500 ms × 12，所以「突觸變弱」與「行為學到」是在兩種刺激下分別看到的。
- **「光照有效」靠補充資料。** Hige 2015 說光脈衝能讓 PPL1-γ1pedc 與 PPL1-α′2α2 可靠放電，證據在補充圖 S2：？待查。Hige 2015 比較了兩個區室的誘發門檻（要多少次「氣味＋光」配對才會讓突觸變弱）：γ1pedc 用 MB320C（一顆 DAN），α2 用 MB099C（多型 DAN）。不同品系每次光照放出的多巴胺可能不同，所以門檻差異可能部分來自活化強度，是這項比較的混淆因子（見 [[e-mb099c]]、[[e-mushroom-body]]）。
- **光本身的作用要排除。** Handler 2019 的行為指標是「訓練後果蠅往氣味源走的距離比訓練前多幾 mm」。只帶 CsChrimson、沒有 DAN 驅動品系（所以光照不會活化 DAN）的對照組，在 DAN 晚氣味 1 s 的時序下也多走了約 0.7 mm（見 [[numbers]]），表示光與流程本身就有小幅效果；光照單獨的對照在補充圖 S1D–E：？待查。
- **「活化 MBON 讓 DAN 有反應」只說明功能上相連。** Felsenberg 2017、2018 的離體實驗沒有氣味、n 小（4–5），不能區分直接突觸與間接路徑；Felsenberg 2018 的 VT1211 同時標 M4β′ 與 M6，分不出是哪一顆在驅動 γ5。
- **Cohn 2015 也提到一種「紅移的 channelrhodopsin」**（補充圖 S6A），論文沒寫是哪一種，本頁不把它算成 CsChrimson。

## 相關

- 細胞：[[e-dopaminergic-neuron]]；品系：[[e-split-gal4]]
- 概念：[[c-us-substitution]]、[[c-cs-us-timing]]、[[c-performance-index]]
- 主題：[[t-timing-rules]]、[[t-mbon-dan-feedback]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
