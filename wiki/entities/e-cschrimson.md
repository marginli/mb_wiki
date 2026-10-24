---
title: CsChrimson（紅光活化通道）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: high
---

# CsChrimson（紅光活化通道）

## 是什麼

一種照紅光就打開、讓正離子流進細胞的通道蛋白（光敏感通道，opsin）。用驅動品系讓特定神經元製造它，紅光一照，那群神經元就放電。這種「用光控制神經元」的方法叫光遺傳（optogenetics）。在本庫，它用來直接活化 [[e-dopaminergic-neuron]]（DAN），代替電擊或糖水當作懲罰或獎賞（見 [[c-us-substitution]]）。優點是時間精確到毫秒，而且只動被標記的那幾顆 DAN。

它需要視黃醛（retinal）當輔因子，所以果蠅要先吃含全反式視黃醛的飼料、養在暗處。

**ChrimsonR** 是另一種紅光活化的通道，Handler 2019 只在閉迴路實驗用它（果蠅頭固定在顯微鏡下、腳踩泡沫球，球的轉動帶動送氣管，可同時看腦與行為）。兩者的差別三篇都沒有說明：？待查。

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
| [[s-hige-2015-heterosynaptic-plasticity]] | PPL1-γ1pedc（MB320C）；四型 PPL1（MB099C）；多數 PPL1 加少數 PAM（TH-GAL4） | 一邊記錄 MBON，一邊讓氣味與 DAN 活化配對；另以光代替電擊訓練果蠅 |
| [[s-handler-2019-dopamine-receptor-timing]] | PAM（MB042B）、PPL（MB504B）；閉迴路用 MB042B 驅動 ChrimsonR | 自由行走果蠅的順向／逆向配對與時間差掃描；閉迴路中同時記錄 γ4 MBON 與行為 |

## 已知的問題

- **光強不能跨篇直接比。** Hige 的 14.7 mW/mm² 照在打開的腦上，Handler 的 18–40 μW/mm² 照在小盒裡自由行走的果蠅身上：一個以毫瓦（mW）、一個以微瓦（μW）為單位，光要穿過的組織也不同，到達 DAN 的實際光量無從比較。
- **同一篇裡，生理與行為的光協定也不同。** Hige 生理用 1 ms 短脈衝、行為用 500 ms × 12，所以「突觸變弱」與「行為學到」是在兩種刺激下分別看到的。
- **「光照有效」靠補充資料。** Hige 2015 說光脈衝能讓 PPL1-γ1pedc 與 PPL1-α′2α2 可靠放電，證據在補充圖 S2：？待查。不同品系每次光照放出的多巴胺可能不同，這是 Hige 比較 γ1 與 α2 門檻時的混淆因子。
- **光本身的作用要排除。** Handler 2019 的行為指標是「訓練後果蠅往氣味源走的距離比訓練前多幾 mm」。只帶 CsChrimson、沒有 DAN 驅動品系（所以光照不會活化 DAN）的對照組，在 DAN 晚氣味 1 s 的時序下也多走了約 0.7 mm（見 [[numbers]]），表示光與流程本身就有小幅效果；光照單獨的對照在補充圖 S1D–E：？待查。

## 相關

- 細胞：[[e-dopaminergic-neuron]]；品系：[[e-split-gal4]]
- 概念：[[c-us-substitution]]、[[c-cs-us-timing]]、[[c-performance-index]]
- 主題：[[t-timing-rules]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]
